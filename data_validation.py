#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
팰월드 CSV 데이터 검증 스크립트
현재 complete_1_to_115_pals.csv 파일의 완성도를 분석
"""

import pandas as pd
import json

def analyze_csv_completeness():
    """CSV 파일의 완성도를 분석"""
    
    # CSV 파일 읽기
    try:
        df = pd.read_csv('complete_1_to_115_pals.csv')
        print(f"✅ CSV 파일 로드 성공: {len(df)}개 행, {len(df.columns)}개 컬럼")
    except Exception as e:
        print(f"❌ CSV 파일 로드 실패: {e}")
        return
    
    print("\n" + "="*80)
    print("📊 기본 데이터 통계")
    print("="*80)
    
    # 기본 통계
    print(f"전체 팰 개수: {len(df)}")
    print(f"컬럼 개수: {len(df.columns)}")
    
    # B variants 분석
    b_variants = df[df['id'].astype(str).str.contains('B', na=False)]
    normal_pals = df[~df['id'].astype(str).str.contains('B', na=False)]
    
    print(f"일반 팰: {len(normal_pals)}개")
    print(f"아종(B variants): {len(b_variants)}개")
    
    if len(b_variants) > 0:
        print(f"포함된 B variants: {', '.join(b_variants['id'].astype(str).tolist())}")
    
    print("\n" + "="*80)
    print("📋 현재 CSV 컬럼 구조")
    print("="*80)
    
    for i, col in enumerate(df.columns, 1):
        print(f"{i:2d}. {col}")
    
    print("\n" + "="*80)
    print("📊 데이터 완성도 분석")
    print("="*80)
    
    # 빈 값 분석
    missing_analysis = {}
    for col in df.columns:
        null_count = df[col].isnull().sum()
        empty_count = (df[col] == '').sum()
        total_missing = null_count + empty_count
        missing_percentage = (total_missing / len(df)) * 100
        
        missing_analysis[col] = {
            'null_count': int(null_count),
            'empty_count': int(empty_count),
            'total_missing': int(total_missing),
            'percentage': round(missing_percentage, 2)
        }
        
        if total_missing > 0:
            print(f"{col:25s}: {total_missing:3d}개 누락 ({missing_percentage:5.1f}%)")
    
    print("\n" + "="*80)
    print("🎯 read.md 요구사항과 비교")
    print("="*80)
    
    # read.md에서 요구하는 필드들 (예상)
    required_fields = {
        'Basic Info': ['id', 'name_kor', 'pal_nick_kor', 'description_kor', 'elements'],
        'Partner Skill': ['partnerSkill_name', 'partnerSkill_describe', 'partnerSkill_needItem', 
                         'partnerSkill_needItemTechLevel', 'partnerSkill_level'],
        'Stats': ['stats_size', 'stats_rarity', 'stats_health', 'stats_food', 'stats_meleeAttack',
                 'stats_attack', 'stats_defense', 'stats_workSpeed', 'stats_support',
                 'stats_captureRateCorrect', 'stats_maleProbability', 'stats_combiRank',
                 'stats_goldCoin', 'stats_egg', 'stats_code'],
        'Movement': ['movement_slowWalkSpeed', 'movement_walkSpeed', 'movement_runSpeed',
                    'movement_rideSprintSpeed', 'movement_transportSpeed'],
        'Level 60 Stats': ['level60_health', 'level60_attack', 'level60_defense'],
        'Skills & Drops': ['activeSkills', 'passiveSkills', 'drops', 'workSuitabilities'],
        'Social': ['tribes', 'spawners']
    }
    
    # 현재 CSV에 있는 필드들 확인
    current_fields = set(df.columns)
    
    for category, fields in required_fields.items():
        print(f"\n{category}:")
        for field in fields:
            if field in current_fields:
                status = "✅ 존재"
                # 데이터 완성도 확인
                missing = missing_analysis.get(field, {}).get('total_missing', 0)
                if missing > 0:
                    status += f" (누락: {missing}개)"
            else:
                status = "❌ 누락"
            print(f"  {field:30s}: {status}")
    
    print("\n" + "="*80)
    print("🚨 추가로 필요한 필드들 (read.md 기준)")
    print("="*80)
    
    # read.md에서 언급된 추가 필드들
    additional_required = [
        'pal_nick_kor',  # 팰 별명
        'PartnerSkillItems', 'PartnerSkillItemQuantity', 'PartnerSkillItemProbability',
        'ActiveSkillDetails', 'PassiveSkillDetails',
        'TribesName', 'TribesType',
        'SpawnerName', 'SpawnerLevel', 'SpawnerArea'
    ]
    
    missing_important = []
    for field in additional_required:
        if field not in current_fields:
            missing_important.append(field)
            print(f"❌ {field}")
    
    print(f"\n총 {len(missing_important)}개의 중요 필드가 누락되었습니다.")
    
    print("\n" + "="*80)
    print("💡 개선 권장사항")
    print("="*80)
    
    recommendations = []
    
    if len(b_variants) < 20:  # 예상되는 B variants 수
        recommendations.append(f"더 많은 아종(B variants) 데이터 추가 필요 (현재: {len(b_variants)}개)")
    
    if missing_important:
        recommendations.append("read.md 요구사항에 맞는 추가 필드들 크롤링 필요")
    
    high_missing_fields = [col for col, data in missing_analysis.items() 
                          if data['percentage'] > 50]
    if high_missing_fields:
        recommendations.append(f"높은 누락률 필드들 보완 필요: {', '.join(high_missing_fields[:3])}")
    
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec}")
    
    print("\n" + "="*80)
    print("📈 전체 데이터 품질 점수")
    print("="*80)
    
    # 간단한 점수 계산
    total_possible_fields = len(required_fields['Basic Info']) + len(required_fields['Partner Skill']) + \
                           len(required_fields['Stats']) + len(required_fields['Movement']) + \
                           len(required_fields['Level 60 Stats']) + len(required_fields['Skills & Drops']) + \
                           len(required_fields['Social']) + len(additional_required)
    
    existing_fields = len([f for category in required_fields.values() for f in category if f in current_fields])
    field_score = (existing_fields / total_possible_fields) * 100
    
    # 데이터 완성도 점수
    completeness_scores = [100 - data['percentage'] for data in missing_analysis.values()]
    avg_completeness = sum(completeness_scores) / len(completeness_scores) if completeness_scores else 0
    
    # B variants 점수 (예상 20개 중 현재 개수)
    b_variant_score = min((len(b_variants) / 20) * 100, 100)
    
    overall_score = (field_score * 0.4 + avg_completeness * 0.4 + b_variant_score * 0.2)
    
    print(f"필드 완성도: {field_score:.1f}%")
    print(f"데이터 완성도: {avg_completeness:.1f}%")
    print(f"아종 데이터: {b_variant_score:.1f}%")
    print(f"전체 점수: {overall_score:.1f}%")
    
    if overall_score >= 90:
        grade = "A+ (매우 우수)"
    elif overall_score >= 80:
        grade = "A (우수)"
    elif overall_score >= 70:
        grade = "B (양호)"
    elif overall_score >= 60:
        grade = "C (보통)"
    else:
        grade = "D (개선 필요)"
    
    print(f"데이터 품질 등급: {grade}")

if __name__ == "__main__":
    print("🔍 팰월드 데이터 검증 시작...")
    analyze_csv_completeness()
    print("\n✨ 검증 완료!") 