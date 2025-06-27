#!/usr/bin/env python3
"""
Enhanced Firecrawl Pal Data Extractor
paldb.cc에서 팰 상세 정보를 크롤링하여 read.md 요구사항에 맞는 확장된 CSV를 생성
"""

import csv
import json
import re
import time
import requests
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class PalDetailedData:
    """팰의 상세 정보를 담는 데이터 클래스"""
    # 기본 정보
    id: str
    name_kor: str
    pal_nick_kor: str = ""
    description_kor: str = ""
    elements: str = ""
    english_name: str = ""
    
    # Stats
    size: str = ""
    rarity: int = 0
    health: int = 0
    food: int = 0
    melee_attack: int = 0
    attack: int = 0
    defense: int = 0
    work_speed: int = 0
    support: int = 0
    capture_rate_correct: float = 0.0
    male_probability: int = 0
    combi_rank: int = 0
    gold_coin: int = 0
    egg: str = ""
    code: str = ""
    
    # Movement
    slow_walk_speed: int = 0
    walk_speed: int = 0
    run_speed: int = 0
    ride_sprint_speed: int = 0
    transport_speed: int = 0
    
    # Level 60 Stats
    level_60_health: str = ""
    level_60_attack: str = ""
    level_60_defense: str = ""
    
    # Partner Skill
    partner_skill_name: str = ""
    partner_skill_describe: str = ""
    partner_skill_level: str = ""
    partner_skill_items: str = ""
    partner_skill_item_quantity: str = ""
    partner_skill_item_probability: str = ""
    partner_skill_need_item: str = ""
    partner_skill_need_item_tech_level: str = ""
    
    # Work Suitabilities
    work_suitabilities: str = ""
    work_levels: str = ""
    
    # Active Skills
    active_skills_name: str = ""
    active_skills_element: str = ""
    active_skills_cool_time: str = ""
    active_skills_power: str = ""
    active_skills_shoot_attack: str = ""
    active_skills_melee_attack: str = ""
    active_skills_accumulated_element: str = ""
    active_skills_accumulated_value: str = ""
    active_skills_describe: str = ""
    active_skills_required_item: str = ""
    active_skills_required_level: str = ""
    
    # Passive Skills
    passive_skills: str = ""
    
    # Possible Drops
    drops_item_name: str = ""
    drops_item_quantity: str = ""
    drops_item_probability: str = ""
    
    # Tribes
    tribes_name: str = ""
    tribes_type: str = ""
    
    # Spawner
    spawner_name: str = ""
    spawner_level: str = ""
    spawner_area: str = ""

