#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import os

def add_pals_73_to_76():
    """73번부터 76번까지의 팰 데이터를 기존 CSV에 추가"""
    
    # 기존 CSV 파일 읽기
    existing_file = 'complete_1_to_72_pals.csv'
    if not os.path.exists(existing_file):
        print(f"❌ {existing_file} 파일을 찾을 수 없습니다!")
        return
    
    df_existing = pd.read_csv(existing_file)
    print(f"✅ 기존 데이터 로드 완료: {len(df_existing)}개 팰")
    
    # 73번-76번 팰 데이터
    new_pals_data = [
        {
            # 73번 라이버드 (Beakon)
            'id': 73,
            'name_kor': '라이버드',
            'description_kor': '적토조의 근연종으로 보이나 관계는 없다. 급강하해 날카로운 주둥이로 적을 처치한다. 그 모습은 마치 낙뢰를 보는 듯하다.',
            'elements': '번개',
            'partnerSkill_name': '천뢰',
            'partnerSkill_describe': '등에 타고 하늘을 날 수 있다. 탑승 중 플레이어의 공격이 번개 속성으로 변화한다.',
            'partnerSkill_needItem': '라이버드 안장',
            'partnerSkill_needItemTechLevel': '기술34',
            'partnerSkill_level': 'Lv.1',
            'stats_size': 'L',
            'stats_rarity': 6,
            'stats_health': 105,
            'stats_food': 475,
            'stats_meleeAttack': 100,
            'stats_attack': 115,
            'stats_defense': 80,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 220,
            'stats_goldCoin': 7490,
            'stats_egg': '찌릿찌릿한 대형 알',
            'stats_code': 'ThunderBird',
            'movement_slowWalkSpeed': 100,
            'movement_walkSpeed': 200,
            'movement_runSpeed': 750,
            'movement_rideSprintSpeed': 1200,
            'movement_transportSpeed': 375,
            'level60_health': '4237-5261',
            'level60_attack': '660-828',
            'level60_defense': '440-557',
            'activeSkills': '공기 대포|스파크 샷|전기 파장|라인 썬더|급강하 번개 강타|트라이 썬더|모래 폭풍|전기 볼트',
            'activeSkills_count': 8,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '발전 기관',
            'drops_count': 1,
            'workSuitabilities': '발전 Lv2|채집 Lv1|운반 Lv3',
            'workSuitabilities_count': 3,
            'tribes': '천둥 번개의 날개 라이버드|라이버드',
            'tribes_count': 2,
            'spawners': '4_2_dessert_1|모래 언덕 동굴|화산 동굴|sakurajima_6_1_NorthDesert|grass_grade_02|Sakurajima_grade_01|Captured Cage: Desert1|습격 14-17|습격 18-99',
            'spawners_count': 9
        },
        {
            # 74번 적토조 (Ragnahawk)
            'id': 74,
            'name_kor': '적토조',
            'description_kor': '라이버드의 근연종이지만 관계는 없다. 암석이 주식이며 오랜 세월에 걸쳐 주둥이는 물론 머리 전체가 단단해졌다.',
            'elements': '화염',
            'partnerSkill_name': '화염 날개',
            'partnerSkill_describe': '등에 타고 하늘을 날 수 있다. 탑승 중 플레이어의 공격이 화염 속성으로 변화한다.',
            'partnerSkill_needItem': '적토조 안장',
            'partnerSkill_needItemTechLevel': '기술37',
            'partnerSkill_level': 'Lv.1',
            'stats_size': 'L',
            'stats_rarity': 7,
            'stats_health': 95,
            'stats_food': 475,
            'stats_meleeAttack': 100,
            'stats_attack': 105,
            'stats_defense': 120,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 380,
            'stats_goldCoin': 6720,
            'stats_egg': '열기 나는 대형 알',
            'stats_code': 'RedArmorBird',
            'movement_slowWalkSpeed': 100,
            'movement_walkSpeed': 200,
            'movement_runSpeed': 800,
            'movement_rideSprintSpeed': 1300,
            'movement_transportSpeed': 375,
            'level60_health': '3912-4838',
            'level60_attack': '611-765',
            'level60_defense': '635-810',
            'activeSkills': '공기 대포|스피릿 파이어|불화살|모래 폭풍|러시 비크|화염 폭풍|파이어 브레스|화염구',
            'activeSkills_count': 8,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '발화 기관',
            'drops_count': 1,
            'workSuitabilities': '불 피우기 Lv3|운반 Lv3',
            'workSuitabilities_count': 2,
            'tribes': '활활 타오르는 날개 적토조|적토조|광폭화한 적토조',
            'tribes_count': 3,
            'spawners': '3_2_volcano_1|3_3_volcano_1|모래 언덕 동굴|yamijima_7_3_RedArea_Magma|volcanic_grade_02|volcanic_grade_01',
            'spawners_count': 6
        },
        {
            # 75번 캐티메이지 (Katress)
            'id': 75,
            'name_kor': '캐티메이지',
            'description_kor': '음기의 힘으로 기괴한 술수를 부린다. 뭐든지 생으로 먹는 걸 좋아한다. 마호하고는 사이가 나쁘다.',
            'elements': '어둠',
            'partnerSkill_name': '마도서 수집가',
            'partnerSkill_describe': '함께 싸우는 동안 무속성 팰을 쓰러뜨렸을 때 드롭 아이템 획득량이 증가한다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': 'Lv.1',
            'stats_size': 'M',
            'stats_rarity': 6,
            'stats_health': 90,
            'stats_food': 350,
            'stats_meleeAttack': 100,
            'stats_attack': 105,
            'stats_defense': 90,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 700,
            'stats_goldCoin': 4120,
            'stats_egg': '암흑의 대형 알',
            'stats_code': 'CatMage',
            'movement_slowWalkSpeed': 70,
            'movement_walkSpeed': 145,
            'movement_runSpeed': 440,
            'movement_rideSprintSpeed': 620,
            'movement_transportSpeed': 292,
            'level60_health': '3750-4627',
            'level60_attack': '611-765',
            'level60_defense': '488-620',
            'activeSkills': '파이어 샷|암흑구|불화살|그림자 폭발|유령의 불꽃|악몽의 구체|어둠의 레이저',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '가죽|캐티메이지의 체모|고도의 기술서',
            'drops_count': 3,
            'workSuitabilities': '수작업 Lv2|제약 Lv2|운반 Lv2',
            'workSuitabilities_count': 3,
            'tribes': '암흑 고양이 마도사 캐티메이지|캐티메이지|캐티위자드',
            'tribes_count': 3,
            'spawners': 'World Map 392,-0|2_1_forest_1|2_1_forest_3|시냇물 동굴|grass_grade_02',
            'spawners_count': 5
        },
        {
            # 76번 마호 (Wixen)
            'id': 76,
            'name_kor': '마호',
            'description_kor': '양기의 힘으로 기괴한 술수를 부린다. 뭐든지 노릇노릇하게 구워 먹는다. 캐티메이지하고는 사이가 나쁘다.',
            'elements': '화염',
            'partnerSkill_name': '여우 아가씨',
            'partnerSkill_describe': '함께 싸우는 동안 플레이어의 공격이 화염 속성으로 변화한다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': 'Lv.1',
            'stats_size': 'M',
            'stats_rarity': 6,
            'stats_health': 90,
            'stats_food': 350,
            'stats_meleeAttack': 50,
            'stats_attack': 110,
            'stats_defense': 80,
            'stats_workSpeed': 100,
            'stats_support': 120,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 1160,
            'stats_goldCoin': 3080,
            'stats_egg': '열기 나는 대형 알',
            'stats_code': 'FoxMage',
            'movement_slowWalkSpeed': 70,
            'movement_walkSpeed': 145,
            'movement_runSpeed': 440,
            'movement_rideSprintSpeed': 620,
            'movement_transportSpeed': 292,
            'level60_health': '3750-4627',
            'level60_attack': '636-797',
            'level60_defense': '440-557',
            'activeSkills': '파이어 샷|스피릿 파이어|불화살|유령의 불꽃|화염 폭풍|화염구|용의 운석',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '발화 기관|고도의 기술서',
            'drops_count': 2,
            'workSuitabilities': '불 피우기 Lv2|수작업 Lv3|운반 Lv2',
            'workSuitabilities_count': 3,
            'tribes': '화염 여우 마도사 마호|마호|영마호',
            'tribes_count': 3,
            'spawners': '3_1_volcano_1|모래 언덕 동굴|3_4_volcano_1|volcanic_grade_02|volcanic_grade_01|Captured Cage: Volcano1',
            'spawners_count': 6
        }
    ]
    
    # DataFrame으로 변환
    df_new = pd.DataFrame(new_pals_data)
    
    # 기존 데이터와 병합
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    
    # 새 파일로 저장
    output_file = 'complete_1_to_76_pals.csv'
    df_combined.to_csv(output_file, index=False, encoding='utf-8')
    
    print(f"✅ 73번-76번 팰 데이터 추가 완료!")
    print(f"📊 총 팰 수: {len(df_combined)}개")
    print(f"📁 저장 파일: {output_file}")
    
    # 추가된 팰들 정보 출력
    print("\n🎯 추가된 팰들:")
    for pal in new_pals_data:
        print(f"   {pal['id']:3d}번 {pal['name_kor']:8s} ({pal['elements']:4s}) - {pal['partnerSkill_name']}")

if __name__ == "__main__":
    add_pals_73_to_76() 