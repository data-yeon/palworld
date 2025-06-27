#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
개선된 팰월드 크롤러
우선순위: passiveSkills, Active Skills 상세, B variants 대량 추가
"""

import requests
import csv
import json
import time
import re
from typing import Dict, List, Optional
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class ImprovedPalCrawler:
    def __init__(self):
        self.base_url = "https://paldb.cc"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        
        # 알려진 B variants 리스트 (검증 결과에서 확인된 76개)
        self.known_b_variants = [
            "5B", "6B", "10B", "11B", "12B", "13B", "14B", "15B", "16B", "17B",
            "24B", "26B", "27B", "28B", "29B", "30B", "31B", "34B", "36B", "38B",
            "39B", "42B", "43B", "44B", "45B", "46B", "47B", "51B", "52B", "55B",
            "56B", "57B", "59B", "60B", "61B", "64B", "65B", "67B", "69B", "71B",
            "72B", "75B", "76B", "77B", "78B", "80B", "82B", "83B", "84B", "85B",
            "86B", "87B", "88B", "89B", "90B", "91B", "92B", "95B", "96B", "98B",
            "100B", "101B", "102B", "103B", "104B", "105B", "106B", "107B", "108B",
            "109B", "110B", "111B", "112B", "113B", "114B", "115B"
        ]
        
    def load_existing_data(self, filename: str = "complete_1_to_115_pals.csv") -> Dict[str, Dict]:
        """기존 CSV 데이터를 로드합니다"""
        existing_data = {}
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    existing_data[row['id']] = row
            print(f"✅ 기존 데이터 로드: {len(existing_data)}개 팰")
        except FileNotFoundError:
            print(f"❌ 파일을 찾을 수 없습니다: {filename}")
        return existing_data
    
    def get_pal_detail_url(self, pal_id: str) -> str:
        """팰 ID로부터 상세 페이지 URL을 생성합니다"""
        if 'B' in pal_id:
            base_id = pal_id.replace('B', '')
            return f"{self.base_url}/ko/Pal/{base_id}/Variant"
        else:
            return f"{self.base_url}/ko/Pal/{pal_id}"
    
    def extract_passive_skills_improved(self, soup: BeautifulSoup) -> Dict:
        """개선된 Passive Skills 추출"""
        passive_data = {}
        
        try:
            passive_skills = []
            
            # 방법 1: 테이블에서 패시브 스킬 찾기
            for table in soup.find_all('table'):
                rows = table.find_all('tr')
                for row in rows:
                    cells = row.find_all(['td', 'th'])
                    for cell in cells:
                        text = cell.get_text().strip()
                        # 패시브 스킬 패턴 매칭
                        if re.search(r'(LV|레벨|Lv)\s*\d+', text) and len(text) > 5:
                            # 일반적인 패시브 스킬 형태 확인
                            if any(keyword in text for keyword in ['LV', '레벨', 'Lv']):
                                skill_name = re.sub(r'\s*(LV|레벨|Lv)\s*\d+.*', '', text).strip()
                                if skill_name and len(skill_name) > 2:
                                    passive_skills.append(skill_name)
            
            # 방법 2: 패시브 섹션에서 직접 추출
            for section in soup.find_all(['div', 'section', 'span']):
                text = section.get_text()
                if '패시브' in text or 'passive' in text.lower():
                    # 주변 텍스트에서 스킬명 찾기
                    parent = section.parent
                    if parent:
                        surrounding_text = parent.get_text()
                        # 한글 패시브 스킬명 패턴
                        skill_matches = re.findall(r'([가-힣\s]{3,15})\s*(?:LV|레벨|Lv)\s*\d+', surrounding_text)
                        for skill in skill_matches:
                            clean_skill = skill.strip()
                            if clean_skill and clean_skill not in passive_skills:
                                passive_skills.append(clean_skill)
            
            # 방법 3: 일반적인 패시브 스킬 키워드로 찾기
            common_passive_keywords = [
                '공격력', '방어력', '체력', '이동속도', '작업속도', '포획률',
                '데미지', '효율', '저항', '면역', '강화', '증가', '감소'
            ]
            
            for element in soup.find_all(text=True):
                text = element.strip()
                if any(keyword in text for keyword in common_passive_keywords):
                    # LV 패턴이 있는 패시브 스킬 찾기
                    if re.search(r'LV\s*\d+', text):
                        skill_match = re.search(r'([가-힣\s]{3,20})\s*LV\s*\d+', text)
                        if skill_match:
                            skill_name = skill_match.group(1).strip()
                            if skill_name and skill_name not in passive_skills:
                                passive_skills.append(skill_name)
            
            # 중복 제거 및 정리
            passive_skills = list(set(passive_skills))
            passive_skills = [skill for skill in passive_skills if len(skill.strip()) > 2]
            
            if passive_skills:
                passive_data['passiveSkills'] = " | ".join(passive_skills)
                passive_data['passiveSkills_count'] = len(passive_skills)
                print(f"  ✅ Passive Skills 발견: {len(passive_skills)}개")
            else:
                passive_data['passiveSkills'] = ""
                passive_data['passiveSkills_count'] = 0
                print(f"  ⚠️ Passive Skills 없음")
                
        except Exception as e:
            print(f"  ❌ Passive Skills 추출 오류: {e}")
            passive_data['passiveSkills'] = ""
            passive_data['passiveSkills_count'] = 0
            
        return passive_data
    
    def extract_active_skills_improved(self, soup: BeautifulSoup) -> Dict:
        """개선된 Active Skills 상세 정보 추출"""
        skills_data = {}
        
        try:
            active_skills = []
            
            # 방법 1: 스킬 테이블에서 정보 추출
            for table in soup.find_all('table'):
                headers = table.find_all('th')
                if any('스킬' in th.get_text() or 'skill' in th.get_text().lower() for th in headers):
                    rows = table.find_all('tr')[1:]  # 헤더 제외
                    
                    for row in rows:
                        cells = row.find_all('td')
                        if len(cells) >= 3:
                            skill_info = {}
                            
                            # 첫 번째 셀: 스킬명
                            if cells[0].get_text().strip():
                                skill_info['name'] = cells[0].get_text().strip()
                            
                            # 나머지 셀들에서 정보 추출
                            for i, cell in enumerate(cells[1:], 1):
                                text = cell.get_text().strip()
                                
                                # 속성 정보
                                if any(element in text for element in ['화염', '물', '풀', '얼음', '번개', '땅', '어둠', '무속성']):
                                    skill_info['element'] = text
                                
                                # 파워 정보
                                power_match = re.search(r'(\d+)\s*파워', text)
                                if power_match:
                                    skill_info['power'] = power_match.group(1)
                                
                                # 쿨타임 정보
                                cooltime_match = re.search(r'(\d+)\s*초', text)
                                if cooltime_match:
                                    skill_info['cooltime'] = cooltime_match.group(1)
                                
                                # 레벨 요구사항
                                level_match = re.search(r'Lv\.?\s*(\d+)', text)
                                if level_match:
                                    skill_info['required_level'] = level_match.group(1)
                            
                            if skill_info.get('name'):
                                active_skills.append(skill_info)
            
            # 방법 2: 기존 activeSkills 필드에서 파싱
            existing_skills_text = ""
            for element in soup.find_all(text=re.compile(r'.*\s*\(\s*\w+\s*속성.*\d+\s*파워.*\d+\s*초\s*\)')):
                existing_skills_text += element + " | "
            
            if existing_skills_text:
                # 기존 형식 파싱: "스킬명(속성, 파워, 쿨타임)"
                skill_patterns = re.findall(r'([^|]+)\(([^,]+),\s*(\d+)\s*파워,\s*(\d+)\s*초\)', existing_skills_text)
                for pattern in skill_patterns:
                    skill_info = {
                        'name': pattern[0].strip(),
                        'element': pattern[1].strip(),
                        'power': pattern[2],
                        'cooltime': pattern[3]
                    }
                    active_skills.append(skill_info)
            
            # 중복 제거
            unique_skills = []
            seen_names = set()
            for skill in active_skills:
                if skill.get('name') and skill['name'] not in seen_names:
                    unique_skills.append(skill)
                    seen_names.add(skill['name'])
            
            if unique_skills:
                skills_data['activeSkills_detailed'] = json.dumps(unique_skills, ensure_ascii=False)
                skills_data['activeSkills_count'] = len(unique_skills)
                print(f"  ✅ Active Skills 상세 정보: {len(unique_skills)}개")
            else:
                skills_data['activeSkills_detailed'] = ""
                skills_data['activeSkills_count'] = 0
                print(f"  ⚠️ Active Skills 상세 정보 없음")
                
        except Exception as e:
            print(f"  ❌ Active Skills 상세 정보 추출 오류: {e}")
            skills_data['activeSkills_detailed'] = ""
            skills_data['activeSkills_count'] = 0
            
        return skills_data
    
    def crawl_pal_detail(self, pal_id: str) -> Dict:
        """팰 상세 정보를 크롤링합니다"""
        url = self.get_pal_detail_url(pal_id)
        print(f"🔍 크롤링: {pal_id} - {url}")
        
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            pal_data = {'id': pal_id}
            
            # 우선순위 1: Passive Skills 추출
            pal_data.update(self.extract_passive_skills_improved(soup))
            
            # 우선순위 2: Active Skills 상세 정보 추출
            pal_data.update(self.extract_active_skills_improved(soup))
            
            # 추가 정보들
            pal_data.update(self.extract_basic_info(soup))
            
            return pal_data
            
        except requests.exceptions.RequestException as e:
            print(f"  ❌ 네트워크 오류 {pal_id}: {str(e)}")
            return {'id': pal_id, 'error': f'network_error: {str(e)}'}
        except Exception as e:
            print(f"  ❌ 파싱 오류 {pal_id}: {str(e)}")
            return {'id': pal_id, 'error': f'parsing_error: {str(e)}'}
    
    def extract_basic_info(self, soup: BeautifulSoup) -> Dict:
        """기본 정보 추출 (이름, 설명 등)"""
        basic_data = {}
        
        try:
            # 팰 이름 추출
            title_element = soup.find('h1') or soup.find('title')
            if title_element:
                basic_data['name_extracted'] = title_element.get_text().strip()
            
            # 설명 추출
            desc_element = soup.find('meta', {'name': 'description'})
            if desc_element and hasattr(desc_element, 'attrs') and 'content' in desc_element.attrs:
                basic_data['description_extracted'] = str(desc_element.attrs['content']).strip()
                
        except Exception as e:
            print(f"  ⚠️ 기본 정보 추출 오류: {e}")
            
        return basic_data
    
    def crawl_priority_data(self):
        """우선순위 데이터를 크롤링합니다"""
        print("🚀 우선순위 데이터 크롤링 시작")
        print("우선순위: 1) passiveSkills 2) Active Skills 상세 3) B variants")
        
        # 기존 데이터 로드
        existing_data = self.load_existing_data()
        
        results = []
        total_count = 0
        success_count = 0
        
        # 1. 기존 115개 팰의 누락된 정보 보완
        print("\n📋 1단계: 기존 팰들의 누락된 정보 보완")
        for pal_id in range(1, 116):
            pal_data = self.crawl_pal_detail(str(pal_id))
            results.append(pal_data)
            total_count += 1
            
            if 'error' not in pal_data:
                success_count += 1
            
            time.sleep(2)  # 서버 부하 방지
        
        # 2. B variants 대량 추가
        print(f"\n📋 2단계: B variants 크롤링 ({len(self.known_b_variants)}개)")
        b_success = 0
        for variant_id in self.known_b_variants:
            print(f"  🔄 {variant_id} 처리 중...")
            pal_data = self.crawl_pal_detail(variant_id)
            results.append(pal_data)
            total_count += 1
            
            if 'error' not in pal_data:
                success_count += 1
                b_success += 1
            
            time.sleep(2)  # 서버 부하 방지
        
        print(f"\n📊 크롤링 완료 결과:")
        print(f"  총 시도: {total_count}개")
        print(f"  성공: {success_count}개 ({success_count/total_count*100:.1f}%)")
        print(f"  B variants 성공: {b_success}개 / {len(self.known_b_variants)}개")
        
        # 결과 저장
        self.save_enhanced_data(existing_data, results)
        
        return results
    
    def save_enhanced_data(self, existing_data: Dict, new_data: List[Dict]):
        """향상된 데이터를 저장합니다"""
        print("\n💾 데이터 병합 및 저장 중...")
        
        # 새 데이터를 딕셔너리로 변환
        new_data_dict = {item['id']: item for item in new_data if 'id' in item}
        
        merged_data = []
        
        # 기존 데이터 업데이트
        for pal_id, existing_row in existing_data.items():
            updated_row = existing_row.copy()
            
            if pal_id in new_data_dict:
                new_row = new_data_dict[pal_id]
                
                # 새로운 정보로 업데이트 (빈 값이 아닌 경우만)
                for key, value in new_row.items():
                    if value and value != "":
                        updated_row[key] = value
            
            merged_data.append(updated_row)
        
        # 새로운 B variants 추가
        existing_ids = set(existing_data.keys())
        for pal_id, new_row in new_data_dict.items():
            if pal_id not in existing_ids and 'error' not in new_row:
                # 기본 구조로 새 행 생성
                new_pal_row = {
                    'id': pal_id,
                    'name_kor': new_row.get('name_extracted', ''),
                    'description_kor': new_row.get('description_extracted', ''),
                    'passiveSkills': new_row.get('passiveSkills', ''),
                    'passiveSkills_count': new_row.get('passiveSkills_count', 0),
                    'activeSkills_detailed': new_row.get('activeSkills_detailed', ''),
                    'activeSkills_count': new_row.get('activeSkills_count', 0)
                }
                merged_data.append(new_pal_row)
        
        # CSV로 저장
        output_filename = 'improved_complete_pals_data.csv'
        
        if merged_data:
            # 모든 컬럼 수집
            all_columns = set()
            for row in merged_data:
                all_columns.update(row.keys())
            
            with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=sorted(all_columns))
                writer.writeheader()
                writer.writerows(merged_data)
            
            print(f"✅ 향상된 데이터 저장 완료: {output_filename}")
            print(f"  총 팰 수: {len(merged_data)}개")
            
            # 통계 출력
            passive_filled = sum(1 for row in merged_data if row.get('passiveSkills', ''))
            active_detailed = sum(1 for row in merged_data if row.get('activeSkills_detailed', ''))
            b_variants = sum(1 for row in merged_data if 'B' in str(row.get('id', '')))
            
            print(f"  Passive Skills 보유: {passive_filled}개")
            print(f"  Active Skills 상세: {active_detailed}개") 
            print(f"  B variants: {b_variants}개")
        else:
            print("❌ 저장할 데이터가 없습니다.")

def main():
    """메인 실행 함수"""
    print("🎯 개선된 팰월드 크롤러 시작")
    print("목표: passiveSkills + Active Skills 상세 + B variants 대량 추가")
    
    crawler = ImprovedPalCrawler()
    
    # 우선순위 크롤링 실행
    results = crawler.crawl_priority_data()
    
    print(f"\n✨ 크롤링 완료! 총 {len(results)}개 팰 처리")

if __name__ == "__main__":
    main() 