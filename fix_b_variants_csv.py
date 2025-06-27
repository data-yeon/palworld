#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
컬럼명을 기존 CSV와 맞춰서 B 변종들을 추가하는 스크립트
5B 아이호, 6B 적부리, 10B 뎅키 추가
"""

import csv

def add_b_variants_fixed():
    """기존 CSV에 B 변종들을 추가 (컬럼명 맞춤)"""
    
    print("🔥 기존 CSV에 B 변종들 추가 시작!")
    
    # 기존 CSV 읽기
    existing_data = []
    try:
        with open('final_1_to_10_pals_without_nick.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            existing_data = list(reader)
        print(f"📄 기존 데이터 {len(existing_data)}개 읽기 완료")
    except FileNotFoundError:
        print("❌ 기존 CSV 파일을 찾을 수 없습니다.")
        return
    
    # B 변종 데이터 (기존 컬럼명으로 맞춤)
    b_variants = [
        {
            'id': '5B',
            'name_kor': '아이호',
            'description_kor': '태어난 직후엔 냉기를 잘 못 다뤄서 걸핏하면 냉기를 뿜다가 숨이 탁 막힌다. 감기에 걸리면 콧물이 어는 바람에 숨이 가빠진다.',
            'elements': '얼음 속성',
            'partnerSkill_name': '포옹 프로스트',
            'partnerSkill_describe': '발동하면 플레이어에게 장착되어 냉기를 방출해 공격할 수 있다.',
            'partnerSkill_needItem': '기술24',
            'partnerSkill_needItemTechLevel': '24',
            'partnerSkill_level': '1',
            'stats_size': 'XS',
            'stats_rarity': '1',
            'stats_health': '65',
            'stats_food': '150',
            'stats_meleeAttack': '70',
            'stats_attack': '80',
            'stats_defense': '70',
            'stats_workSpeed': '100',
            'stats_support': '100',
            'stats_captureRateCorrect': '1.1',
            'stats_maleProbability': '50',
            'stats_combiRank': '1305',
            'stats_goldCoin': '1410',
            'stats_egg': '얼어붙은 알',
            'stats_code': 'Kitsunebi_Ice',
            'movement_slowWalkSpeed': '40',
            'movement_walkSpeed': '80',
            'movement_runSpeed': '400',
            'movement_rideSprintSpeed': '550',
            'movement_transportSpeed': '240',
            'level60_health': '2937 – 3571',
            'level60_attack': '490 – 607',
            'level60_defense': '391 – 493',
            'activeSkills': 'Lv1 얼음 미사일 (위력:30) | Lv15 얼음 칼날 (위력:55)',
            'activeSkills_count': '2',
            'passiveSkills': '',
            'passiveSkills_count': '0',
            'drops': '가죽 x1–2 (100%) | 빙결 기관 x1–3 (100%)',
            'drops_count': '2',
            'workSuitabilities': '냉각 LV.1',
            'workSuitabilities_count': '1',
            'tribes': '여로를 수놓는 얼음꽃 아이호 (Tribe Boss) | 아이호 (Tribe Normal)',
            'tribes_count': '2',
            'spawners': 'Lv52–55 yamijima_7_2_DarkArea',
            'spawners_count': '1'
        },
        {
            'id': '6B',
            'name_kor': '적부리',
            'description_kor': '배의 마찰력이 아주 강한 탓에 보디 서핑을 하면 불이 붙을 정도다. 너무 신나게 미끄러지다 간혹 불덩이가 되기도 한다.',
            'elements': '물 속성|화염 속성',
            'partnerSkill_name': '파이어 태클',
            'partnerSkill_describe': '발동하면 적부리이(가) 적을 향해 파이어 서핑을 하며 달려든다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '0',
            'partnerSkill_level': '1',
            'stats_size': 'XS',
            'stats_rarity': '2',
            'stats_health': '60',
            'stats_food': '150',
            'stats_meleeAttack': '100',
            'stats_attack': '85',
            'stats_defense': '60',
            'stats_workSpeed': '100',
            'stats_support': '100',
            'stats_captureRateCorrect': '1.1',
            'stats_maleProbability': '50',
            'stats_combiRank': '1290',
            'stats_goldCoin': '1340',
            'stats_egg': '축축한 알',
            'stats_code': 'BluePlatypus_Fire',
            'movement_slowWalkSpeed': '70',
            'movement_walkSpeed': '105',
            'movement_runSpeed': '300',
            'movement_rideSprintSpeed': '400',
            'movement_transportSpeed': '202',
            'level60_health': '2775 – 3360',
            'level60_attack': '514 – 638',
            'level60_defense': '342 – 430',
            'activeSkills': 'Lv1 파이어 샷 (위력:30) | Lv15 버블 샷 (위력:65)',
            'activeSkills_count': '2',
            'passiveSkills': '',
            'passiveSkills_count': '0',
            'drops': '가죽 x1 (100%) | 팰의 체액 x1 (100%) | 발화 기관 x1–2 (50%)',
            'drops_count': '3',
            'workSuitabilities': '불 피우기 LV.1 | 관개 LV.1 | 수작업 LV.1 | 운반 LV.1',
            'workSuitabilities_count': '4',
            'tribes': '폭주 중인 파도 타는 꼬맹이 적부리 (Tribe Boss) | 적부리 (Tribe Normal)',
            'tribes_count': '2',
            'spawners': 'Lv16–27 커다란 낚시터 Medium 8.72%',
            'spawners_count': '1'
        },
        {
            'id': '10B',
            'name_kor': '뎅키',
            'description_kor': '날개가 완전히 퇴화해 날 수 없다. 하늘을 향한 미련은 어느덧 질투로 변화하여 하늘을 나는 모든 것을 격추할 전기의 힘을 얻게 되었다!',
            'elements': '물 속성|번개 속성',
            'partnerSkill_name': '뎅키 발사기',
            'partnerSkill_describe': '발동하면 로켓 발사기을(를) 장착하여 뎅키을(를) 탄환 삼아 발사한다. 착탄하여 폭발하면 뎅키이(가) 빈사 상태가 된다.',
            'partnerSkill_needItem': '기술39',
            'partnerSkill_needItemTechLevel': '39',
            'partnerSkill_level': '1',
            'stats_size': 'XS',
            'stats_rarity': '2',
            'stats_health': '70',
            'stats_food': '150',
            'stats_meleeAttack': '100',
            'stats_attack': '80',
            'stats_defense': '70',
            'stats_workSpeed': '100',
            'stats_support': '100',
            'stats_captureRateCorrect': '0.9',
            'stats_maleProbability': '50',
            'stats_combiRank': '1310',
            'stats_goldCoin': '1290',
            'stats_egg': '축축한 알',
            'stats_code': 'Penguin_Electric',
            'movement_slowWalkSpeed': '30',
            'movement_walkSpeed': '60',
            'movement_runSpeed': '500',
            'movement_rideSprintSpeed': '650',
            'movement_transportSpeed': '265',
            'level60_health': '3100 – 3782',
            'level60_attack': '490 – 607',
            'level60_defense': '391 – 493',
            'activeSkills': 'Lv1 번개 창 (위력:30) | Lv15 버블 샷 (위력:65)',
            'activeSkills_count': '2',
            'passiveSkills': '',
            'passiveSkills_count': '0',
            'drops': '발전 기관 x1–2 (100%) | 팰의 체액 x1 (100%)',
            'drops_count': '2',
            'workSuitabilities': '관개 LV.1 | 발전 LV.2 | 수작업 LV.1 | 운반 LV.1',
            'workSuitabilities_count': '4',
            'tribes': '과음한 뎅키 (Tribe Boss) | 뎅키 (Tribe Normal)',
            'tribes_count': '2',
            'spawners': 'Lv16–27 커다란 낚시터 Medium 9.96%',
            'spawners_count': '1'
        }
    ]
    
    # 모든 데이터 합치기 (기존 + 새로운 B 변종들)
    all_data = existing_data + b_variants
    
    # ID별로 정렬 (1, 2, 3, 4, 5, 5B, 6, 6B, 7, 8, 9, 10, 10B)
    def sort_key(item):
        pal_id = item['id']
        if 'B' in pal_id:
            base_num = int(pal_id.replace('B', ''))
            return (base_num, 1)  # B 변종은 기본 팰 다음에
        else:
            return (int(pal_id), 0)  # 기본 팰이 먼저
    
    all_data.sort(key=sort_key)
    
    # 새로운 CSV 생성
    filename = 'complete_1_to_10_with_b_variants.csv'
    
    if all_data:
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=all_data[0].keys())
            writer.writeheader()
            writer.writerows(all_data)
        
        print(f"\n🎉 완성! {filename} 파일 생성 완료!")
        print(f"📋 총 {len(all_data)}개 팰 데이터 (1-10 + B변종들)")
        print(f"📊 컬럼 수: {len(all_data[0].keys())}개")
        
        # 파일 내용 미리보기
        print(f"\n📄 팰 순서:")
        for i, row in enumerate(all_data):
            print(f"  {i+1}. {row['id']} - {row['name_kor']} ({row['elements']})")
    
    else:
        print("❌ 생성할 데이터가 없습니다.")

if __name__ == "__main__":
    add_b_variants_fixed() 