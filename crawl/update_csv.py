import csv
from paldb_crawler import save_pal_data_to_csv

def add_new_pal_data():
    """새로 크롤링한 팰 데이터를 추가합니다."""
    
    # 새로 크롤링한 5개 팰의 데이터
    new_data = [
        {
            "id": "5B", "korean_name": "아이호", "english_name": "Foxparks_Cryst",
            "elements": ["Ice"], "stats": {"hp": "65", "attack": "80", "defense": "70"},
            "work_skills": {"cooling": 1},
            "partner_skill": "포옹 프로스트 Lv.1",
            "active_skills": ["얼음 미사일", "워터 제트", "얼음 칼날", "빙산", "서리 낀 입김", "아이시클 불릿", "눈보라 스파이크"],
            "drops": ["가죽 1–2", "빙결 기관 1–3"]
        },
        {
            "id": "6", "korean_name": "청부리", "english_name": "Fuack",
            "elements": ["Water"], "stats": {"hp": "60", "attack": "80", "defense": "60"},
            "work_skills": {"watering": 1, "handiwork": 1, "transporting": 1},
            "partner_skill": "서핑 태클 Lv.1",
            "active_skills": ["아쿠아 샷", "파워 샷", "워터 제트", "얼음 미사일", "버블 샷", "물폭탄", "하이드로 스트림"],
            "drops": ["가죽", "팰의 체액"]
        },
        {
            "id": "6B", "korean_name": "적부리", "english_name": "Fuack_Ignis",
            "elements": ["물", "화염"], "stats": {"hp": "60", "attack": "85", "defense": "60"},
            "work_skills": {"kindling": 1, "watering": 1, "handiwork": 1, "transporting": 1},
            "partner_skill": "파이어 태클 Lv.1",
            "active_skills": ["파이어 샷", "스피릿 파이어", "버블 샷", "파이어 브레스", "화염 장벽", "하이드로 슬라이서", "분화"],
            "drops": ["가죽", "팰의 체액", "발화 기관"]
        },
        {
            "id": "7", "korean_name": "번개냥", "english_name": "Sparkit",
            "elements": ["Electricity"], "stats": {"hp": "60", "attack": "75", "defense": "70"},
            "work_skills": {"handiwork": 1, "electricity": 1, "transporting": 1},
            "partner_skill": "정전기 Lv.1",
            "active_skills": ["스파크 샷", "모래 돌풍", "전기 파장", "번개 구체", "트라이 썬더", "라인 썬더", "전기 볼트"],
            "drops": ["발전 기관 1–2"]
        },
        {
            "id": "8", "korean_name": "몽지", "english_name": "Tanzee",
            "elements": ["Leaf"], "stats": {"hp": "80", "attack": "70", "defense": "70"},
            "work_skills": {"planting": 1, "gathering": 1, "handiwork": 1, "lumbering": 1, "transporting": 1},
            "partner_skill": "신난 소총 Lv.1",
            "active_skills": ["바람의 칼날", "모래 돌풍", "씨앗 기관총", "씨앗 지뢰", "바위 대포", "초록 폭풍"],
            "drops": ["버섯"]
        }
    ]
    
    # 기존 데이터 읽기
    existing_data = []
    try:
        with open('paldb_pal_info.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # CSV에서 읽은 데이터를 딕셔너리 형태로 변환
                pal_data = {
                    "id": row['id'],
                    "korean_name": row['korean_name'],
                    "english_name": row['english_name'],
                    "elements": [row['elements']] if row['elements'] else [],
                    "stats": {
                        "hp": row['hp'],
                        "attack": row['attack'],
                        "defense": row['defense']
                    },
                    "work_skills": {
                        "kindling": int(row['kindling']) if row['kindling'] else 0,
                        "watering": int(row['watering']) if row['watering'] else 0,
                        "planting": int(row['planting']) if row['planting'] else 0,
                        "electricity": int(row['electricity']) if row['electricity'] else 0,
                        "handiwork": int(row['handiwork']) if row['handiwork'] else 0,
                        "gathering": int(row['gathering']) if row['gathering'] else 0,
                        "lumbering": int(row['lumbering']) if row['lumbering'] else 0,
                        "mining": int(row['mining']) if row['mining'] else 0,
                        "medicine": int(row['medicine']) if row['medicine'] else 0,
                        "cooling": int(row['cooling']) if row['cooling'] else 0,
                        "transporting": int(row['transporting']) if row['transporting'] else 0,
                        "farming": int(row['farming']) if row['farming'] else 0
                    },
                    "partner_skill": row['partner_skill'],
                    "active_skills": row['active_skills'].split(', ') if row['active_skills'] else [],
                    "drops": row['drops'].split(', ') if row['drops'] else []
                }
                existing_data.append(pal_data)
    except FileNotFoundError:
        print("기존 CSV 파일이 없습니다.")
    
    # 새 데이터 추가
    combined_data = existing_data + new_data
    
    # 업데이트된 CSV 저장
    save_pal_data_to_csv(combined_data, "paldb_pal_info_updated.csv")
    
    print(f"총 {len(combined_data)}개의 팰 정보가 업데이트되었습니다.")

if __name__ == "__main__":
    add_new_pal_data() 