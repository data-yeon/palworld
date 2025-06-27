#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
팰월드 크롤러 테스트 스크립트
우선순위 항목들이 제대로 작동하는지 확인
"""

import requests
import csv
import json
import time
import re
from typing import Dict, List
from bs4 import BeautifulSoup

class TestPalCrawler:
    def __init__(self):
        self.base_url = "https://paldb.cc"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
    def get_pal_detail_url(self, pal_id: str) -> str:
        """팰 ID로부터 상세 페이지 URL을 생성합니다"""
        if 'B' in pal_id:
            base_id = pal_id.replace('B', '')
            return f"{self.base_url}/ko/Pal/{base_id}/Variant"
        else:
            return f"{self.base_url}/ko/Pal/{pal_id}"
    
    def test_passive_skills_extraction(self, soup: BeautifulSoup, pal_id: str) -> Dict:
        """Passive Skills 추출 테스트"""
        print(f"  🔍 Passive Skills 추출 테스트 - {pal_id}")
        passive_data = {}
        
        try:
            passive_skills = []
            
            # 전체 텍스트에서 패시브 관련 내용 찾기
            all_text = soup.get_text()
            print(f"    전체 텍스트 길이: {len(all_text)}자")
            
            # LV 패턴이 있는 스킬 찾기
            lv_patterns = re.findall(r'([가-힣\s]{3,20})\s*LV\s*\d+', all_text)
            print(f"    LV 패턴 매칭: {len(lv_patterns)}개")
            for pattern in lv_patterns[:5]:  # 처음 5개만 출력
                print(f"      - {pattern}")
            
            # 일반적인 스킬 키워드 찾기
            skill_keywords = ['공격력', '방어력', '체력', '이동속도', '작업속도', '포획률']
            for keyword in skill_keywords:
                if keyword in all_text:
                    print(f"    키워드 '{keyword}' 발견")
                    # 주변 텍스트 추출
                    context_matches = re.finditer(f'.{{0,50}}{keyword}.{{0,50}}', all_text)
                    for match in list(context_matches)[:2]:  # 처음 2개만
                        context = match.group().strip()
                        print(f"      컨텍스트: {context}")
            
            # 실제 패시브 스킬 리스트 구성
            for pattern in lv_patterns:
                skill_name = pattern.strip()
                if skill_name and len(skill_name) > 2 and skill_name not in passive_skills:
                    passive_skills.append(skill_name)
            
            passive_data['passiveSkills'] = " | ".join(passive_skills) if passive_skills else ""
            passive_data['passiveSkills_count'] = len(passive_skills)
            
            print(f"    ✅ 최종 Passive Skills: {len(passive_skills)}개")
            if passive_skills:
                for skill in passive_skills[:3]:  # 처음 3개만 출력
                    print(f"      - {skill}")
                    
        except Exception as e:
            print(f"    ❌ Passive Skills 추출 오류: {e}")
            passive_data = {'passiveSkills': '', 'passiveSkills_count': 0}
            
        return passive_data
    
    def test_active_skills_extraction(self, soup: BeautifulSoup, pal_id: str) -> Dict:
        """Active Skills 상세 정보 추출 테스트"""
        print(f"  🔍 Active Skills 추출 테스트 - {pal_id}")
        skills_data = {}
        
        try:
            # 기존 activeSkills 형태의 텍스트 찾기
            all_text = soup.get_text()
            
            # 스킬 패턴 매칭: "스킬명(속성, 파워, 쿨타임)"
            skill_patterns = re.findall(r'([^|\(]+)\(([^,]+),\s*(\d+)\s*파워,\s*(\d+)\s*초\)', all_text)
            print(f"    스킬 패턴 매칭: {len(skill_patterns)}개")
            
            active_skills = []
            for pattern in skill_patterns:
                skill_info = {
                    'name': pattern[0].strip(),
                    'element': pattern[1].strip(),
                    'power': pattern[2],
                    'cooltime': pattern[3]
                }
                active_skills.append(skill_info)
                print(f"      - {skill_info['name']}: {skill_info['element']}, {skill_info['power']}파워, {skill_info['cooltime']}초")
            
            # 테이블에서 스킬 정보 찾기
            tables = soup.find_all('table')
            print(f"    테이블 개수: {len(tables)}개")
            
            for i, table in enumerate(tables):
                print(f"      테이블 {i+1}: {len(table.find_all('tr'))}행")
                rows = table.find_all('tr')
                if len(rows) > 1:  # 헤더 + 데이터 행이 있는 경우
                    for j, row in enumerate(rows[:3]):  # 처음 3행만 확인
                        cells = row.find_all(['td', 'th'])
                        if cells:
                            row_text = " | ".join([cell.get_text().strip() for cell in cells])
                            print(f"        행 {j+1}: {row_text[:100]}...")
            
            skills_data['activeSkills_detailed'] = json.dumps(active_skills, ensure_ascii=False) if active_skills else ""
            skills_data['activeSkills_count'] = len(active_skills)
            
            print(f"    ✅ 최종 Active Skills: {len(active_skills)}개")
            
        except Exception as e:
            print(f"    ❌ Active Skills 추출 오류: {e}")
            skills_data = {'activeSkills_detailed': '', 'activeSkills_count': 0}
            
        return skills_data
    
    def test_crawl_pal(self, pal_id: str) -> Dict:
        """단일 팰 크롤링 테스트"""
        url = self.get_pal_detail_url(pal_id)
        print(f"\n🔍 테스트 크롤링: {pal_id}")
        print(f"  URL: {url}")
        
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            print(f"  ✅ HTTP 응답: {response.status_code}")
            
            soup = BeautifulSoup(response.content, 'html.parser')
            print(f"  ✅ HTML 파싱 완료: {len(soup.get_text())}자")
            
            pal_data = {'id': pal_id, 'url': url}
            
            # Passive Skills 테스트
            pal_data.update(self.test_passive_skills_extraction(soup, pal_id))
            
            # Active Skills 테스트  
            pal_data.update(self.test_active_skills_extraction(soup, pal_id))
            
            return pal_data
            
        except Exception as e:
            print(f"  ❌ 크롤링 오류: {e}")
            return {'id': pal_id, 'error': str(e)}
    
    def run_test(self):
        """테스트 실행"""
        print("🧪 팰월드 크롤러 테스트 시작")
        print("=" * 60)
        
        # 테스트할 팰들 (일반 + B variant)
        test_pals = ['1', '2', '5B', '10B']
        
        results = []
        
        for pal_id in test_pals:
            result = self.test_crawl_pal(pal_id)
            results.append(result)
            time.sleep(3)  # 서버 부하 방지
        
        # 결과 요약
        print("\n" + "=" * 60)
        print("📊 테스트 결과 요약")
        print("=" * 60)
        
        for result in results:
            pal_id = result['id']
            if 'error' in result:
                print(f"❌ {pal_id}: 오류 - {result['error']}")
            else:
                passive_count = result.get('passiveSkills_count', 0)
                active_count = result.get('activeSkills_count', 0)
                passive_text = result.get('passiveSkills', '')
                active_text = result.get('activeSkills_detailed', '')
                
                print(f"✅ {pal_id}:")
                print(f"  Passive Skills: {passive_count}개")
                if passive_text:
                    print(f"    {passive_text[:100]}...")
                print(f"  Active Skills: {active_count}개")
                if active_text:
                    print(f"    {active_text[:100]}...")
        
        # 성공률 계산
        successful = sum(1 for r in results if 'error' not in r)
        success_rate = (successful / len(results)) * 100
        
        print(f"\n📈 성공률: {successful}/{len(results)} ({success_rate:.1f}%)")
        
        if success_rate >= 75:
            print("✅ 테스트 통과! 본격적인 크롤링을 진행할 수 있습니다.")
        else:
            print("⚠️ 테스트 결과가 좋지 않습니다. 크롤링 로직을 개선해야 합니다.")
        
        return results

def main():
    """메인 함수"""
    crawler = TestPalCrawler()
    results = crawler.run_test()
    
    # 결과를 JSON으로 저장
    with open('crawler_test_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n💾 테스트 결과 저장: crawler_test_results.json")

if __name__ == "__main__":
    main() 