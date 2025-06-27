#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
궁극의 스마트 크롤러
firecrawl을 사용해서 B variants를 자동으로 탐지, 크롤링, 파싱합니다.
"""

import json
import csv
import re
from typing import Dict, List, Optional

def parse_pal_data_from_markdown(markdown_content: str, pal_id: str, korean_name: str) -> Dict:
    """
    firecrawl로 얻은 마크다운 데이터를 파싱해서 구조화된 데이터로 변환
    """
    data = {
        "ID": pal_id,
        "Name": korean_name,
        "EnglishName": "",
        "Description": "",
        "Type1": "",
        "Type2": "",
        "HP": "",
        "ATK": "",
        "DEF": "",
        "WorkSpeed": "",
        "Rarity": "",
        "Size": "",
        "Tribe": "",
        "PartnerSkill": "",
        "PartnerSkillDescription": "",
        "Work1": "",
        "Work1Level": "",
        "Work2": "",
        "Work2Level": "",
        "Work3": "",
        "Work3Level": "",
        "Work4": "",
        "Work4Level": "",
        "FoodAmount": "",
        "DropItem1": "",
        "ActiveSkill1": "",
        "ActiveSkill2": "",
        "ActiveSkill3": "",
        "ActiveSkill4": "",
        "ActiveSkill5": "",
        "ActiveSkill6": "",
        "ActiveSkill7": "",
        "Nick": ""
    }
    
    try:
        # 기본 정보 추출
        lines = markdown_content.split('\n')
        
        # 속성 추출 (예: "얼음 속성")
        for line in lines:
            if "속성" in line and not line.startswith('#'):
                type_text = line.strip()
                if "얼음" in type_text:
                    data["Type1"] = "얼음"
                elif "불꽃" in type_text or "화염" in type_text:
                    data["Type1"] = "불꽃"
                elif "풀" in type_text:
                    data["Type1"] = "풀"
                elif "땅" in type_text:
                    data["Type1"] = "땅"
                elif "전기" in type_text:
                    data["Type1"] = "전기"
                elif "물" in type_text:
                    data["Type1"] = "물"
                elif "어둠" in type_text:
                    data["Type1"] = "어둠"
                break
        
        # 스탯 추출
        for i, line in enumerate(lines):
            if "HP" in line and line.strip().isdigit() == False:
                # 다음 몇 줄에서 숫자 찾기
                for j in range(i+1, min(i+5, len(lines))):
                    if lines[j].strip().isdigit():
                        data["HP"] = lines[j].strip()
                        break
            elif "공격" in line and "아이콘" not in line:
                for j in range(i+1, min(i+5, len(lines))):
                    if lines[j].strip().isdigit():
                        data["ATK"] = lines[j].strip()
                        break
            elif "방어" in line and "아이콘" not in line:
                for j in range(i+1, min(i+5, len(lines))):
                    if lines[j].strip().isdigit():
                        data["DEF"] = lines[j].strip()
                        break
            elif "작업 속도" in line:
                for j in range(i+1, min(i+5, len(lines))):
                    if lines[j].strip().isdigit():
                        data["WorkSpeed"] = lines[j].strip()
                        break
        
        # 파트너 스킬 추출
        for i, line in enumerate(lines):
            if "파트너 스킬" in line and i < len(lines) - 1:
                # 다음 줄에서 스킬명 찾기
                skill_line = lines[i+1].strip()
                if skill_line and not skill_line.startswith('#'):
                    data["PartnerSkill"] = skill_line
                break
        
        # 작업 적성 추출 (수작업, 냉각 등)
        work_count = 0
        for i, line in enumerate(lines):
            if "작업 적성" in line:
                # 다음 몇 줄에서 작업 종류와 레벨 찾기
                for j in range(i+1, min(i+10, len(lines))):
                    work_line = lines[j].strip()
                    if "Lv" in work_line and work_count < 4:
                        work_count += 1
                        # 작업 종류와 레벨 분리
                        if "수작업" in work_line:
                            data[f"Work{work_count}"] = "수작업"
                        elif "냉각" in work_line:
                            data[f"Work{work_count}"] = "냉각"
                        elif "채광" in work_line:
                            data[f"Work{work_count}"] = "채광"
                        elif "벌목" in work_line:
                            data[f"Work{work_count}"] = "벌목"
                        elif "농사" in work_line:
                            data[f"Work{work_count}"] = "농사"
                        elif "수집" in work_line:
                            data[f"Work{work_count}"] = "수집"
                        elif "운반" in work_line:
                            data[f"Work{work_count}"] = "운반"
                        elif "급수" in work_line:
                            data[f"Work{work_count}"] = "급수"
                        elif "발전" in work_line:
                            data[f"Work{work_count}"] = "발전"
                        elif "제약" in work_line:
                            data[f"Work{work_count}"] = "제약"
                        elif "화로" in work_line:
                            data[f"Work{work_count}"] = "화로"
                        
                        # 레벨 추출
                        level_match = re.search(r'Lv(\d+)', work_line)
                        if level_match:
                            data[f"Work{work_count}Level"] = level_match.group(1)
                break
        
        # 레어도와 사이즈 추출
        for line in lines:
            if line.strip().isdigit() and len(line.strip()) == 1:
                # 1자리 숫자는 레어도일 가능성
                if not data["Rarity"]:
                    data["Rarity"] = line.strip()
            elif line.strip() in ["S", "M", "L", "XL"]:
                data["Size"] = line.strip()
        
        # 식사량 추출 (5개 불꽃 아이콘 = 5)
        food_count = markdown_content.count("T_Icon_foodamount_on.webp")
        if food_count > 0:
            data["FoodAmount"] = str(food_count)
        
        # 영어 이름 추출 (Werewolf_Ice 같은 코드명)
        code_match = re.search(r'Code\s*\n\s*(\w+)', markdown_content)
        if code_match:
            data["EnglishName"] = code_match.group(1)
        
        # Summary 설명 추출
        summary_start = markdown_content.find("##### Summary")
        if summary_start != -1:
            summary_section = markdown_content[summary_start:summary_start+500]
            lines = summary_section.split('\n')
            for line in lines[1:]:  # Summary 제목 다음 줄부터
                if line.strip() and not line.startswith('#'):
                    data["Description"] = line.strip()
                    break
        
        print(f"   ✅ 파싱 완료: {korean_name} ({pal_id})")
        return data
        
    except Exception as e:
        print(f"   ❌ 파싱 실패: {e}")
        return data

def create_test_parsing():
    """
    얼서니 데이터로 파싱 테스트
    """
    # 실제 firecrawl 결과 시뮬레이션 
    sample_markdown = """
얼서니 #46B
얼음 속성

파트너 스킬
냉기로 번쩍이는 발톱날 Lv.1

작업 적성
수작업 Lv2
냉각 Lv3

##### Stats
Size
M
Rarity
3
HP
80
공격
105
방어
80
작업 속도
100

Code
Werewolf_Ice

##### Summary
머리의 뿔은 절대 녹지 않는 신비한 얼음.
뿔을 부러뜨려 빙수를 만들면
엄청난 별미가 된다고 하지만
먹은 본인도 얼서니도 머리가 띵할 만큼 아파진다.
"""
    
    print("🧪 파싱 테스트 시작...")
    result = parse_pal_data_from_markdown(sample_markdown, "46B", "얼서니")
    
    print("\n📊 파싱 결과:")
    for key, value in result.items():
        if value:  # 빈 값이 아닌 것만 출력
            print(f"   {key}: {value}")
    
    return result

if __name__ == "__main__":
    print("🚀 궁극의 스마트 크롤러 테스트")
    create_test_parsing() 