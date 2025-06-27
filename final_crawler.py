#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
최종 개선된 팰월드 크롤러
실제 웹페이지 구조를 반영한 정확한 파싱
우선순위: passiveSkills + Active Skills 상세 + B variants
"""

import requests
import csv
import json
import time
import re
from typing import Dict, List
from bs4 import BeautifulSoup

class FinalPalCrawler:
    def __init__(self):
        self.base_url = "https://paldb.cc"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        # 확장된 팰 이름 매핑 (사이트에서 확인된 정확한 이름들)
        self.pal_url_mapping = {
            "1": "Lamball", "2": "Cattiva", "3": "Chikipi", "4": "Lifmunk", "5": "Foxparks",
            "5B": "Foxparks_Cryst", "6": "Fuack", "6B": "Fuack_Ignis", "7": "Sparkit", 
            "8": "Tanzee", "9": "Rooby", "10": "Pengullet", "10B": "Pengullet_Lux",
            "11": "Penking", "11B": "Penking_Lux", "12": "Jolthog", "12B": "Jolthog_Cryst",
            "13": "Gumoss", "14": "Vixy", "15": "Hoocrates", "16": "Teafant", "17": "Depresso",
            "18": "Cremis", "19": "Daedream", "20": "Rushoar", "21": "Nox", "22": "Fuddler",
            "23": "Killamari", "23B": "Killamari_Primo", "24": "Mau", "24B": "Mau_Cryst",
            "25": "Celaray", "25B": "Celaray_Lux"
        }
        
    def get_pal_url(self, pal_id: str) -> str:
        """팰 ID로부터 실제 URL을 생성합니다"""
        if pal_id in self.pal_url_mapping:
            pal_name = self.pal_url_mapping[pal_id]
            return f"{self.base_url}/ko/{pal_name}"
        else:
            # 매핑에 없는 경우 숫자로만 시도
            base_id = pal_id.replace('B', '')
            return f"{self.base_url}/ko/Pal_{base_id}"
    
    def extract_passive_skills_precise(self, soup: BeautifulSoup, pal_id: str) -> Dict:
        """정확한 Passive Skills 추출"""
        print(f"  🔍 Passive Skills 추출 - {pal_id}")
        passive_data = {}
        
        try:
            # 'Passive Skills' 섹션 찾기
            passive_section = None
            for h5 in soup.find_all('h5'):
                if h5.get_text().strip() == 'Passive Skills':
                    passive_section = h5
                    break
            
            passive_skills = []
            
            if passive_section:
                # Passive Skills 섹션 다음의 내용 확인
                next_element = passive_section.find_next_sibling()
                if next_element:
                    # 테이블이나 리스트에서 패시브 스킬 추출
                    if next_element.name == 'table':
                        rows = next_element.find_all('tr')
                        for row in rows:
                            cells = row.find_all(['td', 'th'])
                            if len(cells) >= 2:
                                skill_name = cells[0].get_text().strip()
                                skill_desc = cells[1].get_text().strip()
                                if skill_name and not skill_name in ['Skill', 'Effect']:
                                    passive_skills.append(f"{skill_name}: {skill_desc}")
                    else:
                        # 일반 텍스트에서 스킬 추출
                        text_content = next_element.get_text()
                        # LV 패턴 찾기
                        lv_patterns = re.findall(r'([가-힣\s]{3,20})\s*LV\s*\d+', text_content)
                        passive_skills.extend([skill.strip() for skill in lv_patterns])
                        print(f"    Passive Skills 섹션에서 {len(lv_patterns)}개 스킬 발견")
                else:
                    print(f"    Passive Skills 섹션이 비어있음")
            else:
                print(f"    Passive Skills 섹션을 찾을 수 없음")
            
            # 전체 페이지에서 패시브 스킬 관련 패턴 찾기 (보조적)
            all_text = soup.get_text()
            
            # 일반적인 패시브 스킬 효과 패턴
            passive_patterns = [
                r'([가-힣\s]{3,15})\s*LV\s*\d+.*?(?:증가|감소|강화|효율|저항)',
                r'([가-힣\s]{3,15})\s*Lv\.\s*\d+.*?(?:\+|\-)\d+%'
            ]
            
            for pattern in passive_patterns:
                matches = re.findall(pattern, all_text)
                for match in matches:
                    skill_name = match.strip()
                    if skill_name and skill_name not in passive_skills:
                        passive_skills.append(skill_name)
            
            # 중복 제거 및 정리
            clean_skills = []
            for skill in passive_skills:
                skill_clean = skill.strip()
                if (skill_clean and 
                    len(skill_clean) > 2 and 
                    skill_clean not in clean_skills):
                    clean_skills.append(skill_clean)
            
            passive_data['passiveSkills'] = " | ".join(clean_skills) if clean_skills else ""
            passive_data['passiveSkills_count'] = len(clean_skills)
            
            print(f"    ✅ 최종 Passive Skills: {len(clean_skills)}개")
            if clean_skills:
                for skill in clean_skills[:3]:
                    print(f"      - {skill}")
            else:
                print(f"      - 패시브 스킬 없음")
                    
        except Exception as e:
            print(f"    ❌ Passive Skills 추출 오류: {e}")
            passive_data = {'passiveSkills': '', 'passiveSkills_count': 0}
            
        return passive_data
    
    def extract_active_skills_precise(self, soup: BeautifulSoup, pal_id: str) -> Dict:
        """정확한 Active Skills 상세 정보 추출"""
        print(f"  🔍 Active Skills 추출 - {pal_id}")
        skills_data = {}
        
        try:
            # 'Active Skills' 섹션 찾기
            active_section = None
            for h5 in soup.find_all('h5'):
                if h5.get_text().strip() == 'Active Skills':
                    active_section = h5
                    break
            
            active_skills = []
            
            if active_section:
                # Active Skills 섹션 다음의 모든 스킬 블록 찾기
                current_element = active_section.find_next_sibling()
                
                while current_element and not (current_element.name == 'h5'):
                    skill_info = {}
                    
                    # 스킬 레벨과 이름 찾기
                    level_pattern = re.search(r'Lv\.\s*(\d+)\s*(.+)', current_element.get_text())
                    if level_pattern:
                        skill_info['level'] = level_pattern.group(1)
                        skill_info['name'] = level_pattern.group(2).strip()
                    
                    # 다음 형제 요소에서 상세 정보 찾기
                    detail_element = current_element.find_next_sibling()
                    if detail_element:
                        detail_text = detail_element.get_text()
                        
                        # 속성 찾기
                        element_match = re.search(r'(무속성|화염|물|풀|얼음|번개|땅|어둠|용)\s*속성', detail_text)
                        if element_match:
                            skill_info['element'] = element_match.group(1)
                        
                        # 쿨타임 찾기 
                        cooltime_match = re.search(r'(?:쿨타임|cooltime).*?(\d+)', detail_text)
                        if cooltime_match:
                            skill_info['cooltime'] = cooltime_match.group(1)
                        
                        # 위력 찾기
                        power_match = re.search(r'위력:\s*(\d+)', detail_text)
                        if power_match:
                            skill_info['power'] = power_match.group(1)
                        
                        # 설명 추출
                        desc_lines = detail_text.split('\n')
                        description = ""
                        for line in desc_lines:
                            if ('위력:' not in line and 
                                '쿨타임' not in line and 
                                '속성' not in line and
                                line.strip() and
                                not re.match(r'^Lv\.\s*\d+', line)):
                                description = line.strip()
                                break
                        if description:
                            skill_info['description'] = description[:100]  # 설명 길이 제한
                    
                    # 스킬 정보가 충분히 수집되면 추가
                    if skill_info.get('name'):
                        if not skill_info.get('element'):
                            skill_info['element'] = '미확인'
                        if not skill_info.get('power'):
                            skill_info['power'] = '0'
                        if not skill_info.get('cooltime'):
                            skill_info['cooltime'] = '0'
                        if not skill_info.get('level'):
                            skill_info['level'] = '1'
                        
                        active_skills.append(skill_info)
                        print(f"      - {skill_info['name']}: {skill_info['element']}, {skill_info['power']}파워, {skill_info['cooltime']}초")
                    
                    current_element = current_element.find_next_sibling()
            else:
                print(f"    Active Skills 섹션을 찾을 수 없음")
            
            skills_data['activeSkills_detailed'] = json.dumps(active_skills, ensure_ascii=False) if active_skills else ""
            skills_data['activeSkills_count'] = len(active_skills)
            
            print(f"    ✅ Active Skills: {len(active_skills)}개")
                
        except Exception as e:
            print(f"    ❌ Active Skills 추출 오류: {e}")
            skills_data = {'activeSkills_detailed': '', 'activeSkills_count': 0}
            
        return skills_data
    
    def extract_additional_data(self, soup: BeautifulSoup, pal_id: str) -> Dict:
        """추가 데이터 추출 (Tribes, Spawner 등)"""
        print(f"  🔍 추가 데이터 추출 - {pal_id}")
        additional_data = {}
        
        try:
            # Tribes 정보 추출
            tribes_section = None
            for h5 in soup.find_all('h5'):
                if h5.get_text().strip() == 'Tribes':
                    tribes_section = h5
                    break
            
            if tribes_section:
                tribes_table = tribes_section.find_next_sibling('table')
                if tribes_table:
                    tribes_info = []
                    rows = tribes_table.find_all('tr')
                    for row in rows:
                        cells = row.find_all(['td', 'th'])
                        if len(cells) >= 2:
                            tribe_name = cells[0].get_text().strip()
                            tribe_type = cells[1].get_text().strip()
                            if tribe_name and tribe_type and 'Tribe' not in tribe_name:
                                tribes_info.append(f"{tribe_name}({tribe_type})")
                    
                    additional_data['tribes'] = " | ".join(tribes_info) if tribes_info else ""
                    print(f"    Tribes: {len(tribes_info)}개")
            
            # Spawner 정보 추출
            spawner_section = None
            for h5 in soup.find_all('h5'):
                if h5.get_text().strip() == 'Spawner':
                    spawner_section = h5
                    break
            
            if spawner_section:
                spawner_table = spawner_section.find_next_sibling('table')
                if spawner_table:
                    spawner_info = []
                    rows = spawner_table.find_all('tr')
                    for row in rows[:5]:  # 최대 5개까지만
                        cells = row.find_all(['td', 'th'])
                        if len(cells) >= 3:
                            spawn_name = cells[0].get_text().strip()
                            spawn_level = cells[1].get_text().strip()
                            spawn_area = cells[2].get_text().strip()
                            if spawn_name and spawn_level:
                                spawner_info.append(f"{spawn_name} Lv.{spawn_level}")
                    
                    additional_data['spawner'] = " | ".join(spawner_info) if spawner_info else ""
                    print(f"    Spawner: {len(spawner_info)}개")
                    
        except Exception as e:
            print(f"    ❌ 추가 데이터 추출 오류: {e}")
            
        return additional_data
    
    def crawl_pal_data(self, pal_id: str) -> Dict:
        """단일 팰 데이터 크롤링"""
        url = self.get_pal_url(pal_id)
        print(f"🔍 크롤링: {pal_id} - {url}")
        
        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            print(f"  ✅ HTTP 응답: {response.status_code}")
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            pal_data = {'id': pal_id, 'url': url}
            
            # 우선순위 1: Passive Skills 정확한 추출
            pal_data.update(self.extract_passive_skills_precise(soup, pal_id))
            
            # 우선순위 2: Active Skills 상세 정보 정확한 추출
            pal_data.update(self.extract_active_skills_precise(soup, pal_id))
            
            # 우선순위 3: 추가 데이터 (Tribes, Spawner)
            pal_data.update(self.extract_additional_data(soup, pal_id))
            
            # 기본 정보 추출
            title = soup.find('title')
            if title:
                pal_data['name_extracted'] = title.get_text().strip()
            
            return pal_data
            
        except requests.exceptions.RequestException as e:
            print(f"  ❌ 네트워크 오류: {e}")
            return {'id': pal_id, 'error': f'network_error: {str(e)}'}
        except Exception as e:
            print(f"  ❌ 파싱 오류: {e}")
            return {'id': pal_id, 'error': f'parsing_error: {str(e)}'}
    
    def test_final_crawling(self):
        """최종 크롤링 테스트"""
        print("🧪 최종 크롤링 테스트 시작")
        print("=" * 70)
        
        # 테스트할 팰들 (다양한 타입)
        test_pals = ['1', '2', '5B', '10B', '24']  # 5개 테스트
        
        results = []
        success_count = 0
        total_passive = 0
        total_active = 0
        
        for pal_id in test_pals:
            result = self.crawl_pal_data(pal_id)
            results.append(result)
            
            if 'error' not in result:
                success_count += 1
                total_passive += result.get('passiveSkills_count', 0)
                total_active += result.get('activeSkills_count', 0)
            
            time.sleep(3)  # 서버 부하 방지
        
        # 결과 요약
        print("\n" + "=" * 70)
        print("📊 최종 테스트 결과 요약")
        print("=" * 70)
        
        for result in results:
            pal_id = result['id']
            if 'error' in result:
                print(f"❌ {pal_id}: {result['error']}")
            else:
                passive_count = result.get('passiveSkills_count', 0)
                active_count = result.get('activeSkills_count', 0)
                tribes_count = len(result.get('tribes', '').split('|')) if result.get('tribes') else 0
                spawner_count = len(result.get('spawner', '').split('|')) if result.get('spawner') else 0
                
                print(f"✅ {pal_id}:")
                print(f"  🔸 Passive Skills: {passive_count}개")
                print(f"  🔸 Active Skills: {active_count}개")
                print(f"  🔸 Tribes: {tribes_count}개")
                print(f"  🔸 Spawner: {spawner_count}개")
                
                if result.get('passiveSkills'):
                    print(f"    패시브: {result['passiveSkills'][:80]}...")
                if result.get('activeSkills_detailed'):
                    skills = json.loads(result['activeSkills_detailed'])
                    if skills:
                        print(f"    액티브: {skills[0]['name']} 등 {len(skills)}개")
        
        success_rate = (success_count / len(test_pals)) * 100
        avg_passive = total_passive / success_count if success_count > 0 else 0
        avg_active = total_active / success_count if success_count > 0 else 0
        
        print(f"\n📈 최종 통계:")
        print(f"  성공률: {success_count}/{len(test_pals)} ({success_rate:.1f}%)")
        print(f"  평균 Passive Skills: {avg_passive:.1f}개")
        print(f"  평균 Active Skills: {avg_active:.1f}개")
        print(f"  총 데이터 포인트: {total_passive + total_active}개")
        
        # 결과를 JSON으로 저장
        with open('final_crawler_test_results.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"\n💾 테스트 결과 저장: final_crawler_test_results.json")
        
        if success_rate >= 80 and (avg_passive > 0 or avg_active > 0):
            print("✅ 테스트 통과! 실제 크롤링 준비 완료")
            return True
        else:
            print("⚠️ 테스트 결과 개선 필요")
            return False

def main():
    """메인 함수"""
    print("🎯 최종 개선된 팰월드 크롤러")
    print("웹페이지 구조를 정확히 반영한 파싱")
    
    crawler = FinalPalCrawler()
    
    # 최종 크롤링 테스트
    success = crawler.test_final_crawling()
    
    if success:
        print("\n🚀 테스트 성공! 우선순위 기능들이 모두 작동합니다.")
        print("이제 전체 크롤링을 실행할 수 있습니다.")
    else:
        print("\n🔧 더 많은 개선이 필요합니다.")

if __name__ == "__main__":
    main() 