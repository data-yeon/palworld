#!/usr/bin/env python3
"""
팰월드 기본 팰 (116-155번) 배치 크롤링 스크립트
MCP Firecrawl을 활용하여 40개 기본 팰 데이터 수집
"""

import json
import time
import csv
from datetime import datetime
from typing import Dict, List, Any

class BasicPalBatchCrawler:
    def __init__(self):
        self.base_url = "https://palworld.fandom.com/wiki/"
        self.crawled_data = {}
        self.failed_pals = []
        self.success_count = 0
        self.total_pals = 40
        
        # 116-155번 기본 팰 목록과 영어 이름 매핑
        self.basic_pals = {
            "116": "Shroomer",
            "117": "Kikit", 
            "118": "Sootseer",
            "119": "Prixter",
            "120": "Knocklem",
            "121": "Yakumo",
            "122": "Dogen",
            "123": "Dazemu",
            "124": "Mimog",
            "125": "Xenovader",
            "126": "Xenogard",
            "127": "Xenolord",
            "128": "Nitemary",
            "129": "Starryon",
            "130": "Silvegis",
            "131": "Smokie",
            "132": "Celesdir",
            "133": "Omascul",
            "134": "Splatterina",
            "135": "Tarantriss",
            "136": "Azurmane",
            "137": "Bastigor",
            "138": "Prunelia",
            "139": "Nyafia",
            "140": "Gildane",
            "141": "Herbil",
            "142": "Icelyn",
            "143": "Frostplume",
            "144": "Palumba",
            "145": "Braloha",
            "146": "Munchill",
            "147": "Polapup",
            "148": "Turtacle",
            "149": "Jellroy",
            "150": "Jelliette",
            "151": "Gloopie",
            "152": "Finsider",
            "153": "Ghangler",
            "154": "Whalaska",
            "155": "Neptilius"
        }
        
    def get_extraction_schema(self):
        """구조화된 데이터 추출을 위한 스키마"""
        return {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "팰의 한글 이름"},
                "englishName": {"type": "string", "description": "팰의 영어 이름"},
                "description": {"type": "string", "description": "팰 설명"},
                "type1": {"type": "string", "description": "첫 번째 속성"},
                "type2": {"type": "string", "description": "두 번째 속성 (선택사항)"},
                "hp": {"type": "string", "description": "체력"},
                "attack": {"type": "string", "description": "공격력"},
                "defense": {"type": "string", "description": "방어력"},
                "rarity": {"type": "string", "description": "희귀도"},
                "size": {"type": "string", "description": "크기"},
                "partnerSkill": {"type": "string", "description": "파트너 스킬"},
                "workSkills": {"type": "string", "description": "작업 스킬들"},
                "activeSkills": {"type": "string", "description": "전투 스킬들"},
                "dropItems": {"type": "string", "description": "드롭 아이템들"},
                "eggType": {"type": "string", "description": "알 타입"}
            },
            "required": ["name", "englishName"]
        }
    
    def save_progress(self, pal_id: str, data: Dict[str, Any]):
        """진행 상황을 JSON 파일로 저장"""
        self.crawled_data[pal_id] = {
            "timestamp": datetime.now().isoformat(),
            "data": data
        }
        
        progress_file = f"basic_pals_progress_{len(self.crawled_data)}.json"
        with open(progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.crawled_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 진행상황 저장: {progress_file}")
    
    def save_to_csv(self):
        """최종 결과를 CSV로 저장"""
        csv_filename = f"crawled_basic_pals_116_155_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        # 기존 CSV 구조와 맞추기 위한 필드 매핑
        fieldnames = [
            'id', 'name', 'englishName', 'description', 'type1', 'type2',
            'hp', 'attack', 'defense', 'rarity', 'size', 'foodAmount',
            'partnerSkill', 'work1', 'work2', 'work3', 'activeSkills',
            'dropItem1', 'dropItem2', 'eggType', 'imageFile'
        ]
        
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for pal_id, pal_info in self.crawled_data.items():
                data = pal_info['data']
                
                # 기본값 설정
                row = {
                    'id': pal_id,
                    'name': data.get('name', ''),
                    'englishName': data.get('englishName', ''),
                    'description': data.get('description', ''),
                    'type1': data.get('type1', ''),
                    'type2': data.get('type2', ''),
                    'hp': data.get('hp', ''),
                    'attack': data.get('attack', ''),
                    'defense': data.get('defense', ''),
                    'rarity': data.get('rarity', ''),
                    'size': data.get('size', ''),
                    'foodAmount': '3',  # 기본값
                    'partnerSkill': data.get('partnerSkill', ''),
                    'work1': data.get('workSkills', ''),
                    'work2': '',
                    'work3': '',
                    'activeSkills': data.get('activeSkills', ''),
                    'dropItem1': data.get('dropItems', ''),
                    'dropItem2': '',
                    'eggType': data.get('eggType', '일반 알'),
                    'imageFile': f"{pal_id}_menu.webp"
                }
                
                writer.writerow(row)
        
        print(f"✅ CSV 파일 생성: {csv_filename}")
        return csv_filename
    
    def print_summary(self):
        """크롤링 결과 요약 출력"""
        print("\n" + "="*50)
        print("🎯 기본 팰 (116-155번) 크롤링 결과 요약")
        print("="*50)
        print(f"📊 총 대상: {self.total_pals}개")
        print(f"✅ 성공: {self.success_count}개")
        print(f"❌ 실패: {len(self.failed_pals)}개")
        print(f"📈 성공률: {(self.success_count/self.total_pals)*100:.1f}%")
        
        if self.failed_pals:
            print(f"\n❌ 실패한 팰들:")
            for pal_id, english_name in self.failed_pals:
                print(f"   - {pal_id}: {english_name}")
        
        print(f"\n⏰ 완료 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*50)

def main():
    """메인 실행 함수"""
    print("🚀 기본 팰 (116-155번) 배치 크롤링 시작!")
    print("="*50)
    
    crawler = BasicPalBatchCrawler()
    
    # 이 스크립트는 실제 MCP Firecrawl 도구와 함께 실행되어야 합니다
    print("⚠️  주의: 이 스크립트는 MCP Firecrawl 도구와 함께 수동으로 실행해야 합니다.")
    print("📋 다음 단계:")
    print("1. 각 팰에 대해 MCP Firecrawl 도구를 호출")
    print("2. 결과를 JSON으로 저장")
    print("3. 최종 CSV 생성")
    print("\n🎯 목표: 40개 기본 팰 완전 크롤링")
    
    return crawler

if __name__ == "__main__":
    crawler = main() 