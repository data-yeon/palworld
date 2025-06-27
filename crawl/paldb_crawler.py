import csv
import json
import time
from typing import List, Dict
import sys

def extract_pals_batch(urls: List[str]) -> List[Dict]:
    """여러 팰의 정보를 한 번에 크롤링합니다."""
    print(f"크롤링 중: {len(urls)}개 팰...")
    
    # 여기서는 예시로 미리 크롤링된 데이터를 사용
    # 실제로는 MCP Firecrawl을 사용해야 합니다
    return []

def get_all_pal_urls() -> List[str]:
    """paldb.cc에서 모든 팰의 URL을 가져옵니다."""
    base_url = "https://paldb.cc/ko"
    
    # 메인 페이지에서 추출한 팰 이름들
    pal_names = [
        "Lamball", "Cattiva", "Chikipi", "Lifmunk", "Foxparks", "Foxparks_Cryst",
        "Fuack", "Fuack_Ignis", "Sparkit", "Tanzee", "Rooby", "Pengullet",
        "Pengullet_Lux", "Penking", "Penking_Lux", "Jolthog", "Jolthog_Cryst",
        "Gumoss", "Vixy", "Hoocrates", "Teafant", "Depresso", "Cremis",
        "Daedream", "Rushoar", "Nox", "Fuddler", "Killamari", "Killamari_Primo",
        "Mau", "Mau_Cryst", "Celaray", "Celaray_Lux", "Direhowl", "Tocotoco",
        "Flopie", "Mozzarina", "Bristla", "Gobfin", "Gobfin_Ignis", "Hangyu",
        "Hangyu_Cryst", "Mossanda", "Mossanda_Lux", "Woolipop", "Caprity",
        "Caprity_Noct", "Melpaca", "Eikthyrdeer", "Eikthyrdeer_Terra",
        "Nitewing", "Ribbuny", "Ribbuny_Botan", "Incineram", "Incineram_Noct",
        "Cinnamoth", "Arsox", "Dumud", "Dumud_Gild", "Cawgnito", "Leezpunk",
        "Leezpunk_Ignis", "Loupmoon", "Loupmoon_Cryst", "Galeclaw",
        "Robinquill", "Robinquill_Terra", "Gorirat", "Gorirat_Terra",
        "Beegarde", "Elizabee", "Grintale", "Swee", "Sweepa", "Chillet",
        "Chillet_Ignis", "Univolt", "Foxcicle", "Pyrin", "Pyrin_Noct",
        "Reindrix", "Rayhound", "Kitsun", "Kitsun_Noct", "Dazzi", "Dazzi_Noct",
        "Lunaris", "Dinossom", "Dinossom_Lux", "Surfent", "Surfent_Terra",
        "Maraith", "Digtoise", "Tombat", "Lovander", "Flambelle", "Vanwyrm",
        "Vanwyrm_Cryst", "Bushi", "Bushi_Noct", "Beakon", "Ragnahawk",
        "Katress", "Katress_Ignis", "Wixen", "Wixen_Noct", "Verdash",
        "Vaelet", "Sibelyx", "Elphidran", "Elphidran_Aqua", "Kelpsea",
        "Kelpsea_Ignis", "Azurobe", "Azurobe_Cryst", "Cryolinx",
        "Cryolinx_Terra", "Blazehowl", "Blazehowl_Noct", "Relaxaurus",
        "Relaxaurus_Lux", "Broncherry", "Broncherry_Aqua", "Petallia",
        "Reptyro", "Reptyro_Cryst", "Kingpaca", "Kingpaca_Cryst", "Mammorest",
        "Mammorest_Cryst", "Wumpo", "Wumpo_Botan", "Warsect", "Warsect_Terra",
        "Fenglope", "Fenglope_Lux", "Felbat", "Quivern", "Quivern_Botan",
        "Blazamut", "Blazamut_Ryu", "Helzephyr", "Helzephyr_Lux", "Astegon",
        "Menasting", "Menasting_Terra", "Anubis", "Jormuntide",
        "Jormuntide_Ignis", "Suzaku", "Suzaku_Aqua", "Grizzbolt", "Lyleen",
        "Lyleen_Noct", "Faleris", "Faleris_Aqua", "Orserk", "Shadowbeak",
        "Paladius", "Necromus", "Frostallion", "Frostallion_Noct", "Jetragon",
        "Bellanoir", "Bellanoir_Libero", "Selyne", "Croajiro", "Croajiro_Noct",
        "Lullu", "Shroomer", "Shroomer_Noct", "Kikit", "Sootseer", "Prixter",
        "Knocklem", "Yakumo", "Dogen", "Dazemu", "Mimog", "Xenovader",
        "Xenogard", "Xenolord", "Nitemary", "Starryon", "Silvegis", "Smokie",
        "Celesdir", "Omascul", "Splatterina", "Tarantriss", "Azurmane",
        "Bastigor", "Prunelia", "Nyafia", "Gildane", "Herbil", "Icelyn",
        "Frostplume", "Palumba", "Braloha", "Munchill", "Polapup", "Turtacle",
        "Turtacle_Terra", "Jellroy", "Jelliette", "Gloopie", "Finsider",
        "Finsider_Ignis", "Ghangler", "Ghangler_Ignis", "Whalaska",
        "Whalaska_Ignis", "Neptilius"
    ]
    
    return [f"{base_url}/{name}" for name in pal_names]

