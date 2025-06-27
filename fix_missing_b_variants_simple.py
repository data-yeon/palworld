#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
간단한 방식으로 누락된 3개 B variants 추가 (31B, 32B, 33B)
"""

import csv
import json

def main():
    input_file = "enhanced_complete_pals_batch4_fixed.csv"
    output_file = "enhanced_complete_pals_batch4_final.csv"
    
    # 누락된 3개 B variants 완전 데이터 - CSV 형식으로
    new_rows = [
        "31B,샤맨더,먼 옛날엔 거대하고 강력한 수생 팰이었지만 먹이가 적어지며 지상으로 나왔다. 걷는 데 상당한 칼로리를 연소한 결과 화염의 힘에 눈뜨게 됐다!,화염,삐돌이 상어,발동하면 목표로 삼은 적을 향해 높은 위력의 스피릿 파이어로 공격한다. 보유하고 있는 동안 플레이어의 공격력이 증가한다.,기술,31,1.0,S,3,90,225,90,75,100,100,100,1,50,1100,1800,열기 나는 알,Gobfin_Ignis,50,80,400,500,120,3750 – 4627,538 – 670,415 – 525,\"[{\"\"level\"\": 1, \"\"name\"\": \"\"파이어 샷\"\", \"\"element\"\": \"\"화염\"\", \"\"cooltime\"\": 2, \"\"power\"\": 30}, {\"\"level\"\": 7, \"\"name\"\": \"\"파워 샷\"\", \"\"element\"\": \"\"무\"\", \"\"cooltime\"\": 4, \"\"power\"\": 35}, {\"\"level\"\": 15, \"\"name\"\": \"\"스피릿 파이어\"\", \"\"element\"\": \"\"화염\"\", \"\"cooltime\"\": 7, \"\"power\"\": 45}, {\"\"level\"\": 22, \"\"name\"\": \"\"불화살\"\", \"\"element\"\": \"\"화염\"\", \"\"cooltime\"\": 10, \"\"power\"\": 55}, {\"\"level\"\": 30, \"\"name\"\": \"\"라인 썬더\"\", \"\"element\"\": \"\"번개\"\", \"\"cooltime\"\": 16, \"\"power\"\": 75}, {\"\"level\"\": 40, \"\"name\"\": \"\"화염구\"\", \"\"element\"\": \"\"화염\"\", \"\"cooltime\"\": 55, \"\"power\"\": 150}, {\"\"level\"\": 50, \"\"name\"\": \"\"인페르노\"\", \"\"element\"\": \"\"화염\"\", \"\"cooltime\"\": 40, \"\"power\"\": 120}]\",7,,,발화 기관 x1 (100%),2,불 피우기:2|수작업:1|운반:1,3,화산의 망나니 샤맨더 (Tribe Boss) | 샤맨더 (Tribe Normal),2,Lv. 23–28 3_2_volcano_1 | Lv. 32–35 모래 언덕 동굴,2,Gobfin_Ignis,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
        "32B,유령건다리,얼음덩어리도 찢어버릴 만큼 거대한 팔이 특징. 대역죄인을 마을 광장에 결박하여 유령건다리의 힘으로 머리채를 쥐어뜯어버리는 잔혹한 형벌이 시행됐던 적도 있다.,얼음,겨울 하늘 그네,보유하고 있는 동안 장착 중인 글라이더의 성능이 변화한다. 활공 중 천천히 상승 기류를 탈 수 있다.,기술,32,1.0,XS,2,80,150,80,70,100,100,100,1,50,1422,1020,얼어붙은 알,Hangyu_Cryst,50,100,400,550,250,3425 – 4205,490 – 607,391 – 493,\"[{\"\"level\"\": 1, \"\"name\"\": \"\"공기 대포\"\", \"\"element\"\": \"\"무\"\", \"\"cooltime\"\": 2, \"\"power\"\": 25}, {\"\"level\"\": 7, \"\"name\"\": \"\"얼음 미사일\"\", \"\"element\"\": \"\"얼음\"\", \"\"cooltime\"\": 3, \"\"power\"\": 30}, {\"\"level\"\": 15, \"\"name\"\": \"\"파워 샷\"\", \"\"element\"\": \"\"무\"\", \"\"cooltime\"\": 4, \"\"power\"\": 35}, {\"\"level\"\": 22, \"\"name\"\": \"\"얼음 칼날\"\", \"\"element\"\": \"\"얼음\"\", \"\"cooltime\"\": 10, \"\"power\"\": 55}, {\"\"level\"\": 30, \"\"name\"\": \"\"빙산\"\", \"\"element\"\": \"\"얼음\"\", \"\"cooltime\"\": 15, \"\"power\"\": 70}, {\"\"level\"\": 40, \"\"name\"\": \"\"서리 낀 입김\"\", \"\"element\"\": \"\"얼음\"\", \"\"cooltime\"\": 22, \"\"power\"\": 90}, {\"\"level\"\": 50, \"\"name\"\": \"\"눈보라 스파이크\"\", \"\"element\"\": \"\"얼음\"\", \"\"cooltime\"\": 45, \"\"power\"\": 130}]\",7,,,섬유 x5–10 (100%) | 빙결 기관 x1 (100%),2,수작업:1|채집:1|냉각:1|운반:2,2,빙하의 운반자 유령건다리 (Tribe Boss) | 유령건다리 (Tribe Normal),2,Lv. 33–35 snow_5_1_snow_1 | Lv. 33–35 snow_5_2_SnowGrass,2,Hangyu_Cryst,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,",
        "33B,썬더판다,믿기 힘든 괴력의 소유자. 전기를 신호로 바꿔 신체 능력의 한계를 돌파했다. 최강 생물이 화제에 오르면 절대 빠지지 않는다.,번개,척탄 판다,등에 타고 이동할 수 있다. 탑승 중 수류탄 발사기 연사가 가능해진다.,기술,33,1.0,L,7,100,350,100,100,100,100,100,1,50,390,6610,찌릿찌릿한 대형 알,Mossanda_Lux,50,100,600,1000,275,4075 – 5050,587 – 733,537 – 683,\"[{\"\"level\"\": 1, \"\"name\"\": \"\"스파크 샷\"\", \"\"element\"\": \"\"번개\"\", \"\"cooltime\"\": 2, \"\"power\"\": 30}, {\"\"level\"\": 7, \"\"name\"\": \"\"전기 파장\"\", \"\"element\"\": \"\"번개\"\", \"\"cooltime\"\": 4, \"\"power\"\": 40}, {\"\"level\"\": 15, \"\"name\"\": \"\"라인 썬더\"\", \"\"element\"\": \"\"번개\"\", \"\"cooltime\"\": 16, \"\"power\"\": 75}, {\"\"level\"\": 22, \"\"name\"\": \"\"폭발 펀치\"\", \"\"element\"\": \"\"번개\"\", \"\"cooltime\"\": 14, \"\"power\"\": 85}, {\"\"level\"\": 30, \"\"name\"\": \"\"트라이 썬더\"\", \"\"element\"\": \"\"번개\"\", \"\"cooltime\"\": 22, \"\"power\"\": 90}, {\"\"level\"\": 40, \"\"name\"\": \"\"번개 일격\"\", \"\"element\"\": \"\"번개\"\", \"\"cooltime\"\": 40, \"\"power\"\": 120}, {\"\"level\"\": 50, \"\"name\"\": \"\"전기 볼트\"\", \"\"element\"\": \"\"번개\"\", \"\"cooltime\"\": 55, \"\"power\"\": 150}]\",7,,,버섯 x2–3 (100%) | 발전 기관 x1–2 (100%) | 가죽 x2–3 (100%),2,발전:2|수작업:2|벌목:2|운반:3,5,번개에 맞은 괴짜 썬더판다 (Tribe Boss) | 썬더판다 (Tribe Normal),2,Lv. 35–37 화산 동굴,2,Mossanda_Lux,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"
    ]
    
    print("🔄 기존 CSV 파일 읽는 중...")
    
    # 기존 파일의 모든 라인 읽기
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print(f"📊 기존 라인 수: {len(lines)}")
    
    # 23B 라인 찾기 (124번째 라인)
    target_line = None
    for i, line in enumerate(lines):
        if line.startswith('23B,'):
            target_line = i
            print(f"🎯 23B 라인 발견: {i+1}번째 라인")
            break
    
    if target_line is not None:
        # 23B 다음에 31B, 32B, 33B 삽입
        for j, new_row in enumerate(new_rows):
            lines.insert(target_line + 1 + j, new_row + '\n')
            print(f"✅ 삽입: {new_row.split(',')[0]} {new_row.split(',')[1]}")
    
    # 새 파일에 저장
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"\n🎉 완료! {output_file}에 저장되었습니다.")
    print(f"📈 새 라인 수: {len(lines)}")
    
    # B variants 개수 확인
    b_count = sum(1 for line in lines if ',B,' in line or line.startswith(('31B,', '32B', '33B,')))
    print(f"📊 B variants 개수: {b_count}")

if __name__ == "__main__":
    main() 