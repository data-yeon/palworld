#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import os

def add_pals_89_to_92():
    """89번부터 92번까지의 팰 데이터를 기존 CSV에 추가"""
    
    # 기존 CSV 파일 읽기
    existing_file = 'complete_1_to_88_pals.csv'
    if not os.path.exists(existing_file):
        print(f"❌ {existing_file} 파일을 찾을 수 없습니다!")
        return
    
    df_existing = pd.read_csv(existing_file)
    print(f"✅ 기존 데이터 로드 완료: {len(df_existing)}개 팰")
    
    # 89번-92번 팰 데이터
    new_pals_data = [
        {
            # 89번 킹파카 (Kingpaca)
            'id': 89,
            'name_kor': '킹파카',
            'description_kor': '멜파카의 시중을 받는다. 킹파카끼리 결투로 서열을 정한다. 혼자인 개체는 패배한 녀석이다.',
            'elements': '무',
            'partnerSkill_name': '파워풀 킹',
            'partnerSkill_describe': '등에 타고 이동할 수 있다. 보유하고 있는 동안 킹파카이가 짐을 대신 짊어져 플레이어의 소지 중량 제한이 증가한다.',
            'partnerSkill_needItem': '킹파카 안장',
            'partnerSkill_needItemTechLevel': 21,
            'partnerSkill_level': '1,2,3,4,5',
            'stats_size': 'XL',
            'stats_rarity': 8,
            'stats_health': 120,
            'stats_food': 475,
            'stats_meleeAttack': 100,
            'stats_attack': 85,
            'stats_defense': 90,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 90,
            'stats_combiRank': 470,
            'stats_goldCoin': 5800,
            'stats_egg': '평범하고 거대한 알',
            'stats_code': 'KingAlpaca',
            'movement_slowWalkSpeed': 80,
            'movement_walkSpeed': 80,
            'movement_runSpeed': 700,
            'movement_rideSprintSpeed': 1040,
            'movement_transportSpeed': 290,
            'level60_health': '4725-5895',
            'level60_attack': '514-638',
            'level60_defense': '488-620',
            'activeSkills': '모래 돌풍(땅)|파워 샷(무)|파워 폭탄(무)|킹 프레스(무)|트라이 썬더(번개)|바위 창(땅)|팰 폭발(무)',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '양털',
            'drops_count': 1,
            'workSuitabilities': '채집 Lv1',
            'workSuitabilities_count': 1,
            'tribes': 'KingAlpaca',
            'tribes_count': 1,
            'spawners': '제2 사냥 금지 구역 Lv.40-45',
            'spawners_count': 1
        },
        {
            # 90번 그린모스 (Mammorest)
            'id': 90,
            'name_kor': '그린모스',
            'description_kor': '등에 있는 식물은 개체마다 제각각이다. 관상용으로 익숙한 역사도 있으며 그린모스 전문 정원사마저 존재했다.',
            'elements': '풀|땅',
            'partnerSkill_name': '가이아 크래셔',
            'partnerSkill_describe': '등에 타고 이동할 수 있다. 탑승 중 나무와 광석 파괴 효율이 향상된다.',
            'partnerSkill_needItem': '그린모스 안장',
            'partnerSkill_needItemTechLevel': 29,
            'partnerSkill_level': '1,2,3,4,5',
            'stats_size': 'XL',
            'stats_rarity': 8,
            'stats_health': 150,
            'stats_food': 525,
            'stats_meleeAttack': 100,
            'stats_attack': 85,
            'stats_defense': 90,
            'stats_workSpeed': 100,
            'stats_support': 30,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 300,
            'stats_goldCoin': 9450,
            'stats_egg': '신록의 거대한 알',
            'stats_code': 'GrassMammoth',
            'movement_slowWalkSpeed': 100,
            'movement_walkSpeed': 135,
            'movement_runSpeed': 600,
            'movement_rideSprintSpeed': 1030,
            'movement_transportSpeed': 282,
            'level60_health': '5700-7162',
            'level60_attack': '514-638',
            'level60_defense': '488-620',
            'activeSkills': '모래 돌풍(땅)|씨앗 기관총(풀)|파워 폭탄(무)|초록 폭풍(풀)|대지 강타(땅)|가시덩굴(풀)|태양 폭발(풀)',
            'activeSkills_count': 7,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '고급 팰 기름|가죽|그린모스의 거대 고기',
            'drops_count': 3,
            'workSuitabilities': '파종 Lv2|벌목 Lv2|채굴 Lv2',
            'workSuitabilities_count': 3,
            'tribes': 'GrassMammoth',
            'tribes_count': 1,
            'spawners': '다수 지역 스폰',
            'spawners_count': 6
        },
        {
            # 91번 움포 (Wumpo)
            'id': 91,
            'name_kor': '움포',
            'description_kor': '정체를 밝혀내려고 연구자가 털을 깎았지만 애초부터 안엔 아무것도 없었다는 듯 털만 남아 있었다.',
            'elements': '얼음',
            'partnerSkill_name': '설산의 거인',
            'partnerSkill_describe': '등에 타고 이동할 수 있다. 보유하고 있는 동안 움포이가 짐을 대신 짊어져 플레이어의 소지 중량 제한이 증가한다.',
            'partnerSkill_needItem': '움포 안장',
            'partnerSkill_needItemTechLevel': 44,
            'partnerSkill_level': '1,2,3,4,5',
            'stats_size': 'L',
            'stats_rarity': 7,
            'stats_health': 140,
            'stats_food': 525,
            'stats_meleeAttack': 100,
            'stats_attack': 80,
            'stats_defense': 100,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 50,
            'stats_combiRank': 460,
            'stats_goldCoin': 5900,
            'stats_egg': '얼어붙은 대형 알',
            'stats_code': 'Yeti',
            'movement_slowWalkSpeed': 70,
            'movement_walkSpeed': 100,
            'movement_runSpeed': 600,
            'movement_rideSprintSpeed': 1050,
            'movement_transportSpeed': 150,
            'level60_health': '5375-6740',
            'level60_attack': '490-607',
            'level60_defense': '537-683',
            'activeSkills': '얼음 미사일(얼음)|바람의 칼날(풀)|얼음 칼날(얼음)|빙산(얼음)|서리 낀 입김(얼음)|눈덩이 굴리기(얼음)|눈보라 스파이크(얼음)|태양 폭발(풀)',
            'activeSkills_count': 8,
            'passiveSkills': '',
            'passiveSkills_count': 0,
            'drops': '빙결 기관|예쁜 꽃',
            'drops_count': 2,
            'workSuitabilities': '수작업 Lv2|벌목 Lv3|냉각 Lv2|운반 Lv4',
            'workSuitabilities_count': 4,
            'tribes': 'Yeti',
            'tribes_count': 1,
            'spawners': '영봉의 동굴 외 다수',
            'spawners_count': 4
        },
        {
            # 92번 장수벌레 (Warsect)
            'id': 92,
            'name_kor': '장수벌레',
            'description_kor': '전신을 감싸는 초강력 장갑은 압도적인 강도와 내열성을 자랑한다. 네이팜탄마저 거의 효과를 못 본다.',
            'elements': '땅|풀',
            'partnerSkill_name': '튼튼한 갑옷',
            'partnerSkill_describe': '함께 싸우는 동안 플레이어의 방어력이 증가하며 화염 속성 피해를 경감한다.',
            'partnerSkill_needItem': '',
            'partnerSkill_needItemTechLevel': '',
            'partnerSkill_level': '1,2,3,4,5',
            'stats_size': 'L',
            'stats_rarity': 8,
            'stats_health': 120,
            'stats_food': 400,
            'stats_meleeAttack': 100,
            'stats_attack': 100,
            'stats_defense': 120,
            'stats_workSpeed': 100,
            'stats_support': 100,
            'stats_captureRateCorrect': 1,
            'stats_maleProbability': 85,
            'stats_combiRank': 340,
            'stats_goldCoin': 6830,
            'stats_egg': '거친 느낌의 거대한 알',
            'stats_code': 'HerculesBeetle',
            'movement_slowWalkSpeed': 55,
            'movement_walkSpeed': 110,
            'movement_runSpeed': 500,
            'movement_rideSprintSpeed': 600,
            'movement_transportSpeed': 110,
            'level60_health': '4725-5895',
            'level60_attack': '587-733',
            'level60_defense': '635-810',
            'activeSkills': '바람의 칼날(풀)|씨앗 기관총(풀)|바위 폭발(땅)|바위 대포(땅)|거대한 뿔(땅)|바위 창(땅)|태양 폭발(풀)',
            'activeSkills_count': 7,
            'passiveSkills': '단단한 피부',
            'passiveSkills_count': 1,
            'drops': '벌꿀',
            'drops_count': 1,
            'workSuitabilities': '파종 Lv1|수작업 Lv1|벌목 Lv3|운반 Lv3',
            'workSuitabilities_count': 4,
            'tribes': 'HerculesBeetle',
            'tribes_count': 1,
            'spawners': '중갑의 투사 장수벌레 외 다수',
            'spawners_count': 4
        }
    ]
    
    # 새로운 팰들을 DataFrame으로 변환
    df_new = pd.DataFrame(new_pals_data)
    print(f"✅ 새로운 팰 데이터 생성: {len(df_new)}개")
    
    # 기존 데이터와 새 데이터 결합
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    
    # 새 파일로 저장
    output_file = 'complete_1_to_92_pals.csv'
    df_combined.to_csv(output_file, index=False, encoding='utf-8-sig')
    
    print(f"🎉 성공! {output_file} 파일이 생성되었습니다!")
    print(f"📊 총 팰 수: {len(df_combined)}개")
    print(f"📈 89-92번 팰 추가 완료!")
    
    # 추가된 팰들 정보 출력
    print("\n🎯 새로 추가된 팰들:")
    for pal in new_pals_data:
        print(f"- {pal['id']}번 {pal['name_kor']} ({pal['elements']}) - {pal['partnerSkill_name']}")

if __name__ == "__main__":
    add_pals_89_to_92() 