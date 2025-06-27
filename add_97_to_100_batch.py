#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import os

def add_pals_97_to_100():
    """97번부터 100번까지의 팰 데이터를 기존 CSV에 추가"""
    
    # 기존 CSV 파일 읽기
    existing_file = 'complete_1_to_96_pals.csv'
    if not os.path.exists(existing_file):
        print(f"❌ {existing_file} 파일을 찾을 수 없습니다!")
        return
    
    df_existing = pd.read_csv(existing_file)
    print(f"✅ 기존 데이터 로드 완료: {len(df_existing)}개 팰")
    
    # 97번-100번 팰 데이터
    new_pals_data = [
        {
            # 97번 헬가루다 (Helzephyr)
            'id': 97,
            'name_kor': '헬가루다',
            'description_kor': '지옥에서 번개를 불러낸다. 헬가루다의 번개에 맞아 불타 죽으면 그 혼은 지옥에 떨어진다.',
            'elements': '어둠',
            'partnerSkill_name': '명부의 날개',
            'partnerSkill_describe': '등에 타고 하늘을 날 수 있다. 탑승 중 플레이어의 공격이 어둠 속성으로 변화한다.',
            'partnerSkill_needItem': '헬가루다 안장',
            'partnerSkill_needItemTechLevel': 33,
            'partnerSkill_level': 1,
            'stats_size': 'L',
            'stats_rarity': 7,
            'stats_health': 100,
            'stats_food': 525,
            'stats_meleeAttack': 100,
            'stats_attack': 125,
            'stats_defense': 100,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 190,
            'stats_goldCoin': 7840,
            'stats_egg': '암흑의 대형 알',
            'stats_code': 'HadesBird',
            'movement_slowWalkSpeed': 100,
            'movement_walkSpeed': 100,
            'movement_runSpeed': 700,
            'movement_rideSprintSpeed': 1100,
            'movement_transportSpeed': 450,
            'level60_health': '4075-5050',
            'level60_attack': '709-892',
            'level60_defense': '537-683',
            'activeSkills': '스피릿 파이어 Lv1|암흑구 Lv7|그림자 폭발 Lv15|화염 폭풍 Lv22|유령의 불꽃 Lv30|악몽의 구체 Lv40|어둠의 레이저 Lv50',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '독샘 1-3개 100%|중간 팰 영혼 1개 3%',
            'drops_count': 2,
            'workSuitabilities': '운반 Lv3',
            'workSuitabilities_count': 1,
            'tribes': '명부의 날개 헬가루다(보스)|헬가루다(일반)|라이가루다(변종)',
            'tribes_count': 3,
            'spawners': '2_1_forest_1 Lv25-28|2_1_forest_3 Lv25-28|2_1_forest_4 Lv24-26',
            'spawners_count': 3
        },
        {
            # 98번 라바드래곤 (Astegon)
            'id': 98,
            'name_kor': '라바드래곤',
            'description_kor': '심연에서 온 난폭한 존재. 그대, 이 용 앞에 서지 말지어다. 그대, 이 용의 울음에 귀를 막을지어다.',
            'elements': '용|어둠',
            'partnerSkill_name': '검은 갑옷의 용',
            'partnerSkill_describe': '등에 타고 하늘을 날 수 있다. 탑승 중 광석에 주는 피해량이 증가하며 금속 광석의 획득량이 증가한다.',
            'partnerSkill_needItem': '라바드래곤 안장',
            'partnerSkill_needItemTechLevel': 47,
            'partnerSkill_level': 1,
            'stats_size': 'XL',
            'stats_rarity': 9,
            'stats_health': 100,
            'stats_food': 600,
            'stats_meleeAttack': 100,
            'stats_attack': 125,
            'stats_defense': 125,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 150,
            'stats_goldCoin': 8200,
            'stats_egg': '용의 거대한 알',
            'stats_code': 'BlackMetalDragon',
            'movement_slowWalkSpeed': 100,
            'movement_walkSpeed': 150,
            'movement_runSpeed': 700,
            'movement_rideSprintSpeed': 1100,
            'movement_transportSpeed': 375,
            'level60_health': '4075-5050',
            'level60_attack': '709-892',
            'level60_defense': '659-842',
            'activeSkills': '용 대포 Lv1|유령의 불꽃 Lv7|용의 파장 Lv15|악몽의 구체 Lv22|용의 숨결 Lv30|펀치 브레스 Lv35|어둠의 레이저 Lv40|용의 운석 Lv50',
            'activeSkills_count': 8,
            'passiveSkills': '단단한 피부 (방어 +10%)',
            'passiveSkills_count': 1,
            'drops': '팰 금속 주괴 1-2개 100%|순수한 석영 3-5개 100%',
            'drops_count': 2,
            'workSuitabilities': '수작업 Lv1|채굴 Lv4',
            'workSuitabilities_count': 2,
            'tribes': '강철의 용왕 라바드래곤(보스)|라바드래곤(일반)',
            'tribes_count': 2,
            'spawners': '제3 사냥 금지 구역 Lv40-45',
            'spawners_count': 1
        },
        {
            # 99번 데스 스팅 (Menasting)
            'id': 99,
            'name_kor': '데스 스팅',
            'description_kor': '본체는 에너지 덩어리로 속이 비었다. 산 채로 먹잇감 속으로 스며들어 흡수한다. 주변엔 지옥 같은 신음이 끝없이 울려 퍼진다.',
            'elements': '어둠|땅',
            'partnerSkill_name': '스틸 스콜피온',
            'partnerSkill_describe': '함께 싸우는 동안 플레이어의 방어력이 증가하고 번개 속성 팰을 쓰러뜨렸을 때 드롭 아이템 획득량이 증가한다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': 1,
            'stats_size': 'L',
            'stats_rarity': 9,
            'stats_health': 100,
            'stats_food': 475,
            'stats_meleeAttack': 100,
            'stats_attack': 100,
            'stats_defense': 130,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 260,
            'stats_goldCoin': 7050,
            'stats_egg': '암흑의 거대한 알',
            'stats_code': 'DarkScorpion',
            'movement_slowWalkSpeed': 100,
            'movement_walkSpeed': 200,
            'movement_runSpeed': 1000,
            'movement_rideSprintSpeed': 1200,
            'movement_transportSpeed': 600,
            'level60_health': '4075-5050',
            'level60_attack': '587-733',
            'level60_defense': '683-873',
            'activeSkills': '모래 돌풍 Lv1|독 사격 Lv7|그림자 폭발 Lv15|바위 대포 Lv22|악몽의 구체 Lv30|점프 찌르기 Lv35|바위 창 Lv40|어둠의 레이저 Lv50',
            'activeSkills_count': 8,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '석탄 10개 100%|독샘 5-10개 100%',
            'drops_count': 2,
            'workSuitabilities': '벌목 Lv2|채굴 Lv3',
            'workSuitabilities_count': 2,
            'tribes': '뭐든지 꿰뚫는 창 데스 스팅(보스)|데스 스팅(일반)|골드 스팅(변종)',
            'tribes_count': 3,
            'spawners': '제2 사냥 금지 구역 Lv40-45|sakurajima_6_1_NorthDesert Lv50-51|sakurajima_6_5_SouthDesert Lv50-51|Sakurajima_grade_01 암흑의 거대한 알',
            'spawners_count': 4
        },
        {
            # 100번 아누비스 (Anubis)
            'id': 100,
            'name_kor': '아누비스',
            'description_kor': '그 풍모 덕택에 일찍이 고귀한 자의 상징이었다. 부와 권력을 멀리하는 이에게도 귀감이었으나 언제부턴가 아누비스는 죽음의 상징이 되었다.',
            'elements': '땅',
            'partnerSkill_name': '사막의 수호신',
            'partnerSkill_describe': '함께 싸우는 동안 플레이어의 공격이 땅 속성으로 변화한다. 전투 중에 가끔씩 고속 스텝으로 공격을 회피한다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': 1,
            'stats_size': 'M',
            'stats_rarity': 10,
            'stats_health': 120,
            'stats_food': 400,
            'stats_meleeAttack': 130,
            'stats_attack': 130,
            'stats_defense': 100,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 570,
            'stats_goldCoin': 4960,
            'stats_egg': '거친 느낌의 거대한 알',
            'stats_code': 'Anubis',
            'movement_slowWalkSpeed': 80,
            'movement_walkSpeed': 160,
            'movement_runSpeed': 800,
            'movement_rideSprintSpeed': 1000,
            'movement_transportSpeed': 480,
            'level60_health': '4725-5895',
            'level60_attack': '733-923',
            'level60_defense': '537-683',
            'activeSkills': '바위 폭발 Lv1|파워 폭탄 Lv7|모래 폭풍 Lv15|스핀 레그 러쉬 Lv22|포스 드라이브 Lv30|그라운드 스매셔 Lv40|바위 창 Lv50',
            'activeSkills_count': 7,
            'passiveSkills': '지제 (땅 속성 공격 피해 증가 20%)',
            'passiveSkills_count': 1,
            'drops': '뼈 3-5개 100%|대형 팰 영혼 1개 100%|혁신적인 기술서 1개 5%',
            'drops_count': 3,
            'workSuitabilities': '수작업 Lv4|채굴 Lv3|운반 Lv2',
            'workSuitabilities_count': 3,
            'tribes': '저무는 태양의 수호자 아누비스(보스)|아누비스(일반)',
            'tribes_count': 2,
            'spawners': '',
            'spawners_count': 0
        }
    ]
    
    # 새 데이터를 DataFrame으로 변환
    df_new = pd.DataFrame(new_pals_data)
    
    # 기존 데이터와 새 데이터 합치기
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    
    # 새로운 파일로 저장
    new_filename = 'complete_1_to_100_pals.csv'
    df_combined.to_csv(new_filename, index=False, encoding='utf-8-sig')
    
    print(f"🎉 97-100번 팰 데이터 추가 완료!")
    print(f"📂 파일명: {new_filename}")
    print(f"📊 총 데이터: {len(df_combined)}개 팰")
    print(f"✨ 새로 추가된 팰들:")
    for pal in new_pals_data:
        print(f"   - {pal['id']:3d}번 {pal['name_kor']} ({pal['elements']} 속성)")

if __name__ == "__main__":
    add_pals_97_to_100() 