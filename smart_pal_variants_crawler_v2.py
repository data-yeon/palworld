#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
스마트 팰 + 아종 통합 크롤러 v2
firecrawl을 사용해서 각 팰의 원본과 모든 아종(B variants)을 자동으로 탐지하고 크롤링합니다.
"""

import json
import time
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

def get_first_50_base_pals() -> List[str]:
    """
    기본 팰 목록 처음 50개를 반환합니다.
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
    ]
    return base_pals

def test_smart_variants():
    """
    스마트 아종 탐지 테스트 - 처음 10개 팰로 시작
    """
    base_pals = get_first_50_base_pals()[:10]  # 처음 10개만 테스트
    found_variants = []
    
    print("🚀 스마트 아종 탐지 테스트 시작!")
    print(f"📊 테스트 대상: {len(base_pals)}개 팰")
    
    for i, base_pal in enumerate(base_pals, 1):
        print(f"\n[{i}/{len(base_pals)}] 🔍 {base_pal} 아종 탐색...")
        
        # 해당 팰의 모든 가능한 아종들 생성
        variants = get_pal_variants(base_pal)
        
        # 각 아종이 존재하는지 확인 (URL 체크만)
        for variant in variants:
            url = f"https://paldb.cc/ko/{variant}"
            print(f"   🔗 체크: {variant}")
            
            # 여기서는 URL만 생성하고 실제 크롤링은 하지 않음
            # 실제로는 firecrawl을 사용해서 체크할 예정
            if variant == base_pal:
                print(f"   ✅ 기본형: {variant}")
                found_variants.append({"type": "base", "name": variant, "url": url})
            else:
                # 아종은 실제 존재 여부를 확인해야 함
                print(f"   🤔 아종 후보: {variant}")
                found_variants.append({"type": "variant", "name": variant, "url": url, "status": "to_check"})
    
    print(f"\n📊 테스트 결과:")
    base_count = len([v for v in found_variants if v["type"] == "base"])
    variant_count = len([v for v in found_variants if v["type"] == "variant"])
    print(f"   기본형: {base_count}개")
    print(f"   아종 후보: {variant_count}개")
    print(f"   총 체크 대상: {len(found_variants)}개")
    
    # 결과 저장
    with open("smart_test_results.json", "w", encoding="utf-8") as f:
        json.dump(found_variants, f, ensure_ascii=False, indent=2)
    
    print(f"💾 결과 저장: smart_test_results.json")
    print("\n💡 다음 단계: firecrawl로 실제 존재 여부 확인!")
    
    return found_variants

if __name__ == "__main__":
    test_smart_variants() 