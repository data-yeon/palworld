import requests
import csv
import json
import time
import re
from typing import Dict, List, Optional
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class EnhancedPalCrawler:
    def __init__(self):
        self.base_url = "https://paldb.cc"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
    def load_existing_data(self, filename: str = "complete_1_to_115_pals.csv") -> Dict[str, Dict]:
        """기존 CSV 데이터를 로드합니다"""
        existing_data = {}
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    existing_data[row['id']] = row
        except FileNotFoundError:
            print(f"파일을 찾을 수 없습니다: {filename}")
        return existing_data
    
    def get_pal_detail_url(self, pal_id: str) -> str:
        """팰 ID로부터 상세 페이지 URL을 생성합니다"""
        # B variant 처리
        if 'B' in pal_id:
            base_id = pal_id.replace('B', '')
            return f"{self.base_url}/ko/Pal/{base_id}/Variant"
        else:
            return f"{self.base_url}/ko/Pal/{pal_id}"
    
    def crawl_pal_detail(self, pal_id: str) -> Dict:
        """팰 상세 정보를 크롤링합니다"""
        url = self.get_pal_detail_url(pal_id)
        print(f"크롤링 중: {pal_id} - {url}")
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            pal_data = {
                'id': pal_id,
                'url': url
            }
            
            # Movement 정보 추출
            pal_data.update(self.extract_movement_stats(soup))
            
            # Level 60 스탯 추출
            pal_data.update(self.extract_level60_stats(soup))
            
            # Partner Skill 상세 정보 추출
            pal_data.update(self.extract_partner_skill_details(soup))
            
            # Active Skills 상세 정보 추출
            pal_data.update(self.extract_active_skills_details(soup))
            
            # Passive Skills 추출
            pal_data.update(self.extract_passive_skills(soup))
            
            # Tribes 정보 추출
            pal_data.update(self.extract_tribes_info(soup))
            
            # Spawner 정보 추출
            pal_data.update(self.extract_spawner_info(soup))
            
            return pal_data
            
        except Exception as e:
            print(f"Error crawling {pal_id}: {str(e)}")
            return {'id': pal_id, 'error': str(e)}
    
    def extract_movement_stats(self, soup: BeautifulSoup) -> Dict:
        """Movement 관련 스탯을 추출합니다"""
        movement_data = {}
        try:
            # Movement 섹션 찾기
            for section in soup.find_all(['div', 'section']):
                text = section.get_text().lower()
                if 'movement' in text or '이동' in text:
                    # 숫자 값들 추출
                    numbers = re.findall(r'\d+\.?\d*', section.get_text())
                    if len(numbers) >= 5:
                        movement_data['movement_slowWalkSpeed'] = numbers[0]
                        movement_data['movement_walkSpeed'] = numbers[1] 
                        movement_data['movement_runSpeed'] = numbers[2]
                        movement_data['movement_rideSprintSpeed'] = numbers[3]
                        movement_data['movement_transportSpeed'] = numbers[4]
                    break
        except Exception as e:
            print(f"Movement 추출 오류: {e}")
        return movement_data
    
    def extract_level60_stats(self, soup: BeautifulSoup) -> Dict:
        """Level 60 스탯을 추출합니다"""
        level60_data = {}
        try:
            # Level 60 또는 Lv.60 텍스트 찾기
            for element in soup.find_all(text=re.compile(r'Level?\s*60|Lv\.?\s*60|레벨\s*60')):
                parent = element.parent
                # 주변 텍스트에서 체력, 공격력, 방어력 값 찾기
                surrounding_text = parent.get_text() if parent else ""
                numbers = re.findall(r'\d+', surrounding_text)
                if len(numbers) >= 3:
                    level60_data['level60_health'] = numbers[0]
                    level60_data['level60_attack'] = numbers[1]
                    level60_data['level60_defense'] = numbers[2]
                break
        except Exception as e:
            print(f"Level 60 스탯 추출 오류: {e}")
        return level60_data
    
    def extract_partner_skill_details(self, soup: BeautifulSoup) -> Dict:
        """Partner Skill 상세 정보를 추출합니다"""
        partner_data = {}
        try:
            # Partner Skill 섹션 찾기
            for section in soup.find_all(['div', 'section']):
                text = section.get_text()
                if 'partner' in text.lower() or '파트너' in text:
                    # 필요 아이템, 확률 등 추출
                    if '아이템' in text:
                        items = re.findall(r'([가-힣\s]+)\s*x?\s*(\d+)', text)
                        if items:
                            partner_data['partnerSkill_items'] = json.dumps(items, ensure_ascii=False)
                    
                    # 확률 정보 추출
                    prob_matches = re.findall(r'(\d+)%', text)
                    if prob_matches:
                        partner_data['partnerSkill_probability'] = prob_matches[0]
                    break
        except Exception as e:
            print(f"Partner Skill 상세 정보 추출 오류: {e}")
        return partner_data
    
    def extract_active_skills_details(self, soup: BeautifulSoup) -> Dict:
        """Active Skills 상세 정보를 추출합니다"""
        skills_data = {}
        try:
            active_skills = []
            
            # 스킬 테이블이나 리스트 찾기
            for table in soup.find_all('table'):
                rows = table.find_all('tr')
                for row in rows:
                    cells = row.find_all(['td', 'th'])
                    if len(cells) >= 4:
                        skill_info = {}
                        for i, cell in enumerate(cells):
                            text = cell.get_text().strip()
                            if i == 0 and text:  # 스킬명
                                skill_info['name'] = text
                            elif i == 1 and '속성' in str(cell) or 'element' in str(cell).lower():
                                skill_info['element'] = text
                            elif i == 2 and ('파워' in str(cell) or 'power' in str(cell).lower()):
                                skill_info['power'] = text
                            elif i == 3 and ('쿨타임' in str(cell) or 'cooltime' in str(cell).lower()):
                                skill_info['cooltime'] = text
                        
                        if skill_info.get('name'):
                            active_skills.append(skill_info)
            
            if active_skills:
                skills_data['activeSkills_detailed'] = json.dumps(active_skills, ensure_ascii=False)
                
        except Exception as e:
            print(f"Active Skills 상세 정보 추출 오류: {e}")
        return skills_data
    
    def extract_passive_skills(self, soup: BeautifulSoup) -> Dict:
        """Passive Skills를 추출합니다"""
        passive_data = {}
        try:
            passive_skills = []
            
            # Passive 또는 패시브 스킬 섹션 찾기
            for section in soup.find_all(['div', 'section']):
                text = section.get_text()
                if 'passive' in text.lower() or '패시브' in text:
                    # 스킬명들 추출
                    skill_names = re.findall(r'([가-힣\s]{2,20})', text)
                    for skill in skill_names:
                        if len(skill.strip()) > 2:
                            passive_skills.append(skill.strip())
            
            if passive_skills:
                passive_data['passiveSkills'] = json.dumps(passive_skills, ensure_ascii=False)
                passive_data['passiveSkills_count'] = len(passive_skills)
                
        except Exception as e:
            print(f"Passive Skills 추출 오류: {e}")
        return passive_data
    
    def extract_tribes_info(self, soup: BeautifulSoup) -> Dict:
        """Tribes 정보를 추출합니다"""
        tribes_data = {}
        try:
            tribes = []
            
            # Tribes 또는 부족 정보 찾기
            for section in soup.find_all(['div', 'section']):
                text = section.get_text()
                if 'tribe' in text.lower() or '부족' in text or 'boss' in text.lower():
                    # 부족 이름들 추출
                    tribe_matches = re.findall(r'([가-힣\s]{3,30})\s*(Boss|Normal|보스|일반)?', text)
                    for match in tribe_matches:
                        if match[0].strip():
                            tribes.append({
                                'name': match[0].strip(),
                                'type': match[1] if match[1] else 'Normal'
                            })
            
            if tribes:
                tribes_data['tribes'] = json.dumps(tribes, ensure_ascii=False)
                tribes_data['tribes_count'] = len(tribes)
                
        except Exception as e:
            print(f"Tribes 정보 추출 오류: {e}")
        return tribes_data
    
    def extract_spawner_info(self, soup: BeautifulSoup) -> Dict:
        """Spawner 정보를 추출합니다"""
        spawner_data = {}
        try:
            spawners = []
            
            # 서식지나 스폰 정보 찾기
            for section in soup.find_all(['div', 'section']):
                text = section.get_text()
                if '서식지' in text or 'spawn' in text.lower() or '출현' in text:
                    # 레벨 정보와 지역명 추출
                    level_matches = re.findall(r'Lv\.?\s*(\d+)-?(\d+)?', text)
                    area_matches = re.findall(r'([가-힣\s]{2,20})\s*\(', text)
                    
                    for i, level_match in enumerate(level_matches):
                        spawner = {
                            'level': f"{level_match[0]}-{level_match[1]}" if level_match[1] else level_match[0],
                            'area': area_matches[i][0].strip() if i < len(area_matches) else "Unknown"
                        }
                        spawners.append(spawner)
            
            if spawners:
                spawner_data['spawners'] = json.dumps(spawners, ensure_ascii=False)
                spawner_data['spawners_count'] = len(spawners)
                
        except Exception as e:
            print(f"Spawner 정보 추출 오류: {e}")
        return spawner_data
    
    def crawl_enhanced_data(self, start_id: int = 1, end_id: int = 115):
        """향상된 데이터 크롤링 실행"""
        print(f"팰 {start_id}부터 {end_id}까지 향상된 데이터 크롤링을 시작합니다...")
        
        # 기존 데이터 로드
        existing_data = self.load_existing_data()
        
        enhanced_results = []
        
        # 일반 팰들 크롤링
        for pal_id in range(start_id, end_id + 1):
            pal_data = self.crawl_pal_detail(str(pal_id))
            enhanced_results.append(pal_data)
            time.sleep(1)  # 서버 부하 방지
        
        # B variants 크롤링 (알려진 것들)
        b_variants = ['5B', '6B', '10B', '11B', '12B', '13B', '110B']
        for variant_id in b_variants:
            if int(variant_id.replace('B', '')) <= end_id:
                pal_data = self.crawl_pal_detail(variant_id)
                enhanced_results.append(pal_data)
                time.sleep(1)
        
        # 결과를 기존 데이터와 합치기
        self.merge_and_save_data(existing_data, enhanced_results)
        
        return enhanced_results
    
    def merge_and_save_data(self, existing_data: Dict, enhanced_data: List[Dict]):
        """기존 데이터와 향상된 데이터를 합쳐서 저장합니다"""
        print("데이터 합치는 중...")
        
        # read.md 요구사항에 맞는 전체 필드 리스트
        all_fields = [
            'id', 'name_kor', 'pal_nick_kor', 'description_kor', 'elements',
            'PartnerSkillName', 'PartnerSkillDescribe', 'PartnerSkillNeedItem', 
            'PartnerSkillNeedItemTechLevel', 'PartnerSkillLevel', 'PartnerSkillItems', 
            'PartnerSkillItemQuantity', 'PartnerSkillItemProbability',
            'Size', 'Rarity', 'Health', 'Food', 'MeleeAttack', 'Attack', 'Defense', 
            'WorkSpeed', 'Support', 'CaptureRateCorrect', 'MaleProbability', 
            'CombiRank', 'GoldCoin', 'Egg', 'Code',
            'SlowWalkSpeed', 'WalkSpeed', 'RunSpeed', 'RideSprintSpeed', 'TransportSpeed',
            'Level60_Health', 'Level60_Attack', 'Level60_Defense',
            'ActiveSkillsName', 'ActiveSkillsElement', 'ActiveSkillsCoolTime', 
            'ActiveSkillsPower', 'ActiveSkillsRequiredLevel', 'ActiveSkillsDescribe',
            'PassiveSkills', 'DropsItemName', 'DropsItemQuantity', 'DropsItemProbability',
            'TribesName', 'TribesType', 'SpawnerName', 'SpawnerLevel', 'SpawnerArea'
        ]
        
        merged_data = []
        
        # 향상된 데이터를 딕셔너리로 변환
        enhanced_dict = {item['id']: item for item in enhanced_data if 'id' in item}
        
        # 기존 데이터와 합치기
        for pal_id, existing_row in existing_data.items():
            merged_row = existing_row.copy()
            
            # 향상된 데이터가 있으면 추가
            if pal_id in enhanced_dict:
                enhanced_row = enhanced_dict[pal_id]
                
                # 기존 필드명을 read.md 표준으로 매핑
                field_mapping = {
                    'name_kor': existing_row.get('name_kor', ''),
                    'pal_nick_kor': '',  # 새로 추가 필요
                    'description_kor': existing_row.get('description_kor', ''),
                    'elements': existing_row.get('elements', ''),
                    'PartnerSkillName': existing_row.get('partnerSkill_name', ''),
                    'PartnerSkillDescribe': existing_row.get('partnerSkill_describe', ''),
                    'SlowWalkSpeed': enhanced_row.get('movement_slowWalkSpeed', ''),
                    'WalkSpeed': enhanced_row.get('movement_walkSpeed', ''),
                    'RunSpeed': enhanced_row.get('movement_runSpeed', ''),
                    'RideSprintSpeed': enhanced_row.get('movement_rideSprintSpeed', ''),
                    'TransportSpeed': enhanced_row.get('movement_transportSpeed', ''),
                    'Level60_Health': enhanced_row.get('level60_health', ''),
                    'Level60_Attack': enhanced_row.get('level60_attack', ''),
                    'Level60_Defense': enhanced_row.get('level60_defense', ''),
                    'PassiveSkills': enhanced_row.get('passiveSkills', ''),
                    'TribesName': enhanced_row.get('tribes', ''),
                    'SpawnerLevel': enhanced_row.get('spawners', '')
                }
                
                merged_row.update(field_mapping)
            
            merged_data.append(merged_row)
        
        # CSV로 저장
        output_filename = 'enhanced_complete_pals_data.csv'
        print(f"향상된 데이터를 {output_filename}에 저장 중...")
        
        with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
            if merged_data:
                # 모든 필드를 포함하는 fieldnames 생성
                all_fieldnames = set()
                for row in merged_data:
                    all_fieldnames.update(row.keys())
                
                writer = csv.DictWriter(csvfile, fieldnames=sorted(all_fieldnames))
                writer.writeheader()
                writer.writerows(merged_data)
        
        print(f"향상된 데이터 저장 완료: {output_filename}")

def main():
    crawler = EnhancedPalCrawler()
    
    # 1~115번 팰의 향상된 데이터 크롤링
    results = crawler.crawl_enhanced_data(1, 115)
    
    print(f"총 {len(results)}개 팰의 향상된 정보를 크롤링했습니다.")

if __name__ == "__main__":
    main() 