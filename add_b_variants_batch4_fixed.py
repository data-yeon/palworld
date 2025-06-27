#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
팰월드 B variants 데이터 추가 스크립트 - Batch 4 (Fixed)
8개의 새로운 B variants를 기존 CSV에 추가합니다.
"""

import csv
import re
from typing import List, Dict, Any

def parse_active_skills(skills_text: str) -> List[Dict[str, Any]]:
    """Active Skills 텍스트를 파싱하여 구조화된 데이터로 변환"""
    skills = []
    
    # 각 스킬을 레벨별로 분리
    skill_patterns = re.findall(r'Lv\.\s*(\d+)\s*\[([^\]]+)\].*?(?=Lv\.\s*\d+|$)', skills_text, re.DOTALL)
    
    for level, skill_name in skill_patterns:
        # 속성 찾기
        element_match = re.search(rf'{re.escape(skill_name)}.*?([가-힣]+)\s*속성', skills_text)
        element = element_match.group(1) if element_match else ""
        
        # 쿨타임 찾기
        cooltime_match = re.search(rf'{re.escape(skill_name)}.*?쿨타임.*?(\d+)', skills_text)
        cooltime = int(cooltime_match.group(1)) if cooltime_match else 0
        
        # 위력 찾기
        power_match = re.search(rf'{re.escape(skill_name)}.*?위력.*?(\d+)', skills_text)
        power = int(power_match.group(1)) if power_match else 0
        
        skills.append({
            "level": int(level),
            "name": skill_name,
            "element": element,
            "cooltime": cooltime,
            "power": power
        })
    
    return skills

def parse_work_suitability(work_text: str) -> Dict[str, int]:
    """작업 적성 정보를 파싱"""
    work_mapping = {
        "불 피우기": "Kindling",
        "관개": "Watering", 
        "파종": "Planting",
        "발전": "Generating Electricity",
        "수작업": "Handiwork",
        "채집": "Gathering",
        "벌목": "Lumbering",
        "채굴": "Mining",
        "냉각": "Cooling",
        "운반": "Transporting",
        "목장": "Farming"
    }
    
    work_suitability = {}
    
    for korean_name, english_name in work_mapping.items():
        pattern = rf'{korean_name}.*?Lv(\d+)'
        match = re.search(pattern, work_text)
        if match:
            work_suitability[english_name] = int(match.group(1))
    
    return work_suitability

def main():
    # 새로운 B variants 데이터 정의
    new_b_variants = [
        {
            "ID": "23B",
            "Name": "드리문",
            "English_Name": "Killamari_Primo", 
            "Elements": "무+물",
            "Rarity": 2,
            "HP": 70,
            "Attack": 60,
            "Defense": 70,
            "Work_Speed": 100,
            "Food": 3,
            "Skills": [
                {"level": 1, "name": "공기 대포", "element": "무", "cooltime": 2, "power": 25},
                {"level": 7, "name": "파워 샷", "element": "무", "cooltime": 4, "power": 35},
                {"level": 15, "name": "버블 샷", "element": "물", "cooltime": 13, "power": 65},
                {"level": 22, "name": "파워 폭탄", "element": "무", "cooltime": 15, "power": 70},
                {"level": 30, "name": "산성비", "element": "물", "cooltime": 18, "power": 80},
                {"level": 40, "name": "고압수 발사", "element": "물", "cooltime": 35, "power": 110},
                {"level": 50, "name": "하이드로 스트림", "element": "물", "cooltime": 55, "power": 150}
            ],
            "Partner_Skill": "꿈튀김",
            "Watering": 1,
            "Gathering": 1, 
            "Transporting": 2
        },
        {
            "ID": "24B",
            "Name": "칠테트",
            "English_Name": "Mau_Cryst",
            "Elements": "얼음",
            "Rarity": 2,
            "HP": 70,
            "Attack": 65,
            "Defense": 70,
            "Work_Speed": 100,
            "Food": 1,
            "Skills": [
                {"level": 1, "name": "얼음 미사일", "element": "얼음", "cooltime": 3, "power": 30},
                {"level": 7, "name": "공기 대포", "element": "무", "cooltime": 2, "power": 25},
                {"level": 15, "name": "모래 돌풍", "element": "땅", "cooltime": 4, "power": 40},
                {"level": 22, "name": "얼음 칼날", "element": "얼음", "cooltime": 10, "power": 55},
                {"level": 30, "name": "빙산", "element": "얼음", "cooltime": 15, "power": 70},
                {"level": 40, "name": "서리 낀 입김", "element": "얼음", "cooltime": 22, "power": 90},
                {"level": 50, "name": "눈보라 스파이크", "element": "얼음", "cooltime": 45, "power": 130}
            ],
            "Partner_Skill": "금화 수집",
            "Cooling": 1,
            "Farming": 1
        },
        {
            "ID": "25B", 
            "Name": "일레카이트",
            "English_Name": "Celaray_Lux",
            "Elements": "물+번개",
            "Rarity": 4,
            "HP": 80,
            "Attack": 75,
            "Defense": 80,
            "Work_Speed": 100,
            "Food": 3,
            "Skills": [
                {"level": 1, "name": "번개 창", "element": "번개", "cooltime": 2, "power": 30},
                {"level": 7, "name": "전기 파장", "element": "번개", "cooltime": 4, "power": 40},
                {"level": 15, "name": "버블 샷", "element": "물", "cooltime": 13, "power": 65},
                {"level": 22, "name": "라인 썬더", "element": "번개", "cooltime": 16, "power": 75},
                {"level": 30, "name": "라인 스플래시", "element": "물", "cooltime": 22, "power": 90},
                {"level": 40, "name": "고압수 발사", "element": "물", "cooltime": 35, "power": 110},
                {"level": 50, "name": "전기 볼트", "element": "번개", "cooltime": 55, "power": 150}
            ],
            "Partner_Skill": "짜릿바람 글라이더",
            "Watering": 1,
            "Generating Electricity": 1,
            "Transporting": 1
        },
        {
            "ID": "35B",
            "Name": "베노고트", 
            "English_Name": "Caprity_Noct",
            "Elements": "어둠",
            "Rarity": 3,
            "HP": 100,
            "Attack": 75,
            "Defense": 90,
            "Work_Speed": 100,
            "Food": 4,
            "Skills": [
                {"level": 1, "name": "독 안개", "element": "어둠", "cooltime": 30, "power": 0},
                {"level": 7, "name": "바람의 칼날", "element": "풀", "cooltime": 2, "power": 30},
                {"level": 15, "name": "독 사격", "element": "어둠", "cooltime": 2, "power": 30},
                {"level": 22, "name": "멀티 커터", "element": "풀", "cooltime": 12, "power": 60},
                {"level": 30, "name": "포이즌 샤워", "element": "어둠", "cooltime": 22, "power": 90},
                {"level": 40, "name": "원형 덩굴", "element": "풀", "cooltime": 40, "power": 120},
                {"level": 50, "name": "어둠의 레이저", "element": "어둠", "cooltime": 55, "power": 150}
            ],
            "Partner_Skill": "독샘 채집",
            "Planting": 2,
            "Farming": 1
        },
        {
            "ID": "37B",
            "Name": "산령사슴",
            "English_Name": "Eikthyrdeer_Terra",
            "Elements": "땅",
            "Rarity": 6,
            "HP": 95,
            "Attack": 80,
            "Defense": 80,
            "Work_Speed": 100,
            "Food": 5,
            "Skills": [
                {"level": 1, "name": "파워 샷", "element": "무", "cooltime": 4, "power": 35},
                {"level": 7, "name": "들이받기", "element": "무", "cooltime": 5, "power": 50},
                {"level": 15, "name": "바위 폭발", "element": "땅", "cooltime": 10, "power": 55},
                {"level": 22, "name": "바위 대포", "element": "땅", "cooltime": 15, "power": 70},
                {"level": 30, "name": "파워 폭탄", "element": "무", "cooltime": 15, "power": 70},
                {"level": 40, "name": "모래 폭풍", "element": "땅", "cooltime": 18, "power": 80},
                {"level": 50, "name": "바위 창", "element": "땅", "cooltime": 55, "power": 150}
            ],
            "Partner_Skill": "금빛 숲의 수호자",
            "Lumbering": 2
        },
        {
            "ID": "39B",
            "Name": "그래토",
            "English_Name": "Ribbuny_Botan",
            "Elements": "풀",
            "Rarity": 1,
            "HP": 80,
            "Attack": 65,
            "Defense": 70,
            "Work_Speed": 100,
            "Food": 2,
            "Skills": [
                {"level": 1, "name": "바람의 칼날", "element": "풀", "cooltime": 2, "power": 30},
                {"level": 7, "name": "모래 돌풍", "element": "땅", "cooltime": 4, "power": 40},
                {"level": 15, "name": "씨앗 기관총", "element": "풀", "cooltime": 9, "power": 50},
                {"level": 22, "name": "씨앗 지뢰", "element": "풀", "cooltime": 13, "power": 65},
                {"level": 30, "name": "윈드 에지", "element": "풀", "cooltime": 22, "power": 90},
                {"level": 40, "name": "원형 덩굴", "element": "풀", "cooltime": 40, "power": 120},
                {"level": 50, "name": "태양 폭발", "element": "풀", "cooltime": 55, "power": 150}
            ],
            "Partner_Skill": "풀뜨기 장인",
            "Planting": 1,
            "Handiwork": 1,
            "Gathering": 1,
            "Transporting": 1
        },
        {
            "ID": "40B",
            "Name": "아비스고트",
            "English_Name": "Incineram_Noct",
            "Elements": "어둠",
            "Rarity": 5,
            "HP": 95,
            "Attack": 105,
            "Defense": 85,
            "Work_Speed": 100,
            "Food": 4,
            "Skills": [
                {"level": 1, "name": "파이어 샷", "element": "화염", "cooltime": 2, "power": 30},
                {"level": 7, "name": "스피릿 파이어", "element": "화염", "cooltime": 7, "power": 45},
                {"level": 15, "name": "불화살", "element": "화염", "cooltime": 10, "power": 55},
                {"level": 22, "name": "지옥불 할퀴기", "element": "화염", "cooltime": 10, "power": 70},
                {"level": 30, "name": "그림자 폭발", "element": "어둠", "cooltime": 10, "power": 55},
                {"level": 40, "name": "화염구", "element": "화염", "cooltime": 55, "power": 150},
                {"level": 50, "name": "인페르노", "element": "화염", "cooltime": 40, "power": 120}
            ],
            "Partner_Skill": "암흑 발톱의 사냥꾼",
            "Handiwork": 2,
            "Mining": 1,
            "Transporting": 2
        },
        {
            "ID": "45B",
            "Name": "칠리자드",
            "English_Name": "Leezpunk_Ignis",
            "Elements": "화염",
            "Rarity": 3,
            "HP": 80,
            "Attack": 80,
            "Defense": 50,
            "Work_Speed": 100,
            "Food": 3,
            "Skills": [
                {"level": 1, "name": "파이어 샷", "element": "화염", "cooltime": 2, "power": 30},
                {"level": 7, "name": "독 사격", "element": "어둠", "cooltime": 2, "power": 30},
                {"level": 15, "name": "스피릿 파이어", "element": "화염", "cooltime": 7, "power": 45},
                {"level": 22, "name": "파이어 브레스", "element": "화염", "cooltime": 15, "power": 70},
                {"level": 30, "name": "화염 폭풍", "element": "화염", "cooltime": 18, "power": 80},
                {"level": 40, "name": "인페르노", "element": "화염", "cooltime": 40, "power": 120},
                {"level": 50, "name": "화염구", "element": "화염", "cooltime": 55, "power": 150}
            ],
            "Partner_Skill": "제6감",
            "Kindling": 1,
            "Handiwork": 1,
            "Gathering": 1,
            "Transporting": 1
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
        # Active Skills를 JSON 형태로 변환
        skills_json = str(variant["Skills"]).replace("'", '"')
        
        # 작업 적성 필드들 설정
        work_fields = {
            "Kindling": 0, "Watering": 0, "Planting": 0, "Generating Electricity": 0,
            "Handiwork": 0, "Gathering": 0, "Lumbering": 0, "Mining": 0,
            "Cooling": 0, "Transporting": 0, "Farming": 0
        }
        
        # 해당 팰의 작업 적성 설정
        for work, level in work_fields.items():
            if work in variant:
                work_fields[work] = variant[work]
        
        new_row = {
            "ID": variant["ID"],
            "Name": variant["Name"],
            "English_Name": variant["English_Name"],
            "Elements": variant["Elements"],
            "Rarity": variant["Rarity"],
            "HP": variant["HP"],
            "Attack": variant["Attack"],
            "Defense": variant["Defense"],
            "Work_Speed": variant["Work_Speed"],
            "Food": variant["Food"],
            "Partner_Skill": variant["Partner_Skill"],
            "Active_Skills": skills_json,
            **work_fields
        }
        
        existing_data.append(new_row)
        print(f"✅ 추가됨: {variant['ID']} {variant['Name']} ({variant['English_Name']})")
    
    # 새 CSV 파일에 저장
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames or [])
        writer.writeheader()
        writer.writerows(existing_data)
    
    print(f"\n🎉 완료! 총 {len(existing_data)}개 팰이 {output_file}에 저장되었습니다.")
    print(f"📈 새로 추가된 B variants: {len(new_b_variants)}개")
    
    # B variants 수 확인
    b_variants_count = sum(1 for row in existing_data if row['ID'].endswith('B'))
    print(f"🔥 총 B variants 수: {b_variants_count}개")

if __name__ == "__main__":
    main() 