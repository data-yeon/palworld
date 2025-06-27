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

def extract_elements_from_text(text):
    """텍스트에서 속성 정보 추출"""
    elements = []
    if "얼음 속성" in text:
        elements.append("Ice")
    if "화염 속성" in text:
        elements.append("Fire")
    if "물 속성" in text:
        elements.append("Water")
    if "번개 속성" in text:
        elements.append("Electric")
    if "풀 속성" in text:
        elements.append("Grass")
    if "땅 속성" in text:
        elements.append("Ground")
    if "어둠 속성" in text:
        elements.append("Dark")
    if "용 속성" in text:
        elements.append("Dragon")
    if "무속성" in text:
        elements.append("Neutral")
    
    return ",".join(elements) if elements else "Neutral"

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

# 두 번째 배치 B variants 데이터
b_variants_batch2 = [
    {
        "id": "64B",
        "name_kor": "찌르르디노",
        "name_eng": "Dinossom_Lux",
        "elements": "Electric,Dragon",
        "text": """
        #64B 찌르르디노 번개 속성 용 속성
        찬란한 번개의 용 Lv.1 등에 타고 이동할 수 있다. 탑승 중 번개 속성 공격이 강화된다.
        발전 Lv2 벌목 Lv2
        Active Skills:
        Lv. 1 [전기 파장] 번개 속성 쿨타임: 4 위력: 40
        Lv. 7 [플라즈마 토네이도] 번개 속성 쿨타임: 13 위력: 65
        Lv. 15 [꼬리 채찍] 풀 속성 쿨타임: 8 위력: 60
        Lv. 22 [용의 숨결] 용 속성 쿨타임: 15 위력: 70
        Lv. 30 [트라이 썬더] 번개 속성 쿨타임: 22 위력: 90
        Lv. 40 [번개 일격] 번개 속성 쿨타임: 40 위력: 120
        Lv. 50 [전기 볼트] 번개 속성 쿨타임: 55 위력: 150
        """
    },
    {
        "id": "65B",
        "name_kor": "스너펜트",
        "name_eng": "Surfent_Terra",
        "elements": "Ground",
        "text": """
        #65B 스너펜트 땅 속성
        스륵스륵 스위머 Lv.1 등에 타고 이동할 수 있다. 보유하고 있는 동안 스너펜트가 짐을 대신 짊어져 인벤토리 내 광석이 가벼워진다.
        채집 Lv1
        Active Skills:
        Lv. 1 [모래 돌풍] 땅 속성 쿨타임: 4 위력: 40
        Lv. 7 [용 대포] 용 속성 쿨타임: 2 위력: 30
        Lv. 15 [바위 폭발] 땅 속성 쿨타임: 10 위력: 55
        Lv. 22 [바위 대포] 땅 속성 쿨타임: 15 위력: 70
        Lv. 30 [모래 폭풍] 땅 속성 쿨타임: 18 위력: 80
        Lv. 40 [용의 숨결] 용 속성 쿨타임: 15 위력: 70
        Lv. 50 [바위 창] 땅 속성 쿨타임: 55 위력: 150
        """
    },
    {
        "id": "75B",
        "name_kor": "캐티위자드",
        "name_eng": "Katress_Ignis", 
        "elements": "Dark,Fire",
        "text": """
        #75B 캐티위자드 어둠 속성 화염 속성
        식물 도감 Lv.1 함께 싸우는 동안 풀 속성 팰을 쓰러뜨렸을 때 드롭 아이템 획득량이 증가한다.
        불 피우기 Lv2 수작업 Lv2 제약 Lv2 운반 Lv2
        Active Skills:
        Lv. 1 [파이어 샷] 화염 속성 쿨타임: 2 위력: 30
        Lv. 7 [어둠 대포] 어둠 속성 쿨타임: 2 위력: 50
        Lv. 15 [불화살] 화염 속성 쿨타임: 10 위력: 55
        Lv. 22 [화염 폭풍] 화염 속성 쿨타임: 18 위력: 80
        Lv. 30 [화염 장벽] 화염 속성 쿨타임: 30 위력: 100
        Lv. 40 [플레임 토네이도] 화염 속성 쿨타임: 40 위력: 120
        Lv. 50 [화염구] 화염 속성 쿨타임: 55 위력: 150
        """
    },
    {
        "id": "72B",
        "name_kor": "어둠무사",
        "name_eng": "Bushi_Noct",
        "elements": "Fire,Dark",
        "text": """
        #72B 어둠무사 화염 속성 어둠 속성
        자전일섬 Lv.1 발동하면 목표로 삼은 적을 향해 높은 위력의 발도술으로 공격한다.
        불 피우기 Lv2 수작업 Lv1 채집 Lv1 벌목 Lv3 운반 Lv2
        Active Skills:
        Lv. 1 [스피릿 파이어] 화염 속성 쿨타임: 7 위력: 45
        Lv. 7 [어둠 파장] 어둠 속성 쿨타임: 2 위력: 40
        Lv. 15 [어둠 대포] 어둠 속성 쿨타임: 2 위력: 50
        Lv. 18 [발도술] 화염 속성 쿨타임: 9 위력: 65
        Lv. 22 [어둠 화살] 어둠 속성 쿨타임: 10 위력: 65
        Lv. 30 [유령의 불꽃] 어둠 속성 쿨타임: 16 위력: 75
        Lv. 40 [화염 장벽] 화염 속성 쿨타임: 30 위력: 100
        Lv. 50 [아포칼립스] 어둠 속성 쿨타임: 55 위력: 110
        """
    }
]

def add_batch2_to_csv():
    """두 번째 배치 B variants를 CSV에 추가"""
    
    # 첫 번째 배치 CSV 로드
    try:
        df = pd.read_csv('enhanced_complete_pals_batch1.csv')
        print(f"📊 Batch 1 CSV 데이터: {len(df)}개 팰")
    except FileNotFoundError:
        print("❌ Batch 1 파일을 찾을 수 없습니다. 원본 CSV를 사용합니다.")
        df = pd.read_csv('complete_1_to_115_pals.csv')
        print(f"📊 원본 CSV 데이터: {len(df)}개 팰")
    
    new_rows = []
    
    for variant in b_variants_batch2:
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
            'food': 5,  # B variants는 보통 5
            'rarity': None,
            'captureRate': None,
            'dropItems': "",
            'description': "",
            'size': "M",  # 대부분 M
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
        updated_df.to_csv('enhanced_complete_pals_batch2.csv', index=False, encoding='utf-8-sig')
        
        print(f"\n🎉 성공적으로 {len(new_rows)}개 B variants 추가!")
        print(f"   전체 팰 수: {len(df)} → {len(updated_df)}")
        print(f"   파일 저장: enhanced_complete_pals_batch2.csv")
        
        # 개선 리포트 생성
        active_skills_added = sum(len(parse_active_skills_from_html(v["text"])) for v in b_variants_batch2)
        print(f"   추가된 Active Skills: {active_skills_added}개")
        
        # 누적 통계
        total_b_variants = len(df[df['id'].astype(str).str.contains('B', na=False)]) + len(new_rows)
        print(f"   총 B variants: {total_b_variants}개")
        
        return True
    
    return False

if __name__ == "__main__":
    print("🚀 B Variants Batch 2 추가 시작...")
    success = add_batch2_to_csv()
    if success:
        print("\n✨ Batch 2 완료! 더 많은 B variants를 크롤링할 준비가 되었습니다.")
    else:
        print("\n❌ 추가할 데이터가 없습니다.") 