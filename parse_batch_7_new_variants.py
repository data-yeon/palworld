#!/usr/bin/env python3
import pandas as pd
import json

def parse_pal_data(raw_data, pal_id, pal_name, english_name):
    """새로운 팰 데이터를 파싱하는 함수"""
    # 기본 데이터 구조 생성
    pal_data = {
        "id": pal_id,
        "name": pal_name,
        "englishName": english_name,
        "types": [],
        "imageFilename": f"{pal_id}_menu.webp",
        "suitabilities": [],
        "drops": [],
        "aReadMe": "",
        "stats": {},
        "breeding": {},
        "activeSkills": [],
        "passiveSkills": []
    }
    
    return pal_data

def create_new_variants():
    """새로 발견한 3개 B variants 데이터 생성"""
    
    # 89B 블루파카 (Kingpaca_Cryst)
    blue_kingpaca = {
        "id": "89B",
        "name": "블루파카",
        "englishName": "Kingpaca_Cryst",
        "types": ["얼음"],
        "imageFilename": "89B_menu.webp",
        "suitabilities": [
            {"type": "채집", "level": 1},
            {"type": "냉각", "level": 3}
        ],
        "drops": [
            {"name": "양털", "quantity": 5},
            {"name": "빙결 기관", "quantity": "3-6"}
        ],
        "aReadMe": "냉담한 성격으로 감정 표현이 서투르다. 외톨이인 개체는 멜파카와의 의사소통이 너무 서툴렀던 슬픈 개체다.",
        "stats": {
            "HP": 120,
            "ATK": 85,
            "DEF": 90,
            "WorkSpeed": 100,
            "Rarity": 9,
            "Size": "XL",
            "FoodAmount": 7
        },
        "breeding": {
            "CombiRank": 440,
            "EggType": "얼어붙은 거대한 알"
        },
        "activeSkills": [
            "얼음 미사일",
            "얼음 칼날", 
            "빙산",
            "킹 프레스",
            "서리 낀 입김",
            "물폭탄",
            "눈보라 스파이크"
        ],
        "passiveSkills": [],
        "partnerSkill": "파워풀 킹 - 등에 타고 이동할 수 있다. 보유하고 있는 동안 블루파카이가 짐을 대신 짊어져 플레이어의 소지 중량 제한이 증가한다."
    }
    
    # 90B 블리자모스 (Mammorest_Cryst)
    blizzmorest = {
        "id": "90B",
        "name": "블리자모스",
        "englishName": "Mammorest_Cryst",
        "types": ["얼음", "땅"],
        "imageFilename": "90B_menu.webp",
        "suitabilities": [
            {"type": "벌목", "level": 2},
            {"type": "채굴", "level": 2},
            {"type": "냉각", "level": 2}
        ],
        "drops": [
            {"name": "고급 팰 기름", "quantity": "5-10"},
            {"name": "가죽", "quantity": "5-10"},
            {"name": "그린모스의 거대 고기", "quantity": 2}
        ],
        "aReadMe": "등 위의 식물은 개체마다 제각각이다. 멸종한 줄 알았던 식물이 얼어붙은 채로 블리자모스의 등에서 발견되는 경우도 있다.",
        "stats": {
            "HP": 150,
            "ATK": 85,
            "DEF": 90,
            "WorkSpeed": 100,
            "Rarity": 9,
            "Size": "XL",
            "FoodAmount": 8
        },
        "breeding": {
            "CombiRank": 290,
            "EggType": "얼어붙은 거대한 알"
        },
        "activeSkills": [
            "바위 대포",
            "얼음 칼날",
            "파워 폭탄", 
            "빙산",
            "대지 강타",
            "서리 낀 입김",
            "눈보라 스파이크"
        ],
        "passiveSkills": [],
        "partnerSkill": "아이스 크래셔 - 등에 타고 이동할 수 있다. 탑승 중 나무와 광석 파괴 효율이 향상된다."
    }
    
    # 86B 스프라돈 (Broncherry_Aqua)
    spradon = {
        "id": "86B",
        "name": "스프라돈",
        "englishName": "Broncherry_Aqua",
        "types": ["풀", "물"],
        "imageFilename": "86B_menu.webp",
        "suitabilities": [
            {"type": "관개", "level": 3}
        ],
        "drops": [
            {"name": "라브라돈의 공룡고기", "quantity": 2},
            {"name": "양상추 씨", "quantity": "1-2"},
            {"name": "감자 종자", "quantity": 1}
        ],
        "aReadMe": "교미 전후로 체취가 크게 달라진다. 파트너를 발견한 뒤엔 좋은 향기가 나 '순결의 향기'라고 불린다.",
        "stats": {
            "HP": 120,
            "ATK": 95,
            "DEF": 100,
            "WorkSpeed": 100,
            "Rarity": 8,
            "Size": "XL",
            "FoodAmount": 7
        },
        "breeding": {
            "CombiRank": 840,
            "EggType": "신록의 거대한 알"
        },
        "activeSkills": [
            "아쿠아 샷",
            "버블 샷",
            "몸통 박치기",
            "씨앗 지뢰",
            "가시덩굴",
            "물폭탄",
            "하이드로 스트림"
        ],
        "passiveSkills": [],
        "partnerSkill": "애정 과적재 - 등에 타고 이동할 수 있다. 보유하고 있는 동안 스프라돈이가 짐을 대신 짊어져 플레이어의 소지 중량 제한이 증가한다."
    }
    
    return [blue_kingpaca, blizzmorest, spradon]

