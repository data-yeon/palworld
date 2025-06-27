#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import os

def add_pals_93_to_96():
    """93번부터 96번까지의 팰 데이터를 기존 CSV에 추가"""
    
    # 기존 CSV 파일 읽기
    existing_file = 'complete_1_to_92_pals.csv'
    if not os.path.exists(existing_file):
        print(f"❌ {existing_file} 파일을 찾을 수 없습니다!")
        return
    
    df_existing = pd.read_csv(existing_file)
    print(f"✅ 기존 데이터 로드 완료: {len(df_existing)}개 팰")
    
    # 93번-96번 팰 데이터
    new_pals_data = [
        {
            # 93번 윈드디어 (Fenglope)
            'id': 93,
            'name_kor': '윈드디어',
            'description_kor': '먼 옛날, 그 아름다움 덕에 그림의 소재가 된 친근한 존재였다. 시대가 흐르며 아름다운 털가죽과 뿔도 예술품의 재료가 되어 일상적인 존재가 됐다.',
            'elements': '무',
            'partnerSkill_name': '풍운',
            'partnerSkill_describe': '등에 타고 이동할 수 있다. 탑승 중 2단 점프가 가능해진다.',
            'partnerSkill_needItem': '윈드디어 안장',
            'partnerSkill_needItemTechLevel': 26,
            'partnerSkill_level': 1,
            'stats_size': 'S',
            'stats_rarity': 3,
            'stats_health': 110,
            'stats_food': 400,
            'stats_meleeAttack': 110,
            'stats_attack': 110,
            'stats_defense': 90,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 980,
            'stats_goldCoin': 2250,
            'stats_egg': '평범한 알',
            'stats_code': 'FengyunDeeper',
            'movement_slowWalkSpeed': 85,
            'movement_walkSpeed': 100,
            'movement_runSpeed': 750,
            'movement_rideSprintSpeed': 1050,
            'movement_transportSpeed': 417,
            'level60_health': '4400-5472',
            'level60_attack': '636-797',
            'level60_defense': '488-620',
            'activeSkills': '공기 대포, 아쿠아 샷, 구름 폭풍, 산성비, 물폭탄, 눈보라 스파이크, 팰 폭발',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '가죽 3, 뿔 2',
            'drops_count': 2,
            'workSuitabilities': '벌목 Lv2',
            'workSuitabilities_count': 1,
            'tribes': '유유자적하는 구름 윈드디어 (보스), 윈드디어 (일반)',
            'tribes_count': 2,
            'spawners': '3_3_volcano_1 (34-37), 제3 사냥 금지 구역 (40-45), 모래 언덕 동굴 (36-38)',
            'spawners_count': 3
        },
        {
            # 94번 블러드캐티 (Felbat)
            'id': 94,
            'name_kor': '블러드캐티',
            'description_kor': '어둠 속에서 먹잇감을 습격해 망토 같은 날개로 가둬 버린다. 안에서 무슨 일이 벌어지는지 날개 안이 왜 시뻘건지는 모르는 게 약이다.',
            'elements': '어둠',
            'partnerSkill_name': '생명 흡수',
            'partnerSkill_describe': '함께 싸우는 동안 피해를 주면 그 일부를 흡수하여 HP를 회복하는 생명 흡수 효과를 플레이어와 블러드캐티에게 부여한다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': 0,
            'partnerSkill_level': 1,
            'stats_size': 'M',
            'stats_rarity': 6,
            'stats_health': 100,
            'stats_food': 350,
            'stats_meleeAttack': 100,
            'stats_attack': 105,
            'stats_defense': 110,
            'stats_workSpeed': 100,
            'stats_support': 110,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 1010,
            'stats_goldCoin': 2100,
            'stats_egg': '암흑의 대형 알',
            'stats_code': 'CatVampire',
            'movement_slowWalkSpeed': 60,
            'movement_walkSpeed': 100,
            'movement_runSpeed': 550,
            'movement_rideSprintSpeed': 700,
            'movement_transportSpeed': 325,
            'level60_health': '4075-5050',
            'level60_attack': '611-765',
            'level60_defense': '586-747',
            'activeSkills': '독 사격, 암흑구, 그림자 폭발, 유령의 불꽃, 악몽의 구체, 인페르노, 어둠의 레이저',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '천 1-2, 작은 팰 영혼 1',
            'drops_count': 2,
            'workSuitabilities': '제약 Lv3',
            'workSuitabilities_count': 1,
            'tribes': '어스름의 흡혈귀 블러드캐티 (보스), 블러드캐티 (일반)',
            'tribes_count': 2,
            'spawners': '시냇물 동굴 (20-23), 월드맵 -21,175 (23), 습격 25-99 (50)',
            'spawners_count': 3
        },
        {
            # 95번 페스키 (Quivern)
            'id': 95,
            'name_kor': '페스키',
            'description_kor': '페스키을(를) 껴안고 자면 천국에 온 듯한 기분이나 잠버릇이 험한 개체와 자면 깔려 죽어서 천국으로 직행이다.',
            'elements': '용',
            'partnerSkill_name': '천공용의 자애',
            'partnerSkill_describe': '등에 타고 하늘을 날 수 있으며 탑승 중 용 속성 공격이 강화된다. 하늘을 나는 동안 이동 속도가 상승한다.',
            'partnerSkill_needItem': '페스키 안장',
            'partnerSkill_needItemTechLevel': 36,
            'partnerSkill_level': 1,
            'stats_size': 'L',
            'stats_rarity': 7,
            'stats_health': 105,
            'stats_food': 300,
            'stats_meleeAttack': 100,
            'stats_attack': 100,
            'stats_defense': 100,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 350,
            'stats_goldCoin': 6830,
            'stats_egg': '용의 대형 알',
            'stats_code': 'SkyDragon',
            'movement_slowWalkSpeed': 120,
            'movement_walkSpeed': 240,
            'movement_runSpeed': 900,
            'movement_rideSprintSpeed': 1400,
            'movement_transportSpeed': 470,
            'level60_health': '4237-5261',
            'level60_attack': '587-733',
            'level60_defense': '537-683',
            'activeSkills': '용 대포, 스피릿 파이어, 산성비, 용의 숨결, 초록 폭풍, 물폭탄, 용의 운석',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '고급 팰 기름 3',
            'drops_count': 1,
            'workSuitabilities': '수작업 Lv1, 채집 Lv2, 채굴 Lv2, 운반 Lv3',
            'workSuitabilities_count': 4,
            'tribes': '순백의 비행자 페스키 (보스), 페스키 (일반), 포레스키 (변종)',
            'tribes_count': 3,
            'spawners': '월드맵 77,127 (23), 제2 사냥 금지 구역 (40-45), 영봉의 동굴 (42-45), sakurajima_6_3_Grassland (50-52)',
            'spawners_count': 4
        },
        {
            # 96번 마그마 카이저 (Blazamut)
            'id': 96,
            'name_kor': '마그마 카이저',
            'description_kor': '화산 분화와 함께 태어났다는 전설이 있다. 이 대지는 거대한 마그마 카이저의 등이라고 주장하는 괴상한 단체도 있었다.',
            'elements': '화염',
            'partnerSkill_name': '마그마 카이저',
            'partnerSkill_describe': '등에 타고 이동할 수 있다. 탑승 중 화염 속성 공격이 강화된다.',
            'partnerSkill_needItem': '마그마 카이저 안장',
            'partnerSkill_needItemTechLevel': 40,
            'partnerSkill_level': 1,
            'stats_size': 'XL',
            'stats_rarity': 9,
            'stats_health': 100,
            'stats_food': 600,
            'stats_meleeAttack': 150,
            'stats_attack': 125,
            'stats_defense': 120,
            'stats_workSpeed': 100,
            'stats_support': 50,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 10,
            'stats_goldCoin': 10520,
            'stats_egg': '열기 나는 거대한 알',
            'stats_code': 'KingBahamut',
            'movement_slowWalkSpeed': 150,
            'movement_walkSpeed': 400,
            'movement_runSpeed': 800,
            'movement_rideSprintSpeed': 1200,
            'movement_transportSpeed': 500,
            'level60_health': '4075-5050',
            'level60_attack': '709-892',
            'level60_defense': '635-810',
            'activeSkills': '파워 샷, 파이어 샷, 바위 폭발, 파이어 브레스, 인페르노, 완력 강타, 화염구, 바위 창',
            'activeSkills_count': 8,
            'passiveSkills': '염제',
            'passiveSkills_count': 1,
            'drops': '석탄 10, 발화 기관 10',
            'drops_count': 2,
            'workSuitabilities': '불 피우기 Lv3, 채굴 Lv4',
            'workSuitabilities_count': 2,
            'tribes': '연옥의 폭군 마그마 카이저 (보스), 마그마 카이저 (일반), 마그마 드라고 (변종)',
            'tribes_count': 3,
            'spawners': '제3 사냥 금지 구역 (40-45)',
            'spawners_count': 1
        }
    ]
    
    # 새 데이터를 DataFrame으로 변환
    df_new = pd.DataFrame(new_pals_data)
    
    # 기존 데이터와 새 데이터 합치기
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    
    # 새 파일로 저장
    output_file = 'complete_1_to_96_pals.csv'
    df_combined.to_csv(output_file, index=False, encoding='utf-8-sig')
    
    print(f"✅ 성공적으로 저장되었습니다!")
    print(f"📁 파일명: {output_file}")
    print(f"📊 총 팰 개수: {len(df_combined)}개")
    print(f"🎯 추가된 팰: 93번 윈드디어, 94번 블러드캐티, 95번 페스키, 96번 마그마 카이저")
    
    # 새로 추가된 팰들 확인
    new_pals = df_combined[df_combined['id'].isin([93, 94, 95, 96])]
    print(f"\n🔍 새로 추가된 팰들:")
    for _, pal in new_pals.iterrows():
        print(f"   {pal['id']}번 {pal['name_kor']} ({pal['elements']}) - {pal['partnerSkill_name']}")

if __name__ == "__main__":
    add_pals_93_to_96() 