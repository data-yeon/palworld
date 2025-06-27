#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
팰월드 B variants 데이터 추가 스크립트 - Batch 4 (Corrected)
8개의 새로운 B variants를 기존 CSV에 추가합니다.
실제 CSV 필드명에 맞춰서 수정됨.
"""

import csv

def main():
    # 새로운 B variants 데이터 정의 (기존 CSV 필드명에 맞춤)
    new_b_variants = [
        {
            "id": "23B",
            "name_kor": "드리문", 
            "name_eng": "Killamari_Primo",
            "description_kor": "적의 목을 물어 혈액을 모조리 빨아들인다.",
            "elements": "무+물",
            "stats_rarity": 2,
            "stats_health": 70,
            "stats_attack": 60,
            "stats_defense": 70,
            "stats_workSpeed": 100,
            "stats_food": 3,
            "partnerSkill_name": "꿈튀김",
            "partnerSkill_describe": "보유하고 있는 동안 장착 중인 글라이더의 성능이 변화한다.",
            "activeSkills": "[{\"level\": 1, \"name\": \"공기 대포\", \"element\": \"무\", \"cooltime\": 2, \"power\": 25}, {\"level\": 7, \"name\": \"파워 샷\", \"element\": \"무\", \"cooltime\": 4, \"power\": 35}, {\"level\": 15, \"name\": \"버블 샷\", \"element\": \"물\", \"cooltime\": 13, \"power\": 65}, {\"level\": 22, \"name\": \"파워 폭탄\", \"element\": \"무\", \"cooltime\": 15, \"power\": 70}, {\"level\": 30, \"name\": \"산성비\", \"element\": \"물\", \"cooltime\": 18, \"power\": 80}, {\"level\": 40, \"name\": \"고압수 발사\", \"element\": \"물\", \"cooltime\": 35, \"power\": 110}, {\"level\": 50, \"name\": \"하이드로 스트림\", \"element\": \"물\", \"cooltime\": 55, \"power\": 150}]",
            "workSuitabilities": "관개:1,채집:1,운반:2"
        },
        {
            "id": "24B",
            "name_kor": "칠테트",
            "name_eng": "Mau_Cryst", 
            "description_kor": "꼬리의 결정은 아름답지만 죽기 무섭게 망가져 버린다.",
            "elements": "얼음",
            "stats_rarity": 2,
            "stats_health": 70,
            "stats_attack": 65,
            "stats_defense": 70,
            "stats_workSpeed": 100,
            "stats_food": 1,
            "partnerSkill_name": "금화 수집",
            "partnerSkill_describe": "가축 목장에 배치하면 지면에서 금화를 파내기도 한다.",
            "activeSkills": "[{\"level\": 1, \"name\": \"얼음 미사일\", \"element\": \"얼음\", \"cooltime\": 3, \"power\": 30}, {\"level\": 7, \"name\": \"공기 대포\", \"element\": \"무\", \"cooltime\": 2, \"power\": 25}, {\"level\": 15, \"name\": \"모래 돌풍\", \"element\": \"땅\", \"cooltime\": 4, \"power\": 40}, {\"level\": 22, \"name\": \"얼음 칼날\", \"element\": \"얼음\", \"cooltime\": 10, \"power\": 55}, {\"level\": 30, \"name\": \"빙산\", \"element\": \"얼음\", \"cooltime\": 15, \"power\": 70}, {\"level\": 40, \"name\": \"서리 낀 입김\", \"element\": \"얼음\", \"cooltime\": 22, \"power\": 90}, {\"level\": 50, \"name\": \"눈보라 스파이크\", \"element\": \"얼음\", \"cooltime\": 45, \"power\": 130}]",
            "workSuitabilities": "냉각:1,목장:1"
        },
        {
            "id": "25B",
            "name_kor": "일레카이트",
            "name_eng": "Celaray_Lux",
            "description_kor": "무늬가 화려할수록 파트너의 이목을 끌 수 있다고 한다.",
            "elements": "물+번개",
            "stats_rarity": 4,
            "stats_health": 80,
            "stats_attack": 75,
            "stats_defense": 80,
            "stats_workSpeed": 100,
            "stats_food": 3,
            "partnerSkill_name": "짜릿바람 글라이더",
            "partnerSkill_describe": "보유하고 있는 동안 장착 중인 글라이더의 성능이 변화한다.",
            "activeSkills": "[{\"level\": 1, \"name\": \"번개 창\", \"element\": \"번개\", \"cooltime\": 2, \"power\": 30}, {\"level\": 7, \"name\": \"전기 파장\", \"element\": \"번개\", \"cooltime\": 4, \"power\": 40}, {\"level\": 15, \"name\": \"버블 샷\", \"element\": \"물\", \"cooltime\": 13, \"power\": 65}, {\"level\": 22, \"name\": \"라인 썬더\", \"element\": \"번개\", \"cooltime\": 16, \"power\": 75}, {\"level\": 30, \"name\": \"라인 스플래시\", \"element\": \"물\", \"cooltime\": 22, \"power\": 90}, {\"level\": 40, \"name\": \"고압수 발사\", \"element\": \"물\", \"cooltime\": 35, \"power\": 110}, {\"level\": 50, \"name\": \"전기 볼트\", \"element\": \"번개\", \"cooltime\": 55, \"power\": 150}]",
            "workSuitabilities": "관개:1,발전:1,운반:1"
        },
        {
            "id": "35B",
            "name_kor": "베노고트",
            "name_eng": "Caprity_Noct",
            "description_kor": "정신 상태에 따라 등의 덤불에 맺히는 열매의 맛이 변화한다.",
            "elements": "어둠",
            "stats_rarity": 3,
            "stats_health": 100,
            "stats_attack": 75,
            "stats_defense": 90,
            "stats_workSpeed": 100,
            "stats_food": 4,
            "partnerSkill_name": "독샘 채집",
            "partnerSkill_describe": "가축 목장에 배치하면 등에서 독샘을 떨어뜨리기도 한다.",
            "activeSkills": "[{\"level\": 1, \"name\": \"독 안개\", \"element\": \"어둠\", \"cooltime\": 30, \"power\": 0}, {\"level\": 7, \"name\": \"바람의 칼날\", \"element\": \"풀\", \"cooltime\": 2, \"power\": 30}, {\"level\": 15, \"name\": \"독 사격\", \"element\": \"어둠\", \"cooltime\": 2, \"power\": 30}, {\"level\": 22, \"name\": \"멀티 커터\", \"element\": \"풀\", \"cooltime\": 12, \"power\": 60}, {\"level\": 30, \"name\": \"포이즌 샤워\", \"element\": \"어둠\", \"cooltime\": 22, \"power\": 90}, {\"level\": 40, \"name\": \"원형 덩굴\", \"element\": \"풀\", \"cooltime\": 40, \"power\": 120}, {\"level\": 50, \"name\": \"어둠의 레이저\", \"element\": \"어둠\", \"cooltime\": 55, \"power\": 150}]",
            "workSuitabilities": "파종:2,목장:1"
        },
        {
            "id": "37B",
            "name_kor": "산령사슴",
            "name_eng": "Eikthyrdeer_Terra",
            "description_kor": "뿔이 제일 단단한 개체가 우두머리가 된다.",
            "elements": "땅",
            "stats_rarity": 6,
            "stats_health": 95,
            "stats_attack": 80,
            "stats_defense": 80,
            "stats_workSpeed": 100,
            "stats_food": 5,
            "partnerSkill_name": "금빛 숲의 수호자",
            "partnerSkill_describe": "등에 타고 이동할 수 있다. 탑승 중 2단 점프가 가능해지며 나무 파괴 효율이 향상된다.",
            "activeSkills": "[{\"level\": 1, \"name\": \"파워 샷\", \"element\": \"무\", \"cooltime\": 4, \"power\": 35}, {\"level\": 7, \"name\": \"들이받기\", \"element\": \"무\", \"cooltime\": 5, \"power\": 50}, {\"level\": 15, \"name\": \"바위 폭발\", \"element\": \"땅\", \"cooltime\": 10, \"power\": 55}, {\"level\": 22, \"name\": \"바위 대포\", \"element\": \"땅\", \"cooltime\": 15, \"power\": 70}, {\"level\": 30, \"name\": \"파워 폭탄\", \"element\": \"무\", \"cooltime\": 15, \"power\": 70}, {\"level\": 40, \"name\": \"모래 폭풍\", \"element\": \"땅\", \"cooltime\": 18, \"power\": 80}, {\"level\": 50, \"name\": \"바위 창\", \"element\": \"땅\", \"cooltime\": 55, \"power\": 150}]",
            "workSuitabilities": "벌목:2"
        },
        {
            "id": "39B",
            "name_kor": "그래토",
            "name_eng": "Ribbuny_Botan",
            "description_kor": "항상 방긋방긋 웃는 얼굴로 지낸다.",
            "elements": "풀",
            "stats_rarity": 1,
            "stats_health": 80,
            "stats_attack": 65,
            "stats_defense": 70,
            "stats_workSpeed": 100,
            "stats_food": 2,
            "partnerSkill_name": "풀뜨기 장인",
            "partnerSkill_describe": "보유하고 있는 동안 풀 속성 팰의 공격력이 증가한다.",
            "activeSkills": "[{\"level\": 1, \"name\": \"바람의 칼날\", \"element\": \"풀\", \"cooltime\": 2, \"power\": 30}, {\"level\": 7, \"name\": \"모래 돌풍\", \"element\": \"땅\", \"cooltime\": 4, \"power\": 40}, {\"level\": 15, \"name\": \"씨앗 기관총\", \"element\": \"풀\", \"cooltime\": 9, \"power\": 50}, {\"level\": 22, \"name\": \"씨앗 지뢰\", \"element\": \"풀\", \"cooltime\": 13, \"power\": 65}, {\"level\": 30, \"name\": \"윈드 에지\", \"element\": \"풀\", \"cooltime\": 22, \"power\": 90}, {\"level\": 40, \"name\": \"원형 덩굴\", \"element\": \"풀\", \"cooltime\": 40, \"power\": 120}, {\"level\": 50, \"name\": \"태양 폭발\", \"element\": \"풀\", \"cooltime\": 55, \"power\": 150}]",
            "workSuitabilities": "파종:1,수작업:1,채집:1,운반:1"
        },
        {
            "id": "40B",
            "name_kor": "아비스고트",
            "name_eng": "Incineram_Noct",
            "description_kor": "어린 팰만 노려 자기 구역에 데리고 간다.",
            "elements": "어둠",
            "stats_rarity": 5,
            "stats_health": 95,
            "stats_attack": 105,
            "stats_defense": 85,
            "stats_workSpeed": 100,
            "stats_food": 4,
            "partnerSkill_name": "암흑 발톱의 사냥꾼",
            "partnerSkill_describe": "발동하면 목표로 삼은 적을 향해 높은 위력의 지옥불 할퀴기로 공격한다.",
            "activeSkills": "[{\"level\": 1, \"name\": \"파이어 샷\", \"element\": \"화염\", \"cooltime\": 2, \"power\": 30}, {\"level\": 7, \"name\": \"스피릿 파이어\", \"element\": \"화염\", \"cooltime\": 7, \"power\": 45}, {\"level\": 15, \"name\": \"불화살\", \"element\": \"화염\", \"cooltime\": 10, \"power\": 55}, {\"level\": 22, \"name\": \"지옥불 할퀴기\", \"element\": \"화염\", \"cooltime\": 10, \"power\": 70}, {\"level\": 30, \"name\": \"그림자 폭발\", \"element\": \"어둠\", \"cooltime\": 10, \"power\": 55}, {\"level\": 40, \"name\": \"화염구\", \"element\": \"화염\", \"cooltime\": 55, \"power\": 150}, {\"level\": 50, \"name\": \"인페르노\", \"element\": \"화염\", \"cooltime\": 40, \"power\": 120}]",
            "workSuitabilities": "수작업:2,채굴:1,운반:2"
        },
        {
            "id": "45B",
            "name_kor": "칠리자드",
            "name_eng": "Leezpunk_Ignis",
            "description_kor": "자신의 포즈에 이상한 집착을 보인다.",
            "elements": "화염",
            "stats_rarity": 3,
            "stats_health": 80,
            "stats_attack": 80,
            "stats_defense": 50,
            "stats_workSpeed": 100,
            "stats_food": 3,
            "partnerSkill_name": "제6감",
            "partnerSkill_describe": "발동하면 6번째 감각을 활용해 가까이 있는 던전의 위치를 탐지할 수 있다.",
            "activeSkills": "[{\"level\": 1, \"name\": \"파이어 샷\", \"element\": \"화염\", \"cooltime\": 2, \"power\": 30}, {\"level\": 7, \"name\": \"독 사격\", \"element\": \"어둠\", \"cooltime\": 2, \"power\": 30}, {\"level\": 15, \"name\": \"스피릿 파이어\", \"element\": \"화염\", \"cooltime\": 7, \"power\": 45}, {\"level\": 22, \"name\": \"파이어 브레스\", \"element\": \"화염\", \"cooltime\": 15, \"power\": 70}, {\"level\": 30, \"name\": \"화염 폭풍\", \"element\": \"화염\", \"cooltime\": 18, \"power\": 80}, {\"level\": 40, \"name\": \"인페르노\", \"element\": \"화염\", \"cooltime\": 40, \"power\": 120}, {\"level\": 50, \"name\": \"화염구\", \"element\": \"화염\", \"cooltime\": 55, \"power\": 150}]",
            "workSuitabilities": "불 피우기:1,수작업:1,채집:1,운반:1"
        }
    ]
    
    # 기존 CSV 파일 읽기
    input_file = "enhanced_complete_pals_batch3.csv"
    output_file = "enhanced_complete_pals_batch4.csv"
    
    existing_data = []
    fieldnames = None
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        existing_data = list(reader)
    
    print(f"기존 데이터: {len(existing_data)}개 팰")
    
    # 새로운 B variants 추가
    for variant in new_b_variants:
        # 기존 필드에 맞춰 빈 값들로 채우기
        new_row = {}
        for field in fieldnames:
            if field in variant:
                new_row[field] = variant[field]
            else:
                new_row[field] = ""  # 빈 값으로 설정
        
        existing_data.append(new_row)
        print(f"✅ 추가됨: {variant['id']} {variant['name_kor']} ({variant['name_eng']})")
    
    # 새 CSV 파일에 저장
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames or [])
        writer.writeheader()
        writer.writerows(existing_data)
    
    print(f"\n🎉 완료! 총 {len(existing_data)}개 팰이 {output_file}에 저장되었습니다.")
    print(f"📈 새로 추가된 B variants: {len(new_b_variants)}개")
    
    # B variants 수 확인
    b_variants_count = sum(1 for row in existing_data if row['id'].endswith('B'))
    print(f"🔥 총 B variants 수: {b_variants_count}개")

if __name__ == "__main__":
    main() 