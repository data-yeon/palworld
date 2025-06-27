#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import os

def add_pals_81_to_84():
    """81번부터 84번까지의 팰 데이터를 기존 CSV에 추가"""
    
    # 기존 CSV 파일 읽기
    existing_file = 'complete_1_to_80_pals.csv'
    if not os.path.exists(existing_file):
        print(f"❌ {existing_file} 파일을 찾을 수 없습니다!")
        return
    
    df_existing = pd.read_csv(existing_file)
    print(f"✅ 기존 데이터 로드 완료: {len(df_existing)}개 팰")
    
    # 81번-84번 팰 데이터
    new_pals_data = [
        {
            # 81번 켈시 (Kelpsea)
            'id': 81,
            'name_kor': '켈시',
            'description_kor': '태어난 장소의 수질에 따라 성격이 달라진다. 더러운 웅덩이에서 태어난 켈시은(는) 대체로 성격이 나쁘고 흉악하기 일쑤다.',
            'elements': '물',
            'partnerSkill_name': '물 뿌리기',
            'partnerSkill_describe': '보유하고 있는 동안 물 속성 팰의 공격력이 증가한다. 가축 목장에 배치하면 팰의 체액을(를) 떨어뜨리기도 한다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': 1,
            'stats_size': 'XS',
            'stats_rarity': 1,
            'stats_health': 70,
            'stats_food': 100,
            'stats_meleeAttack': 100,
            'stats_attack': 70,
            'stats_defense': 70,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 1260,
            'stats_goldCoin': 1260,
            'stats_egg': '축축한 알',
            'stats_code': 'Kelpie',
            'movement_slowWalkSpeed': 50,
            'movement_walkSpeed': 100,
            'movement_runSpeed': 700,
            'movement_rideSprintSpeed': 900,
            'movement_transportSpeed': 400,
            'level60_health': '3100 – 3782',
            'level60_attack': '441 – 543',
            'level60_defense': '391 – 493',
            'activeSkills': '워터 제트, 용 대포, 아쿠아 샷, 버블 샷, 파워 폭탄, 물폭탄, 하이드로 스트림',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '켈시의 살코기, 팰의 체액',
            'drops_count': 2,
            'workSuitabilities': '관개 Lv1, 목장 Lv1',
            'workSuitabilities_count': 2,
            'tribes': 'Kelpie',
            'tribes_count': 1,
            'spawners': '1_11_plain_Kelpee, 계곡의 동굴, 낚시터',
            'spawners_count': 3
        },
        {
            # 82번 아주리비 (Azurobe)
            'id': 82,
            'name_kor': '아주리비',
            'description_kor': '새하얀 띠는 불순한 물에 닿아 시커멓게 변색한다. 독성 확인에 유용하다고 남획된 터라 지금도 인간을 안 좋게 생각한다.',
            'elements': '물|용',
            'partnerSkill_name': '물 위의 춤',
            'partnerSkill_describe': '등에 타고 물 위를 이동할 수 있다. 탑승 중 플레이어의 공격이 물 속성(으)로 변화한다.',
            'partnerSkill_needItem': '아주리비 안장',
            'partnerSkill_needItemTechLevel': '기술24',
            'partnerSkill_level': 1,
            'stats_size': 'L',
            'stats_rarity': 7,
            'stats_health': 110,
            'stats_food': 400,
            'stats_meleeAttack': 70,
            'stats_attack': 100,
            'stats_defense': 100,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 500,
            'stats_goldCoin': 5600,
            'stats_egg': '축축한 대형 알',
            'stats_code': 'BlueDragon',
            'movement_slowWalkSpeed': 75,
            'movement_walkSpeed': 150,
            'movement_runSpeed': 600,
            'movement_rideSprintSpeed': 900,
            'movement_transportSpeed': 350,
            'level60_health': '4400 – 5472',
            'level60_attack': '587 – 733',
            'level60_defense': '537 – 683',
            'activeSkills': '아쿠아 샷, 용 대포, 버블 샷, 용의 파장, 용의 숨결, 하이드로 스트림, 용의 운석',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '천',
            'drops_count': 1,
            'workSuitabilities': '관개 Lv3',
            'workSuitabilities_count': 1,
            'tribes': 'BlueDragon',
            'tribes_count': 1,
            'spawners': '제1 사냥 금지 구역, 낚시터',
            'spawners_count': 2
        },
        {
            # 83번 백랑이 (Cryolinx)
            'id': 83,
            'name_kor': '백랑이',
            'description_kor': '단단한 발톱으로 험한 산도 즐겁게 오른다. 하지만 다리가 짧아 하산이 힘들어 종종 높은 곳에서 이러지도 저러지도 못한다.',
            'elements': '얼음',
            'partnerSkill_name': '용 사냥꾼',
            'partnerSkill_describe': '함께 싸우는 동안 용 속성 팰을 쓰러뜨렸을 때 드롭 아이템 획득량이 증가한다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': 1,
            'stats_size': 'L',
            'stats_rarity': 7,
            'stats_health': 100,
            'stats_food': 475,
            'stats_meleeAttack': 140,
            'stats_attack': 100,
            'stats_defense': 110,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 130,
            'stats_goldCoin': 8440,
            'stats_egg': '얼어붙은 대형 알',
            'stats_code': 'WhiteTiger',
            'movement_slowWalkSpeed': 100,
            'movement_walkSpeed': 280,
            'movement_runSpeed': 720,
            'movement_rideSprintSpeed': 900,
            'movement_transportSpeed': 460,
            'level60_health': '4075 – 5050',
            'level60_attack': '587 – 733',
            'level60_defense': '586 – 747',
            'activeSkills': '파워 샷, 얼음 미사일, 바위 대포, 얼음 칼날, 빙산, 눈보라 할퀴기, 서리 낀 입김, 눈보라 스파이크',
            'activeSkills_count': 8,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '빙결 기관',
            'drops_count': 1,
            'workSuitabilities': '수작업 Lv1, 벌목 Lv2, 냉각 Lv3, 운반 Lv3',
            'workSuitabilities_count': 4,
            'tribes': 'WhiteTiger',
            'tribes_count': 1,
            'spawners': 'snow_5_1_snow_1, 영봉의 동굴, glacier_grade_01, glacier_grade_02',
            'spawners_count': 4
        },
        {
            # 84번 만티파이어 (Blazehowl)
            'id': 84,
            'name_kor': '만티파이어',
            'description_kor': '생고기를 좋아하지만 항상 익힌 고기를 먹는다. 타오르는 발톱을 무기로 삼은 탓에 잡은 먹이가 바싹 익어버린다는 것을 깨닫지 못했기 때문이다.',
            'elements': '화염',
            'partnerSkill_name': '지옥불 사자',
            'partnerSkill_describe': '등에 타고 이동할 수 있다. 함께 싸우는 동안 풀 속성 팰을 쓰러뜨렸을 때 드롭 아이템 획득량이 증가한다.',
            'partnerSkill_needItem': '만티파이어 안장',
            'partnerSkill_needItemTechLevel': '기술33',
            'partnerSkill_level': 1,
            'stats_size': 'L',
            'stats_rarity': 7,
            'stats_health': 105,
            'stats_food': 475,
            'stats_meleeAttack': 100,
            'stats_attack': 110,
            'stats_defense': 80,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 710,
            'stats_goldCoin': 4040,
            'stats_egg': '열기 나는 대형 알',
            'stats_code': 'Manticore',
            'movement_slowWalkSpeed': 90,
            'movement_walkSpeed': 180,
            'movement_runSpeed': 800,
            'movement_rideSprintSpeed': 1200,
            'movement_transportSpeed': 465,
            'level60_health': '4237 – 5261',
            'level60_attack': '636 – 797',
            'level60_defense': '440 – 557',
            'activeSkills': '파이어 샷, 파워 샷, 불화살, 파이어 브레스, 인페르노, 화산의 일격, 화염구, 팰 폭발',
            'activeSkills_count': 8,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '발화 기관',
            'drops_count': 1,
            'workSuitabilities': '불 피우기 Lv3, 벌목 Lv2',
            'workSuitabilities_count': 2,
            'tribes': 'Manticore',
            'tribes_count': 1,
            'spawners': '3_2_volcano_1, 모래 언덕 동굴, yamijima_7_3_RedArea_Magma',
            'spawners_count': 3
        }
    ]
    
    # 새 데이터를 DataFrame으로 변환
    df_new = pd.DataFrame(new_pals_data)
    print(f"✅ 새로운 팰 데이터 생성 완료: {len(df_new)}개 팰")
    
    # 기존 데이터와 병합
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    
    # 새 파일로 저장
    output_file = 'complete_1_to_84_pals.csv'
    df_combined.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"✅ 데이터 병합 및 저장 완료: {output_file}")
    print(f"📊 총 팰 수: {len(df_combined)}개")
    
    # 81-84번 팰들 정보 출력
    print("\n🎯 새로 추가된 팰들:")
    for i, pal in enumerate(new_pals_data, 1):
        print(f"{i}. {pal['id']}번 {pal['name_kor']} ({pal['elements']} 속성)")
        print(f"   파트너 스킬: {pal['partnerSkill_name']}")
        print(f"   작업 적성: {pal['workSuitabilities']}")
        print()

if __name__ == "__main__":
    add_pals_81_to_84() 