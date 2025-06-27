#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
수정된 팰월드 크롤러 - 올바른 URL 구조 사용
우선순위: passiveSkills + Active Skills 상세 + B variants
"""

import requests
import csv
import json
import time
import re
from typing import Dict, List
from bs4 import BeautifulSoup

class FixedPalCrawler:
    def __init__(self):
        self.base_url = "https://paldb.cc"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        # 실제 사이트에서 확인된 팰 이름 매핑 (ID -> URL 이름)
        self.pal_url_mapping = {
            "1": "Lamball",
            "2": "Cattiva", 
            "3": "Chikipi",
            "4": "Lifmunk",
            "5": "Foxparks",
            "5B": "Foxparks_Cryst",
            "6": "Fuack",
            "6B": "Fuack_Ignis",
            "7": "Sparkit",
            "8": "Tanzee",
            "9": "Rooby",
            "10": "Pengullet",
            "10B": "Pengullet_Lux",
            "11": "Penking",
            "11B": "Penking_Lux",
            "12": "Jolthog",
            "12B": "Jolthog_Cryst"
        }
        
    def get_pal_url(self, pal_id: str) -> str:
        """팰 ID로부터 실제 URL을 생성합니다"""
        if pal_id in self.pal_url_mapping:
            pal_name = self.pal_url_mapping[pal_id]
            return f"{self.base_url}/ko/{pal_name}"
        else:
            # 매핑에 없는 경우 기본 패턴 시도
            return f"{self.base_url}/ko/Pal{pal_id}"
    
    def extract_passive_skills_smart(self, soup: BeautifulSoup, pal_id: str) -> Dict:
        """스마트한 Passive Skills 추출"""
        print(f"  🔍 Passive Skills 추출 - {pal_id}")
        passive_data = {}
        
        try:
            passive_skills = []
            all_text = soup.get_text()
            
            # 패턴 1: LV 숫자와 함께 나오는 스킬명
            lv_patterns = re.findall(r'([가-힣\s]{3,20})\s*LV\s*\d+', all_text)
            print(f"    LV 패턴: {len(lv_patterns)}개")
            
            # 패턴 2: "스킬" 키워드 주변 텍스트
            skill_sections = re.findall(r'.{0,100}스킬.{0,100}', all_text)
            print(f"    스킬 섹션: {len(skill_sections)}개")
            
            # 패턴 3: 일반적인 패시브 스킬 효과 단어들
            passive_keywords = ['증가', '감소', '강화', '효율', '저항', '면역', '데미지', '공격력', '방어력', '체력']
            for keyword in passive_keywords:
                if keyword in all_text:
                    # 키워드 주변에서 LV 패턴 찾기
                    context_patterns = re.findall(
                        f'([가-힣\s]{{3,15}}){keyword}[^가-힣]*LV\s*\d+',
                        all_text
                    )
                    if context_patterns:
                        print(f"    '{keyword}' 관련 스킬: {len(context_patterns)}개")
                        passive_skills.extend(context_patterns)
            
            # 중복 제거 및 정리
            clean_skills = []
            for skill in lv_patterns + passive_skills:
                skill_clean = skill.strip()
                if (skill_clean and 
                    len(skill_clean) > 2 and 
                    skill_clean not in clean_skills and
                    not any(char.isdigit() for char in skill_clean)):  # 숫자 포함된 것 제외
                    clean_skills.append(skill_clean)
            
            passive_data['passiveSkills'] = " | ".join(clean_skills[:5]) if clean_skills else ""  # 최대 5개까지
            passive_data['passiveSkills_count'] = len(clean_skills)
            
            print(f"    ✅ 최종 Passive Skills: {len(clean_skills)}개")
            if clean_skills:
                for skill in clean_skills[:3]:
                    print(f"      - {skill}")
                    
        except Exception as e:
            print(f"    ❌ Passive Skills 추출 오류: {e}")
            passive_data = {'passiveSkills': '', 'passiveSkills_count': 0}
            
        return passive_data
    
    def extract_active_skills_smart(self, soup: BeautifulSoup, pal_id: str) -> Dict:
        """스마트한 Active Skills 상세 정보 추출"""
        print(f"  🔍 Active Skills 추출 - {pal_id}")
        skills_data = {}
        
        try:
            all_text = soup.get_text()
            active_skills = []
            
            # 패턴 1: 기존 형식 "스킬명(속성, 파워, 쿨타임)"
            pattern1 = re.findall(r'([^(]+)\(([^,]+),\s*(\d+)\s*파워,\s*(\d+)\s*초\)', all_text)
            for match in pattern1:
                skill_info = {
                    'name': match[0].strip(),
                    'element': match[1].strip(),
                    'power': match[2],
                    'cooltime': match[3]
                }
                active_skills.append(skill_info)
            
            # 패턴 2: 속성과 파워, 쿨타임이 분리된 형태
            skill_blocks = re.findall(r'([가-힣\s]{2,20})\s*(?:속성|element)[^0-9]*(\d+)[^0-9]*파워[^0-9]*(\d+)[^0-9]*초', all_text, re.IGNORECASE)
            for match in skill_blocks:
                skill_info = {
                    'name': match[0].strip(),
                    'element': '미확인',
                    'power': match[1],
                    'cooltime': match[2]
                }
                active_skills.append(skill_info)
            
            # 패턴 3: 테이블에서 스킬 정보 추출
            tables = soup.find_all('table')
            for table in tables:
                rows = table.find_all('tr')
                for row in rows:
                    cells = row.find_all(['td', 'th'])
                    if len(cells) >= 3:
                        cell_texts = [cell.get_text().strip() for cell in cells]
                        
                        # 스킬명, 속성, 파워, 쿨타임 패턴 찾기
                        skill_name = ""
                        element = ""
                        power = ""
                        cooltime = ""
                        
                        for i, text in enumerate(cell_texts):
                            if re.match(r'^[가-힣\s]{2,20}$', text) and not skill_name:
                                skill_name = text
                            elif any(elem in text for elem in ['화염', '물', '풀', '얼음', '번개', '땅', '어둠', '무속성']):
                                element = text
                            elif re.search(r'(\d+).*파워', text):
                                power = re.search(r'(\d+)', text).group(1)
                            elif re.search(r'(\d+).*초', text):
                                cooltime = re.search(r'(\d+)', text).group(1)
                        
                        if skill_name and (power or cooltime):
                            skill_info = {
                                'name': skill_name,
                                'element': element or '미확인',
                                'power': power or '0',
                                'cooltime': cooltime or '0'
                            }
                            active_skills.append(skill_info)
            
            # 중복 제거
            unique_skills = []
            seen_names = set()
            for skill in active_skills:
                if skill.get('name') and skill['name'] not in seen_names:
                    unique_skills.append(skill)
                    seen_names.add(skill['name'])
            
            skills_data['activeSkills_detailed'] = json.dumps(unique_skills, ensure_ascii=False) if unique_skills else ""
            skills_data['activeSkills_count'] = len(unique_skills)
            
            print(f"    ✅ Active Skills: {len(unique_skills)}개")
            for skill in unique_skills[:2]:  # 처음 2개만 출력
                print(f"      - {skill['name']}: {skill['element']}, {skill['power']}파워, {skill['cooltime']}초")
                
        except Exception as e:
            print(f"    ❌ Active Skills 추출 오류: {e}")
            skills_data = {'activeSkills_detailed': '', 'activeSkills_count': 0}
            
        return skills_data
    
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
            
            # 우선순위 1: Passive Skills
            pal_data.update(self.extract_passive_skills_smart(soup, pal_id))
            
            # 우선순위 2: Active Skills 상세 정보
            pal_data.update(self.extract_active_skills_smart(soup, pal_id))
            
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
    
    def test_priority_crawling(self):
        """우선순위 크롤링 테스트"""
        print("🧪 우선순위 크롤링 테스트 시작")
        print("=" * 60)
        
        # 테스트할 팰들 (URL 매핑 확인된 것들)
        test_pals = ['1', '2', '5B', '10B']
        
        results = []
        success_count = 0
        
        for pal_id in test_pals:
            result = self.crawl_pal_data(pal_id)
            results.append(result)
            
            if 'error' not in result:
                success_count += 1
            
            time.sleep(3)  # 서버 부하 방지
        
        # 결과 요약
        print("\n" + "=" * 60)
        print("📊 테스트 결과 요약")
        print("=" * 60)
        
        for result in results:
            pal_id = result['id']
            if 'error' in result:
                print(f"❌ {pal_id}: {result['error']}")
            else:
                passive_count = result.get('passiveSkills_count', 0)
                active_count = result.get('activeSkills_count', 0)
                
                print(f"✅ {pal_id}:")
                print(f"  Passive Skills: {passive_count}개")
                print(f"  Active Skills: {active_count}개")
                
                if result.get('passiveSkills'):
                    print(f"    패시브: {result['passiveSkills'][:100]}...")
                if result.get('activeSkills_detailed'):
                    print(f"    액티브: {result['activeSkills_detailed'][:100]}...")
        
        success_rate = (success_count / len(test_pals)) * 100
        print(f"\n📈 성공률: {success_count}/{len(test_pals)} ({success_rate:.1f}%)")
        
        # 결과를 JSON으로 저장
        with open('fixed_crawler_test_results.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"💾 테스트 결과 저장: fixed_crawler_test_results.json")
        
        if success_rate >= 75:
            print("✅ 테스트 통과! 본격적인 크롤링 진행 가능")
            return True
        else:
            print("⚠️ 테스트 실패. URL 매핑이나 파싱 로직 개선 필요")
            return False

def main():
    """메인 함수"""
    print("🎯 수정된 팰월드 크롤러")
    print("올바른 URL 구조 사용")
    
    crawler = FixedPalCrawler()
    
    # 우선순위 크롤링 테스트
    success = crawler.test_priority_crawling()
    
    if success:
        print("\n🚀 테스트 성공! 이제 전체 크롤링을 실행할 수 있습니다.")
    else:
        print("\n🔧 테스트 실패. 문제를 수정한 후 다시 시도하세요.")

if __name__ == "__main__":
    main() 