class FirecrawlPalExtractor:
    def __init__(self):
        self.base_url = "https://paldb.cc/ko"
        self.session = requests.Session()
        
    def scrape_with_mcp_firecrawl(self, url: str) -> Optional[str]:
        """MCP Firecrawl을 사용하여 페이지 크롤링 (실제로는 외부 API 호출)"""
        try:
            # 실제 구현에서는 MCP Firecrawl 도구를 사용
            # 여기서는 시뮬레이션을 위한 더미 구현
            logger.info(f"Scraping {url} with MCP Firecrawl...")
            time.sleep(1)  # API 호출 시뮬레이션
            return "sample_markdown_content"
        except Exception as e:
            logger.error(f"Error scraping {url}: {e}")
            return None
            
    def parse_pal_data(self, markdown_content: str, english_name: str) -> PalDetailedData:
        """마크다운 콘텐츠에서 팰 데이터 파싱"""
        pal_data = PalDetailedData(id="", name_kor="", english_name=english_name)
        
        if not markdown_content:
            return pal_data
            
        try:
            # ID와 이름 추출
            id_match = re.search(r'#(\d+[B]?)', markdown_content)
            if id_match:
                pal_data.id = id_match.group(1)
                
            name_match = re.search(r'\[([^\]]+)\]\([^)]+\)#\d+', markdown_content)
            if name_match:
                pal_data.name_kor = name_match.group(1)
                
            # 속성 추출
            element_match = re.search(r'(무속성|화염|물|풀|번개|얼음|땅|어둠|용)\s*속성', markdown_content)
            if element_match:
                pal_data.elements = element_match.group(1)
                
            # Stats 섹션 파싱
            stats_section = re.search(r'##### Stats(.*?)##### Movement', markdown_content, re.DOTALL)
            if stats_section:
                stats_text = stats_section.group(1)
                
                # Size
                size_match = re.search(r'Size\s*(\w+)', stats_text)
                if size_match:
                    pal_data.size = size_match.group(1)
                    
                # Rarity
                rarity_match = re.search(r'Rarity\s*(\d+)', stats_text)
                if rarity_match:
                    pal_data.rarity = int(rarity_match.group(1))
                    
                # HP
                hp_match = re.search(r'HP\s*(\d+)', stats_text)
                if hp_match:
                    pal_data.health = int(hp_match.group(1))
                    
                # 식사량
                food_match = re.search(r'식사량\s*(\d+)', stats_text)
                if food_match:
                    pal_data.food = int(food_match.group(1))
                    
                # MeleeAttack
                melee_attack_match = re.search(r'MeleeAttack\s*(\d+)', stats_text)
                if melee_attack_match:
                    pal_data.melee_attack = int(melee_attack_match.group(1))
                    
                # 공격
                attack_match = re.search(r'공격\s*(\d+)', stats_text)
                if attack_match:
                    pal_data.attack = int(attack_match.group(1))
                    
                # 방어
                defense_match = re.search(r'방어\s*(\d+)', stats_text)
                if defense_match:
                    pal_data.defense = int(defense_match.group(1))
                    
                # 작업 속도
                work_speed_match = re.search(r'작업 속도\s*(\d+)', stats_text)
                if work_speed_match:
                    pal_data.work_speed = int(work_speed_match.group(1))
                    
                # Support
                support_match = re.search(r'Support\s*(\d+)', stats_text)
                if support_match:
                    pal_data.support = int(support_match.group(1))
                    
                # CaptureRateCorrect
                capture_rate_match = re.search(r'CaptureRateCorrect\s*([\d.]+)', stats_text)
                if capture_rate_match:
                    pal_data.capture_rate_correct = float(capture_rate_match.group(1))
                    
                # MaleProbability
                male_prob_match = re.search(r'MaleProbability\s*(\d+)', stats_text)
                if male_prob_match:
                    pal_data.male_probability = int(male_prob_match.group(1))
                    
                # CombiRank
                combi_rank_match = re.search(r'CombiRank.*?(\d+)', stats_text)
                if combi_rank_match:
                    pal_data.combi_rank = int(combi_rank_match.group(1))
                    
                # 금화
                gold_match = re.search(r'금화.*?(\d+)', stats_text)
                if gold_match:
                    pal_data.gold_coin = int(gold_match.group(1))
                    
                # Egg
                egg_match = re.search(r'Egg.*?\[([^\]]+)\]', stats_text)
                if egg_match:
                    pal_data.egg = egg_match.group(1)
                    
                # Code
                code_match = re.search(r'Code\s*(\w+)', stats_text)
                if code_match:
                    pal_data.code = code_match.group(1)
                    
            # Movement 섹션 파싱
            movement_section = re.search(r'##### Movement(.*?)##### Level 60', markdown_content, re.DOTALL)
            if movement_section:
                movement_text = movement_section.group(1)
                
                # SlowWalkSpeed
                slow_walk_match = re.search(r'SlowWalkSpeed\s*(\d+)', movement_text)
                if slow_walk_match:
                    pal_data.slow_walk_speed = int(slow_walk_match.group(1))
                    
                # WalkSpeed
                walk_speed_match = re.search(r'WalkSpeed\s*(\d+)', movement_text)
                if walk_speed_match:
                    pal_data.walk_speed = int(walk_speed_match.group(1))
                    
                # RunSpeed
                run_speed_match = re.search(r'RunSpeed\s*(\d+)', movement_text)
                if run_speed_match:
                    pal_data.run_speed = int(run_speed_match.group(1))
                    
                # RideSprintSpeed
                ride_sprint_match = re.search(r'RideSprintSpeed\s*(\d+)', movement_text)
                if ride_sprint_match:
                    pal_data.ride_sprint_speed = int(ride_sprint_match.group(1))
                    
                # TransportSpeed
                transport_speed_match = re.search(r'TransportSpeed\s*(\d+)', movement_text)
                if transport_speed_match:
                    pal_data.transport_speed = int(transport_speed_match.group(1))
                    
            # Level 60 Stats
            level_60_section = re.search(r'##### Level 60(.*?)#####', markdown_content, re.DOTALL)
            if level_60_section:
                level_60_text = level_60_section.group(1)
                
                hp_60_match = re.search(r'HP\s*([\d\s–]+)', level_60_text)
                if hp_60_match:
                    pal_data.level_60_health = hp_60_match.group(1).strip()
                    
                attack_60_match = re.search(r'공격\s*([\d\s–]+)', level_60_text)
                if attack_60_match:
                    pal_data.level_60_attack = attack_60_match.group(1).strip()
                    
                defense_60_match = re.search(r'방어\s*([\d\s–]+)', level_60_text)
                if defense_60_match:
                    pal_data.level_60_defense = defense_60_match.group(1).strip()
                    
            # 파트너 스킬 파싱
            partner_skill_section = re.search(r'##### 파트너 스킬[:\s]*([^\n]*)(.*?)(?=#####|$)', markdown_content, re.DOTALL)
            if partner_skill_section:
                skill_name = partner_skill_section.group(1).strip()
                skill_desc_section = partner_skill_section.group(2)
                
                pal_data.partner_skill_name = skill_name
                
                # 파트너 스킬 설명 추출
                desc_lines = skill_desc_section.split('\n')
                description_parts = []
                for line in desc_lines:
                    if line.strip() and not line.startswith('|') and not line.startswith('Lv.'):
                        description_parts.append(line.strip())
                        
                pal_data.partner_skill_describe = ' '.join(description_parts[:3])  # 처음 3줄만
                
            # 작업 적성 파싱
            work_section = re.search(r'작업 적성\](.*?)식사량', markdown_content, re.DOTALL)
            if work_section:
                work_text = work_section.group(1)
                work_types = []
                work_levels = []
                
                work_matches = re.findall(r'\[\s*([^\]]+)\].*?Lv(\d+)', work_text)
                for work_type, level in work_matches:
                    work_types.append(work_type.strip())
                    work_levels.append(f"Lv{level}")
                    
                pal_data.work_suitabilities = '; '.join(work_types)
                pal_data.work_levels = '; '.join(work_levels)
                
            # 액티브 스킬 파싱
            active_skills_section = re.search(r'##### 액티브 스킬(.*?)##### 패시브 스킬', markdown_content, re.DOTALL)
            if active_skills_section:
                skills_text = active_skills_section.group(1)
                
                skill_names = []
                skill_elements = []
                skill_cool_times = []
                skill_powers = []
                skill_descriptions = []
                skill_levels = []
                
                # 각 스킬 블록 파싱
                skill_blocks = re.findall(r'Lv\.\s*(\d+)\s*\[([^\]]+)\].*?([무화물풀번얼땅어용]*)\s*속성.*?위력:\s*(\d+).*?쿨타임[:\s]*(\d+).*?(?=Lv\.|$)', skills_text, re.DOTALL)
                
                for level, name, element, power, cooltime in skill_blocks:
                    skill_levels.append(f"Lv.{level}")
                    skill_names.append(name)
                    skill_elements.append(element if element else "무속성")
                    skill_powers.append(power)
                    skill_cool_times.append(cooltime)
                    
                pal_data.active_skills_required_level = '; '.join(skill_levels)
                pal_data.active_skills_name = '; '.join(skill_names)
                pal_data.active_skills_element = '; '.join(skill_elements)
                pal_data.active_skills_power = '; '.join(skill_powers)
                pal_data.active_skills_cool_time = '; '.join(skill_cool_times)
                
            # 드롭 아이템 파싱
            drops_section = re.search(r'##### 드롭하는 아이템(.*?)##### Tribes', markdown_content, re.DOTALL)
            if drops_section:
                drops_text = drops_section.group(1)
                
                drop_items = []
                drop_quantities = []
                drop_probabilities = []
                
                # 테이블 행 파싱
                drop_matches = re.findall(r'\[([^\]]+)\].*?(\d+(?:–\d+)?)\s*\|\s*(\d+%)', drops_text)
                for item_name, quantity, probability in drop_matches:
                    drop_items.append(item_name)
                    drop_quantities.append(quantity)
                    drop_probabilities.append(probability)
                    
                pal_data.drops_item_name = '; '.join(drop_items)
                pal_data.drops_item_quantity = '; '.join(drop_quantities)
                pal_data.drops_item_probability = '; '.join(drop_probabilities)
                
            # Tribes 파싱
            tribes_section = re.search(r'##### Tribes(.*?)##### Spawner', markdown_content, re.DOTALL)
            if tribes_section:
                tribes_text = tribes_section.group(1)
                
                tribe_names = []
                tribe_types = []
                
                tribe_matches = re.findall(r'\[([^\]]+)\].*?\|\s*(Tribe\s+\w+)', tribes_text)
                for name, tribe_type in tribe_matches:
                    tribe_names.append(name)
                    tribe_types.append(tribe_type)
                    
                pal_data.tribes_name = '; '.join(tribe_names)
                pal_data.tribes_type = '; '.join(tribe_types)
                
            # Spawner 파싱
            spawner_section = re.search(r'##### Spawner(.*?)(?=###|$)', markdown_content, re.DOTALL)
            if spawner_section:
                spawner_text = spawner_section.group(1)
                
                spawner_names = []
                spawner_levels = []
                spawner_areas = []
                
                spawner_matches = re.findall(r'\[([^\]]+)\].*?\|\s*Lv\.\s*([\d\s–]+)\s*\|\s*([^\|]+)', spawner_text)
                for name, level, area in spawner_matches:
                    spawner_names.append(name)
                    spawner_levels.append(level.strip())
                    spawner_areas.append(area.strip())
                    
                pal_data.spawner_name = '; '.join(spawner_names)
                pal_data.spawner_level = '; '.join(spawner_levels)
                pal_data.spawner_area = '; '.join(spawner_areas)
                
            # Summary에서 설명 추출
            summary_section = re.search(r'##### Summary(.*?)(?=###|$)', markdown_content, re.DOTALL)
            if summary_section:
                summary_text = summary_section.group(1).strip()
                # 불필요한 줄 제거하고 설명만 추출
                description_lines = []
                for line in summary_text.split('\n'):
                    line = line.strip()
                    if line and not line.startswith('[') and not line.startswith('!'):
                        description_lines.append(line)
                        
                pal_data.description_kor = ' '.join(description_lines[:3])  # 처음 3줄만
                
        except Exception as e:
            logger.error(f"Error parsing pal data for {english_name}: {e}")
            
        return pal_data
        
    def load_existing_csv(self, filename: str) -> List[Dict[str, str]]:
        """기존 CSV 파일 로드"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return list(csv.DictReader(f))
        except Exception as e:
            logger.error(f"Error loading CSV {filename}: {e}")
            return []
            
    def save_enhanced_csv(self, pal_data_list: List[PalDetailedData], filename: str):
        """확장된 팰 데이터를 CSV로 저장"""
        fieldnames = [
            'id', 'name_kor', 'pal_nick_kor', 'description_kor', 'elements', 'english_name',
            # Stats
            'size', 'rarity', 'health', 'food', 'melee_attack', 'attack', 'defense', 
            'work_speed', 'support', 'capture_rate_correct', 'male_probability', 
            'combi_rank', 'gold_coin', 'egg', 'code',
            # Movement
            'slow_walk_speed', 'walk_speed', 'run_speed', 'ride_sprint_speed', 'transport_speed',
            # Level 60
            'level_60_health', 'level_60_attack', 'level_60_defense',
            # Partner Skill
            'partner_skill_name', 'partner_skill_describe', 'partner_skill_level',
            'partner_skill_items', 'partner_skill_item_quantity', 'partner_skill_item_probability',
            'partner_skill_need_item', 'partner_skill_need_item_tech_level',
            # Work
            'work_suitabilities', 'work_levels',
            # Active Skills
            'active_skills_name', 'active_skills_element', 'active_skills_cool_time',
            'active_skills_power', 'active_skills_shoot_attack', 'active_skills_melee_attack',
            'active_skills_accumulated_element', 'active_skills_accumulated_value',
            'active_skills_describe', 'active_skills_required_item', 'active_skills_required_level',
            # Passive Skills
            'passive_skills',
            # Drops
            'drops_item_name', 'drops_item_quantity', 'drops_item_probability',
            # Tribes
            'tribes_name', 'tribes_type',
            # Spawner
            'spawner_name', 'spawner_level', 'spawner_area'
        ]
        
        try:
            with open(filename, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                
                for pal_data in pal_data_list:
                    row_data = {}
                    for field in fieldnames:
                        row_data[field] = getattr(pal_data, field, "")
                    writer.writerow(row_data)
                    
            logger.info(f"Enhanced CSV saved to {filename}")
            
        except Exception as e:
            logger.error(f"Error saving enhanced CSV: {e}")

def main():
    """메인 실행 함수 - 이 스크립트는 실제로는 MCP 환경에서 실행되어야 합니다"""
    logger.info("Enhanced Firecrawl Pal Data Extractor script created.")
    logger.info("This script should be used in MCP environment with firecrawl tools.")
    logger.info("Use the functions in this script to process pal data with MCP firecrawl tools.")

if __name__ == "__main__":
    main() 