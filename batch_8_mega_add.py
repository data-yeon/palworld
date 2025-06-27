#!/usr/bin/env python3
import csv

def add_batch_8_variants():
    """8개의 새로운 B variants를 기존 CSV에 추가"""
    
    # 새로운 B variants 데이터 (Batch 8)
    new_variants = [
        {
            "id": "80B",
            "name": "실티아", 
            "englishName": "Elphidran_Aqua",
            "types": '["용", "물"]',
            "stats": '{"HP": 115, "ATK": 80, "DEF": 95, "Rarity": 8, "Size": "L", "FoodAmount": 6}',
            "suitabilities": '[{"type": "관개", "level": 3}, {"type": "벌목", "level": 2}]',
            "drops": '[{"name": "고급 팰 기름", "quantity": "2-3"}]',
            "activeSkills": '["아쿠아 샷", "용 대포", "용의 파장", "신비의 허리케인", "산성비", "하이드로 스트림", "용의 운석"]',
            "partnerSkill": "아량을 베푸는 수룡 - 등에 타고 하늘을 날 수 있다. 하늘을 나는 동안 이동 속도가 상승한다",
            "aReadMe": "겉모습처럼 천진난만한 성격이다. 그래서인지 어떤 행동에도 악의가 없어서 누군가를 죽여도 별생각이 없을 정도다"
        },
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
        },
        {
            "id": "95B",
            "name": "포레스키", 
            "englishName": "Quivern_Botan",
            "types": '["용", "풀"]',
            "stats": '{"HP": 105, "ATK": 105, "DEF": 100, "Rarity": 8, "Size": "L", "FoodAmount": 4}',
            "suitabilities": '[{"type": "파종", "level": 2}, {"type": "수작업", "level": 1}, {"type": "채집", "level": 2}, {"type": "채굴", "level": 2}, {"type": "운반", "level": 3}]',
            "drops": '[{"name": "고급 팰 기름", "quantity": 3}, {"name": "예쁜 꽃", "quantity": "2-3"}]',
            "activeSkills": '["용 대포", "바람의 칼날", "씨앗 기관총", "용의 숨결", "초록 폭풍", "혜성", "원형 덩굴"]',
            "partnerSkill": "초룡의 자애 - 등에 타고 하늘을 날 수 있으며 탑승 중 풀 속성 공격이 강화된다",
            "aReadMe": "포레스키를 안고 있을 때 햇님과 초원의 향기가 난다면 내일 날씨는 맑다. 아직 축축한 냄새가 난다면 내일은 장대비가 온다"
        },
        {
            "id": "101B",
            "name": "아그니드라", 
            "englishName": "Jormuntide_Ignis",
            "types": '["용", "화염"]',
            "stats": '{"HP": 130, "ATK": 130, "DEF": 100, "Rarity": 9, "Size": "XL", "FoodAmount": 7}',
            "suitabilities": '[{"type": "불 피우기", "level": 4}]',
            "drops": '[{"name": "고급 팰 기름", "quantity": "2-3"}, {"name": "발화 기관", "quantity": "2-3"}]',
            "activeSkills": '["파이어 샷", "용 대포", "화염 폭풍", "파이어 브레스", "트라이 썬더", "용암뱀", "화염구", "용의 운석"]',
            "partnerSkill": "폭풍을 부르는 용암룡 - 등에 타고 이동할 수 있다. 탑승 중 화염 속성 공격이 강화된다",
            "aReadMe": "억울한 누명으로 화산에 떨어진 전사가 아그니드라로 환생하여 한 나라를 모조리 불살라버렸다는 전설이 있다"
        },
        {
            "id": "102B",
            "name": "시바", 
            "englishName": "Suzaku_Aqua",
            "types": '["물"]',
            "stats": '{"HP": 125, "ATK": 105, "DEF": 105, "Rarity": 9, "Size": "XL", "FoodAmount": 8}',
            "suitabilities": '[{"type": "관개", "level": 3}]',
            "drops": '[{"name": "팰의 체액", "quantity": 5}]',
            "activeSkills": '["워터 제트", "얼음 미사일", "아쿠아 샷", "서리 낀 입김", "물폭탄", "눈보라 스파이크", "하이드로 스트림"]',
            "partnerSkill": "물의 날개 - 등에 타고 하늘을 날 수 있으며 탑승 중 물 속성 공격이 강화된다",
            "aReadMe": "옛날에는 우기를 불러오는 존재로 여겨졌다. 지난 해에 수해가 발생했다면 다음 해의 안전을 기원하며 이 녀석을 집요하게 사냥하곤 했다"
        },
        {
            "id": "105B",
            "name": "이시스", 
            "englishName": "Faleris_Aqua",
            "types": '["물"]',
            "stats": '{"HP": 100, "ATK": 110, "DEF": 110, "Rarity": 9, "Size": "L", "FoodAmount": 8}',
            "suitabilities": '[{"type": "관개", "level": 4}, {"type": "운반", "level": 3}]',
            "drops": '[{"name": "팰의 체액", "quantity": "2-4"}]',
            "activeSkills": '["워터 제트", "버블 샷", "산성비", "라인 스플래시", "월 스플래시", "봉황의 파도", "하이드로 스트림"]',
            "partnerSkill": "썰물의 포식자 - 등에 타고 하늘을 날 수 있다. 함께 싸우는 동안 화염 속성 팰을 쓰러뜨렸을 때 드롭 아이템 획득량이 증가한다",
            "aReadMe": "무리 지어 다니는 사냥감을 발견하면 급류를 만들어 주변 일대를 모조리 휩쓸어 버린다. 정작 휩쓸린 사냥감을 못 찾는 경우가 허다하기에 이걸 사냥이라고 불러도 될지는 알 수 없다"
        }
    ]
    
    # 기존 파일 사용
    base_file = 'enhanced_complete_pals_batch7_quick.csv'
    output_file = 'enhanced_complete_pals_batch8_mega.csv'
    
    try:
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
        
        print(f"🎉 Batch 8 MEGA 통합 완료!")
        print(f"💾 저장된 파일: {output_file}")
        print(f"➕ 추가된 B variants: {len(new_variants)}개")
        print(f"📊 이전 126개 → 현재 {126 + len(new_variants)}개 (+{len(new_variants)})")
        
        print(f"\n🆕 새로 추가된 B variants:")
        for variant in new_variants:
            print(f"   - {variant['id']} {variant['name']} ({variant['englishName']})")
            
        total_b_variants = 29 + len(new_variants)  # 이전 29개 + 새로운 8개
        print(f"\n🔢 현재 총 B variants: {total_b_variants}개")
        print(f"📈 완성도: {total_b_variants}/59 = {(total_b_variants/59)*100:.1f}%")
        
    except FileNotFoundError:
        print(f"❌ {base_file} 파일을 찾을 수 없습니다!")

if __name__ == "__main__":
    add_batch_8_variants() 