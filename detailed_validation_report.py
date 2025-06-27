#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
팰월드 CSV 데이터 상세 검증 리포트
read.md의 정확한 요구사항과 현재 데이터를 비교
"""

import pandas as pd

def generate_detailed_report():
    """read.md 요구사항 기반 상세 분석"""
    
    # CSV 파일 읽기
    df = pd.read_csv('complete_1_to_115_pals.csv')
    
    print("🔍 팰월드 데이터 상세 검증 리포트")
    print("=" * 80)
    print(f"분석 대상: complete_1_to_115_pals.csv")
    print(f"총 데이터: {len(df)}개 팰, {len(df.columns)}개 필드")
    
    # read.md 요구사항 매핑
    required_fields_mapping = {
        # 기본 정보
        "id": "id",
        "name_kor": "name_kor", 
        "pal_nick_kor": "❌ 누락",  # 현재 없음
        "description_kor": "description_kor",
        "elements": "elements",
        
        # 파트너 스킬
        "PartnerSkillName": "partnerSkill_name",
        "PartnerSkillDescribe": "partnerSkill_describe", 
        "PartnerSkillNeedItem": "partnerSkill_needItem",
        "PartnerSkillNeedItemTechLevel": "partnerSkill_needItemTechLevel",
        "PartnerSkillLevel": "partnerSkill_level",
        "PartnerSkillItems": "❌ 누락",
        "PartnerSkillItemQuantity": "❌ 누락", 
        "PartnerSkillItemProbability": "❌ 누락",
        
        # Stats
        "Size": "stats_size",
        "Rarity": "stats_rarity",
        "Health": "stats_health", 
        "Food": "stats_food",
        "MeleeAttack": "stats_meleeAttack",
        "Attack": "stats_attack",
        "Defense": "stats_defense",
        "Work Speed": "stats_workSpeed",
        "Support": "stats_support",
        "CaptureRateCorrect": "stats_captureRateCorrect",
        "MaleProbability": "stats_maleProbability",
        "CombiRank": "stats_combiRank", 
        "Gold Coin": "stats_goldCoin",
        "Egg": "stats_egg",
        "Code": "stats_code",
        
        # Movement
        "SlowWalkSpeed": "movement_slowWalkSpeed",
        "WalkSpeed": "movement_walkSpeed",
        "RunSpeed": "movement_runSpeed", 
        "RideSprintSpeed": "movement_rideSprintSpeed",
        "TransportSpeed": "movement_transportSpeed",
        
        # Level 60 Stats
        "Level60 Health": "level60_health",
        "Level60 Attack": "level60_attack",
        "Level60 Defense": "level60_defense",
        
        # Active Skills (상세 정보 누락)
        "Active Skills": "activeSkills",
        "Active SkillsRequiredItem": "❌ 누락",
        "Active SkillsRequiredLevel": "❌ 누락", 
        "Active SkillsName": "❌ 누락",
        "Active SkillsElement": "❌ 누락",
        "Active SkillsCoolTime": "❌ 누락",
        "Active SkillsPower": "❌ 누락",
        "Active SkillsShootAttack": "❌ 누락",
        "Active SkillsMeleeAttack": "❌ 누락",
        "Active SkillsAccumulatedElement": "❌ 누락",
        "Active SkillsAccumulatedValue": "❌ 누락", 
        "Active SkillsDescribe": "❌ 누락",
        
        # Passive Skills & Drops
        "Passive Skills": "passiveSkills",
        "Possible Drops": "drops",
        "DropsItemName": "❌ 누락",
        "DropsItemQuantity": "❌ 누락", 
        "DropsItemProbability": "❌ 누락",
        
        # 작업 적성
        "작업적성": "workSuitabilities",
        
        # Tribes & Spawner
        "Tribes": "tribes",
        "TribesName": "❌ 누락",
        "TribesType": "❌ 누락",
        "Spawner": "spawners", 
        "SpawnerName": "❌ 누락",
        "SpawnerLevel": "❌ 누락",
        "SpawnerArea": "❌ 누락"
    }
    
    print("\n📋 read.md 요구사항 대비 현재 상태")
    print("=" * 80)
    
    # 카테고리별 분석
    categories = {
        "🔹 기본 정보": ["id", "name_kor", "pal_nick_kor", "description_kor", "elements"],
        "🔹 파트너 스킬": [
            "PartnerSkillName", "PartnerSkillDescribe", "PartnerSkillNeedItem",
            "PartnerSkillNeedItemTechLevel", "PartnerSkillLevel", "PartnerSkillItems",
            "PartnerSkillItemQuantity", "PartnerSkillItemProbability"
        ],
        "🔹 기본 스탯": [
            "Size", "Rarity", "Health", "Food", "MeleeAttack", "Attack", "Defense",
            "Work Speed", "Support", "CaptureRateCorrect", "MaleProbability", 
            "CombiRank", "Gold Coin", "Egg", "Code"
        ],
        "🔹 이동 속도": [
            "SlowWalkSpeed", "WalkSpeed", "RunSpeed", "RideSprintSpeed", "TransportSpeed"
        ],
        "🔹 레벨 60 스탯": [
            "Level60 Health", "Level60 Attack", "Level60 Defense"
        ],
        "🔹 액티브 스킬": [
            "Active Skills", "Active SkillsRequiredItem", "Active SkillsRequiredLevel",
            "Active SkillsName", "Active SkillsElement", "Active SkillsCoolTime",
            "Active SkillsPower", "Active SkillsShootAttack", "Active SkillsMeleeAttack",
            "Active SkillsAccumulatedElement", "Active SkillsAccumulatedValue", "Active SkillsDescribe"
        ],
        "🔹 패시브 & 드롭": [
            "Passive Skills", "Possible Drops", "DropsItemName", "DropsItemQuantity", "DropsItemProbability"
        ],
        "🔹 작업 & 사회": [
            "작업적성", "Tribes", "TribesName", "TribesType", "Spawner", "SpawnerName", "SpawnerLevel", "SpawnerArea"
        ]
    }
    
    total_required = 0
    total_existing = 0
    total_missing = 0
    
    for category, fields in categories.items():
        print(f"\n{category}")
        print("-" * 50)
        
        existing_in_category = 0
        missing_in_category = 0
        
        for field in fields:
            total_required += 1
            csv_field = required_fields_mapping.get(field, "❌ 누락")
            
            if csv_field == "❌ 누락":
                status = "❌ 누락"
                missing_in_category += 1
                total_missing += 1
            else:
                # 데이터 완성도 확인
                if csv_field in df.columns:
                    null_count = df[csv_field].isnull().sum()
                    empty_count = (df[csv_field] == '').sum()
                    missing_data = null_count + empty_count
                    
                    if missing_data == 0:
                        status = "✅ 완료"
                    else:
                        status = f"⚠️  있음 (누락 {missing_data}개)"
                else:
                    status = "❌ 누락"
                    missing_in_category += 1
                    total_missing += 1
                    
                existing_in_category += 1
                total_existing += 1
            
            print(f"  {field:35s}: {status}")
        
        completion_rate = (existing_in_category / len(fields)) * 100 if fields else 0
        print(f"  📊 카테고리 완성도: {completion_rate:.1f}% ({existing_in_category}/{len(fields)})")
    
    print("\n" + "=" * 80)
    print("📊 전체 요구사항 분석 결과")
    print("=" * 80)
    
    overall_completion = (total_existing / total_required) * 100
    print(f"전체 요구사항 개수: {total_required}개")
    print(f"현재 구현된 항목: {total_existing}개")
    print(f"누락된 항목: {total_missing}개")
    print(f"전체 완성도: {overall_completion:.1f}%")
    
    # 아종 데이터 분석
    print("\n🔹 아종(B variants) 데이터 분석")
    print("-" * 50)
    
    b_variants = df[df['id'].astype(str).str.contains('B', na=False)]
    print(f"현재 포함된 B variants: {len(b_variants)}개")
    if len(b_variants) > 0:
        print(f"포함된 아종: {', '.join(b_variants['id'].astype(str).tolist())}")
    
    # 예상 B variants (팰DB에서 확인 가능한)
    expected_b_variants = [
        "5B", "6B", "10B", "11B", "12B", "13B", "14B", "15B", "16B", "17B",
        "24B", "26B", "27B", "28B", "29B", "30B", "31B", "34B", "36B", "38B",
        "39B", "42B", "43B", "44B", "45B", "46B", "47B", "51B", "52B", "55B",
        "56B", "57B", "59B", "60B", "61B", "64B", "65B", "67B", "69B", "71B",
        "72B", "75B", "76B", "77B", "78B", "80B", "82B", "83B", "84B", "85B",
        "86B", "87B", "88B", "89B", "90B", "91B", "92B", "95B", "96B", "98B",
        "100B", "101B", "102B", "103B", "104B", "105B", "106B", "107B", "108B",
        "109B", "110B", "111B", "112B", "113B", "114B", "115B"
    ]
    
    current_b_ids = set(b_variants['id'].astype(str).tolist())
    missing_b_variants = [b for b in expected_b_variants if b not in current_b_ids]
    
    print(f"예상 B variants: {len(expected_b_variants)}개")
    print(f"누락된 B variants: {len(missing_b_variants)}개")
    if len(missing_b_variants) <= 10:
        print(f"누락된 일부: {', '.join(missing_b_variants[:10])}")
    else:
        print(f"누락된 일부: {', '.join(missing_b_variants[:10])}... 등")
    
    b_variant_completion = (len(b_variants) / len(expected_b_variants)) * 100
    print(f"B variants 완성도: {b_variant_completion:.1f}%")
    
    print("\n" + "=" * 80)
    print("💡 우선순위별 개선 방안")
    print("=" * 80)
    
    print("🔴 긴급 (core 기능)")
    if "pal_nick_kor" not in df.columns:
        print("• pal_nick_kor 필드 추가 (팰 별명/수식어)")
    
    high_missing_fields = []
    for col in df.columns:
        if col in df.columns:
            missing_count = df[col].isnull().sum() + (df[col] == '').sum()
            missing_rate = (missing_count / len(df)) * 100
            if missing_rate > 50:
                high_missing_fields.append((col, missing_rate))
    
    if high_missing_fields:
        print("• 높은 누락률 필드 보완:")
        for field, rate in sorted(high_missing_fields, key=lambda x: x[1], reverse=True)[:3]:
            print(f"  - {field}: {rate:.1f}% 누락")
    
    print("\n🟠 중요 (상세 정보)")
    print("• Active Skills 상세 정보 (RequiredItem, Element, Power, CoolTime 등)")
    print("• Drops 상세 정보 (ItemName, Quantity, Probability)")
    print("• Tribes/Spawner 상세 정보")
    
    print("\n🟡 권장 (완성도 향상)")
    print(f"• B variants 데이터 추가 ({len(missing_b_variants)}개 누락)")
    print("• 기존 데이터의 빈 값 보완")
    
    # 최종 등급
    print("\n" + "=" * 80)
    print("📈 최종 데이터 품질 평가")
    print("=" * 80)
    
    # 가중치 적용 점수 계산
    field_weight = 0.4  # 필드 완성도
    data_weight = 0.3   # 데이터 완성도  
    b_variant_weight = 0.3  # B variants
    
    field_score = overall_completion
    
    # 데이터 완성도 (비어있지 않은 비율)
    data_completeness_scores = []
    for col in df.columns:
        missing = df[col].isnull().sum() + (df[col] == '').sum()
        completeness = ((len(df) - missing) / len(df)) * 100
        data_completeness_scores.append(completeness)
    
    avg_data_completeness = sum(data_completeness_scores) / len(data_completeness_scores)
    
    final_score = (field_score * field_weight + 
                   avg_data_completeness * data_weight + 
                   b_variant_completion * b_variant_weight)
    
    print(f"필드 완성도: {field_score:.1f}% (가중치 {field_weight*100:.0f}%)")
    print(f"데이터 완성도: {avg_data_completeness:.1f}% (가중치 {data_weight*100:.0f}%)")
    print(f"B variants: {b_variant_completion:.1f}% (가중치 {b_variant_weight*100:.0f}%)")
    print(f"최종 점수: {final_score:.1f}%")
    
    if final_score >= 90:
        grade = "A+ (매우 우수)"
        comment = "read.md 요구사항을 거의 완벽하게 충족"
    elif final_score >= 80:
        grade = "A (우수)"
        comment = "대부분의 요구사항을 충족, 일부 보완 필요"
    elif final_score >= 70:
        grade = "B (양호)"
        comment = "핵심 요구사항은 충족, 상세 정보 보완 필요"
    elif final_score >= 60:
        grade = "C (보통)"
        comment = "기본 요구사항 충족, 많은 보완 필요"
    else:
        grade = "D (개선 필요)"
        comment = "대부분의 요구사항 미충족, 전면 재작업 필요"
    
    print(f"등급: {grade}")
    print(f"평가: {comment}")

if __name__ == "__main__":
    generate_detailed_report() 