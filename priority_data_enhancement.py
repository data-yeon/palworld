#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
우선순위 데이터 보강 스크립트
1. passiveSkills 데이터 수집 
2. Active Skills 상세 정보 보강
3. B variants 대량 추가

기존 complete_1_to_115_pals.csv를 개선된 데이터로 보강
"""

import requests
import csv
import json
import time
import re
import pandas as pd
from typing import Dict, List
from bs4 import BeautifulSoup

class PriorityDataEnhancer:
    def __init__(self):
        self.base_url = "https://paldb.cc"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        # 확장된 팰 URL 매핑 (B variants 포함)
        self.pal_url_mapping = {
            # 기본 팰들
            "1": "Lamball", "2": "Cattiva", "3": "Chikipi", "4": "Lifmunk", "5": "Foxparks",
            "6": "Fuack", "7": "Sparkit", "8": "Tanzee", "9": "Rooby", "10": "Pengullet",
            "11": "Penking", "12": "Jolthog", "13": "Gumoss", "14": "Vixy", "15": "Hoocrates",
            "16": "Teafant", "17": "Depresso", "18": "Cremis", "19": "Daedream", "20": "Rushoar",
            "21": "Nox", "22": "Fuddler", "23": "Killamari", "24": "Mau", "25": "Celaray",
            
            # B variants (아종)
            "5B": "Foxparks_Cryst", "6B": "Fuack_Ignis", "10B": "Pengullet_Lux", 
            "11B": "Penking_Lux", "12B": "Jolthog_Cryst", "13B": "Gumoss_Special",
            "14B": "Vixy_Prime", "15B": "Hoocrates_Elite", "16B": "Teafant_Lux",
            "17B": "Depresso_Dark", "18B": "Cremis_Blaze", "19B": "Daedream_Shadow",
            "20B": "Rushoar_Savage", "21B": "Nox_Phantom", "22B": "Fuddler_Chaos",
            "23B": "Killamari_Primo", "24B": "Mau_Cryst", "25B": "Celaray_Lux"
        }
        
    def get_pal_url(self, pal_id: str) -> str:
        """팰 ID로부터 실제 URL을 생성합니다"""
        if pal_id in self.pal_url_mapping:
            pal_name = self.pal_url_mapping[pal_id]
            return f"{self.base_url}/ko/{pal_name}"
        else:
            # 매핑에 없는 경우 기본 패턴 시도
            base_id = pal_id.replace('B', '')
            return f"{self.base_url}/ko/Pal_{base_id}"
    
    def extract_passive_skills(self, soup: BeautifulSoup, pal_id: str) -> Dict:
        """Passive Skills 추출 (우선순위 1)"""
        print(f"  🔍 Passive Skills 추출 - {pal_id}")
        passive_data = {}
        
        try:
            # Passive Skills 섹션 찾기
            passive_section = None
            for h5 in soup.find_all('h5'):
                if h5.get_text().strip() == 'Passive Skills':
                    passive_section = h5
                    break
            
            passive_skills = []
            
            if passive_section:
                # 섹션 다음의 텍스트 가져오기
                passive_text = ""
                current = passive_section.next_sibling
                while current:
                    if hasattr(current, 'name') and current.name == 'h5':
                        break
                    if hasattr(current, 'get_text'):
                        passive_text += current.get_text() + "\n"
                    current = current.next_sibling
                
                # 테이블 형태로 되어있는 경우
                if passive_section.find_next_sibling('table'):
                    table = passive_section.find_next_sibling('table')
                    rows = table.find_all('tr')
                    for row in rows:
                        cells = row.find_all(['td', 'th'])
                        if len(cells) >= 2:
                            skill_name = cells[0].get_text().strip()
                            skill_desc = cells[1].get_text().strip()
                            if skill_name and skill_name not in ['Skill', 'Name', 'Effect']:
                                passive_skills.append(f"{skill_name}: {skill_desc}")
                
                # 패턴 매칭으로 스킬 찾기
                patterns = [
                    r'([가-힣\s]{3,20})\s*LV\s*\d+.*?(?:증가|감소|강화|효율|저항)',
                    r'([가-힣\s]{3,15})\s*Lv\.\s*\d+.*?(?:\+|\-)\d+%',
                    r'([가-힣\s]{3,15})\s*(?:LV|Lv\.)\s*\d+'
                ]
                
                for pattern in patterns:
                    matches = re.findall(pattern, passive_text)
                    for match in matches:
                        skill_name = match.strip()
                        if (skill_name and 
                            skill_name not in passive_skills and
                            len(skill_name) > 2):
                            passive_skills.append(skill_name)
            
            # 전체 페이지에서 패시브 스킬 관련 키워드 찾기 (보조)
            all_text = soup.get_text()
            passive_keywords = ['작업 효율', '공격력 증가', '방어력 증가', '체력 증가', '이동 속도']
            
            for keyword in passive_keywords:
                if keyword in all_text:
                    context = re.search(f'.{{0,50}}{keyword}.{{0,50}}', all_text)
                    if context:
                        context_text = context.group(0)
                        lv_match = re.search(r'([가-힣\s]{3,15})\s*LV\s*\d+', context_text)
                        if lv_match and lv_match.group(1).strip() not in passive_skills:
                            passive_skills.append(lv_match.group(1).strip())
            
            # 중복 제거 및 정리
            clean_skills = []
            for skill in passive_skills:
                skill_clean = skill.strip()
                if (skill_clean and 
                    len(skill_clean) > 2 and 
                    skill_clean not in clean_skills):
                    clean_skills.append(skill_clean)
            
            passive_data['passiveSkills_new'] = " | ".join(clean_skills) if clean_skills else ""
            passive_data['passiveSkills_count_new'] = len(clean_skills)
            
            print(f"    ✅ Passive Skills: {len(clean_skills)}개")
            if clean_skills:
                for skill in clean_skills[:3]:
                    print(f"      - {skill}")
            else:
                print(f"      - 패시브 스킬 없음")
                    
        except Exception as e:
            print(f"    ❌ Passive Skills 추출 오류: {e}")
            passive_data = {'passiveSkills_new': '', 'passiveSkills_count_new': 0}
            
        return passive_data
    
    def extract_active_skills_enhanced(self, soup: BeautifulSoup, pal_id: str) -> Dict:
        """Enhanced Active Skills 추출 (우선순위 2)"""
        print(f"  🔍 Enhanced Active Skills 추출 - {pal_id}")
        
        try:
            # Active Skills 섹션 찾기
            active_section = None
            for h5 in soup.find_all('h5'):
                if h5.get_text().strip() == 'Active Skills':
                    active_section = h5
                    break
            
            if not active_section:
                print(f"    ❌ Active Skills 섹션을 찾을 수 없음")
                return {'activeSkills_enhanced': '', 'activeSkills_count_new': 0}
            
            # Active Skills 섹션 전체 텍스트 가져오기
            active_text = ""
            current = active_section.next_sibling
            while current:
                if hasattr(current, 'name') and current.name == 'h5':
                    break
                if hasattr(current, 'get_text'):
                    active_text += current.get_text() + "\n"
                current = current.next_sibling
            
            # 스킬 블록들을 분리
            skill_blocks = re.split(r'(?=Lv\.\s*\d+)', active_text)
            skill_blocks = [block.strip() for block in skill_blocks if block.strip()]
            
            active_skills = []
            
            for block in skill_blocks:
                skill_info = {}
                
                # 레벨과 스킬명 추출
                level_match = re.search(r'Lv\.\s*(\d+)\s*(.+?)(?:\n|$)', block)
                if level_match:
                    skill_info['level'] = level_match.group(1)
                    skill_name = level_match.group(2).strip()
                    skill_name = re.sub(r'[\[\]()]', '', skill_name)
                    skill_info['name'] = skill_name
                
                # 속성 추출
                element_patterns = [
                    r'(무속성|화염|물|풀|얼음|번개|땅|어둠|용)\s*속성',
                    r'(무속성|화염|물|풀|얼음|번개|땅|어둠|용)(?:\s|$|\n)'
                ]
                element_found = False
                for pattern in element_patterns:
                    element_match = re.search(pattern, block)
                    if element_match:
                        skill_info['element'] = element_match.group(1)
                        element_found = True
                        break
                
                if not element_found:
                    skill_info['element'] = '미확인'
                
                # 위력 추출
                power_patterns = [
                    r'위력:\s*(\d+)',
                    r'위력\s*(\d+)',
                    r'파워:\s*(\d+)'
                ]
                for pattern in power_patterns:
                    power_match = re.search(pattern, block)
                    if power_match:
                        skill_info['power'] = power_match.group(1)
                        break
                else:
                    skill_info['power'] = '0'
                
                # 쿨타임 추출
                cooltime_patterns = [
                    r'T_Icon_PalSkillCoolTime\.webp.*?:\s*(\d+)',
                    r':\s*(\d+)(?:\s|$|\n)',  # 단순히 : 다음 숫자
                    r'쿨타임.*?(\d+)'
                ]
                for pattern in cooltime_patterns:
                    cooltime_match = re.search(pattern, block)
                    if cooltime_match:
                        skill_info['cooltime'] = cooltime_match.group(1)
                        break
                else:
                    skill_info['cooltime'] = '0'
                
                # 스킬 정보가 있으면 추가
                if skill_info.get('name'):
                    active_skills.append(skill_info)
                    print(f"      ✅ {skill_info['name']}: {skill_info.get('element', '미확인')}, {skill_info.get('power', '0')}파워, {skill_info.get('cooltime', '0')}초")
            
            return {
                'activeSkills_enhanced': json.dumps(active_skills, ensure_ascii=False) if active_skills else "",
                'activeSkills_count_new': len(active_skills)
            }
            
        except Exception as e:
            print(f"    ❌ Active Skills 추출 오류: {e}")
            return {'activeSkills_enhanced': '', 'activeSkills_count_new': 0}
    
    def crawl_enhanced_data(self, pal_id: str) -> Dict:
        """단일 팰의 보강된 데이터 크롤링"""
        url = self.get_pal_url(pal_id)
        print(f"🔍 데이터 보강 크롤링: {pal_id} - {url}")
        
        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            print(f"  ✅ HTTP 응답: {response.status_code}")
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            pal_data = {'id': pal_id, 'url': url}
            
            # 우선순위 1: Passive Skills
            pal_data.update(self.extract_passive_skills(soup, pal_id))
            
            # 우선순위 2: Enhanced Active Skills  
            pal_data.update(self.extract_active_skills_enhanced(soup, pal_id))
            
            return pal_data
            
        except requests.exceptions.RequestException as e:
            print(f"  ❌ 네트워크 오류: {e}")
            return {'id': pal_id, 'error': f'network_error: {str(e)}'}
        except Exception as e:
            print(f"  ❌ 파싱 오류: {e}")
            return {'id': pal_id, 'error': f'parsing_error: {str(e)}'}
    
    def enhance_existing_data(self, sample_size: int = 10):
        """기존 CSV 데이터 보강 테스트"""
        print("🎯 우선순위 데이터 보강 시작")
        print("=" * 70)
        
        # 기존 CSV 파일 읽기
        try:
            df = pd.read_csv('complete_1_to_115_pals.csv')
            print(f"📁 기존 데이터 로드: {len(df)}개 팰")
        except Exception as e:
            print(f"❌ CSV 파일 읽기 오류: {e}")
            return False
        
        # 샘플 팰들 선택 (일반 + B variants)
        sample_pals = []
        
        # 일반 팰 몇 개
        normal_pals = [str(i) for i in range(1, 6)]  # 1-5번
        sample_pals.extend(normal_pals)
        
        # B variants 몇 개
        b_variants = ['5B', '6B', '10B', '11B', '12B']
        sample_pals.extend(b_variants)
        
        sample_pals = sample_pals[:sample_size]  # 지정된 샘플 크기로 제한
        
        print(f"🧪 테스트 샘플: {len(sample_pals)}개 팰")
        print(f"   일반: {normal_pals}")
        print(f"   아종: {b_variants}")
        
        enhanced_results = []
        success_count = 0
        total_passive = 0
        total_active = 0
        
        for pal_id in sample_pals:
            result = self.crawl_enhanced_data(pal_id)
            enhanced_results.append(result)
            
            if 'error' not in result:
                success_count += 1
                total_passive += result.get('passiveSkills_count_new', 0)
                total_active += result.get('activeSkills_count_new', 0)
            
            time.sleep(2)  # 서버 부하 방지
        
        # 결과 분석
        print("\n" + "=" * 70)
        print("📊 우선순위 데이터 보강 결과")
        print("=" * 70)
        
        passive_improvements = 0
        active_improvements = 0
        
        for result in enhanced_results:
            pal_id = result['id']
            if 'error' in result:
                print(f"❌ {pal_id}: {result['error']}")
                continue
                
            passive_count = result.get('passiveSkills_count_new', 0)
            active_count = result.get('activeSkills_count_new', 0)
            
            # 기존 데이터와 비교
            existing_row = df[df['id'].astype(str) == pal_id]
            
            if not existing_row.empty:
                existing_passive = existing_row.iloc[0].get('passiveSkills', '')
                existing_active = existing_row.iloc[0].get('activeSkills', '')
                
                # 개선 여부 확인
                if passive_count > 0 and (not existing_passive or existing_passive == ''):
                    passive_improvements += 1
                if active_count > 0 and (not existing_active or existing_active == ''):
                    active_improvements += 1
            else:
                # 새로운 B variant
                if 'B' in pal_id:
                    print(f"🆕 {pal_id}: 새로운 B variant 추가됨")
            
            print(f"✅ {pal_id}: Passive {passive_count}개, Active {active_count}개")
            
            if result.get('passiveSkills_new'):
                print(f"   패시브: {result['passiveSkills_new'][:80]}...")
            if result.get('activeSkills_enhanced'):
                skills = json.loads(result['activeSkills_enhanced'])
                if skills:
                    print(f"   액티브: {skills[0]['name']} 등 {len(skills)}개")
        
        # 전체 통계
        success_rate = (success_count / len(sample_pals)) * 100
        avg_passive = total_passive / success_count if success_count > 0 else 0
        avg_active = total_active / success_count if success_count > 0 else 0
        
        print(f"\n📈 보강 통계:")
        print(f"  성공률: {success_count}/{len(sample_pals)} ({success_rate:.1f}%)")
        print(f"  평균 Passive Skills: {avg_passive:.1f}개")
        print(f"  평균 Active Skills: {avg_active:.1f}개")
        print(f"  Passive 데이터 개선: {passive_improvements}건")
        print(f"  Active 데이터 개선: {active_improvements}건")
        
        # 결과를 JSON으로 저장
        with open('priority_enhancement_results.json', 'w', encoding='utf-8') as f:
            json.dump(enhanced_results, f, ensure_ascii=False, indent=2)
        
        print(f"\n💾 보강 결과 저장: priority_enhancement_results.json")
        
        if success_rate >= 80 and (passive_improvements > 0 or active_improvements > 0):
            print("✅ 우선순위 데이터 보강 성공!")
            return True
        else:
            print("⚠️ 추가 개선이 필요합니다.")
            return False

def main():
    """메인 함수"""
    print("🎯 팰월드 우선순위 데이터 보강")
    print("1. passiveSkills 데이터 수집")
    print("2. Active Skills 상세 정보 보강")
    print("3. B variants 추가")
    
    enhancer = PriorityDataEnhancer()
    
    # 샘플 테스트 실행 (10개 팰)
    success = enhancer.enhance_existing_data(sample_size=10)
    
    if success:
        print("\n🚀 우선순위 작업 완료! 이제 전체 데이터를 보강할 수 있습니다.")
        print("\n다음 단계:")
        print("1. 전체 115개 + B variants 크롤링 실행")
        print("2. 기존 CSV와 병합")
        print("3. read.md 요구사항 완성도 재검증")
    else:
        print("\n🔧 개선이 필요합니다.")

if __name__ == "__main__":
    main() 