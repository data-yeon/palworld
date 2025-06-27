#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import os

def add_pals_85_to_88():
    """85번부터 88번까지의 팰 데이터를 기존 CSV에 추가"""
    
    # 기존 CSV 파일 읽기
    existing_file = 'complete_1_to_84_pals.csv'
    if not os.path.exists(existing_file):
        print(f"❌ {existing_file} 파일을 찾을 수 없습니다!")
        return
    
    df_existing = pd.read_csv(existing_file)
    print(f"✅ 기존 데이터 로드 완료: {len(df_existing)}개 팰")
    
    # 85번-88번 팰 데이터
    new_pals_data = [
        {
            # 85번 헤로롱 (Relaxaurus)
            'id': 85,
            'name_kor': '헤로롱',
            'description_kor': '어리바리한 겉모습과 달리 속은 사납다. 눈에 띄는 모든 걸 먹이로 인식하여 닥치는 대로 잡아먹으려고 든다.',
            'elements': '용|물',
            'partnerSkill_name': '꾸벅꾸벅 미사일',
            'partnerSkill_describe': '등에 타고 이동할 수 있다. 탑승 중 미사일 발사기 연사가 가능해진다.',
            'partnerSkill_needItem': '헤로롱 미사일 런처',
            'partnerSkill_needItemTechLevel': 44,
            'partnerSkill_level': 1,
            'stats_size': 'XL',
            'stats_rarity': 8,
            'stats_health': 110,
            'stats_food': 475,
            'stats_meleeAttack': 110,
            'stats_attack': 100,
            'stats_defense': 70,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1.0,
            'stats_maleProbability': 50,
            'stats_combiRank': 280,
            'stats_goldCoin': 10240,
            'stats_egg': '용의 거대한 알',
            'stats_code': 'LazyDragon',
            'movement_slowWalkSpeed': 40,
            'movement_walkSpeed': 60,
            'movement_runSpeed': 650,
            'movement_rideSprintSpeed': 1000,
            'movement_transportSpeed': 150,
            'level60_health': '4400 – 5472',
            'level60_attack': '587 – 733',
            'level60_defense': '391 – 493',
            'activeSkills': '용 대포|아쿠아 샷|용의 파장|버블 샷|용의 숨결|물폭탄|용의 운석',
            'activeSkills_count': 7,
            'passiveSkills': '먹보',
            'passiveSkills_count': 1,
            'drops': '고급 팰 기름|루비',
            'drops_count': 2,
            'workSuitabilities': '관개 Lv2|운반 Lv1',
            'workSuitabilities_count': 2,
            'tribes': '폭식룡 헤로롱|헤로롱|광폭화한 헤로롱|핑피롱',
            'tribes_count': 4,
            'spawners': '1_7_plain_Pekodon|sakurajima_6_6_MushroomForest|용의 거대한 알|습격',
            'spawners_count': 4
        },
        {
            # 86번 라브라돈 (Broncherry)
            'id': 86,
            'name_kor': '라브라돈',
            'description_kor': '교미 전후로 체취가 크게 달라진다. 파트너를 발견한 뒤엔 좋은 향기가 나 \'첫사랑의 향기\'라고 불린다.',
            'elements': '풀',
            'partnerSkill_name': '애정 과적재',
            'partnerSkill_describe': '등에 타고 이동할 수 있다. 보유하고 있는 동안 라브라돈이 짐을 대신 짊어져 플레이어의 소지 중량 제한이 증가한다.',
            'partnerSkill_needItem': '라브라돈 안장',
            'partnerSkill_needItemTechLevel': 19,
            'partnerSkill_level': 1,
            'stats_size': 'XL',
            'stats_rarity': 7,
            'stats_health': 120,
            'stats_food': 475,
            'stats_meleeAttack': 80,
            'stats_attack': 90,
            'stats_defense': 100,
            'stats_workSpeed': 100,
            'stats_support': 120,
            'stats_captureRateCorrect': 1.0,
            'stats_maleProbability': 50,
            'stats_combiRank': 860,
            'stats_goldCoin': 2920,
            'stats_egg': '신록의 대형 알',
            'stats_code': 'SakuraSaurus',
            'movement_slowWalkSpeed': 50,
            'movement_walkSpeed': 75,
            'movement_runSpeed': 550,
            'movement_rideSprintSpeed': 1020,
            'movement_transportSpeed': 200,
            'level60_health': '4725 – 5895',
            'level60_attack': '538 – 670',
            'level60_defense': '537 – 683',
            'activeSkills': '바람의 칼날|모래 돌풍|몸통 박치기|씨앗 지뢰|초록 폭풍|가시덩굴|태양 폭발',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '라브라돈의 공룡고기|토마토 씨|감자 종자',
            'drops_count': 3,
            'workSuitabilities': '파종 Lv3',
            'workSuitabilities_count': 1,
            'tribes': '봄을 알리는 바람 라브라돈|라브라돈|스프라돈',
            'tribes_count': 3,
            'spawners': '1_6_plain_Kirin|1_9_plain_SweetsSheep|신록의 대형 알',
            'spawners_count': 3
        },
        {
            # 87번 플로리나 (Petallia)
            'id': 87,
            'name_kor': '플로리나',
            'description_kor': '수명이 다하면 큰 식물로 변한다. 10년에 한 번 아주 예쁜 꽃을 피우며 거기서 새 플로리나가 자란다.',
            'elements': '풀',
            'partnerSkill_name': '꽃의 정령의 축복',
            'partnerSkill_describe': '발동하면 꽃의 치유력으로 플레이어의 HP를 회복한다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': 1,
            'stats_size': 'M',
            'stats_rarity': 8,
            'stats_health': 100,
            'stats_food': 225,
            'stats_meleeAttack': 100,
            'stats_attack': 95,
            'stats_defense': 100,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1.0,
            'stats_maleProbability': 50,
            'stats_combiRank': 780,
            'stats_goldCoin': 3590,
            'stats_egg': '신록의 거대한 알',
            'stats_code': 'FlowerDoll',
            'movement_slowWalkSpeed': 100,
            'movement_walkSpeed': 150,
            'movement_runSpeed': 550,
            'movement_rideSprintSpeed': 700,
            'movement_transportSpeed': 350,
            'level60_health': '4075 – 5050',
            'level60_attack': '563 – 702',
            'level60_defense': '537 – 683',
            'activeSkills': '바람의 칼날|아쿠아 샷|씨앗 기관총|버블 샷|초록 폭풍|가시덩굴|태양 폭발',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '예쁜 꽃',
            'drops_count': 1,
            'workSuitabilities': '파종 Lv3|수작업 Lv2|채집 Lv2|제약 Lv2|운반 Lv1',
            'workSuitabilities_count': 5,
            'tribes': '화원의 아가씨 플로리나|플로리나',
            'tribes_count': 2,
            'spawners': '제1 사냥 금지 구역|sakurajima_6_7_FlowerGarden|신록의 거대한 알',
            'spawners_count': 3
        },
        {
            # 88번 볼카노 (Reptyro)
            'id': 88,
            'name_kor': '볼카노',
            'description_kor': '마그마 같은 피가 전신에 힘차게 흐르고 있다. 물을 흠뻑 끼얹으면 순식간에 가열돼 엄청난 수증기 폭발이 발생한다.',
            'elements': '화염|땅',
            'partnerSkill_name': '광석을 탐하는 야수',
            'partnerSkill_describe': '등에 타고 이동할 수 있다. 탑승 중 광석 파괴 효율이 향상된다.',
            'partnerSkill_needItem': '볼카노 안장',
            'partnerSkill_needItemTechLevel': 32,
            'partnerSkill_level': 1,
            'stats_size': 'L',
            'stats_rarity': 6,
            'stats_health': 110,
            'stats_food': 350,
            'stats_meleeAttack': 100,
            'stats_attack': 105,
            'stats_defense': 120,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1.0,
            'stats_maleProbability': 50,
            'stats_combiRank': 320,
            'stats_goldCoin': 6940,
            'stats_egg': '열기 나는 대형 알',
            'stats_code': 'VolcanicMonster',
            'movement_slowWalkSpeed': 50,
            'movement_walkSpeed': 80,
            'movement_runSpeed': 550,
            'movement_rideSprintSpeed': 1000,
            'movement_transportSpeed': 235,
            'level60_health': '4400 – 5472',
            'level60_attack': '611 – 765',
            'level60_defense': '635 – 810',
            'activeSkills': '파이어 샷|바위 폭발|바위 대포|파이어 브레스|화산 폭발|인페르노|바위 창',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '발화 기관',
            'drops_count': 1,
            'workSuitabilities': '불 피우기 Lv3|채굴 Lv3',
            'workSuitabilities_count': 2,
            'tribes': '용암에 굶주린 야수 볼카노|볼카노|프로스카노',
            'tribes_count': 3,
            'spawners': '3_1_volcano_1|모래 언덕 동굴|열기 나는 대형 알|습격',
            'spawners_count': 4
        }
    ]
    
    # 새 데이터를 DataFrame으로 변환
    df_new = pd.DataFrame(new_pals_data)
    
    # 컬럼 순서를 기존 DataFrame과 맞춤
    df_new = df_new.reindex(columns=df_existing.columns)
    
    # 데이터 결합
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    
    # 새 파일명으로 저장
    output_file = 'complete_1_to_88_pals.csv'
    df_combined.to_csv(output_file, index=False, encoding='utf-8')
    
    print(f"🎉 완료! {len(new_pals_data)}개 팰 추가")
    print(f"📄 파일 저장: {output_file}")
    print(f"📊 총 팰 수: {len(df_combined)}개")
    print()
    print("🆕 새로 추가된 팰들:")
    for pal in new_pals_data:
        print(f"  • {pal['id']}번 {pal['name_kor']} ({pal['elements']}) - {pal['partnerSkill_name']}")

if __name__ == "__main__":
    add_pals_85_to_88() 