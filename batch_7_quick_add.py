#!/usr/bin/env python3
import csv

def add_new_variants():
    """새로운 B variants를 기존 CSV에 빠르게 추가"""
    
    # 새로운 B variants 데이터 (간단한 형태)
    new_variants = [
        {
            "id": "86B",
            "name": "스프라돈", 
            "englishName": "Broncherry_Aqua",
            "types": '["풀", "물"]',
            "stats": '{"HP": 120, "ATK": 95, "DEF": 100, "Rarity": 8, "Size": "XL", "FoodAmount": 7}',
            "suitabilities": '[{"type": "관개", "level": 3}]',
            "drops": '[{"name": "라브라돈의 공룡고기", "quantity": 2}]',
            "activeSkills": '["아쿠아 샷", "버블 샷", "몸통 박치기", "씨앗 지뢰", "가시덩굴", "물폭탄", "하이드로 스트림"]',
            "partnerSkill": "애정 과적재 - 등에 타고 이동할 수 있다",
            "aReadMe": "교미 전후로 체취가 크게 달라진다. 파트너를 발견한 뒤엔 좋은 향기가 나 순결의 향기라고 불린다"
        },
        {
            "id": "89B", 
            "name": "블루파카",
            "englishName": "Kingpaca_Cryst",
            "types": '["얼음"]',
            "stats": '{"HP": 120, "ATK": 85, "DEF": 90, "Rarity": 9, "Size": "XL", "FoodAmount": 7}',
            "suitabilities": '[{"type": "채집", "level": 1}, {"type": "냉각", "level": 3}]',
            "drops": '[{"name": "양털", "quantity": 5}, {"name": "빙결 기관", "quantity": "3-6"}]',
            "activeSkills": '["얼음 미사일", "얼음 칼날", "빙산", "킹 프레스", "서리 낀 입김", "물폭탄", "눈보라 스파이크"]',
            "partnerSkill": "파워풀 킹 - 등에 타고 이동할 수 있다. 소지 중량 제한이 증가한다",
            "aReadMe": "냉담한 성격으로 감정 표현이 서투르다. 외톨이인 개체는 멜파카와의 의사소통이 너무 서툴렀던 슬픈 개체다"
        },
        {
            "id": "90B",
            "name": "블리자모스", 
            "englishName": "Mammorest_Cryst",
            "types": '["얼음", "땅"]',
            "stats": '{"HP": 150, "ATK": 85, "DEF": 90, "Rarity": 9, "Size": "XL", "FoodAmount": 8}',
            "suitabilities": '[{"type": "벌목", "level": 2}, {"type": "채굴", "level": 2}, {"type": "냉각", "level": 2}]',
            "drops": '[{"name": "고급 팰 기름", "quantity": "5-10"}, {"name": "가죽", "quantity": "5-10"}]',
            "activeSkills": '["바위 대포", "얼음 칼날", "파워 폭탄", "빙산", "대지 강타", "서리 낀 입김", "눈보라 스파이크"]',
            "partnerSkill": "아이스 크래셔 - 등에 타고 이동할 수 있다. 탑승 중 나무와 광석 파괴 효율이 향상된다",
            "aReadMe": "등 위의 식물은 개체마다 제각각이다. 멸종한 줄 알았던 식물이 얼어붙은 채로 블리자모스의 등에서 발견되는 경우도 있다"
        }
    ]
    
    # 기존 가장 간단한 형태의 완전한 CSV 찾기
    base_files = [
        'complete_1_to_115_pals.csv',
        'complete_1_to_111_pals.csv', 
        'complete_1_to_108_pals.csv'
    ]
    
    base_file = None
    for file in base_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                f.readline()  # 헤더 확인
                base_file = file
                break
        except FileNotFoundError:
            continue
    
    if not base_file:
        print("❌ 기본 CSV 파일을 찾을 수 없습니다!")
        return
    
    print(f"📁 기본 파일: {base_file}")
    
    # 새로운 파일명 생성
    output_file = 'enhanced_complete_pals_batch7_quick.csv'
    
    # 기존 파일 복사 후 새로운 항목 추가
    with open(base_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        
        # 기존 내용 전체 복사
        content = infile.read()
        outfile.write(content)
        
        # 새로운 B variants 추가 (간단한 형태)
        for variant in new_variants:
            # 간단한 CSV 라인 작성
            line = f'{variant["id"]},{variant["name"]},{variant["englishName"]},{variant["types"]},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,{variant["activeSkills"]},,,,{variant["drops"]},,{variant["suitabilities"]},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,{variant["partnerSkill"]},{variant["aReadMe"]}\n'
            outfile.write(line)
    
    print(f"🎉 Batch 7 Quick 추가 완료!")
    print(f"💾 저장된 파일: {output_file}")
    print(f"➕ 추가된 B variants: {len(new_variants)}개")
    
    for variant in new_variants:
        print(f"   - {variant['id']} {variant['name']} ({variant['englishName']})")

if __name__ == "__main__":
    add_new_variants() 