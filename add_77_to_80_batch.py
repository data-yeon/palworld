#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import os

def add_pals_77_to_80():
    """77번부터 80번까지의 팰 데이터를 기존 CSV에 추가"""
    
    # 기존 CSV 파일 읽기
    existing_file = 'complete_1_to_76_pals.csv'
    if not os.path.exists(existing_file):
        print(f"❌ {existing_file} 파일을 찾을 수 없습니다!")
        return
    
    df_existing = pd.read_csv(existing_file)
    print(f"✅ 기존 데이터 로드 완료: {len(df_existing)}개 팰")
    
    # 77번-80번 팰 데이터
    new_pals_data = [
        {
            # 77번 초토리 (Verdash)
            'id': 77,
            'name_kor': '초토리',
            'description_kor': '초토리가 달리고 나면 토질이 좋아져 초목이 우거진다. 제초제를 뿌리면 그곳은 달리지 않는다.',
            'elements': '풀',
            'partnerSkill_name': '초원의 스피드스터',
            'partnerSkill_describe': '함께 싸우는 동안 플레이어의 이동 속도가 증가하며 플레이어의 공격이 풀 속성으로 변화한다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': 1,
            'stats_size': 'M',
            'stats_rarity': 8,
            'stats_health': 90,
            'stats_food': 225,
            'stats_meleeAttack': 100,
            'stats_attack': 115,
            'stats_defense': 90,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 990,
            'stats_goldCoin': 2200,
            'stats_egg': '신록의 거대한 알',
            'stats_code': 'GrassRabbitMan',
            'movement_slowWalkSpeed': 50,
            'movement_walkSpeed': 195,
            'movement_runSpeed': 500,
            'movement_rideSprintSpeed': 700,
            'movement_transportSpeed': 275,
            'level60_health': '3750-4627',
            'level60_attack': '660-828',
            'level60_defense': '488-620',
            'activeSkills': '바람의 칼날, 바위 대포, 씨앗 기관총, 바위 폭발, 초록 폭풍, 스핀 레그 러시, 가시덩굴, 태양 폭발',
            'activeSkills_count': 8,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '가죽, 뼈',
            'drops_count': 2,
            'workSuitabilities': '파종 Lv2, 수작업 Lv3, 채집 Lv3, 벌목 Lv2, 운반 Lv2',
            'workSuitabilities_count': 5,
            'tribes': '숲을 휩쓰는 질풍 초토리 (보스), 초토리 (일반)',
            'tribes_count': 2,
            'spawners': '제2 사냥 금지 구역, sakurajima_6_3_Grassland, yamijima_7_1_YellowArea, 신록의 거대한 알',
            'spawners_count': 4
        },
        {
            # 78번 비오레타 (Vaelet)
            'id': 78,
            'name_kor': '비오레타',
            'description_kor': '성에는 임금님께서 좋아하시는 꽃이 잔뜩 피어 있었습니다. 어느 날 큰 싸움이 벌어져, 성까지 불이 옮겨붙으려 하고 있었습니다. 바로 그곳에서, 한 꽃의 정령이 나타났습니다. - 동화 \'임금님의 꽃\'에서 발췌.',
            'elements': '풀',
            'partnerSkill_name': '대지 정화',
            'partnerSkill_describe': '함께 싸우는 동안 땅 속성 팰을 쓰러뜨렸을 때 드롭 아이템 획득량이 증가한다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': 1,
            'stats_size': 'M',
            'stats_rarity': 8,
            'stats_health': 100,
            'stats_food': 225,
            'stats_meleeAttack': 100,
            'stats_attack': 100,
            'stats_defense': 120,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 1050,
            'stats_goldCoin': 1960,
            'stats_egg': '신록의 거대한 알',
            'stats_code': 'VioletFairy',
            'movement_slowWalkSpeed': 100,
            'movement_walkSpeed': 150,
            'movement_runSpeed': 400,
            'movement_rideSprintSpeed': 550,
            'movement_transportSpeed': 275,
            'level60_health': '4075-5050',
            'level60_attack': '587-733',
            'level60_defense': '635-810',
            'activeSkills': '독 안개, 바람의 칼날, 독 사격, 씨앗 지뢰, 초록 폭풍, 악몽의 구체, 태양 폭발',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '하급 의약품, 토마토 씨, 양파 씨',
            'drops_count': 3,
            'workSuitabilities': '파종 Lv2, 수작업 Lv2, 채집 Lv2, 제약 Lv3, 운반 Lv1',
            'workSuitabilities_count': 5,
            'tribes': '자줏빛 감색 풀의 환영 비오레타 (보스), 비오레타 (일반)',
            'tribes_count': 2,
            'spawners': '제1 사냥 금지 구역',
            'spawners_count': 1
        },
        {
            # 79번 실키누 (Sibelyx)
            'id': 79,
            'name_kor': '실키누',
            'description_kor': '비를 좋아해서 비가 내리는 동안 꼼작 않고 있는 경우가 많다. 파이호가 자주 비를 피하러 찾아온다.',
            'elements': '얼음',
            'partnerSkill_name': '실크 메이커',
            'partnerSkill_describe': '발동하면 목표로 삼은 적을 향해 높은 위력의 눈보라 스파이크로 공격한다. 가축 목장에 배치하면 상급 천을 만들기도 한다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': 1,
            'stats_size': 'L',
            'stats_rarity': 7,
            'stats_health': 110,
            'stats_food': 350,
            'stats_meleeAttack': 90,
            'stats_attack': 90,
            'stats_defense': 100,
            'stats_workSpeed': 100,
            'stats_support': 90,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 450,
            'stats_goldCoin': 5900,
            'stats_egg': '얼어붙은 대형 알',
            'stats_code': 'WhiteMoth',
            'movement_slowWalkSpeed': 50,
            'movement_walkSpeed': 100,
            'movement_runSpeed': 400,
            'movement_rideSprintSpeed': 550,
            'movement_transportSpeed': 250,
            'level60_health': '4400-5472',
            'level60_attack': '538-670',
            'level60_defense': '537-683',
            'activeSkills': '얼음 미사일, 얼음 칼날, 빙산, 서리 낀 입김, 유령의 불꽃, 물폭탄, 눈보라 스파이크',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '상급 천, 빙결 기관',
            'drops_count': 2,
            'workSuitabilities': '제약 Lv2, 냉각 Lv2, 목장 Lv1',
            'workSuitabilities_count': 3,
            'tribes': '순백의 귀부인 실키누 (보스), 실키누 (일반)',
            'tribes_count': 2,
            'spawners': 'snow_5_1_snow_1, 영봉의 동굴, 얼어붙은 대형 알',
            'spawners_count': 3
        },
        {
            # 80번 실피아 (Elphidran)
            'id': 80,
            'name_kor': '실피아',
            'description_kor': '겉모습처럼 천진난만한 성격이다. 그래서인지 선악의 구별에 어두워 악의를 가진 인간에게 이용당하기 십상이다.',
            'elements': '용',
            'partnerSkill_name': '마음씨 착한 성룡',
            'partnerSkill_describe': '등에 타고 하늘을 날 수 있다. 하늘을 나는 동안 이동 속도가 상승한다. 함께 싸우는 동안 어둠 속성 팰을 쓰러뜨렸을 때 드롭 아이템 획득량이 증가한다.',
            'partnerSkill_needItem': '실피아 안장',
            'partnerSkill_needItemTechLevel': '기술20',
            'partnerSkill_level': 1,
            'stats_size': 'L',
            'stats_rarity': 7,
            'stats_health': 110,
            'stats_food': 400,
            'stats_meleeAttack': 80,
            'stats_attack': 80,
            'stats_defense': 90,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 540,
            'stats_goldCoin': 5230,
            'stats_egg': '용의 대형 알',
            'stats_code': 'FairyDragon',
            'movement_slowWalkSpeed': 83,
            'movement_walkSpeed': 83,
            'movement_runSpeed': 700,
            'movement_rideSprintSpeed': 1000,
            'movement_transportSpeed': 456,
            'level60_health': '4400-5472',
            'level60_attack': '490-607',
            'level60_defense': '488-620',
            'activeSkills': '용 대포, 용의 파장, 불화살, 신비의 허리케인, 용의 숨결, 팰 폭발, 용의 운석',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '고급 팰 기름',
            'drops_count': 1,
            'workSuitabilities': '벌목 Lv2',
            'workSuitabilities_count': 1,
            'tribes': '온후한 하늘의 용 실피아 (보스), 실피아 (일반), 광폭화한 실피아 (보스), 실티아 (아종)',
            'tribes_count': 4,
            'spawners': '제1 사냥 금지 구역, 영봉의 동굴',
            'spawners_count': 2
        }
    ]
    
    # 새로운 데이터를 DataFrame으로 변환
    df_new = pd.DataFrame(new_pals_data)
    
    # 기존 데이터와 새 데이터 합치기
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    
    # 새로운 파일로 저장
    output_file = 'complete_1_to_80_pals.csv'
    df_combined.to_csv(output_file, index=False, encoding='utf-8-sig')
    
    print(f"✅ 77-80번 팰 데이터 추가 완료!")
    print(f"📄 총 팰 수: {len(df_combined)}개")
    print(f"💾 저장 파일: {output_file}")
    
    # 추가된 팰들 정보 출력
    print(f"\n🎯 새로 추가된 팰들:")
    for pal in new_pals_data:
        print(f"   {pal['id']}번 {pal['name_kor']} ({pal['elements']} 속성)")

if __name__ == "__main__":
    add_pals_77_to_80() 