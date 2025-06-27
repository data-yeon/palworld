import requests
import pandas as pd
import json
import time

# Constants
API_BASE_URL = "https://api.palworld.dev/api/pals"
OUTPUT_CSV_FILE = "enhanced_complete_pals_from_api.csv"
REQUEST_TIMEOUT = 20  # seconds

def fetch_all_pals_data():
    """
    Fetches all Pal data from the palworld-paldex-api.
    The API seems to return all pals when no limit is specified.
    """
    print("API에서 모든 팰 데이터를 가져오는 중...")
    try:
        response = requests.get(API_BASE_URL, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        print(f"성공! 총 {len(data)}개의 팰 데이터를 가져왔습니다.")
        return data
    except requests.exceptions.RequestException as e:
        print(f"API 요청 중 오류 발생: {e}")
        return None

def parse_suitability(suitability_list):
    """Parses suitability data into a readable string."""
    if not suitability_list:
        return ""
    return ", ".join([f"{item['type']}(Lv.{item['level']})" for item in suitability_list])

def parse_skills(skills_list):
    """Parses skill data into a readable string."""
    if not skills_list:
        return ""
    return ", ".join([f"{skill['name']}(Lv.{skill['level']})" for skill in skills_list])

def flatten_data(pals_data):
    """
    Flattens the JSON data from the API into a list of dictionaries
    suitable for a CSV file.
    """
    flat_data = []
    for pal in pals_data:
        # Basic Info
        row = {
            'id': pal.get('id'),
            'key': pal.get('key'),
            'name': pal.get('name'),
            'description': pal.get('description'),
            'wiki': pal.get('wiki'),
        }

        # Types
        types = pal.get('types', [])
        row['type1'] = types[0] if len(types) > 0 else None
        row['type2'] = types[1] if len(types) > 1 else None

        # Suitability
        row['suitability'] = parse_suitability(pal.get('suitability', []))

        # Drops
        drops = pal.get('drops', [])
        row['drop1'] = drops[0] if len(drops) > 0 else None
        row['drop2'] = drops[1] if len(drops) > 1 else None
        row['drop3'] = drops[2] if len(drops) > 2 else None


        # Aura (Partner Skill)
        aura = pal.get('aura', {})
        row['partner_skill_name'] = aura.get('name')
        row['partner_skill_description'] = aura.get('description')

        # Stats
        stats = pal.get('stats', {})
        row['stats_hp'] = stats.get('hp')
        row['stats_melee_attack'] = stats.get('attack', {}).get('melee')
        row['stats_ranged_attack'] = stats.get('attack', {}).get('ranged')
        row['stats_defense'] = stats.get('defense')
        row['stats_ride_speed'] = stats.get('speed', {}).get('ride')
        row['stats_run_speed'] = stats.get('speed', {}).get('run')
        row['stats_walk_speed'] = stats.get('speed', {}).get('walk')
        row['stats_stamina'] = stats.get('stamina')
        row['stats_support'] = stats.get('support')
        row['stats_rarity'] = pal.get('rarity')
        row['stats_price'] = pal.get('price')

        # Breeding
        breeding = pal.get('breeding', {})
        row['breeding_rank'] = breeding.get('rank')
        row['breeding_order'] = breeding.get('order')
        row['breeding_male_prob'] = breeding.get('male_probability')

        # Skills
        row['active_skills'] = parse_skills(pal.get('skills', []))

        # Misc
        row['size'] = pal.get('size')
        row['image_wiki'] = pal.get('imageWiki')

        flat_data.append(row)
    return flat_data

def save_to_csv(data):
    """Saves the flattened data to a CSV file."""
    if not data:
        print("저장할 데이터가 없습니다.")
        return

    df = pd.DataFrame(data)
    print(f"데이터를 '{OUTPUT_CSV_FILE}' 파일로 저장하는 중...")
    df.to_csv(OUTPUT_CSV_FILE, index=False, encoding='utf-8-sig')
    print("CSV 파일 저장이 완료되었습니다!")
    print(f"총 {len(df)}개의 팰 정보가 저장되었습니다.")
    print("\n미리보기:")
    print(df.head().to_string())


if __name__ == "__main__":
    pals_json = fetch_all_pals_data()
    if pals_json:
        # The API returns a list directly under the main key
        # In case the structure changes, this might need adjustment.
        # Based on docs, it seems to be a list. Let's assume it is.
        # Correction: The doc shows a "content" key, let's try to access that.
        # But let's check first if it's a dict with 'content' or just a list.
        if isinstance(pals_json, dict) and 'content' in pals_json:
             pals_list = pals_json['content']
        else:
             # Assume the whole response is the list of pals
             pals_list = pals_json

        flattened_pals = flatten_data(pals_list)
        save_to_csv(flattened_pals) 