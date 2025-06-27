import pandas as pd
import json
import re

def parse_active_skills_from_html(text):
    """HTML 형태의 Active Skills 데이터에서 스킬 정보 추출"""
    skills = []
    
    # 패턴: Lv. X [스킬명] ... 속성 ... 쿨타임: X 위력: X
    pattern = r'Lv\.\s*(\d+)\s*\[([^\]]+)\][^레]*?(?:번개|얼음|화염|물|풀|땅|어둠|용|무속성)\s*속성[^위]*?위력:\s*(\d+)'
    
    matches = re.findall(pattern, text, re.DOTALL)
    
    for match in matches:
        level, name, power = match
        
        # 쿨타임 추출 시도
        cooltime_pattern = f'Lv\\.\\s*{level}\\s*\\[{re.escape(name)}\\][^위]*?쿨타임:\\s*(\\d+)'
        cooltime_match = re.search(cooltime_pattern, text, re.DOTALL)
        cooltime = int(cooltime_match.group(1)) if cooltime_match else None
        
        skill = {
            "level": int(level),
            "name": name.strip(),
            "coolTime": cooltime,
            "power": int(power)
        }
        skills.append(skill)
    
    return skills

def extract_work_suitability_from_html(text):
    """HTML에서 작업 적성 정보 추출"""
    work_map = {
        "불 피우기": "Kindling",
        "관개": "Watering", 
        "파종": "Planting",
        "발전": "Generating Electricity",
        "수작업": "Handiwork",
        "채집": "Gathering",
        "벌목": "Lumbering",
        "채굴": "Mining",
        "제약": "Medicine Production",
        "냉각": "Cooling",
        "운반": "Transporting",
        "목장": "Farming"
    }
    
    work_suitability = {}
    for korean, english in work_map.items():
        pattern = f'{korean}.*?Lv(\\d+)'
        match = re.search(pattern, text)
        if match:
            work_suitability[english] = int(match.group(1))
    
    return work_suitability

# 세 번째 배치 B variants 데이터
b_variants_batch3 = [
    {
        "id": "31B",
        "name_kor": "샤맨더",
        "name_eng": "Gobfin_Ignis",
        "elements": "Fire",
        "text": """
        #31B 샤맨더 화염 속성
        삐돌이 상어 Lv.1 발동하면 목표로 삼은 적을 향해 높은 위력의 스피릿 파이어로 공격한다. 보유하고 있는 동안 플레이어의 공격력이 증가한다.
        불 피우기 Lv2 수작업 Lv1 운반 Lv1
        Active Skills:
        Lv. 1 [파이어 샷] 화염 속성 쿨타임: 2 위력: 30
        Lv. 7 [파워 샷] 무속성 쿨타임: 4 위력: 35
        Lv. 15 [스피릿 파이어] 화염 속성 쿨타임: 7 위력: 45
        Lv. 22 [불화살] 화염 속성 쿨타임: 10 위력: 55
        Lv. 30 [라인 썬더] 번개 속성 쿨타임: 16 위력: 75
        Lv. 40 [화염구] 화염 속성 쿨타임: 55 위력: 150
        Lv. 50 [인페르노] 화염 속성 쿨타임: 40 위력: 120
        """
    },
    {
        "id": "32B",
        "name_kor": "유령건다리",
        "name_eng": "Hangyu_Cryst",
        "elements": "Ice",
        "text": """
        #32B 유령건다리 얼음 속성
        겨울 하늘 그네 Lv.1 보유하고 있는 동안 장착 중인 글라이더의 성능이 변화한다. 활공 중 천천히 상승 기류를 탈 수 있다.
        수작업 Lv1 채집 Lv1 냉각 Lv1 운반 Lv2
        Active Skills:
        Lv. 1 [공기 대포] 무속성 쿨타임: 2 위력: 25
        Lv. 7 [얼음 미사일] 얼음 속성 쿨타임: 3 위력: 30
        Lv. 15 [파워 샷] 무속성 쿨타임: 4 위력: 35
        Lv. 22 [얼음 칼날] 얼음 속성 쿨타임: 10 위력: 55
        Lv. 30 [빙산] 얼음 속성 쿨타임: 15 위력: 70
        Lv. 40 [서리 낀 입김] 얼음 속성 쿨타임: 22 위력: 90
        Lv. 50 [눈보라 스파이크] 얼음 속성 쿨타임: 45 위력: 130
        """
    },
    {
        "id": "33B",
        "name_kor": "썬더판다",
        "name_eng": "Mossanda_Lux",
        "elements": "Electric",
        "text": """
        #33B 썬더판다 번개 속성
        척탄 판다 Lv.1 등에 타고 이동할 수 있다. 탑승 중 수류탄 발사기 연사가 가능해진다.
        발전 Lv2 수작업 Lv2 벌목 Lv2 운반 Lv3
        Active Skills:
        Lv. 1 [스파크 샷] 번개 속성 쿨타임: 2 위력: 30
        Lv. 7 [전기 파장] 번개 속성 쿨타임: 4 위력: 40
        Lv. 15 [라인 썬더] 번개 속성 쿨타임: 16 위력: 75
        Lv. 22 [폭발 펀치] 번개 속성 쿨타임: 14 위력: 85
        Lv. 30 [트라이 썬더] 번개 속성 쿨타임: 22 위력: 90
        Lv. 40 [번개 일격] 번개 속성 쿨타임: 40 위력: 120
        Lv. 50 [전기 볼트] 번개 속성 쿨타임: 55 위력: 150
        """
    }
]

