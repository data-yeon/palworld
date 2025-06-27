#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import os

def add_pals_101_to_104():
    """101번부터 104번까지의 팰 데이터를 기존 CSV에 추가"""
    
    # 기존 CSV 파일 읽기
    existing_file = 'complete_1_to_100_pals.csv'
    if not os.path.exists(existing_file):
        print(f"❌ {existing_file} 파일을 찾을 수 없습니다!")
        return
    
    df_existing = pd.read_csv(existing_file)
    print(f"✅ 기존 데이터 로드 완료: {len(df_existing)}개 팰")
    
    # 101번-104번 팰 데이터
    new_pals_data = [
        {
            # 101번 레비드라 (Jormuntide)
            'id': 101,
            'name_kor': '레비드라',
            'description_kor': '억울한 누명으로 소용돌이치는 물속에 떨어진 현자가 레비드라(으)로 환생하여 나라를 멸망시켰다는 전설이 있다.',
            'elements': '용|물',
            'partnerSkill_name': '폭풍을 부르는 해룡',
            'partnerSkill_describe': '등에 타고 물 위를 이동할 수 있다. 탑승 중 수상 이동으로 인한 기력 소비를 무효화한다.',
            'partnerSkill_needItem': '레비드라 안장',
            'partnerSkill_needItemTechLevel': 39,
            'partnerSkill_level': 1,
            'stats_size': 'XL',
            'stats_rarity': 8,
            'stats_health': 130,
            'stats_food': 475,
            'stats_meleeAttack': 150,
            'stats_attack': 120,
            'stats_defense': 100,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1.0,
            'stats_maleProbability': 50.0,
            'stats_combiRank': 310,
            'stats_goldCoin': 9320,
            'stats_egg': '용의 거대한 알',
            'stats_code': 'Umihebi',
            'movement_slowWalkSpeed': 100,
            'movement_walkSpeed': 175,
            'movement_runSpeed': 600,
            'movement_rideSprintSpeed': 1000,
            'movement_transportSpeed': 350,
            'level60_health': '5050-6317',
            'level60_attack': '685-860',
            'level60_defense': '537-683',
            'activeSkills': '아쿠아 샷|용 대포|용의 숨결|물폭탄|트라이 썬더|바다뱀|하이드로 스트림|용의 운석',
            'activeSkills_count': 8,
            'passiveSkills': '해황',
            'passiveSkills_count': 1,
            'drops': '팰의 체액',
            'drops_count': 1,
            'workSuitabilities': '관개 Lv4',
            'workSuitabilities_count': 1,
            'tribes': '해상의 패자 레비드라|레비드라|아그니드라',
            'tribes_count': 3,
            'spawners': '무',
            'spawners_count': 0
        },
        {
            # 102번 주작 (Suzaku)
            'id': 102,
            'name_kor': '주작',
            'description_kor': '옛날에는 건기를 불러오는 존재로 여겨졌다. 지난 해에 가물었다면 다음 해의 풍작을 기원하며 이 녀석을 집요하게 사냥하곤 했다.',
            'elements': '화염',
            'partnerSkill_name': '화염의 날개',
            'partnerSkill_describe': '등에 타고 하늘을 날 수 있으며 탑승 중 화염 속성 공격이 강화된다.',
            'partnerSkill_needItem': '주작 안장',
            'partnerSkill_needItemTechLevel': 41,
            'partnerSkill_level': 1,
            'stats_size': 'XL',
            'stats_rarity': 8,
            'stats_health': 120,
            'stats_food': 525,
            'stats_meleeAttack': 100,
            'stats_attack': 105,
            'stats_defense': 105,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1.0,
            'stats_maleProbability': 50.0,
            'stats_combiRank': 50,
            'stats_goldCoin': 9840,
            'stats_egg': '열기 나는 거대한 알',
            'stats_code': 'Suzaku',
            'movement_slowWalkSpeed': 100,
            'movement_walkSpeed': 200,
            'movement_runSpeed': 850,
            'movement_rideSprintSpeed': 1100,
            'movement_transportSpeed': 450,
            'level60_health': '4725-5895',
            'level60_attack': '611-765',
            'level60_defense': '561-715',
            'activeSkills': '공기 대포|파이어 샷|스피릿 파이어|불화살|파이어 브레스|화염 폭풍|화염구',
            'activeSkills_count': 7,
            'passiveSkills': '무',
            'passiveSkills_count': 0,
            'drops': '발화 기관',
            'drops_count': 1,
            'workSuitabilities': '불 피우기 Lv3',
            'workSuitabilities_count': 1,
            'tribes': '하늘의 왕자 주작|주작|시바',
            'tribes_count': 3,
            'spawners': '4_1_dessert_1 Lv40-42|desert_grade_01 열기 나는 거대한 알',
            'spawners_count': 2
        },
        {
            # 103번 일렉판다 (Grizzbolt)
            'id': 103,
            'name_kor': '일렉판다',
            'description_kor': '호쾌한 얼굴에 듬직한 체구를 가졌으며 친구로 인정한 상대에겐 순종적이다. 하지만 어쩐 일인지 미니건만 맡기면 돌변한다.',
            'elements': '번개',
            'partnerSkill_name': '노란 중전차',
            'partnerSkill_describe': '등에 타고 이동할 수 있다. 탑승 중 미니건 연사가 가능해진다.',
            'partnerSkill_needItem': '일렉판다 미니건',
            'partnerSkill_needItemTechLevel': 40,
            'partnerSkill_level': 1,
            'stats_size': 'L',
            'stats_rarity': 8,
            'stats_health': 105,
            'stats_food': 475,
            'stats_meleeAttack': 120,
            'stats_attack': 100,
            'stats_defense': 100,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1.0,
            'stats_maleProbability': 50.0,
            'stats_combiRank': 200,
            'stats_goldCoin': 7720,
            'stats_egg': '찌릿찌릿한 거대한 알',
            'stats_code': 'ElecPanda',
            'movement_slowWalkSpeed': 80,
            'movement_walkSpeed': 140,
            'movement_runSpeed': 600,
            'movement_rideSprintSpeed': 1000,
            'movement_transportSpeed': 210,
            'level60_health': '4237-5261',
            'level60_attack': '587-733',
            'level60_defense': '537-683',
            'activeSkills': '스파크 샷|전기 파장|전기 할퀴기|라인 썬더|트라이 썬더|번개 일격|전기 볼트|뇌격의 중전차',
            'activeSkills_count': 8,
            'passiveSkills': '무',
            'passiveSkills_count': 0,
            'drops': '발전 기관|가죽',
            'drops_count': 2,
            'workSuitabilities': '발전 Lv3|수작업 Lv2|벌목 Lv2|운반 Lv3',
            'workSuitabilities_count': 4,
            'tribes': '레인 밀렵단 간부 조이&일렉판다|천둥의 쌍발톱 일렉판다|일렉판다',
            'tribes_count': 3,
            'spawners': '제1 사냥 금지 구역 Lv18-22',
            'spawners_count': 1
        },
        {
            # 104번 릴린 (Lyleen)
            'id': 104,
            'name_kor': '릴린',
            'description_kor': '자애심으로 가득한 온화한 팰. 부모를 잃은 어린 팰들을 돌봐주고 있다. 버릇은 전력으로 쏘는 태양 폭발.',
            'elements': '풀',
            'partnerSkill_name': '풍요의 여신',
            'partnerSkill_describe': '발동하면 여왕의 치유력으로 플레이어의 HP를 대폭 회복한다.',
            'partnerSkill_needItem': '무',
            'partnerSkill_needItemTechLevel': 0,
            'partnerSkill_level': 1,
            'stats_size': 'L',
            'stats_rarity': 9,
            'stats_health': 110,
            'stats_food': 400,
            'stats_meleeAttack': 100,
            'stats_attack': 110,
            'stats_defense': 105,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1.0,
            'stats_maleProbability': 30.0,
            'stats_combiRank': 250,
            'stats_goldCoin': 7160,
            'stats_egg': '신록의 거대한 알',
            'stats_code': 'LilyQueen',
            'movement_slowWalkSpeed': 60,
            'movement_walkSpeed': 100,
            'movement_runSpeed': 450,
            'movement_rideSprintSpeed': 550,
            'movement_transportSpeed': 275,
            'level60_health': '4400-5472',
            'level60_attack': '636-797',
            'level60_defense': '561-715',
            'activeSkills': '바람의 칼날|씨앗 기관총|씨앗 지뢰|물폭탄|초록 폭풍|가시덩굴|태양 폭발|풍양의 가호',
            'activeSkills_count': 8,
            'passiveSkills': '정령왕',
            'passiveSkills_count': 1,
            'drops': '하급 의약품|예쁜 꽃|혁신적인 기술서',
            'drops_count': 3,
            'workSuitabilities': '파종 Lv4|수작업 Lv3|채집 Lv2|제약 Lv3',
            'workSuitabilities_count': 4,
            'tribes': '팰 애호 단체 창시자 릴리&릴린|백합의 여제 릴린|릴린|루나퀸',
            'tribes_count': 4,
            'spawners': '2_1_forest_test Lv15-18|제3 사냥 금지 구역 Lv40-45|sakurajima_6_7_FlowerGarden Lv50-51|5_2_island_shipwreck_BOSS Lv35-45|Sakurajima_grade_01 신록의 거대한 알|습격 18-99 Lv39',
            'spawners_count': 6
        }
    ]
    
    # 새로운 데이터를 DataFrame으로 변환
    df_new = pd.DataFrame(new_pals_data)
    
    # 기존 데이터와 새 데이터 결합
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    
    # 새 파일명 생성
    output_file = 'complete_1_to_104_pals.csv'
    
    # CSV 파일로 저장
    df_combined.to_csv(output_file, index=False, encoding='utf-8-sig')
    
    print(f"🎉 완료! {output_file} 파일이 생성되었습니다!")
    print(f"📊 총 {len(df_combined)}개의 팰 데이터가 포함되어 있습니다")
    print(f"✨ 새로 추가된 팰: 101번 레비드라, 102번 주작, 103번 일렉판다, 104번 릴린")

if __name__ == "__main__":
    add_pals_101_to_104() 