#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Active Skills 파싱을 개선한 크롤러
"""

import requests
import json
import time
import re
from bs4 import BeautifulSoup

class ImprovedActiveSkillsCrawler:
    def __init__(self):
        self.base_url = "https://paldb.cc"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        # 팰 URL 매핑
        self.pal_url_mapping = {
            "1": "Lamball", "2": "Cattiva", "5B": "Foxparks_Cryst", 
            "10B": "Pengullet_Lux", "24": "Mau"
        }
        
    def get_pal_url(self, pal_id: str) -> str:
        """팰 ID로부터 실제 URL을 생성합니다"""
        if pal_id in self.pal_url_mapping:
            pal_name = self.pal_url_mapping[pal_id]
            return f"{self.base_url}/ko/{pal_name}"
        return f"{self.base_url}/ko/Pal_{pal_id}"
    
    def extract_active_skills_improved(self, soup: BeautifulSoup, pal_id: str) -> dict:
        """개선된 Active Skills 추출"""
        print(f"  🔍 개선된 Active Skills 추출 - {pal_id}")
        
        try:
            # Active Skills 섹션 찾기
            active_section = None
            for h5 in soup.find_all('h5'):
                if h5.get_text().strip() == 'Active Skills':
                    active_section = h5
                    break
            
            if not active_section:
                print(f"    ❌ Active Skills 섹션을 찾을 수 없음")
                return {'activeSkills_detailed': '', 'activeSkills_count': 0}
            
            # Active Skills 섹션부터 다음 h5까지의 모든 텍스트 가져오기
            active_text = ""
            current = active_section.next_sibling
            while current:
                if hasattr(current, 'name') and current.name == 'h5':
                    break
                if hasattr(current, 'get_text'):
                    active_text += current.get_text() + "\n"
                current = current.next_sibling
            
            print(f"    📄 Active Skills 섹션 텍스트 길이: {len(active_text)} 문자")
            
            # 스킬 블록들을 분리 (Lv. 숫자로 시작하는 부분)
            skill_blocks = re.split(r'(?=Lv\.\s*\d+)', active_text)
            skill_blocks = [block.strip() for block in skill_blocks if block.strip()]
            
            print(f"    🔍 발견된 스킬 블록: {len(skill_blocks)}개")
            
            active_skills = []
            
            for i, block in enumerate(skill_blocks):
                print(f"    📝 블록 {i+1}: {block[:100]}...")
                
                skill_info = {}
                
                # 레벨과 스킬명 추출
                level_name_pattern = r'Lv\.\s*(\d+)\s*(.+?)(?:\n|$)'
                level_match = re.search(level_name_pattern, block)
                if level_match:
                    skill_info['level'] = level_match.group(1)
                    # 스킬명에서 링크나 특수문자 제거
                    skill_name = level_match.group(2).strip()
                    skill_name = re.sub(r'[\[\]()]', '', skill_name)  # 대괄호, 괄호 제거
                    skill_info['name'] = skill_name
                
                # 속성 추출 (무속성, 화염, 물, 풀, 얼음, 번개, 땅, 어둠, 용)
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
                    r'파워:\s*(\d+)',
                    r'Power:\s*(\d+)'
                ]
                power_found = False
                for pattern in power_patterns:
                    power_match = re.search(pattern, block)
                    if power_match:
                        skill_info['power'] = power_match.group(1)
                        power_found = True
                        break
                
                if not power_found:
                    skill_info['power'] = '0'
                
                # 쿨타임 추출 (아이콘 다음 숫자 패턴)
                cooltime_patterns = [
                    r'T_Icon_PalSkillCoolTime\.webp.*?:\s*(\d+)',
                    r'쿨타임.*?(\d+)',
                    r'cooltime.*?(\d+)',
                    r'(?:쿨|Cool).*?(\d+)',
                    # 단순히 : 다음 숫자 패턴
                    r':\s*(\d+)(?:\s|$|\n)'
                ]
                cooltime_found = False
                for pattern in cooltime_patterns:
                    cooltime_match = re.search(pattern, block, re.IGNORECASE)
                    if cooltime_match:
                        skill_info['cooltime'] = cooltime_match.group(1)
                        cooltime_found = True
                        break
                
                if not cooltime_found:
                    skill_info['cooltime'] = '0'
                
                # 설명 추출 (마지막 줄에서)
                lines = block.split('\n')
                description = ""
                for line in reversed(lines):
                    line = line.strip()
                    if (line and 
                        'Lv.' not in line and 
                        '위력:' not in line and 
                        '속성' not in line and
                        'webp' not in line and
                        len(line) > 10):
                        description = line[:100]  # 100자로 제한
                        break
                
                if description:
                    skill_info['description'] = description
                
                # 스킬 정보가 충분히 있으면 추가
                if skill_info.get('name'):
                    active_skills.append(skill_info)
                    print(f"      ✅ {skill_info['name']}: {skill_info.get('element', '미확인')}, {skill_info.get('power', '0')}파워, {skill_info.get('cooltime', '0')}초")
                else:
                    print(f"      ⚠️ 스킬명을 찾을 수 없음")
            
            return {
                'activeSkills_detailed': json.dumps(active_skills, ensure_ascii=False) if active_skills else "",
                'activeSkills_count': len(active_skills)
            }
            
        except Exception as e:
            print(f"    ❌ Active Skills 추출 오류: {e}")
            return {'activeSkills_detailed': '', 'activeSkills_count': 0}
    
    def test_pal(self, pal_id: str):
        """단일 팰 테스트"""
        url = self.get_pal_url(pal_id)
        print(f"🔍 테스트: {pal_id} - {url}")
        
        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            print(f"  ✅ HTTP 응답: {response.status_code}")
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # 개선된 Active Skills 추출 테스트
            result = self.extract_active_skills_improved(soup, pal_id)
            
            print(f"  📊 결과: {result['activeSkills_count']}개 스킬")
            
            if result['activeSkills_detailed']:
                skills = json.loads(result['activeSkills_detailed'])
                print(f"  📋 상세 정보:")
                for skill in skills:
                    print(f"    - {skill['name']}: {skill.get('element', '미확인')} 속성, {skill.get('power', '0')} 위력, {skill.get('cooltime', '0')}초 쿨타임")
                    if skill.get('description'):
                        print(f"      설명: {skill['description'][:80]}...")
            
            return result
            
        except Exception as e:
            print(f"  ❌ 오류: {e}")
            return {'activeSkills_detailed': '', 'activeSkills_count': 0}
    
    def run_test(self):
        """테스트 실행"""
        print("🧪 개선된 Active Skills 파싱 테스트")
        print("=" * 60)
        
        test_pals = ['1', '2']  # 도로롱, 까부냥
        
        results = []
        total_skills = 0
        successful_extractions = 0
        
        for pal_id in test_pals:
            result = self.test_pal(pal_id)
            results.append({
                'pal_id': pal_id,
                'result': result
            })
            
            if result['activeSkills_count'] > 0:
                total_skills += result['activeSkills_count']
                successful_extractions += 1
            
            time.sleep(2)  # 서버 부하 방지
        
        print("\n" + "=" * 60)
        print("📊 테스트 결과 요약")
        print("=" * 60)
        
        for item in results:
            pal_id = item['pal_id']
            result = item['result']
            skills_count = result['activeSkills_count']
            
            if skills_count > 0:
                skills = json.loads(result['activeSkills_detailed'])
                # 속성, 위력, 쿨타임이 올바르게 추출된 스킬 개수 계산
                complete_skills = 0
                for skill in skills:
                    if (skill.get('element', '미확인') != '미확인' and 
                        skill.get('power', '0') != '0' and 
                        skill.get('cooltime', '0') != '0'):
                        complete_skills += 1
                
                print(f"✅ {pal_id}: {skills_count}개 스킬, {complete_skills}개 완전 추출")
                
                # 처음 스킬의 상세 정보 출력
                if skills:
                    first_skill = skills[0]
                    print(f"   예시: {first_skill['name']} ({first_skill.get('element', '미확인')}, {first_skill.get('power', '0')}파워, {first_skill.get('cooltime', '0')}초)")
            else:
                print(f"❌ {pal_id}: 스킬 추출 실패")
        
        success_rate = (successful_extractions / len(test_pals)) * 100
        avg_skills = total_skills / len(test_pals) if test_pals else 0
        
        print(f"\n📈 통계:")
        print(f"  성공률: {successful_extractions}/{len(test_pals)} ({success_rate:.1f}%)")
        print(f"  평균 스킬 수: {avg_skills:.1f}개")
        
        if success_rate >= 100 and avg_skills >= 1:
            print("✅ 테스트 통과! Active Skills 파싱이 크게 개선되었습니다.")
            return True
        else:
            print("⚠️ 추가 개선이 필요합니다.")
            return False

def main():
    crawler = ImprovedActiveSkillsCrawler()
    success = crawler.run_test()
    
    if success:
        print("\n🚀 Active Skills 파싱 개선 완료!")
    else:
        print("\n🔧 추가 개선 작업이 필요합니다.")

if __name__ == "__main__":
    main() 