#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
스마트 팰 + 아종 통합 크롤러
각 팰의 원본과 모든 아종(B variants)을 자동으로 탐지하고 크롤링합니다.
"""

import requests
import json
import time
import re
from typing import List, Dict, Optional

def get_pal_variants(base_pal_name: str) -> List[str]:
    """
    주어진 기본 팰 이름으로부터 모든 아종들을 찾아서 반환합니다.
    """
    variants = []
    base_variants = [
        "_Ice", "_Ignis", "_Cryst", "_Lux", "_Terra", "_Noct", "_Botan",
        "_Fire", "_Electric", "_Ground", "_Dark", "_Grass", "_Water"
    ]
    
    # 기본 팰 추가
    variants.append(base_pal_name)
    
    # 모든 가능한 아종 suffix 시도
    for suffix in base_variants:
        variant_name = base_pal_name + suffix
        variants.append(variant_name)
    
    return variants

def crawl_pal_from_paldb(pal_name: str) -> Optional[Dict]:
    """
    paldb.cc에서 특정 팰의 정보를 크롤링합니다.
    """
    url = f"https://paldb.cc/ko/{pal_name}"
    
    try:
        response = requests.get(url)
        if response.status_code == 404:
            return None
            
        if response.status_code == 200:
            # 여기서 실제 파싱 로직 구현
            # 지금은 성공 여부만 확인
            print(f"✅ 발견: {pal_name}")
            return {"name": pal_name, "url": url, "status": "found"}
        else:
            return None
            
    except Exception as e:
        print(f"❌ 에러 ({pal_name}): {e}")
        return None

def get_base_pal_list() -> List[str]:
    """
    기본 팰 목록을 반환합니다. (1번부터 115번까지의 영어 이름)
    """
    base_pals = [
        "Lamball",        # 1
        "Cattiva",        # 2
        "Chikipi",        # 3
        "Lifmunk",        # 4
        "Foxparks",       # 5
        "Fuack",          # 6
        "Sparkit",        # 7
        "Tanzee",         # 8
        "Rooby",          # 9
        "Pengullet",      # 10
        "Penking",        # 11
        "Jolthog",        # 12
        "Gumoss",         # 13
        "Vixy",           # 14
        "Hoocrates",      # 15
        "Teafant",        # 16
        "Depresso",       # 17
        "Cremis",         # 18
        "Daedream",       # 19
        "Rushoar",        # 20
        "Nox",            # 21
        "Fuddler",        # 22
        "Killamari",      # 23
        "Mau",            # 24
        "Celaray",        # 25
        "Direhowl",       # 26
        "Tocotoco",       # 27
        "Flopie",         # 28
        "Mozzarina",      # 29
        "Bristla",        # 30
        "Gobfin",         # 31
        "Hangyu",         # 32
        "Mossanda",       # 33
        "Woolipop",       # 34
        "Caprity",        # 35
        "Melpaca",        # 36
        "Eikthyrdeer",    # 37
        "Nitewing",       # 38
        "Ribbuny",        # 39
        "Incineram",      # 40
        "Cinnamoth",      # 41
        "Arsox",          # 42
        "Dumud",          # 43
        "Cawgnito",       # 44
        "Leezpunk",       # 45
        "Loupmoon",       # 46
        "Galeclaw",       # 47
        "Robinquill",     # 48
        "Gorirat",        # 49
        "Beegarde",       # 50
        # ... 더 많은 팰들 (예시로 50개만)
    ]
    return base_pals

def smart_crawl_all_variants():
    """
    모든 기본 팰과 그들의 아종을 스마트하게 크롤링합니다.
    """
    base_pals = get_base_pal_list()
    all_found_pals = []
    all_found_variants = []
    
    print("🚀 스마트 팰 + 아종 통합 크롤링 시작!")
    print(f"📊 대상 기본 팰 수: {len(base_pals)}개")
    
    for i, base_pal in enumerate(base_pals, 1):
        print(f"\n[{i}/{len(base_pals)}] 🔍 {base_pal} 및 아종들 탐색 중...")
        
        # 해당 팰의 모든 가능한 아종들 생성
        variants = get_pal_variants(base_pal)
        
        found_for_this_pal = []
        
        for variant in variants:
            result = crawl_pal_from_paldb(variant)
            if result:
                found_for_this_pal.append(result)
                
                # 기본 팰인지 아종인지 구분
                if variant == base_pal:
                    all_found_pals.append(result)
                else:
                    all_found_variants.append(result)
            
            # 요청 간 간격 (서버 부하 방지)
            time.sleep(0.5)
        
        print(f"   📈 {base_pal}: {len(found_for_this_pal)}개 발견")
        
        # 10개마다 중간 결과 출력
        if i % 10 == 0:
            print(f"\n📊 중간 결과 ({i}개 완료):")
            print(f"   기본 팰: {len(all_found_pals)}개")
            print(f"   아종: {len(all_found_variants)}개")
    
    # 최종 결과
    print(f"\n🎉 크롤링 완료!")
    print(f"📊 최종 결과:")
    print(f"   기본 팰: {len(all_found_pals)}개")
    print(f"   아종(B variants): {len(all_found_variants)}개")
    print(f"   총계: {len(all_found_pals) + len(all_found_variants)}개")
    
    # 결과를 JSON 파일로 저장
    results = {
        "base_pals": all_found_pals,
        "variants": all_found_variants,
        "summary": {
            "base_count": len(all_found_pals),
            "variant_count": len(all_found_variants),
            "total_count": len(all_found_pals) + len(all_found_variants)
        }
    }
    
    with open("smart_crawl_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"💾 결과 저장: smart_crawl_results.json")
    
    return results

if __name__ == "__main__":
    smart_crawl_all_variants() 