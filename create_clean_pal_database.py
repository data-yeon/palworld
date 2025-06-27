#!/usr/bin/env python3
import csv
import re

def create_clean_pal_database():
    """현재 데이터를 정리해서 깔끔한 CSV 데이터베이스 생성"""
    
    print("🧹 깔끔한 팰 데이터베이스 생성 시작...")
    
    # 기존 데이터 읽기
    try:
        with open('enhanced_complete_pals_batch10_ultra_mega.csv', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        print(f"✅ 기존 데이터 로드 완료: {len(lines)-1}개 팰")
    except FileNotFoundError:
        print("❌ 파일을 찾을 수 없습니다!")
        return
    
    # 새로운 CSV 헤더 정의 (간단하고 명확하게)
    headers = [
        'ID', 'Name', 'EnglishName', 'Type1', 'Type2', 
        'HP', 'Attack', 'Defense', 'Rarity', 'Size', 'FoodAmount',
        'PartnerSkill', 'Work1', 'Work2', 'Work3',
        'DropItem1', 'DropItem2', 'ActiveSkills', 'Description'
    ]
    
    # 정리된 데이터 저장할 리스트
    clean_data = []
    
    # 헤더 스킵하고 데이터 처리
    for i, line in enumerate(lines[1:], 1):
        try:
            # CSV 파싱
            parts = line.strip().split(',')
            if len(parts) < 10:
                continue
                
            # 기본 정보 추출
            pal_id = parts[0]
            pal_name = parts[1]
            description = parts[2][:100] + "..." if len(parts[2]) > 100 else parts[2]  # 설명 줄이기
            
            # 타입 파싱 ([풀;물] 형태에서 추출)
            type_str = parts[3] if len(parts) > 3 else ""
            types = []
            if '[' in type_str and ']' in type_str:
                type_content = type_str.split('[')[1].split(']')[0]
                types = [t.strip().replace('"', '') for t in type_content.split(';')]
            
            type1 = types[0] if len(types) > 0 else ""
            type2 = types[1] if len(types) > 1 else ""
            
            # 영어 이름 추출 (코드에서)
            english_name = ""
            for j, part in enumerate(parts):
                if any(keyword in part for keyword in ['SaintCentaur', 'NightLady', 'MoonQueen', 'Kitsunebi', 'SheepBall']):
                    english_name = part
                    break
            
            # 스탯 정보 추출 (대략적인 위치에서)
            try:
                hp = parts[11] if len(parts) > 11 else "70"
                attack = parts[14] if len(parts) > 14 else "70"  
                defense = parts[15] if len(parts) > 15 else "70"
                rarity = parts[10] if len(parts) > 10 else "1"
                size = parts[9] if len(parts) > 9 else "M"
                food_amount = parts[12] if len(parts) > 12 else "2"
            except:
                hp, attack, defense, rarity, size, food_amount = "70", "70", "70", "1", "M", "2"
            
            # 파트너 스킬 추출
            partner_skill = parts[4] if len(parts) > 4 else ""
            
            # 작업 적성 추출 (간단하게)
            work_skills = []
            for part in parts:
                if "Lv" in part and any(work in part for work in ["수작업", "채집", "벌목", "채굴", "운반", "냉각", "불 피우기", "관개", "파종", "제약"]):
                    work_skills.append(part.strip())
                    if len(work_skills) >= 3:
                        break
            
            work1 = work_skills[0] if len(work_skills) > 0 else ""
            work2 = work_skills[1] if len(work_skills) > 1 else ""
            work3 = work_skills[2] if len(work_skills) > 2 else ""
            
            # 드롭 아이템 추출 (간단하게)
            drop_items = []
            for part in parts:
                if any(keyword in part for keyword in ["양털", "뿔", "가죽", "열매", "기관", "고기", "주괴", "다이아몬드"]):
                    drop_items.append(part.strip())
                    if len(drop_items) >= 2:
                        break
            
            drop1 = drop_items[0] if len(drop_items) > 0 else ""
            drop2 = drop_items[1] if len(drop_items) > 1 else ""
            
            # 액티브 스킬 추출 (첫 3개만)
            active_skills = ""
            for part in parts:
                if any(skill in part for skill in ["샷", "미사일", "폭발", "칼날", "화살", "불꽃", "스파이크"]):
                    skills = part.split(';')[:3]  # 처음 3개만
                    active_skills = ', '.join(skills)
                    break
            
            # 정리된 데이터 추가
            clean_row = [
                pal_id, pal_name, english_name, type1, type2,
                hp, attack, defense, rarity, size, food_amount,
                partner_skill, work1, work2, work3,
                drop1, drop2, active_skills, description
            ]
            
            clean_data.append(clean_row)
            
            if i % 20 == 0:
                print(f"🔄 처리 중... {i}/{len(lines)-1}")
                
        except Exception as e:
            print(f"⚠️ {i}번째 라인 처리 중 오류: {e}")
            continue
    
    # 새로운 CSV 파일 생성
    output_filename = 'clean_pal_database.csv'
    with open(output_filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(clean_data)
    
    print(f"\n🎉 깔끔한 데이터베이스 생성 완료!")
    print(f"📁 파일명: {output_filename}")
    print(f"📊 총 팰 개수: {len(clean_data)}개")
    
    # 통계 출력
    regular_pals = [row for row in clean_data if not row[0].endswith('B')]
    b_variants = [row for row in clean_data if row[0].endswith('B')]
    
    print(f"🔢 일반 팰: {len(regular_pals)}개")
    print(f"🔢 B variants: {len(b_variants)}개")
    print(f"📈 B variants 완성도: {len(b_variants)}/59 = {len(b_variants)/59*100:.1f}%")
    
    # 샘플 데이터 출력
    print(f"\n📋 샘플 데이터 (처음 3개):")
    print("ID | Name | Type1 | Type2 | HP | Attack | Defense")
    print("-" * 50)
    for i, row in enumerate(clean_data[:3]):
        print(f"{row[0]:3} | {row[1]:8} | {row[3]:4} | {row[4]:4} | {row[5]:3} | {row[6]:6} | {row[7]:7}")
    
    print(f"\n✨ 이제 {output_filename} 파일이 깔끔하게 정리되었습니다!")
    return output_filename

if __name__ == "__main__":
    create_clean_pal_database() 