import pandas as pd
import json
import re

def parse_active_skills(text):
    """Active Skills 섹션에서 스킬 정보 추출"""
    skills = []
    
    # Active Skills가 포함된 텍스트에서 각 스킬 정보 추출
    skill_pattern = r'Lv\.\s*(\d+)\s*\[([^\]]+)\].*?(?:얼음|화염|물|번개|풀|땅|어둠|용|무속성)\s*속성.*?(?:![^:]*:|\s)(\d+).*?위력:\s*(\d+)'
    
    matches = re.findall(skill_pattern, text, re.DOTALL)
    
    for match in matches:
        level, name, cooltime, power = match
        skill = {
            "level": int(level),
            "name": name.strip(),
            "coolTime": int(cooltime) if cooltime.isdigit() else None,
            "power": int(power)
        }
        skills.append(skill)
    
    return skills

def extract_elements(text):
    """속성 정보 추출"""
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

def extract_work_suitability(text):
    """작업 적성 정보 추출"""
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
        if korean in text:
            # Lv 숫자 추출
            pattern = f"{korean}.*?Lv(\\d+)"
            match = re.search(pattern, text)
            if match:
                work_suitability[english] = int(match.group(1))
    
    return work_suitability

# 크롤링한 B variants 데이터
b_variants_data = [
    {
        "id": "5B",
        "name_kor": "아이호",
        "name_eng": "Foxparks_Cryst",  
        "elements": "Ice",
        "text": """
        #5B 아이호 얼음 속성
        포옹 프로스트 Lv.1 발동하면 플레이어에게 장착되어 냉기를 방출해 공격할 수 있다.
        냉각 Lv1
        식사량 2
        Active Skills:
        Lv. 1 [얼음 미사일] 얼음 속성 쿨타임: 3 위력: 30
        Lv. 7 [워터 제트] 물 속성 쿨타임: 2 위력: 30  
        Lv. 15 [얼음 칼날] 얼음 속성 쿨타임: 10 위력: 55
        Lv. 22 [빙산] 얼음 속성 쿨타임: 15 위력: 70
        Lv. 30 [서리 낀 입김] 얼음 속성 쿨타임: 22 위력: 90
        Lv. 40 [아이시클 불릿] 얼음 속성 쿨타임: 35 위력: 110
        Lv. 50 [눈보라 스파이크] 얼음 속성 쿨타임: 45 위력: 130
        """
    },
    {
        "id": "6B", 
        "name_kor": "적부리",
        "name_eng": "Fuack_Ignis",
        "elements": "Water,Fire",
        "text": """
        #6B 적부리 물 속성 화염 속성
        파이어 태클 Lv.1 발동하면 적부리가 적을 향해 파이어 서핑을 하며 달려든다.
        불 피우기 Lv1 관개 Lv1 수작업 Lv1 운반 Lv1
        Active Skills:
        Lv. 1 [파이어 샷] 화염 속성 쿨타임: 2 위력: 30
        Lv. 7 [스피릿 파이어] 화염 속성 쿨타임: 7 위력: 45
        Lv. 15 [버블 샷] 물 속성 쿨타임: 13 위력: 65
        Lv. 22 [파이어 브레스] 화염 속성 쿨타임: 15 위력: 70
        Lv. 30 [화염 장벽] 화염 속성 쿨타임: 30 위력: 100
        Lv. 40 [하이드로 슬라이서] 물 속성 쿨타임: 45 위력: 130
        Lv. 50 [분화] 화염 속성 쿨타임: 45 위력: 130
        """
    },
    {
        "id": "10B",
        "name_kor": "뎅키", 
        "name_eng": "Pengullet_Lux",
        "elements": "Water,Electric",
        "text": """
        #10B 뎅키 물 속성 번개 속성
        뎅키 발사기 Lv.1 발동하면 로켓 발사기를 장착하여 뎅키를 탄환 삼아 발사한다.
        관개 Lv1 발전 Lv2 수작업 Lv1 운반 Lv1
        Active Skills:
        Lv. 1 [번개 창] 번개 속성 쿨타임: 2 위력: 30
        Lv. 7 [번개 구체] 번개 속성 쿨타임: 9 위력: 50
        Lv. 15 [버블 샷] 물 속성 쿨타임: 13 위력: 65
        Lv. 22 [라인 스플래시] 물 속성 쿨타임: 22 위력: 90
        Lv. 30 [물폭탄] 물 속성 쿨타임: 30 위력: 100
        Lv. 40 [트라이 스파크] 번개 속성 쿨타임: 35 위력: 110
        Lv. 50 [번개 일격] 번개 속성 쿨타임: 40 위력: 120
        """
    },
    {
        "id": "12B",
        "name_kor": "코치도치",
        "name_eng": "Jolthog_Cryst", 
        "elements": "Ice",
        "text": """
        #12B 코치도치 얼음 속성
        딱딱 폭탄 Lv.1 발동하면 코치도치를 손에 장착하며 적에게 던져 착탄할 시 얼음 폭발을 일으킨다.
        냉각 Lv1
        Active Skills:
        Lv. 1 [얼음 미사일] 얼음 속성 쿨타임: 3 위력: 30
        Lv. 7 [파워 샷] 무속성 쿨타임: 4 위력: 35
        Lv. 15 [빙산] 얼음 속성 쿨타임: 15 위력: 70
        Lv. 22 [파워 폭탄] 무속성 쿨타임: 15 위력: 70
        Lv. 30 [얼음 칼날] 얼음 속성 쿨타임: 10 위력: 55
        Lv. 40 [서리 낀 입김] 얼음 속성 쿨타임: 22 위력: 90
        Lv. 50 [눈보라 스파이크] 얼음 속성 쿨타임: 45 위력: 130
        """
    }
]

