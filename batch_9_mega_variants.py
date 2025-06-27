#!/usr/bin/env python3
import csv

def add_batch_9_variants():
    """4개의 새로운 B variants를 기존 CSV에 추가 (Batch 9)"""
    
    # 새로운 B variants 데이터 (Batch 9)
    new_variants = [
        {
            "id": "40B",
            "name": "아비스고트", 
            "englishName": "Incineram_Noct",
            "types": '["어둠"]',
            "stats": '{"HP": 95, "ATK": 105, "DEF": 85, "Rarity": 5, "Size": "M", "FoodAmount": 4}',
            "suitabilities": '[{"type": "수작업", "level": 2}, {"type": "채굴", "level": 1}, {"type": "운반", "level": 2}]',
            "drops": '[{"name": "뿔", "quantity": 1}, {"name": "가죽", "quantity": 1}]',
            "activeSkills": '["파이어 샷", "스피릿 파이어", "불화살", "지옥불 할퀴기", "그림자 폭발", "화염구", "인페르노"]',
            "partnerSkill": "암흑 발톱의 사냥꾼 - 발동하면 목표로 삼은 적을 향해 높은 위력의 지옥불 할퀴기로 공격한다",
            "aReadMe": "어린 팰만 노려 자기 구역에 데리고 간다. 아이를 빼앗긴 부모 팰이 얼마나 절망에 빠졌을지 상상도 안 된다",
            "breeding": '{"Unique": "헬고트 + 고스호스 = 아비스고트"}',
            "imageFilename": "40B_menu.webp"
        },
        {
            "id": "58B",
            "name": "사라블랙",
            "englishName": "Pyrin_Noct", 
            "types": '["화염", "어둠"]',
            "stats": '{"HP": 100, "ATK": 95, "DEF": 90, "Rarity": 7, "Size": "L", "FoodAmount": 5}',
            "suitabilities": '[{"type": "불 피우기", "level": 2}, {"type": "벌목", "level": 1}]',
            "drops": '[{"name": "발화 기관", "quantity": "4-5"}, {"name": "가죽", "quantity": "2-3"}]',
            "activeSkills": '["파이어 샷", "그림자 폭발", "파이어 브레스", "유령의 불꽃", "어둠의 돌격", "인페르노", "어둠의 레이저"]',
            "partnerSkill": "흑토마 - 등에 타고 이동할 수 있다. 탑승 중 플레이어의 공격이 어둠 속성으로 변화한다",
            "aReadMe": "정체불명의 암흑 물질을 태워 에너지로 삼으며 남은 어둠의 입자를 전신에서 방출한다. 누군가 탑승하면 그가 어둠에 물들지 않도록, 눈치 있게 배려하는 면도 있다",
            "breeding": '{"Unique": "파이린 + 캐티메이지 = 사라블랙"}',
            "imageFilename": "58B_menu.webp"
        },
        {
            "id": "85B",
            "name": "핑피롱",
            "englishName": "Relaxaurus_Lux",
            "types": '["용", "번개"]',
            "stats": '{"HP": 110, "ATK": 110, "DEF": 75, "Rarity": 9, "Size": "XL", "FoodAmount": 7}',
            "suitabilities": '[{"type": "발전", "level": 3}, {"type": "운반", "level": 1}]',
            "drops": '[{"name": "고급 팰 기름", "quantity": "1-4"}, {"name": "발전 기관", "quantity": "2-3"}, {"name": "사파이어", "quantity": 1}]',
            "activeSkills": '["스파크 샷", "용 대포", "전기 파장", "라인 썬더", "용의 숨결", "번개 일격", "전기 볼트"]',
            "partnerSkill": "미사일 파티 - 등에 타고 이동할 수 있다. 탑승 중 미사일 발사기 연사가 가능해진다",
            "aReadMe": "헤로롱은 생각했다. 슬슬 자신을 바꿀 때라고. 그 순간 전신에 전기가 흘렀다!",
            "breeding": '{"Unique": "헤로롱 + 번개냥 = 핑피롱"}',
            "imageFilename": "85B_menu.webp"
        },
        {
            "id": "99B",
            "name": "골드 스팅",
            "englishName": "Menasting_Terra",
            "types": '["땅"]',
            "stats": '{"HP": 100, "ATK": 105, "DEF": 130, "Rarity": 10, "Size": "L", "FoodAmount": 7}',
            "suitabilities": '[{"type": "벌목", "level": 2}, {"type": "채굴", "level": 3}]',
            "drops": '[{"name": "원유", "quantity": 1}, {"name": "발화 기관", "quantity": "1-2"}]',
            "activeSkills": '["모래 돌풍", "바위 폭발", "바위 대포", "모래 폭풍", "점프 찌르기", "바위 창", "암석 폭발"]',
            "partnerSkill": "스틸 스콜피온 - 함께 싸우는 동안 플레이어의 방어력이 증가하고 번개 속성 팰을 쓰러뜨렸을 때 드롭 아이템 획득량이 증가한다",
            "aReadMe": "본체는 에너지 덩어리로 속이 비었다. 토사나 광물을 외피 속에 채워 압도적인 질량을 보여준다. 공격한 상대는 지옥 같은 신음을 내지를 수밖에 없다",
            "breeding": '{"Unique": "데스 스팅 + 테라나이트 = 골드 스팅"}',
            "imageFilename": "99B_menu.webp"
        }
    ]
    
    # 기존 CSV 파일 읽기
    try:
        with open('enhanced_complete_pals_batch8_mega.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            existing_data = list(reader)
            fieldnames = reader.fieldnames or []
        print(f"✅ 기존 데이터 로드 완료: {len(existing_data)}개 팰")
        if not fieldnames:
            print("❌ CSV 파일의 fieldnames를 읽을 수 없습니다!")
            return
    except FileNotFoundError:
        print("❌ enhanced_complete_pals_batch8_mega.csv 파일을 찾을 수 없습니다!")
        return
    
    # 새로운 데이터 추가
    for variant in new_variants:
        # 기존 fieldnames에 맞춘 기본값으로 채우기
        new_row = {field: '' for field in fieldnames}
        new_row.update(variant)
        existing_data.append(new_row)
        print(f"✅ {variant['id']} {variant['name']} 추가 완료")
    
    # 새로운 CSV 파일 생성
    output_filename = 'enhanced_complete_pals_batch9_mega.csv'
    with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(existing_data)
    
    print(f"\n🎉 Batch 9 완료!")
    print(f"📊 총 팰 개수: {len(existing_data)}개")
    print(f"💾 파일명: {output_filename}")
    
    # B variants 개수 계산
    b_variants = [row for row in existing_data if 'B' in row.get('id', '')]
    print(f"🔢 B variants: {len(b_variants)}개")
    print(f"📈 완성도: {len(b_variants)}/59 = {len(b_variants)/59*100:.1f}%")

if __name__ == "__main__":
    add_batch_9_variants() 