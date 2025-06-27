#!/usr/bin/env python3
"""
팰월드 누락 팰 배치 크롤링 스크립트
MCP Firecrawl을 활용하여 92개 누락 팰 데이터 수집
"""

import json
import time
import csv
import os
from datetime import datetime
from typing import Dict, List, Any, Optional
import requests

class PalBatchCrawler:
    def __init__(self):
        self.base_url = "https://palworld.fandom.com/wiki/"
        self.crawled_data = {}
        self.failed_pals = []
        self.session_start = datetime.now()
        
        # 누락된 팰 목록 정의
        self.missing_pals = self.get_missing_pal_list()
        
    def get_missing_pal_list(self) -> Dict[str, List[str]]:
        """누락된 팰 목록을 카테고리별로 반환"""
        return {
            "basic_pals": [str(i) for i in range(116, 156)],  # 116-155
            "b_variants": [
                "23B", "24B", "25B", "31B", "32B", "33B", "35B", "37B", "39B", "40B",
                "43B", "45B", "58B", "61B", "62B", "64B", "65B", "72B", "75B", "76B",
                "80B", "81B", "82B", "83B", "85B", "86B", "88B", "89B", "90B", "92B",
                "95B", "99B", "101B", "102B", "105B", "112B", "116B", "148B", "152B", "153B", "154B"
            ],
            "s_series": [f"S{i}" for i in range(1, 12)]  # S1-S11
        }
    
    def get_pal_wiki_url(self, pal_id: str) -> str:
        """팰 ID를 기반으로 위키 URL 생성"""
        # 기본 팰 (숫자만)
        if pal_id.isdigit():
            # 기존 데이터에서 영어 이름 매핑 필요
            pal_name_mapping = {
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
            return f"{self.base_url}{pal_name_mapping.get(pal_id, f'Pal_{pal_id}')}"
        
        # B 아종 팰들
        elif 'B' in pal_id:
            base_num = pal_id.replace('B', '')
            # B 아종 매핑 로직 (기존 데이터 참조 필요)
            return f"{self.base_url}Pal_{pal_id}"
            
        # S 시리즈
        elif pal_id.startswith('S'):
            s_mapping = {
                "S1": "Green_Slime",
                "S2": "Blue_Slime", 
                "S3": "Red_Slime",
                "S4": "Purple_Slime",
                "S5": "Illuminant_Slime",
                "S6": "Rainbow_Slime",
                "S7": "Enchanted_Sword",
                "S8": "Cave_Bat",
                "S9": "Illuminant_Bat",
                "S10": "Eye_of_Cthulhu",
                "S11": "Demon_Eye"
            }
            return f"{self.base_url}{s_mapping.get(pal_id, f'Special_{pal_id}')}"
        
        return f"{self.base_url}Pal_{pal_id}"
    
    def crawl_single_pal(self, pal_id: str) -> Optional[Dict[str, Any]]:
        """MCP Firecrawl을 사용하여 단일 팰 데이터 크롤링"""
        url = self.get_pal_wiki_url(pal_id)
        
        try:
            print(f"🔍 크롤링 중: {pal_id} ({url})")
            
            # MCP Firecrawl 호출 (실제 구현 시 MCP 도구 사용)
            # 여기서는 구조를 보여주는 예시
            pal_data = self.extract_pal_data_from_url(url, pal_id)
            
            if pal_data:
                print(f"✅ 성공: {pal_id} - {pal_data.get('name', 'Unknown')}")
                return pal_data
            else:
                print(f"❌ 실패: {pal_id} - 데이터 추출 실패")
                self.failed_pals.append(pal_id)
                return None
                
        except Exception as e:
            print(f"❌ 오류: {pal_id} - {str(e)}")
            self.failed_pals.append(pal_id)
            return None
    
    def extract_pal_data_from_url(self, url: str, pal_id: str) -> Optional[Dict[str, Any]]:
        """URL에서 팰 데이터 추출 (MCP Firecrawl 래퍼)"""
        # 실제 MCP Firecrawl 호출 로직
        # 여기서는 구조만 보여줌
        
        # 기본 데이터 구조
        pal_data = {
            "id": pal_id,
            "name": "",
            "englishName": "",
            "description": "",
            "type1": "",
            "type2": "",
            "hp": "",
            "attack": "",
            "defense": "",
            "rarity": "",
            "size": "",
            "foodAmount": "",
            "partnerSkill": "",
            "work1": "",
            "work2": "",
            "work3": "",
            "activeSkills": "",
            "dropItem1": "",
            "dropItem2": "",
            "eggType": "",
            "imageFile": f"{pal_id}_menu.webp"
        }
        
        # TODO: 실제 MCP Firecrawl 구현
        # extracted_data = mcp_firecrawl.scrape(url, extract_schema=pal_schema)
        
        return pal_data
    
    def batch_crawl_category(self, category: str, pal_list: List[str], batch_size: int = 5):
        """카테고리별 배치 크롤링"""
        print(f"\n🚀 {category} 카테고리 크롤링 시작 ({len(pal_list)}개)")
        
        for i in range(0, len(pal_list), batch_size):
            batch = pal_list[i:i + batch_size]
            print(f"\n📦 배치 {i//batch_size + 1}: {batch}")
            
            for pal_id in batch:
                pal_data = self.crawl_single_pal(pal_id)
                if pal_data:
                    self.crawled_data[pal_id] = pal_data
                
                # 요청 간 딜레이 (위키 서버 보호)
                time.sleep(1)
            
            # 배치 간 더 긴 딜레이
            time.sleep(3)
            
            # 진행상황 저장
            self.save_progress(category, i + batch_size)
    
    def save_progress(self, category: str, completed_count: int):
        """진행상황을 JSON 파일로 저장"""
        progress_data = {
            "timestamp": datetime.now().isoformat(),
            "session_start": self.session_start.isoformat(),
            "category": category,
            "completed_count": completed_count,
            "crawled_data": self.crawled_data,
            "failed_pals": self.failed_pals,
            "total_crawled": len(self.crawled_data)
        }
        
        filename = f"missing_pals_progress_{category}_{completed_count}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(progress_data, f, ensure_ascii=False, indent=2)
        
        print(f"💾 진행상황 저장됨: {filename}")
    
    def run_full_crawl(self):
        """전체 누락 팰 크롤링 실행"""
        print("=" * 60)
        print("🎯 팰월드 누락 팰 배치 크롤링 시작")
        print(f"📅 시작 시간: {self.session_start.strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        
        total_missing = sum(len(pal_list) for pal_list in self.missing_pals.values())
        print(f"📊 총 누락 팰: {total_missing}개")
        
        for category, pal_list in self.missing_pals.items():
            print(f"   - {category}: {len(pal_list)}개")
        
        # 카테고리별 순차 크롤링
        for category, pal_list in self.missing_pals.items():
            self.batch_crawl_category(category, pal_list)
        
        # 최종 결과 저장
        self.save_final_results()
        self.generate_csv_output()
        
        print("\n" + "=" * 60)
        print("🎉 크롤링 완료!")
        print(f"✅ 성공: {len(self.crawled_data)}개")
        print(f"❌ 실패: {len(self.failed_pals)}개")
        if self.failed_pals:
            print(f"실패 목록: {', '.join(self.failed_pals)}")
        print("=" * 60)
    
    def save_final_results(self):
        """최종 결과를 JSON으로 저장"""
        final_results = {
            "crawl_session": {
                "start_time": self.session_start.isoformat(),
                "end_time": datetime.now().isoformat(),
                "total_attempted": sum(len(pal_list) for pal_list in self.missing_pals.values()),
                "total_success": len(self.crawled_data),
                "total_failed": len(self.failed_pals)
            },
            "crawled_data": self.crawled_data,
            "failed_pals": self.failed_pals
        }
        
        filename = f"missing_pals_final_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(final_results, f, ensure_ascii=False, indent=2)
        
        print(f"💾 최종 결과 저장됨: {filename}")
    
    def generate_csv_output(self):
        """크롤링 결과를 CSV로 변환"""
        if not self.crawled_data:
            print("⚠️ 크롤링된 데이터가 없어 CSV 생성을 건너뜁니다.")
            return
        
        filename = f"missing_pals_crawled_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        # CSV 필드명 (기존 데이터와 호환)
        fieldnames = [
            "id", "name", "englishName", "description", "type1", "type2",
            "hp", "attack", "defense", "rarity", "size", "foodAmount",
            "partnerSkill", "work1", "work2", "work3", "activeSkills",
            "dropItem1", "dropItem2", "eggType", "imageFile"
        ]
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for pal_data in self.crawled_data.values():
                writer.writerow(pal_data)
        
        print(f"📄 CSV 파일 생성됨: {filename}")

def main():
    """메인 실행 함수"""
    crawler = PalBatchCrawler()
    crawler.run_full_crawl()

if __name__ == "__main__":
    main() 