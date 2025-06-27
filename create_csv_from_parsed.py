#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
파싱된 팰 데이터를 CSV로 변환
기존 데이터 구조와 호환되는 형태로 생성
"""

import csv
import json
from typing import Dict, List

def create_sample_parsed_data():
    """
    파싱된 얼서니 데이터 예시
    """
    return {
        "ID": "46B",
        "Name": "얼서니",
        "EnglishName": "Werewolf_Ice",
        "Description": "머리의 뿔은 절대 녹지 않는 신비한 얼음.",
        "Type1": "얼음",
        "Type2": "",
        "HP": "80",
        "ATK": "105",
        "DEF": "80",
        "WorkSpeed": "100",
        "Rarity": "3",
        "Size": "M",
        "Tribe": "",
        "PartnerSkill": "냉기로 번쩍이는 발톱날",
        "PartnerSkillDescription": "",
        "Work1": "수작업",
        "Work1Level": "2",
        "Work2": "냉각",
        "Work2Level": "3",
        "Work3": "",
        "Work3Level": "",
        "Work4": "",
        "Work4Level": "",
        "FoodAmount": "5",
        "DropItem1": "뼈",
        "ActiveSkill1": "얼음 미사일",
        "ActiveSkill2": "얼음 칼날",
        "ActiveSkill3": "옥설 발톱",
        "ActiveSkill4": "아이시클 불릿",
        "ActiveSkill5": "아이시클 라인",
        "ActiveSkill6": "눈보라 스파이크",
        "ActiveSkill7": "",
        "Nick": ""
    }

def save_parsed_data_to_csv(pal_data_list: List[Dict], filename: str):
    """
    파싱된 팰 데이터 리스트를 CSV로 저장
    """
    
    # 기존 CSV 구조와 일치하는 필드 순서
    fieldnames = [
        'ID', 'Name', 'EnglishName', 'Description', 'Type1', 'Type2',
        'HP', 'ATK', 'DEF', 'WorkSpeed', 'Rarity', 'Size', 'Tribe',
        'PartnerSkill', 'PartnerSkillDescription',
        'Work1', 'Work1Level', 'Work2', 'Work2Level', 
        'Work3', 'Work3Level', 'Work4', 'Work4Level',
        'FoodAmount', 'DropItem1',
        'ActiveSkill1', 'ActiveSkill2', 'ActiveSkill3', 'ActiveSkill4',
        'ActiveSkill5', 'ActiveSkill6', 'ActiveSkill7',
        'Nick'
    ]
    
    print(f"💾 CSV 저장 시작: {filename}")
    print(f"📊 데이터 개수: {len(pal_data_list)}개")
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # 헤더 작성
        writer.writeheader()
        
        # 데이터 작성
        for pal_data in pal_data_list:
            # 모든 필드가 존재하도록 보장
            complete_data = {}
            for field in fieldnames:
                complete_data[field] = pal_data.get(field, "")
            
            writer.writerow(complete_data)
    
    print(f"✅ CSV 저장 완료: {filename}")
    return filename

def append_to_existing_csv(new_pal_data: Dict, existing_csv: str, output_csv: str):
    """
    기존 CSV에 새로운 팰 데이터를 추가
    """
    print(f"🔄 기존 CSV 업데이트: {existing_csv} → {output_csv}")
    
    # 기존 데이터 읽기
    existing_data = []
    try:
        with open(existing_csv, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            existing_data = list(reader)
        print(f"   📖 기존 데이터: {len(existing_data)}개")
    except FileNotFoundError:
        print(f"   ⚠️ 기존 파일 없음, 새로 생성: {existing_csv}")
    
    # 새 데이터 추가
    existing_data.append(new_pal_data)
    print(f"   ➕ 새 데이터 추가: {new_pal_data['Name']} ({new_pal_data['ID']})")
    
    # 업데이트된 데이터 저장
    save_parsed_data_to_csv(existing_data, output_csv)
    print(f"   📊 최종 데이터: {len(existing_data)}개")
    
    return output_csv

def test_csv_creation():
    """
    CSV 생성 테스트
    """
    print("🧪 CSV 생성 테스트 시작")
    
    # 샘플 데이터 생성
    sample_data = create_sample_parsed_data()
    
    # 단일 데이터로 CSV 생성
    single_csv = save_parsed_data_to_csv([sample_data], "test_single_pal.csv")
    
    # 기존 CSV에 추가 (시뮬레이션)
    updated_csv = append_to_existing_csv(
        sample_data, 
        "enhanced_complete_pals_batch5.csv",  # 기존 파일
        "enhanced_complete_pals_batch6.csv"   # 새 파일
    )
    
    print(f"\n🎯 테스트 결과:")
    print(f"   단일 CSV: {single_csv}")
    print(f"   업데이트 CSV: {updated_csv}")
    
    return sample_data

if __name__ == "__main__":
    test_csv_creation() 