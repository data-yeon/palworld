#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
까부냥 페이지 데이터를 파싱하여 완벽한 JSON 구조로 변환
"""

import re
import json

def parse_cattiva_data():
    """까부냥 마크다운 데이터를 JSON으로 파싱"""
    
    # 파싱된 까부냥 데이터
    cattiva_data = {
        "id": "2",
        "name_kor": "까부냥",
        "pal_nick_kor": "#2",
        "description_kor": "얼핏 보기엔 당당하지만 실은 대단한 겁쟁이다. 까부냥이(가) 핥아준다는 건 어떤 의미에선 최고의 굴욕이다.",
        "elements": ["무속성"],
        "stats": {
            "size": "XS",
            "rarity": 1,
            "health": 70,
            "food": 150,
            "meleeAttack": 70,
            "attack": 70,
            "defense": 70,
            "workSpeed": 100,
            "support": 100,
            "captureRateCorrect": 1.5,
            "maleProbability": 50,
            "combiRank": 1460,
            "goldCoin": 1000,
            "egg": "평범한 알",
            "code": "PinkCat"
        },
        "movement": {
            "slowWalkSpeed": 30,
            "walkSpeed": 60,
            "runSpeed": 400,
            "rideSprintSpeed": 550,
            "transportSpeed": 160
        },
        "level60Stats": {
            "health": "3100–3782",
            "attack": "441–543", 
            "defense": "391–493"
        },
        "partnerSkill": {
            "name": "고양이 손 빌리기",
            "describe": "보유하고 있는 동안 까부냥이(가) 짐을 대신 짊어져 플레이어의 소지 중량 제한이 증가한다.",
            "needItem": "",
            "needItemTechLevel": 0,
            "level": 1
        },
        "activeSkills": [
            {
                "name": "냥냥 펀치",
                "element": "무속성",
                "power": 40,
                "coolTime": 1,
                "level": 1,
                "meleeAttack": True,
                "shootAttack": False,
                "describe": "아누비스 전용 스킬. 적을 쫓아가며 양팔을 휘둘러 연속으로 펀치를 퍼붓는다."
            },
            {
                "name": "공기 대포",
                "element": "무속성", 
                "power": 25,
                "coolTime": 2,
                "level": 7,
                "meleeAttack": False,
                "shootAttack": True,
                "describe": "고속으로 날아가는 공기 덩어리를 발사한다."
            },
            {
                "name": "모래 돌풍",
                "element": "땅 속성",
                "power": 40,
                "coolTime": 4,
                "level": 15,
                "meleeAttack": False,
                "shootAttack": True,
                "accumulatedElement": "진흙",
                "accumulatedValue": 50,
                "describe": "끈적거리는 진흙을 적을 향해 발사한다."
            },
            {
                "name": "파워 샷",
                "element": "무속성",
                "power": 35,
                "coolTime": 4,
                "level": 22,
                "meleeAttack": False,
                "shootAttack": True,
                "describe": "에너지를 모아 탄환 형태로 발사한다."
            },
            {
                "name": "바람의 칼날",
                "element": "풀 속성",
                "power": 30,
                "coolTime": 2,
                "level": 30,
                "meleeAttack": False,
                "shootAttack": True,
                "accumulatedElement": "덩굴",
                "accumulatedValue": 35,
                "describe": "적을 향해 일직선으로 날아가는 초고속 바람의 칼날을 발사한다."
            },
            {
                "name": "씨앗 기관총",
                "element": "풀 속성",
                "power": 50,
                "coolTime": 9,
                "level": 40,
                "meleeAttack": False,
                "shootAttack": True,
                "accumulatedElement": "덩굴",
                "accumulatedValue": 100,
                "describe": "딱딱한 씨앗을 많이 쏟아내며 전방의 적을 공격한다."
            },
            {
                "name": "팰 폭발",
                "element": "무속성",
                "power": 150,
                "coolTime": 55,
                "level": 50,
                "meleeAttack": False,
                "shootAttack": True,
                "describe": "파괴 에너지를 모아 전방에 광범위하게 초강력 광선을 발사한다."
            }
        ],
        "passiveSkills": [
            {
                "name": "겁쟁이",
                "effect": "공격 -10%"
            }
        ],
        "drops": [
            {
                "itemName": "빨간 열매",
                "quantity": "1",
                "probability": "100%"
            }
        ],
        "workSuitabilities": [
            {"work": "수작업", "level": 1},
            {"work": "채집", "level": 1},
            {"work": "채굴", "level": 1},
            {"work": "운반", "level": 1}
        ],
        "tribes": [
            {
                "name": "잘난 척 대마왕 까부냥",
                "type": "Tribe Boss"
            },
            {
                "name": "까부냥",
                "type": "Tribe Normal"
            }
        ],
        "spawners": [
            {
                "name": "까부냥",
                "level": "Lv. 1–3",
                "area": "1_1_plain_begginer"
            },
            {
                "name": "까부냥", 
                "level": "Lv. 3–5",
                "area": "1_3_plain_kitsunbi"
            },
            {
                "name": "까부냥",
                "level": "Lv. 2–5", 
                "area": "PvP_21_1_1"
            },
            {
                "name": "까부냥",
                "level": "Lv. 2–5",
                "area": "PvP_21_2_1"
            },
            {
                "name": "잘난 척 대마왕 까부냥",
                "level": "Lv. 10–13",
                "area": "구릉 동굴, 외딴 섬의 동굴"
            },
            {
                "name": "까부냥",
                "level": "Lv. 6–9",
                "area": "구릉 동굴, 외딴 섬의 동굴"
            },
            {
                "name": "까부냥",
                "level": "Lv. 40–45",
                "area": "sakurajima_6_2_SakuraArea"
            },
            {
                "name": "까부냥",
                "level": "평범한 알",
                "area": "Sakurajima_grade_01"
            },
            {
                "name": "까부냥",
                "level": "Lv. 10 – 20",
                "area": "Captured Cage: Grass2"
            }
        ]
    }
    
    return cattiva_data

def main():
    print("🔍 까부냥 데이터 파싱 시작...")
    
    # 데이터 파싱
    cattiva_data = parse_cattiva_data()
    
    # JSON 파일로 저장
    output_file = 'cattiva_parsed.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cattiva_data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 까부냥 데이터 저장 완료: {output_file}")
    
    # 데이터 요약 출력
    print(f"\n📄 까부냥 데이터 요약:")
    print(f"   - ID: {cattiva_data['id']}")
    print(f"   - 이름: {cattiva_data['name_kor']}")
    print(f"   - 속성: {', '.join(cattiva_data['elements'])}")
    print(f"   - 액티브 스킬: {len(cattiva_data['activeSkills'])}개")
    print(f"   - 작업 적성: {len(cattiva_data['workSuitabilities'])}개")
    print(f"   - 스포너: {len(cattiva_data['spawners'])}개")
    
    print(f"\n🎯 이 구조로 214개 팰을 모두 추출하면 완전한 CSV 생성 가능!")
    print(f"💡 다음 단계: 자동 파싱 스크립트로 나머지 팰들도 빠르게 추출")

if __name__ == "__main__":
    main() 