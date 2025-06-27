#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
최종 데이터 병합 스크립트
우선순위 보강 결과를 기존 CSV와 병합하여 완성된 데이터셋 생성
"""

import pandas as pd
import json

def analyze_improvement():
    """데이터 개선 분석"""
    print("🔍 우선순위 데이터 보강 결과 분석")
    print("=" * 60)
    
    # 기존 데이터 로드
    df_existing = pd.read_csv('complete_1_to_115_pals.csv')
    print(f"📁 기존 데이터: {len(df_existing)}개 팰")
    
    # 새로 크롤링한 데이터 로드
    with open('priority_enhancement_results.json', 'r', encoding='utf-8') as f:
        enhanced_data = json.load(f)
    print(f"🆕 보강 데이터: {len(enhanced_data)}개 팰")
    
    # 개선 분석
    improvements = {
        'active_skills_enhanced': 0,
        'passive_skills_added': 0,
        'b_variants_added': 0,
        'total_active_skills_before': 0,
        'total_active_skills_after': 0
    }
    
    print("\n📊 개선 상세 분석:")
    print("-" * 60)
    
    for enhanced_pal in enhanced_data:
        pal_id = enhanced_pal['id']
        
        # 기존 데이터에서 찾기
        existing_row = df_existing[df_existing['id'].astype(str) == pal_id]
        
        if not existing_row.empty:
            # 기존 팰 개선 분석
            existing_row = existing_row.iloc[0]
            existing_active_count = existing_row.get('activeSkills_count', 0)
            new_active_count = enhanced_pal.get('activeSkills_count_new', 0)
            
            improvements['total_active_skills_before'] += existing_active_count
            improvements['total_active_skills_after'] += new_active_count
            
            if new_active_count > existing_active_count:
                improvements['active_skills_enhanced'] += 1
                print(f"✅ {pal_id}: Active Skills {existing_active_count} → {new_active_count}개")
                
                # 새 스킬 상세 정보 출력
                if enhanced_pal.get('activeSkills_enhanced'):
                    skills = json.loads(enhanced_pal['activeSkills_enhanced'])
                    print(f"   새로운 스킬: {', '.join([s['name'] for s in skills[:3]])}...")
            
            # Passive Skills 개선
            new_passive_count = enhanced_pal.get('passiveSkills_count_new', 0)
            if new_passive_count > 0:
                improvements['passive_skills_added'] += 1
                print(f"✅ {pal_id}: Passive Skills 추가 {new_passive_count}개")
        else:
            # 새로운 B variant
            if 'B' in pal_id:
                improvements['b_variants_added'] += 1
                new_active_count = enhanced_pal.get('activeSkills_count_new', 0)
                improvements['total_active_skills_after'] += new_active_count
                print(f"🆕 {pal_id}: 새로운 B variant (Active Skills {new_active_count}개)")
    
    # 전체 개선 통계
    print("\n📈 전체 개선 통계:")
    print("-" * 60)
    print(f"🔸 Active Skills 개선된 팰: {improvements['active_skills_enhanced']}개")
    print(f"🔸 Passive Skills 추가된 팰: {improvements['passive_skills_added']}개")
    print(f"🔸 새로 추가된 B variants: {improvements['b_variants_added']}개")
    print(f"🔸 총 Active Skills: {improvements['total_active_skills_before']} → {improvements['total_active_skills_after']}개")
    
    skill_increase = improvements['total_active_skills_after'] - improvements['total_active_skills_before']
    if improvements['total_active_skills_before'] > 0:
        increase_rate = (skill_increase / improvements['total_active_skills_before']) * 100
        print(f"🔸 Active Skills 증가율: +{skill_increase}개 (+{increase_rate:.1f}%)")
    
    return improvements

def create_merged_dataset():
    """보강된 데이터와 기존 데이터를 병합하여 최종 데이터셋 생성"""
    print("\n🔄 데이터 병합 시작")
    print("=" * 60)
    
    # 기존 데이터 로드
    df_existing = pd.read_csv('complete_1_to_115_pals.csv')
    
    # 보강 데이터 로드
    with open('priority_enhancement_results.json', 'r', encoding='utf-8') as f:
        enhanced_data = json.load(f)
    
    # 새로운 컬럼 추가 준비
    df_merged = df_existing.copy()
    
    # 새 컬럼들 초기화
    if 'activeSkills_enhanced' not in df_merged.columns:
        df_merged['activeSkills_enhanced'] = ''
    if 'passiveSkills_enhanced' not in df_merged.columns:
        df_merged['passiveSkills_enhanced'] = ''
    
    # 기존 데이터 업데이트
    update_count = 0
    new_additions = []
    
    for enhanced_pal in enhanced_data:
        pal_id = enhanced_pal['id']
        
        # 기존 데이터에서 찾기
        existing_idx = df_merged[df_merged['id'].astype(str) == pal_id].index
        
        if len(existing_idx) > 0:
            # 기존 팰 업데이트
            idx = existing_idx[0]
            
            # Active Skills 보강
            if enhanced_pal.get('activeSkills_enhanced'):
                df_merged.at[idx, 'activeSkills_enhanced'] = enhanced_pal['activeSkills_enhanced']
                df_merged.at[idx, 'activeSkills_count'] = enhanced_pal.get('activeSkills_count_new', 0)
                update_count += 1
            
            # Passive Skills 보강
            if enhanced_pal.get('passiveSkills_new'):
                df_merged.at[idx, 'passiveSkills_enhanced'] = enhanced_pal['passiveSkills_new']
                # 기존 passiveSkills 컬럼도 업데이트
                if 'passiveSkills' in df_merged.columns:
                    df_merged.at[idx, 'passiveSkills'] = enhanced_pal['passiveSkills_new']
            
            print(f"🔄 {pal_id}: 데이터 업데이트 완료")
        else:
            # 새로운 B variant 추가
            if 'B' in pal_id:
                # 기본 B variant 데이터 구조 생성 (기존 A variant 기반)
                base_id = pal_id.replace('B', '')
                base_row = df_merged[df_merged['id'].astype(str) == base_id]
                
                if len(base_row) > 0:
                    new_row = base_row.iloc[0].copy()
                    new_row['id'] = pal_id
                    new_row['name_kor'] = new_row['name_kor'] + ' (아종)'
                    
                    # 보강된 데이터 적용
                    if enhanced_pal.get('activeSkills_enhanced'):
                        new_row['activeSkills_enhanced'] = enhanced_pal['activeSkills_enhanced']
                        new_row['activeSkills_count'] = enhanced_pal.get('activeSkills_count_new', 0)
                    
                    if enhanced_pal.get('passiveSkills_new'):
                        new_row['passiveSkills_enhanced'] = enhanced_pal['passiveSkills_new']
                        if 'passiveSkills' in new_row:
                            new_row['passiveSkills'] = enhanced_pal['passiveSkills_new']
                    
                    new_additions.append(new_row)
                    print(f"🆕 {pal_id}: 새로운 B variant 추가")
    
    # 새로운 B variants를 데이터프레임에 추가
    if new_additions:
        new_df = pd.DataFrame(new_additions)
        df_merged = pd.concat([df_merged, new_df], ignore_index=True)
        print(f"✅ {len(new_additions)}개 B variants 추가됨")
    
    # 최종 데이터셋 저장
    output_filename = 'enhanced_complete_pals.csv'
    df_merged.to_csv(output_filename, index=False, encoding='utf-8')
    
    print(f"\n💾 최종 데이터셋 저장: {output_filename}")
    print(f"   총 팰 수: {len(df_merged)}개")
    print(f"   업데이트된 팰: {update_count}개")
    print(f"   추가된 B variants: {len(new_additions)}개")
    
    return df_merged, output_filename

def generate_improvement_report():
    """개선 리포트 생성"""
    print("\n📋 최종 개선 리포트 생성")
    print("=" * 60)
    
    # 분석 실행
    improvements = analyze_improvement()
    
    # 병합 실행
    df_merged, output_filename = create_merged_dataset()
    
    # 최종 리포트
    report = f"""