def add_batch3_to_csv():
    """세 번째 배치 B variants를 CSV에 추가"""
    
    # 두 번째 배치 CSV 로드
    try:
        df = pd.read_csv('enhanced_complete_pals_batch2.csv')
        print(f"📊 Batch 2 CSV 데이터: {len(df)}개 팰")
    except FileNotFoundError:
        try:
            df = pd.read_csv('enhanced_complete_pals_batch1.csv')
            print(f"📊 Batch 1 CSV 데이터: {len(df)}개 팰")
        except FileNotFoundError:
            df = pd.read_csv('complete_1_to_115_pals.csv')
            print(f"📊 원본 CSV 데이터: {len(df)}개 팰")
    
    new_rows = []
    
    for variant in b_variants_batch3:
        # Active Skills 파싱
        active_skills = parse_active_skills_from_html(variant["text"])
        active_skills_json = json.dumps(active_skills, ensure_ascii=False) if active_skills else ""
        
        # Work Suitability 파싱  
        work_suitability = extract_work_suitability_from_html(variant["text"])
        
        # 새 행 생성 - 기존 CSV 컬럼 구조에 맞춰서
        new_row = {
            'id': variant["id"],
            'name_kor': variant["name_kor"],
            'name_eng': variant["name_eng"],
            'elements': variant["elements"],
            'activeSkills': active_skills_json,
            'passiveSkills': "",
            'partnerSkill': "",
            'workSuitabilities': json.dumps(work_suitability, ensure_ascii=False),
            'hp': None,
            'attack': None,
            'defense': None,
            'speed': None,
            'food': 3 if variant["id"] == "31B" else 2 if variant["id"] == "32B" else 5,  # 크기에 따라
            'rarity': None,
            'captureRate': None,
            'dropItems': "",
            'description': "",
            'size': "S" if variant["id"] == "31B" else "XS" if variant["id"] == "32B" else "L",
            'tribe': variant["name_eng"],
            'habitat': "",
            'spawnLocations': "",
            'breedingCombination': "",
            'eggType': "",
            'hatchTime': None,
            'maleProbability': 50,
            'friendship': "",
            'stats': "",
            'moves': "",
            'ai': "",
            'sounds': "",
            'models': "",
            'animations': "",
            'effects': "",
            'materials': "",
            'locations': "",
            'spawners': "",
            'variants': "",
            'unique_moves': "",
            'special_attacks': "",
            'status_effects': "",
            'item_drops': "",
            'capture_mechanics': "",
            'behavioral_notes': "",
            'lore': "",
            'gameplay_tips': ""
        }
        
        new_rows.append(new_row)
        print(f"✅ 추가: {variant['id']} - {variant['name_kor']} ({len(active_skills)}개 Active Skills)")
    
    # 새 데이터 추가
    if new_rows:
        new_df = pd.DataFrame(new_rows)
        updated_df = pd.concat([df, new_df], ignore_index=True)
        
        # CSV 저장
        updated_df.to_csv('enhanced_complete_pals_batch3.csv', index=False, encoding='utf-8-sig')
        
        print(f"\n🎉 성공적으로 {len(new_rows)}개 B variants 추가!")
        print(f"   전체 팰 수: {len(df)} → {len(updated_df)}")
        print(f"   파일 저장: enhanced_complete_pals_batch3.csv")
        
        # 개선 리포트 생성
        active_skills_added = sum(len(parse_active_skills_from_html(v["text"])) for v in b_variants_batch3)
        print(f"   추가된 Active Skills: {active_skills_added}개")
        
        # 누적 통계
        total_b_variants = len(df[df['id'].astype(str).str.contains('B', na=False)]) + len(new_rows)
        print(f"   총 B variants: {total_b_variants}개")
        
        return True
    
    return False

if __name__ == "__main__":
    print("🚀 B Variants Batch 3 추가 시작...")
    success = add_batch3_to_csv()
    if success:
        print("\n✨ Batch 3 완료! 계속해서 더 많은 B variants를 크롤링할 수 있습니다.")
        print("\n📊 현재까지 진행 상황:")
        print("   - 원본 CSV: 122개 팰 (일반 115개 + 아종 7개)")
        print("   - Batch 1: +4개 B variants (5B, 6B, 10B, 12B)")  
        print("   - Batch 2: +4개 B variants (64B, 65B, 75B, 72B)")
        print("   - Batch 3: +3개 B variants (31B, 32B, 33B)")
        print("   - 총계: 133개 팰 (일반 115개 + 아종 18개)")
        print("\n   🎯 아종 완성도: 18/59 = 30.5% (C등급)")
        print("   📈 크게 개선됨! 처음 7개(11.9%)에서 18개(30.5%)로 증가")
    else:
        print("\n❌ 추가할 데이터가 없습니다.") 