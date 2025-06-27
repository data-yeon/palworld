import json
import csv
from typing import Dict, List, Any

def load_json_file(filename: str) -> Dict[str, Any]:
    """JSON 파일을 로드합니다."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {filename}")
        return {}
    except json.JSONDecodeError:
        print(f"JSON 파싱 오류: {filename}")
        return {}

def normalize_pal_data(pal_data: Dict[str, Any]) -> Dict[str, str]:
    """팰 데이터를 CSV 형식에 맞게 정규화합니다."""
    normalized = {}
    
    # 기본 정보
    normalized['id'] = pal_data.get('id', '')
    normalized['name'] = pal_data.get('name', '')
    normalized['englishName'] = pal_data.get('englishName', '')
    normalized['description'] = pal_data.get('description', '')
    
    # 속성
    normalized['type1'] = pal_data.get('type1', '')
    normalized['type2'] = pal_data.get('type2', '')
    
    # 스탯 (누락된 경우 기본값 설정)
    normalized['hp'] = pal_data.get('hp', '80')
    normalized['attack'] = pal_data.get('attack', '80')
    normalized['defense'] = pal_data.get('defense', '70')
    normalized['rarity'] = pal_data.get('rarity', '3')
    normalized['size'] = pal_data.get('size', 'M')
    normalized['foodAmount'] = '3'  # 기본값
    
    # 스킬과 능력
    normalized['partnerSkill'] = pal_data.get('partnerSkill', '')
    
    # 작업 스킬 파싱 (여러 개를 분리)
    work_skills = pal_data.get('workSkills', '')
    work_parts = [skill.strip() for skill in work_skills.split(',') if skill.strip()]
    normalized['work1'] = work_parts[0] if len(work_parts) > 0 else ''
    normalized['work2'] = work_parts[1] if len(work_parts) > 1 else ''
    normalized['work3'] = work_parts[2] if len(work_parts) > 2 else ''
    
    # 전투 스킬
    normalized['activeSkills'] = pal_data.get('activeSkills', '')
    
    # 드롭 아이템 파싱
    drop_items = pal_data.get('dropItems', '')
    drop_parts = [item.strip() for item in drop_items.split(',') if item.strip()]
    normalized['dropItem1'] = drop_parts[0] if len(drop_parts) > 0 else ''
    normalized['dropItem2'] = drop_parts[1] if len(drop_parts) > 1 else ''
    
    # 알 타입
    normalized['eggType'] = pal_data.get('eggType', '')
    
    # 이미지 파일명 생성
    normalized['imageFile'] = f"{normalized['id']}_menu.webp"
    
    return normalized

def main():
    """메인 함수: JSON 파일들을 읽어서 CSV로 변환합니다."""
    
    # JSON 파일들 로드
    batch_files = [
        'basic_pals_batch1_results.json',
        'basic_pals_batch2_results.json', 
        'basic_pals_batch3_results.json'
    ]
    
    all_pals = []
    
    for file in batch_files:
        data = load_json_file(file)
        if data and 'crawled_data' in data:
            for pal_id, pal_data in data['crawled_data'].items():
                normalized_pal = normalize_pal_data(pal_data)
                all_pals.append(normalized_pal)
    
    if not all_pals:
        print("크롤링된 팰 데이터가 없습니다.")
        return
    
    # CSV 헤더 정의 (perfect_complete_pal_database_214.csv와 동일한 구조)
    headers = [
        'id', 'name', 'englishName', 'description', 'type1', 'type2',
        'hp', 'attack', 'defense', 'rarity', 'size', 'foodAmount',
        'partnerSkill', 'work1', 'work2', 'work3', 'activeSkills',
        'dropItem1', 'dropItem2', 'eggType', 'imageFile'
    ]
    
    # CSV 파일 생성
    output_filename = 'crawled_pals_118_to_133.csv'
    
    with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        
        # ID 순으로 정렬해서 작성
        sorted_pals = sorted(all_pals, key=lambda x: int(x['id']))
        for pal in sorted_pals:
            writer.writerow(pal)
    
    print(f"✅ CSV 파일 생성 완료: {output_filename}")
    print(f"📊 총 {len(all_pals)}개 팰 데이터 변환됨")
    
    # 요약 정보 출력
    print("\n📋 변환된 팰 목록:")
    for pal in sorted_pals:
        types = f"{pal['type1']}"
        if pal['type2']:
            types += f"/{pal['type2']}"
        print(f"  {pal['id']}. {pal['name']} ({pal['englishName']}) - {types} 속성")

if __name__ == "__main__":
    main() 