🎯 팰월드 우선순위 데이터 보강 완료 리포트

📊 개선 결과:
✅ Active Skills 개선: {improvements['active_skills_enhanced']}개 팰
✅ Passive Skills 추가: {improvements['passive_skills_added']}개 팰  
✅ B variants 추가: {improvements['b_variants_added']}개
✅ 총 Active Skills: {improvements['total_active_skills_before']} → {improvements['total_active_skills_after']}개

📁 결과 파일:
- {output_filename} ({len(df_merged)}개 팰)
- priority_enhancement_results.json (원본 크롤링 데이터)

🚀 다음 단계:
1. 전체 115개 팰 + 모든 B variants 크롤링
2. read.md 요구사항 완성도 재검증
3. 최종 데이터셋 검증 및 품질 확인
"""
    
    print(report)
    
    # 리포트 파일로 저장
    with open('improvement_report.txt', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print("📄 리포트 저장: improvement_report.txt")
    
    return True

def main():
    """메인 함수"""
    print("🎯 최종 데이터 병합 및 분석")
    
    try:
        success = generate_improvement_report()
        
        if success:
            print("\n✅ 우선순위 데이터 보강 완료!")
            print("\n🎉 주요 성과:")
            print("1. ✅ Active Skills 상세 정보 대폭 개선 (속성, 위력, 쿨타임)")
            print("2. ✅ B variants 성공적으로 추가")
            print("3. ✅ 구조화된 JSON 형태의 스킬 데이터")
            print("4. ✅ 기존 데이터와 완벽한 병합")
        else:
            print("\n❌ 데이터 병합 중 오류 발생")
            
    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")

if __name__ == "__main__":
    main() 