def add_b_variants_to_csv():
    """B variants를 CSV에 추가"""
    
    # 기존 CSV 로드
    df = pd.read_csv('complete_1_to_115_pals.csv')
    
    print(f"📊 기존 CSV 데이터: {len(df)}개 팰")
    
    new_rows = []
    
    for variant in b_variants_data:
        # Active Skills 파싱
        active_skills = parse_active_skills(variant["text"])
        active_skills_json = json.dumps(active_skills, ensure_ascii=False) if active_skills else ""
        
        # Work Suitability 파싱  
        work_suitability = extract_work_suitability(variant["text"])
        
        # 새 행 생성
        new_row = {
            'id': variant["id"],
            'name_kor': variant["name_kor"],
            'name_eng': variant["name_eng"],
            'elements': variant["elements"],
            'activeSkills': active_skills_json,
            'passiveSkills': "",  # B variants는 보통 패시브 스킬이 없음
            'partnerSkill': "",   # 파트너 스킬은 별도로 파싱 필요
            'workSuitabilities': json.dumps(work_suitability, ensure_ascii=False),
            'hp': None,
            'attack': None,
            'defense': None,
            'speed': None,
            'food': 2,  # 대부분 2
            'rarity': None,
            'captureRate': None,
            'dropItems': "",
            'description': "",
            'size': "XS",  # 대부분 XS
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
        updated_df.to_csv('enhanced_complete_pals_batch1.csv', index=False, encoding='utf-8-sig')
        
        print(f"\n🎉 성공적으로 {len(new_rows)}개 B variants 추가!")
        print(f"   전체 팰 수: {len(df)} → {len(updated_df)}")
        print(f"   파일 저장: enhanced_complete_pals_batch1.csv")
        
        # 개선 리포트 생성
        active_skills_added = sum(len(parse_active_skills(v["text"])) for v in b_variants_data)
        print(f"   추가된 Active Skills: {active_skills_added}개")
        
        return True
    
    return False

if __name__ == "__main__":
    print("🚀 B Variants Batch 1 추가 시작...")
    success = add_b_variants_to_csv()
    if success:
        print("\n✨ Batch 1 완료! 다음 배치를 준비하겠습니다.")
    else:
        print("\n❌ 추가할 데이터가 없습니다.") 