def save_pal_data_to_csv(pal_data: List[Dict], filename: str = "paldb_pal_info.csv"):
    """팰 데이터를 CSV 파일로 저장합니다."""
    print(f"CSV 파일로 저장 중: {filename}")
    
    fieldnames = [
        'id', 'korean_name', 'english_name', 'elements',
        'hp', 'attack', 'defense',
        'kindling', 'watering', 'planting', 'electricity', 'handiwork',
        'gathering', 'lumbering', 'mining', 'medicine', 'cooling',
        'transporting', 'farming',
        'partner_skill', 'active_skills', 'drops'
    ]
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for pal in pal_data:
            # 복잡한 데이터는 JSON 문자열로 변환
            elements_str = ', '.join(pal.get('elements', []))
            active_skills_str = ', '.join(pal.get('active_skills', []))
            drops_str = ', '.join(pal.get('drops', []))
            
            # 작업 적성 정보 추출
            work_skills = pal.get('work_skills', {})
            stats = pal.get('stats', {})
            
            writer.writerow({
                'id': pal.get('id', ''),
                'korean_name': pal.get('korean_name', ''),
                'english_name': pal.get('english_name', ''),
                'elements': elements_str,
                'hp': stats.get('hp', ''),
                'attack': stats.get('attack', ''),
                'defense': stats.get('defense', ''),
                'kindling': work_skills.get('kindling', 0),
                'watering': work_skills.get('watering', 0),
                'planting': work_skills.get('planting', 0),
                'electricity': work_skills.get('electricity', 0),
                'handiwork': work_skills.get('handiwork', 0),
                'gathering': work_skills.get('gathering', 0),
                'lumbering': work_skills.get('lumbering', 0),
                'mining': work_skills.get('mining', 0),
                'medicine': work_skills.get('medicine', 0),
                'cooling': work_skills.get('cooling', 0),
                'transporting': work_skills.get('transporting', 0),
                'farming': work_skills.get('farming', 0),
                'partner_skill': pal.get('partner_skill', ''),
                'active_skills': active_skills_str,
                'drops': drops_str
            })
    
    print(f"총 {len(pal_data)}개의 팰 정보가 저장되었습니다.")

def main():
    """메인 크롤링 함수"""
    print("Paldb.cc 팰 정보 크롤링을 시작합니다...")
    
    # 이미 크롤링된 5개 팰의 데이터 (예시)
    sample_data = [
        {
            "id": "1", "korean_name": "도로롱", "english_name": "Lamball",
            "elements": ["무속성"], "stats": {"hp": "70", "attack": "70", "defense": "70"},
            "work_skills": {"handiwork": 1, "transporting": 1, "farming": 1},
            "partner_skill": "복슬복슬 방패 Lv.1",
            "active_skills": ["데굴데굴 솜사탕", "공기 대포", "파워 샷", "자폭", "번개 구체", "파워 폭탄", "팰 폭발"],
            "drops": ["양털", "도로롱의 양고기"]
        },
        {
            "id": "2", "korean_name": "까부냥", "english_name": "Cattiva",
            "elements": ["무속성"], "stats": {"hp": "70", "attack": "70", "defense": "70"},
            "work_skills": {"handiwork": 1, "gathering": 1, "mining": 1, "transporting": 1},
            "partner_skill": "고양이 손 빌리기 Lv.1",
            "active_skills": ["냥냥 펀치", "공기 대포", "모래 돌풍", "파워 샷", "바람의 칼날", "씨앗 기관총", "팰 폭발"],
            "drops": ["빨간 열매"]
        },
        {
            "id": "3", "korean_name": "꼬꼬닭", "english_name": "Chikipi",
            "elements": ["무속성"], "stats": {"hp": "60", "attack": "60", "defense": "60"},
            "work_skills": {"gathering": 1, "farming": 1},
            "partner_skill": "알 생산 Lv.1",
            "active_skills": ["치킨 태클", "공기 대포", "파워 샷", "자폭", "초록 폭풍", "모래 폭풍", "화염 폭풍"],
            "drops": ["알", "꼬꼬닭의 닭고기"]
        },
        {
            "id": "4", "korean_name": "큐룰리스", "english_name": "Lifmunk",
            "elements": ["풀"], "stats": {"hp": "75", "attack": "70", "defense": "70"},
            "work_skills": {"planting": 1, "handiwork": 1, "gathering": 1, "lumbering": 1, "medicine": 1},
            "partner_skill": "큐룰리스 리코일 Lv.1",
            "active_skills": ["바람의 칼날", "공기 대포", "파워 샷", "씨앗 기관총", "파워 폭탄", "가시덩굴", "태양 폭발"],
            "drops": ["열매 씨", "하급 의약품"]
        },
        {
            "id": "5", "korean_name": "파이호", "english_name": "Foxparks",
            "elements": ["Fire"], "stats": {"hp": "65", "attack": "75", "defense": "70"},
            "work_skills": {"kindling": 1},
            "partner_skill": "포옹 파이어 Lv.1",
            "active_skills": ["파이어 샷", "모래 돌풍", "스피릿 파이어", "불화살", "파이어 브레스", "유령의 불꽃", "화염구"],
            "drops": ["가죽", "발화 기관"]
        }
    ]
    
    # CSV 파일로 저장
    save_pal_data_to_csv(sample_data)
    
    print("크롤링이 완료되었습니다!")

if __name__ == "__main__":
    main() 