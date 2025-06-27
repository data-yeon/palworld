import json
import pandas as pd
import os

# --- Constants ---
SOURCE_JSON_FILE = "paldex_repo_temp/graveyard/app/data/pals.json"
OUTPUT_CSV_FILE = "enhanced_complete_pals_from_json.csv"

def load_json_data(file_path):
    """Loads data from a JSON file."""
    print(f"'{file_path}'에서 JSON 데이터 로드 중...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f"성공! {len(data)}개의 팰 데이터를 로드했습니다.")
            return data
    except FileNotFoundError:
        print(f"오류: 파일을 찾을 수 없습니다 - {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"오류: JSON 파일을 디코딩할 수 없습니다 - {file_path}")
        return None

def parse_work_suitability(work_data):
    """Parses work suitability data into a more readable format."""
    if not isinstance(work_data, dict):
        return ""
    
    parts = []
    for work, level in work_data.items():
        if level > 0:
            # Simple re-mapping for clarity if needed, otherwise use raw names
            work_name = work.replace('_', ' ').title()
            parts.append(f"{work_name}(Lv.{level})")
    return ", ".join(parts)

def parse_active_skills(skills_data):
    """Parses active skills into a detailed string."""
    if not isinstance(skills_data, list):
        return ""
        
    parts = []
    for skill in skills_data:
        parts.append(
            f"{skill.get('name', 'N/A')} "
            f"(Lv.{skill.get('level_learned', 0)} | "
            f"Pwr.{skill.get('power', 0)} | "
            f"CD.{skill.get('cool_down_time', 0)}s)"
        )
    return " | ".join(parts)

def flatten_pal_data(pals_data):
    """Flattens the complex JSON structure into a list of dictionaries for CSV."""
    flattened_list = []
    for pal in pals_data:
        # Skip non-pal entries if any
        if not pal.get('is_pal', False):
            continue

        stats = pal.get('stats', {})
        
        flat_pal = {
            'pal_index': pal.get('pal_index'),
            'pal_name': pal.get('pal_name'),
            'pal_description': pal.get('pal_description'),
            'is_boss': pal.get('is_boss', False),
            'is_tower_boss': pal.get('is_tower_boss', False),
            
            # Elements
            'element_1': pal.get('elements')[0] if pal.get('elements') else None,
            'element_2': pal.get('elements')[1] if pal.get('elements') and len(pal.get('elements')) > 1 else None,
            
            # Drops
            'item_drop_1': pal.get('item_drops')[0] if pal.get('item_drops') else None,
            'item_drop_2': pal.get('item_drops')[1] if pal.get('item_drops') and len(pal.get('item_drops')) > 1 else None,
            
            # Partner Skill
            'partner_skill_title': pal.get('partner_skill_title'),
            'partner_skill_description': pal.get('partner_skill_description'),

            # Work Suitability
            'work_suitability': parse_work_suitability(pal.get('work_suitability')),
            
            # Stats
            'stats_hp': stats.get('hp'),
            'stats_melee_attack': stats.get('melee_attack'),
            'stats_shot_attack': stats.get('shot_attack'),
            'stats_defense': stats.get('defense'),
            'stats_support': stats.get('support'),
            'stats_stamina': stats.get('stamina'),
            'stats_walk_speed': stats.get('walk_speed'),
            'stats_run_speed': stats.get('run_speed'),
            'stats_ride_sprint_speed': stats.get('ride_sprint_speed'),
            'stats_food_amount': stats.get('food_amount'),
            'stats_rarity': pal.get('rarity'),
            'stats_price': pal.get('price'),

            # Breeding
            'male_probability': pal.get('male_probability'),
            'combi_rank': pal.get('combi_rank'),

            # Active Skills
            'active_skills': parse_active_skills(pal.get('active_skills'))
        }
        flattened_list.append(flat_pal)
        
    return flattened_list

def save_to_csv(data, file_path):
    """Saves the flattened data to a CSV file."""
    if not data:
        print("저장할 데이터가 없습니다.")
        return

    df = pd.DataFrame(data)
    print(f"데이터를 '{file_path}' 파일로 저장하는 중...")
    
    # Sort by pal_index, handling non-numeric values
    df['pal_index_num'] = pd.to_numeric(df['pal_index'], errors='coerce')
    df = df.sort_values(by='pal_index_num').drop(columns=['pal_index_num'])

    df.to_csv(file_path, index=False, encoding='utf-8-sig')
    print("CSV 파일 저장이 완료되었습니다!")
    print(f"총 {len(df)}개의 팰 정보가 성공적으로 저장되었습니다.")
    print("\n미리보기 (처음 5개 행):")
    print(df.head().to_string())

def main():
    """Main function to run the script."""
    pal_data_json = load_json_data(SOURCE_JSON_FILE)
    
    if pal_data_json:
        flattened_data = flatten_pal_data(pal_data_json)
        save_to_csv(flattened_data, OUTPUT_CSV_FILE)

if __name__ == "__main__":
    main() 