def convert_to_csv_format(pal_data):
    """팰 데이터를 CSV 형식으로 변환"""
    
    # 타입들을 문자열로 변환
    types_str = json.dumps(pal_data["types"], ensure_ascii=False) if pal_data["types"] else "[]"
    
    # 작업 적성을 문자열로 변환
    suitabilities_str = json.dumps([
        {"type": suit["type"], "level": suit["level"]} 
        for suit in pal_data["suitabilities"]
    ], ensure_ascii=False) if pal_data["suitabilities"] else "[]"
    
    # 드롭 아이템을 문자열로 변환
    drops_str = json.dumps([
        {"name": drop["name"], "quantity": drop["quantity"]}
        for drop in pal_data["drops"]
    ], ensure_ascii=False) if pal_data["drops"] else "[]"
    
    # 액티브 스킬을 문자열로 변환
    active_skills_str = json.dumps(pal_data["activeSkills"], ensure_ascii=False) if pal_data["activeSkills"] else "[]"
    
    # 패시브 스킬을 문자열로 변환  
    passive_skills_str = json.dumps(pal_data["passiveSkills"], ensure_ascii=False) if pal_data["passiveSkills"] else "[]"
    
    return {
        "id": pal_data["id"],
        "name": pal_data["name"],
        "englishName": pal_data["englishName"],
        "types": types_str,
        "imageFilename": pal_data["imageFilename"],
        "suitabilities": suitabilities_str,
        "drops": drops_str,
        "aReadMe": pal_data["aReadMe"],
        "stats": json.dumps(pal_data["stats"], ensure_ascii=False),
        "breeding": json.dumps(pal_data["breeding"], ensure_ascii=False),
        "activeSkills": active_skills_str,
        "passiveSkills": passive_skills_str,
        "partnerSkill": pal_data.get("partnerSkill", "")
    }

def main():
    print("🚀 Batch 7 새로운 B variants 통합 시작...")
    
    # 기존 CSV 파일 읽기
    try:
        df_existing = pd.read_csv('enhanced_complete_pals_batch5.csv')
        print(f"✅ 기존 데이터 로드 완료: {len(df_existing)}개 팰")
    except FileNotFoundError:
        print("❌ enhanced_complete_pals_batch5.csv 파일을 찾을 수 없습니다!")
        return
    
    # 새로운 B variants 생성
    new_variants = create_new_variants()
    
    # CSV 형식으로 변환
    new_rows = []
    for variant in new_variants:
        csv_row = convert_to_csv_format(variant)
        new_rows.append(csv_row)
        print(f"✅ {variant['id']} {variant['name']} 변환 완료")
    
    # 새로운 데이터프레임 생성 및 기존 데이터와 결합
    df_new = pd.DataFrame(new_rows)
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    
    # 새로운 CSV 파일로 저장
    output_file = 'enhanced_complete_pals_batch7.csv'
    df_combined.to_csv(output_file, index=False, encoding='utf-8')
    
    print(f"🎉 Batch 7 통합 완료!")
    print(f"📊 총 팰 수: {len(df_existing)} → {len(df_combined)} (+{len(new_rows)})")
    print(f"💾 저장된 파일: {output_file}")
    
    # B variants 개수 확인
    b_variants = df_combined[df_combined['id'].str.contains('B', na=False)]
    print(f"🔢 현재 B variants: {len(b_variants)}개")

if __name__ == "__main__":
    main() 