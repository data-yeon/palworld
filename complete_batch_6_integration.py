#!/usr/bin/env python3
"""
Palworld Batch 6 Complete Integration
새로 발견된 4개 B variants를 모두 CSV에 추가
"""

import csv
import os

def get_new_b_variants():
    """
    새로 발견된 B variants 데이터 정의
    """
    variants = [
        {
            'ID': '71B',
            'Name': '시로카바네',
            'EnglishName': 'Vanwyrm_Cryst',
            'Description': '시로카바네의 외골격으로 만든 피리 소리는 천 개의 봉우리를 건넌다고 한다. 고대의 전쟁에선 승리의 나팔로 사용했다.',
            'Type1': '얼음',
            'Type2': '어둠',
            'PartnerSkill': '하늘에서 온 습격자',
            'PartnerSkillDesc': '등에 타고 하늘을 날 수 있다. 탑승 중 플레이어가 적의 약점 부위를 공격할 때 주는 피해량이 증가한다.',
            'HP': '90',
            'ATK': '120',
            'DEF': '95',
            'WorkSpeed': '100',
            'Rarity': '5',
            'Size': 'L',
            'FoodAmount': '6',
            'Work1': '냉각 Lv2',
            'Work2': '운반 Lv3',
            'Work3': '',
            'DropItem1': '뼈',
            'DropItem2': '빙결 기관',
            'ActiveSkills': '공기 대포, 얼음 미사일, 얼음 칼날, 서리 낀 입김, 플라잉 블리자드, 악몽의 구체, 눈보라 스파이크, 어둠의 레이저',
        },
        {
            'ID': '84B',
            'Name': '시니에노',
            'EnglishName': 'Blazehowl_Noct',
            'Description': '평범한 고기를 좋아하지만 항상 오염된 고기를 먹는다. 암흑의 발톱을 무기로 삼은 탓에 잡은 먹이가 저주받는다는 걸 깨닫지 못했기 때문이다.',
            'Type1': '화염',
            'Type2': '어둠',
            'PartnerSkill': '검은 불 사자',
            'PartnerSkillDesc': '등에 타고 이동할 수 있다. 함께 싸우는 동안 무속성 팰을 쓰러뜨렸을 때 드롭 아이템 획득량이 증가한다.',
            'HP': '105',
            'ATK': '115',
            'DEF': '80',
            'WorkSpeed': '100',
            'Rarity': '8',
            'Size': 'L',
            'FoodAmount': '7',
            'Work1': '불 피우기 Lv3',
            'Work2': '벌목 Lv2',
            'Work3': '',
            'DropItem1': '발화 기관',
            'DropItem2': '',
            'ActiveSkills': '그림자 폭발, 불화살, 파이어 브레스, 유령의 불꽃, 인페르노, 화산의 일격, 화염구, 어둠의 레이저',
        },
        {
            'ID': '91B',
            'Name': '트로피티',
            'EnglishName': 'Wumpo_Botan',
            'Description': '정체를 밝혀내려고 연구자가 풀을 벴지만 애초부터 안엔 아무것도 없었다는 듯 풀만 남아 있었다.',
            'Type1': '풀',
            'Type2': '',
            'PartnerSkill': '남국의 거인',
            'PartnerSkillDesc': '등에 타고 이동할 수 있다. 보유하고 있는 동안 트로피티가 짐을 대신 짊어져 플레이어의 소지 중량 제한이 증가한다.',
            'HP': '140',
            'ATK': '80',
            'DEF': '110',
            'WorkSpeed': '100',
            'Rarity': '8',
            'Size': 'L',
            'FoodAmount': '8',
            'Work1': '파종 Lv1',
            'Work2': '수작업 Lv2',
            'Work3': '벌목 Lv3',
            'DropItem1': '양상추 씨',
            'DropItem2': '토마토 씨',
            'ActiveSkills': '바람의 칼날, 아쿠아 샷, 씨앗 지뢰, 초록 폭풍, 가시덩굴, 풀덩이 굴리기, 물폭탄, 태양 폭발',
        },
        {
            'ID': '104B',
            'Name': '루나퀸',
            'EnglishName': 'Lyleen_Noct',
            'Description': '기품이 넘치는 우아한 팰. 무례한 녀석에겐 눈물이 쏙 빠지는 따귀를 날린다. 그걸 노리는 팰도 더러 있다.',
            'Type1': '어둠',
            'Type2': '',
            'PartnerSkill': '희미한 빛의 여신',
            'PartnerSkillDesc': '발동하면 여왕의 치유력으로 플레이어의 HP를 대폭 회복한다.',
            'HP': '110',
            'ATK': '110',
            'DEF': '115',
            'WorkSpeed': '100',
            'Rarity': '10',
            'Size': 'L',
            'FoodAmount': '6',
            'Work1': '수작업 Lv3',
            'Work2': '채집 Lv2',
            'Work3': '제약 Lv3',
            'DropItem1': '하급 의약품',
            'DropItem2': '예쁜 꽃',
            'ActiveSkills': '암흑구, 얼음 칼날, 그림자 폭발, 서리 낀 입김, 악몽의 구체, 눈보라 스파이크, 어둠의 레이저',
        }
    ]
    
    return variants

def add_all_variants_to_csv():
    """
    모든 새로운 B variants를 CSV에 추가
    """
    new_variants = get_new_b_variants()
    
    # 기존 CSV 파일 읽기
    input_file = 'enhanced_complete_pals_batch5.csv'
    output_file = 'enhanced_complete_pals_batch6.csv'
    
    if not os.path.exists(input_file):
        print(f"❌ 입력 파일을 찾을 수 없습니다: {input_file}")
        return
    
    # CSV 읽기
    rows = []
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows.append(header)
        
        # 기존 데이터 추가
        for row in reader:
            rows.append(row)
    
    # 새로운 variants 추가
    for variant in new_variants:
        new_row = []
        for field in header:
            if field in variant:
                new_row.append(str(variant[field]))
            else:
                new_row.append('')  # 매칭되지 않는 필드는 빈 값
        
        rows.append(new_row)
    
    # 새 CSV 파일 작성
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    
    print(f"✅ Batch 6 완성! 총 {len(new_variants)}개 B variants 추가됨")
    print(f"📁 출력 파일: {output_file}")
    print(f"📊 총 {len(rows)-1}개 팰 (이전 {len(rows)-1-len(new_variants)}개 + 새로운 {len(new_variants)}개)")
    
    # 요약 정보 출력
    print(f"\n🆕 새로 추가된 B variants:")
    for i, variant in enumerate(new_variants, 1):
        print(f"{i:2d}. {variant['ID']} {variant['Name']} ({variant['EnglishName']})")
        print(f"    타입: {variant['Type1']}" + (f", {variant['Type2']}" if variant['Type2'] else ""))
        print(f"    스탯: HP {variant['HP']}, 공격 {variant['ATK']}, 방어 {variant['DEF']}")
    
    # 전체 B variants 현황
    print(f"\n📈 B variants 진행 현황:")
    print(f"   이전: 22개 B variants")
    print(f"   추가: {len(new_variants)}개 B variants")
    print(f"   현재: {22 + len(new_variants)}개 B variants")
    print(f"   완성도: {((22 + len(new_variants)) / 59 * 100):.1f}% (목표: 59개)")

if __name__ == "__main__":
    print("🎮 Palworld Batch 6 Complete Integration")
    print("=" * 50)
    
    add_all_variants_to_csv() 