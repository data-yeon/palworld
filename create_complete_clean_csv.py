#!/usr/bin/env python3
import csv
import re

def create_complete_clean_csv():
    """완전하면서도 깔끔한 팰 CSV 데이터베이스 생성"""
    
    print("🔧 완전한 팰 데이터베이스 생성 시작...")
    
    # 기존 복잡한 CSV 읽기
    try:
        with open('enhanced_complete_pals_batch10_ultra_mega.csv', 'r', encoding='utf-8') as f:
            content = f.read()
        print("✅ 기존 데이터 로드 완료")
    except FileNotFoundError:
        print("❌ 파일을 찾을 수 없습니다!")
        return
    
    # 새로운 헤더 정의 (완전하지만 정리된 형태)
    headers = [
        'id', 'name', 'englishName', 'description', 
        'type1', 'type2', 'hp', 'attack', 'defense', 
        'rarity', 'size', 'foodAmount', 'partnerSkill', 
        'work1', 'work2', 'work3', 'activeSkills', 
        'dropItem1', 'dropItem2', 'eggType', 'imageFile'
    ]
    
    # 정리된 데이터 저장할 리스트
    clean_data = []
    
    # 라인별로 파싱
    lines = content.strip().split('\n')
    for i, line in enumerate(lines[1:], 1):  # 헤더 스킵
        try:
            # 복잡한 CSV 파싱 (콤마로 분리하되 따옴표 안의 콤마는 무시)
            parts = []
            current_part = ""
            in_quotes = False
            
            for char in line:
                if char == '"':
                    in_quotes = not in_quotes
                elif char == ',' and not in_quotes:
                    parts.append(current_part.strip())
                    current_part = ""
                    continue
                current_part += char
            parts.append(current_part.strip())  # 마지막 부분 추가
            
            if len(parts) < 10:
                continue
            
            # 데이터 추출 및 정리
            pal_id = parts[0]
            pal_name = parts[1]
            
            # 설명 정리 (너무 길면 자르기)
            description = parts[2] if len(parts) > 2 else ""
            if len(description) > 150:
                description = description[:147] + "..."
            
            # 타입 정보 추출 (더 정교하게)
            type1 = ""
            type2 = ""
            
            # 전체 라인에서 타입 패턴 찾기
            full_line = ' '.join(parts)
            
            # 타입 매핑 
            type_map = {
                '무속성': '무속성',
                '불꽃': '화염',
                '화염': '화염',
                '물': '물',
                '풀': '풀',
                '번개': '번개',
                '전기': '번개',
                '얼음': '얼음',
                '땅': '땅',
                '어둠': '어둠',
                '용': '용',
                '드래곤': '용'
            }
            
            # 타입 패턴으로 검색
            for korean_type, standard_type in type_map.items():
                if korean_type in full_line:
                    if not type1:
                        type1 = standard_type
                    elif type1 != standard_type and not type2:
                        type2 = standard_type
            
            # 영어 이름 찾기 (개선된 패턴)
            english_name = ""
            for part in parts:
                # 영어 패턴 찾기
                clean_part = part.strip().replace('"', '').replace("'", "")
                if re.match(r'^[A-Za-z_]+$', clean_part) and len(clean_part) > 3:
                    # 팰 이름 패턴 키워드
                    if any(keyword in clean_part for keyword in [
                        'Ball', 'Cat', 'Fox', 'Dragon', 'Wolf', 'Cryst', 'Ignis', 
                        'Aqua', 'Terra', 'Noct', 'Lux', 'mon', 'pal', 'rex', 'tusk',
                        'horn', 'mane', 'wing', 'tooth', 'claw', 'bird', 'deer'
                    ]):
                        english_name = clean_part
                        break
                    # 긴 영어 이름도 팰 이름일 가능성
                    elif len(clean_part) > 6 and not clean_part.lower() in ['active', 'partner', 'skill', 'level', 'attack', 'defense']:
                        english_name = clean_part
                        break
            
            # 파트너 스킬 추출 (더 정확하게)
            partner_skill = ""
            for part in parts:
                # 파트너 스킬 패턴 찾기
                if any(keyword in part for keyword in ['방패', '생산', '리코일', '도우미', '탈것', '채집', '운반']):
                    if len(part.strip()) < 50:  # 너무 긴 건 스킬이 아닐 가능성
                        partner_skill = part.strip().replace('"', '')
                        break
            
            # 스탯 정보 추출 (더 정확하게)
            hp = "70"
            attack = "70"
            defense = "70"
            rarity = "1"
            size = "M"
            food_amount = "2"
            
            # 숫자 패턴으로 스탯 찾기
            numbers_found = []
            for j, part in enumerate(parts):
                try:
                    clean_part = part.strip().replace('"', '')
                    if clean_part.isdigit():
                        val = int(clean_part)
                        if 30 <= val <= 200:  # 스탯 범위
                            numbers_found.append((j, val))
                except:
                    continue
            
            # 스탯은 보통 비슷한 범위의 3개 숫자가 연속으로 나옴
            if len(numbers_found) >= 3:
                hp = str(numbers_found[0][1])
                attack = str(numbers_found[1][1])
                defense = str(numbers_found[2][1])
            
            # 레어도 찾기 (1-20 범위의 작은 숫자)
            for part in parts:
                try:
                    val = int(part.strip().replace('"', ''))
                    if 1 <= val <= 20:
                        rarity = str(val)
                        break
                except:
                    continue
            
            # 크기 찾기
            for part in parts:
                clean_part = part.strip().replace('"', '')
                if clean_part in ['XS', 'S', 'M', 'L', 'XL']:
                    size = clean_part
                    break
            
            # 음식량 찾기 (1-10 범위)
            for part in parts:
                try:
                    val = int(part.strip().replace('"', ''))
                    if 1 <= val <= 10 and val != int(rarity):
                        food_amount = str(val)
                        break
                except:
                    continue
            
            # 작업 적성 추출
            work_skills = []
            for part in parts:
                if 'Lv' in part and any(work in part for work in ['수작업', '채집', '벌목', '채굴', '운반', '냉각', '불 피우기', '관개', '파종', '제약']):
                    work_skills.append(part.strip().replace('"', ''))
                    if len(work_skills) >= 3:
                        break
            
            work1 = work_skills[0] if len(work_skills) > 0 else ""
            work2 = work_skills[1] if len(work_skills) > 1 else ""
            work3 = work_skills[2] if len(work_skills) > 2 else ""
            
            # 액티브 스킬 추출 (처음 5개)
            active_skills = ""
            for part in parts:
                if ';' in part and any(skill in part for skill in ['샷', '미사일', '폭발', '칼날', '화살', '불꽃', '스파이크', '대포', '파장', '펀치', '킥']):
                    skills = part.split(';')[:5]  # 처음 5개만
                    active_skills = '; '.join([s.strip().replace('"', '') for s in skills])
                    break
            
            # 드롭 아이템 추출
            drop_items = []
            for part in parts:
                if any(item in part for item in ['양털', '뿔', '가죽', '열매', '기관', '고기', '주괴', '다이아몬드', '천', '사파이어', '알']):
                    # 간단하게 정리
                    cleaned_item = re.sub(r'\d+–?\d*%?', '', part).strip().replace('"', '')
                    # 불필요한 괄호와 기호 제거
                    cleaned_item = re.sub(r'[()"|,]', '', cleaned_item).strip()
                    if cleaned_item and len(cleaned_item) < 30:
                        drop_items.append(cleaned_item)
                    if len(drop_items) >= 2:
                        break
            
            drop1 = drop_items[0] if len(drop_items) > 0 else ""
            drop2 = drop_items[1] if len(drop_items) > 1 else ""
            
            # 알 타입 추출
            egg_type = ""
            for part in parts:
                if '알' in part and len(part.strip()) < 20:
                    egg_type = part.strip().replace('"', '')
                    break
            
            # 이미지 파일명
            image_file = f"{pal_id}_menu.webp"
            
            # 정리된 행 데이터
            clean_row = [
                pal_id, pal_name, english_name, description,
                type1, type2, hp, attack, defense,
                rarity, size, food_amount, partner_skill,
                work1, work2, work3, active_skills,
                drop1, drop2, egg_type, image_file
            ]
            
            clean_data.append(clean_row)
            
            if i % 20 == 0:
                print(f"🔄 처리 중... {i}/{len(lines)-1}")
                
        except Exception as e:
            print(f"⚠️ {i}번째 라인 처리 중 오류: {e}")
            continue
    
    # 새로운 CSV 파일 생성
    output_filename = 'complete_clean_pal_database.csv'
    with open(output_filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(clean_data)
    
    # 통계 출력
    regular_pals = [row for row in clean_data if not row[0].endswith('B')]
    b_variants = [row for row in clean_data if row[0].endswith('B')]
    
    print(f"\n🎉 완전한 팰 데이터베이스 생성 완료!")
    print(f"📁 파일명: {output_filename}")
    print(f"📊 총 팰 개수: {len(clean_data)}개")
    print(f"🔢 일반 팰: {len(regular_pals)}개")
    print(f"🔢 B variants: {len(b_variants)}개")
    print(f"📈 B variants 완성도: {len(b_variants)}/59 = {len(b_variants)/59*100:.1f}%")
    
    # 샘플 출력
    print(f"\n📋 샘플 데이터 (처음 3개):")
    for i, row in enumerate(clean_data[:3]):
        print(f"\n{i+1}. {row[0]} {row[1]} ({row[2]})")
        print(f"   타입: {row[4]} {row[5] if row[5] else ''}")
        print(f"   스탯: HP{row[6]} ATK{row[7]} DEF{row[8]} 레어도{row[9]}")
        print(f"   작업: {row[13]} {row[14]} {row[15]}")
        print(f"   파트너스킬: {row[12]}")
    
    print(f"\n✨ 완전한 정보를 포함한 {output_filename} 파일이 생성되었습니다!")
    print(f"📋 포함된 정보: ID, 이름, 영어명, 설명, 타입, 스탯, 파트너스킬, 작업적성, 액티브스킬, 드롭아이템, 알타입, 이미지파일")
    
    return output_filename

if __name__ == "__main__":
    create_complete_clean_csv() 