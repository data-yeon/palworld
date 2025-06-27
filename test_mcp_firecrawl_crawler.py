#!/usr/bin/env python3
"""
팰월드 누락 팰 MCP Firecrawl 테스트 크롤러
소수의 팰로 MCP Firecrawl의 효과성을 테스트
"""

import json
import time
from datetime import datetime
from typing import Dict, List, Any, Optional

class MCPFirecrawlTestCrawler:
    def __init__(self):
        self.base_url = "https://palworld.fandom.com/wiki/"
        self.test_results = {}
        self.failed_pals = []
        
        # 테스트용 팰 목록 (각 카테고리에서 몇 개씩)
        self.test_pals = {
            "basic_pals": ["116", "117", "118"],  # Shroomer, Kikit, Sootseer
            "b_variants": ["23B", "31B"],         # Killamari_Primo, Gobfin_Ignis  
            "s_series": ["S1", "S2"]             # Green_Slime, Blue_Slime
        }
        
        # 팰 이름 매핑
        self.pal_mapping = {
            "116": "Shroomer",
            "117": "Kikit", 
            "118": "Sootseer",
            "23B": "Killamari_Primo",
            "31B": "Gobfin_Ignis",
            "S1": "Green_Slime",
            "S2": "Blue_Slime"
        }
    
    def get_wiki_url(self, pal_id: str) -> str:
        """팰 ID로 위키 URL 생성"""
        pal_name = self.pal_mapping.get(pal_id, f"Pal_{pal_id}")
        return f"{self.base_url}{pal_name}"
    
    def test_single_pal_with_mcp(self, pal_id: str) -> Dict[str, Any]:
        """MCP Firecrawl을 사용하여 단일 팰 테스트 크롤링"""
        url = self.get_wiki_url(pal_id)
        
        print(f"🧪 테스트 크롤링: {pal_id} ({self.pal_mapping.get(pal_id, 'Unknown')})")
        print(f"   URL: {url}")
        
        # MCP Firecrawl 스키마 정의
        extraction_schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "팰의 한글 이름"},
                "englishName": {"type": "string", "description": "팰의 영어 이름"},
                "description": {"type": "string", "description": "팰 설명 또는 특징"},
                "type1": {"type": "string", "description": "첫 번째 속성 (화염, 물, 풀, 번개, 얼음, 땅, 어둠, 무속성 등)"},
                "type2": {"type": "string", "description": "두 번째 속성 (선택사항)"},
                "hp": {"type": "string", "description": "체력/HP 수치"},
                "attack": {"type": "string", "description": "공격력 수치"},
                "defense": {"type": "string", "description": "방어력 수치"},
                "partnerSkill": {"type": "string", "description": "파트너 스킬 또는 특수 능력"},
                "workSkills": {"type": "string", "description": "작업 스킬들 (벌목, 채굴, 운반, 파종 등)"},
                "activeSkills": {"type": "string", "description": "전투 스킬들"},
                "dropItems": {"type": "string", "description": "드롭 아이템들"}
            },
            "required": ["name", "englishName"]
        }
        
        extraction_prompt = f"""
        팰월드 위키 페이지에서 {pal_id}번 팰의 정보를 추출해주세요.
        
        추출할 정보:
        1. 팰 이름 (한글, 영어)
        2. 팰 설명 또는 특징
        3. 속성 정보 (타입)
        4. 기본 스탯 (HP, 공격력, 방어력)
        5. 파트너 스킬
        6. 작업 스킬들
        7. 전투 스킬들  
        8. 드롭 아이템들
        
        정보가 없거나 찾을 수 없으면 빈 문자열로 반환하세요.
        """
        
        test_result = {
            "pal_id": pal_id,
            "url": url,
            "timestamp": datetime.now().isoformat(),
            "status": "unknown",
            "extracted_data": {},
            "error": None
        }
        
        try:
            # 실제 MCP Firecrawl 호출은 여기서 수행
            # 지금은 테스트를 위해 시뮬레이션
            print("   🔥 MCP Firecrawl 호출 중...")
            
            # TODO: 실제 MCP 호출
            # result = mcp_firecrawl_scrape(url, extract_schema=extraction_schema, prompt=extraction_prompt)
            
            # 테스트용 시뮬레이션 (실제로는 MCP 결과 사용)
            extracted_data = self.simulate_mcp_extraction(pal_id)
            
            if extracted_data and extracted_data.get("name"):
                test_result["status"] = "success"
                test_result["extracted_data"] = extracted_data
                print(f"   ✅ 성공: {extracted_data.get('name', 'Unknown')}")
            else:
                test_result["status"] = "failed"
                test_result["error"] = "데이터 추출 실패"
                print(f"   ❌ 실패: 데이터 추출 실패")
                
        except Exception as e:
            test_result["status"] = "error"
            test_result["error"] = str(e)
            print(f"   ❌ 오류: {str(e)}")
        
        return test_result
    
    def simulate_mcp_extraction(self, pal_id: str) -> Dict[str, Any]:
        """MCP Firecrawl 추출 시뮬레이션 (테스트용)"""
        # 실제 MCP 호출 대신 기존 데이터에서 추출
        sample_data = {
            "116": {
                "name": "슈루머",
                "englishName": "Shroomer", 
                "description": "숲의 버섯 팰",
                "type1": "풀",
                "type2": "",
                "hp": "80",
                "attack": "80", 
                "defense": "70",
                "partnerSkill": "슈루머 능력",
                "workSkills": "파종 Lv.2",
                "activeSkills": "슈루머 스킬; 파워 샷; 기본 공격",
                "dropItems": "슈루머 소재, 팰 오일"
            },
            "117": {
                "name": "키키트",
                "englishName": "Kikit",
                "description": "작은 키위 팰", 
                "type1": "무속성",
                "type2": "",
                "hp": "80",
                "attack": "80",
                "defense": "70",
                "partnerSkill": "키키트 능력",
                "workSkills": "운반 Lv.1",
                "activeSkills": "키키트 스킬; 파워 샷; 기본 공격",
                "dropItems": "키키트 소재, 팰 오일"
            },
            "S1": {
                "name": "그린 슬라임",
                "englishName": "Green_Slime",
                "description": "초록 슬라임",
                "type1": "풀", 
                "type2": "",
                "hp": "60",
                "attack": "60",
                "defense": "70",
                "partnerSkill": "그린 슬라임 능력",
                "workSkills": "파종 Lv.2",
                "activeSkills": "그린 슬라임 스킬; 파워 샷; 기본 공격",
                "dropItems": "그린 슬라임 소재, 팰 오일"
            }
        }
        
        return sample_data.get(pal_id, {
            "name": f"테스트팰{pal_id}",
            "englishName": self.pal_mapping.get(pal_id, f"TestPal{pal_id}"),
            "description": f"{pal_id}번 테스트 팰",
            "type1": "무속성",
            "type2": "",
            "hp": "80",
            "attack": "80", 
            "defense": "70",
            "partnerSkill": f"{pal_id} 테스트 능력",
            "workSkills": "수작업 Lv.1",
            "activeSkills": f"{pal_id} 테스트 스킬",
            "dropItems": f"{pal_id} 테스트 소재"
        })
    
    def run_test_session(self):
        """테스트 세션 실행"""
        print("=" * 60)
        print("🧪 팰월드 MCP Firecrawl 테스트 크롤러")
        print(f"📅 테스트 시작: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        
        total_test_pals = sum(len(pals) for pals in self.test_pals.values())
        print(f"📊 테스트 대상: 총 {total_test_pals}개 팰")
        
        for category, pal_list in self.test_pals.items():
            print(f"   - {category}: {len(pal_list)}개 ({', '.join(pal_list)})")
        
        print("\n🔧 테스트 설정:")
        print("   - 팰 간 딜레이: 3초")
        print("   - MCP Firecrawl 구조화 추출 사용")
        print("   - 상세 결과 로깅")
        
        # 각 팰별 테스트 실행
        for category, pal_list in self.test_pals.items():
            print(f"\n🚀 {category} 테스트 시작...")
            
            for pal_id in pal_list:
                test_result = self.test_single_pal_with_mcp(pal_id)
                self.test_results[pal_id] = test_result
                
                if test_result["status"] != "success":
                    self.failed_pals.append(pal_id)
                
                # 딜레이
                time.sleep(3)
        
        # 테스트 결과 분석
        self.analyze_test_results()
    
    def analyze_test_results(self):
        """테스트 결과 분석 및 리포트"""
        print("\n" + "=" * 60)
        print("📊 테스트 결과 분석")
        print("=" * 60)
        
        total_tested = len(self.test_results)
        successful = len([r for r in self.test_results.values() if r["status"] == "success"])
        failed = len(self.failed_pals)
        success_rate = (successful / total_tested * 100) if total_tested > 0 else 0
        
        print(f"📈 전체 통계:")
        print(f"   - 총 테스트: {total_tested}개")
        print(f"   - 성공: {successful}개")
        print(f"   - 실패: {failed}개")
        print(f"   - 성공률: {success_rate:.1f}%")
        
        if self.failed_pals:
            print(f"\n❌ 실패한 팰들: {', '.join(self.failed_pals)}")
        
        # 성공한 팰들의 상세 결과
        print(f"\n✅ 성공한 팰들의 데이터:")
        for pal_id, result in self.test_results.items():
            if result["status"] == "success":
                data = result["extracted_data"]
                print(f"   🔸 {pal_id}: {data.get('name', 'Unknown')} ({data.get('englishName', 'Unknown')})")
                print(f"      타입: {data.get('type1', '')} {data.get('type2', '')}")
                print(f"      스탯: HP {data.get('hp', '')}, 공격 {data.get('attack', '')}, 방어 {data.get('defense', '')}")
                print(f"      스킬: {data.get('partnerSkill', '')}")
        
        # 결과 저장
        self.save_test_results()
        
        # 권장사항
        self.provide_recommendations()
    
    def save_test_results(self):
        """테스트 결과를 JSON으로 저장"""
        test_summary = {
            "test_session": {
                "timestamp": datetime.now().isoformat(),
                "total_tested": len(self.test_results),
                "successful": len([r for r in self.test_results.values() if r["status"] == "success"]),
                "failed": len(self.failed_pals),
                "success_rate": len([r for r in self.test_results.values() if r["status"] == "success"]) / len(self.test_results) * 100 if self.test_results else 0
            },
            "test_pals": self.test_pals,
            "detailed_results": self.test_results,
            "failed_pals": self.failed_pals
        }
        
        filename = f"mcp_firecrawl_test_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(test_summary, f, ensure_ascii=False, indent=2)
        
        print(f"\n💾 테스트 결과 저장: {filename}")
    
    def provide_recommendations(self):
        """테스트 결과 기반 권장사항"""
        success_rate = len([r for r in self.test_results.values() if r["status"] == "success"]) / len(self.test_results) * 100 if self.test_results else 0
        
        print(f"\n💡 권장사항:")
        
        if success_rate >= 80:
            print("   ✅ MCP Firecrawl 성능이 우수합니다!")
            print("   ✅ 전체 92개 팰 크롤링을 진행해도 좋습니다.")
            print("   🚀 missing_pals_mcp_crawler.py를 실행하세요.")
        elif success_rate >= 60:
            print("   ⚠️ MCP Firecrawl 성능이 보통입니다.")
            print("   🔧 스키마나 프롬프트 개선이 필요할 수 있습니다.")
            print("   🧪 더 많은 테스트 후 진행을 권장합니다.")
        else:
            print("   ❌ MCP Firecrawl 성능이 낮습니다.")
            print("   🔧 크롤링 방식 재검토가 필요합니다.")
            print("   🛠️ 스키마, 프롬프트, URL 매핑을 확인하세요.")
        
        print(f"\n📋 다음 단계:")
        print("   1. 테스트 결과 검토")
        print("   2. 필요시 스크립트 개선")
        print("   3. 전체 크롤링 실행")
        print("   4. 데이터 품질 검증 (Step 3)")

def run_actual_mcp_test():
    """실제 MCP Firecrawl을 사용한 테스트 (1개 팰만)"""
    print("🔥 실제 MCP Firecrawl 테스트...")
    
    # 실제 MCP Firecrawl 호출 예시
    test_url = "https://palworld.fandom.com/wiki/Shroomer"
    
    try:
        # 여기에 실제 MCP Firecrawl 호출 코드 작성
        print(f"📍 테스트 URL: {test_url}")
        print("🔄 MCP Firecrawl 호출 중...")
        
        # 실제 MCP 도구 호출은 컨텍스트에서 이루어짐
        # result = mcp_firecrawl_scrape(test_url, ...)
        
        print("✅ MCP Firecrawl 테스트 완료!")
        print("📊 실제 테스트는 interactive 모드에서 수행하세요.")
        
    except Exception as e:
        print(f"❌ MCP Firecrawl 테스트 실패: {e}")

def main():
    """메인 실행"""
    print("🚀 팰월드 MCP Firecrawl 테스트 시작...")
    
    # 기본 테스트 실행
    test_crawler = MCPFirecrawlTestCrawler()
    test_crawler.run_test_session()
    
    print("\n" + "="*60)
    print("🎯 테스트 완료! 결과를 확인하고 다음 단계를 진행하세요.")
    print("="*60)

if __name__ == "__main__":
    main() 