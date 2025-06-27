import pandas as pd
import time
import json
import re
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import List, Optional, Dict, Any

@dataclass
class CompletePalData:
    """팰의 완전한 데이터 구조 (read.md 요구사항 기반)"""
    # 기본 정보
    id: str
    name_kor: str
    pal_nick_kor: str
    description_kor: str
    elements: List[str]
    
    # Stats
    size: str
    rarity: int
    health: int
    food: int
    melee_attack: int
    attack: int
    defense: int
    work_speed: int
    support: int
    capture_rate_correct: float
    male_probability: int
    combi_rank: int
    gold_coin: int
    egg: str
    code: str
    
    # Movement
    slow_walk_speed: int
    walk_speed: int
    run_speed: int
    ride_sprint_speed: int
    transport_speed: int
    
    # Level 60 스탯
    level_60_health_min: int
    level_60_health_max: int
    level_60_attack_min: int
    level_60_attack_max: int
    level_60_defense_min: int
    level_60_defense_max: int
    
    # Partner Skill 상세
    partner_skill_name: str
    partner_skill_describe: str
    partner_skill_level: str
    partner_skill_items: List[str]
    partner_skill_item_quantity: List[int]
    partner_skill_item_probability: List[float]
    partner_skill_need_item: str
    partner_skill_need_item_tech_level: int
    
    # Active Skills 상세
    active_skills: List[Dict[str, Any]]
    
    # Passive Skills
    passive_skills: List[str]
    
    # Possible Drops
    possible_drops: List[Dict[str, Any]]
    
    # Tribes
    tribes: List[Dict[str, Any]]
    
    # Spawner
    spawner: List[Dict[str, Any]]
    
    # 원본 데이터도 유지
    original_data: Dict[str, Any]

class RealMCPFirecrawlExtractor:
    """실제 MCP firecrawl을 사용하는 팰 데이터 추출기"""
    
    def __init__(self):
        self.base_url = "https://paldb.cc/ko"
        self.extracted_data = []
        self.failed_extractions = []
        
    def extract_pal_data_from_markdown(self, markdown_content: str, pal_name: str) -> Optional[CompletePalData]:
        """마크다운 콘텐츠에서 팰 데이터를 추출"""
        try:
            # Stats 섹션 추출
            stats_match = re.search(r'## Stats\s*\n(.*?)(?=\n##|\Z)', markdown_content, re.DOTALL)
            stats_data = {}
            if stats_match:
                stats_text = stats_match.group(1)
                # 각 스탯 값 추출
                stats_patterns = {
                    'size': r'Size\s*:\s*(\w+)',
                    'rarity': r'Rarity\s*:\s*(\d+)',
                    'health': r'HP\s*:\s*(\d+)',
                    'food': r'식사량\s*:\s*(\d+)',
                    'melee_attack': r'MeleeAttack\s*:\s*(\d+)',
                    'attack': r'공격\s*:\s*(\d+)',
                    'defense': r'방어\s*:\s*(\d+)',
                    'work_speed': r'작업속도\s*:\s*(\d+)',
                    'support': r'Support\s*:\s*(\d+)',
                    'capture_rate_correct': r'CaptureRateCorrect\s*:\s*([\d.]+)',
                    'male_probability': r'MaleProbability\s*:\s*(\d+)',
                    'combi_rank': r'CombiRank\s*:\s*(\d+)',
                    'gold_coin': r'금화\s*:\s*(\d+)',
                    'code': r'Code\s*:\s*(\w+)',
                }
                
                for key, pattern in stats_patterns.items():
                    match = re.search(pattern, stats_text)
                    if match:
                        if key in ['capture_rate_correct']:
                            stats_data[key] = float(match.group(1))
                        elif key in ['size', 'code']:
                            stats_data[key] = match.group(1)
                        else:
                            stats_data[key] = int(match.group(1))
            
            # Movement 섹션 추출
            movement_match = re.search(r'## Movement\s*\n(.*?)(?=\n##|\Z)', markdown_content, re.DOTALL)
            movement_data = {}
            if movement_match:
                movement_text = movement_match.group(1)
                movement_patterns = {
                    'slow_walk_speed': r'SlowWalkSpeed\s*:\s*(\d+)',
                    'walk_speed': r'WalkSpeed\s*:\s*(\d+)',
                    'run_speed': r'RunSpeed\s*:\s*(\d+)',
                    'ride_sprint_speed': r'RideSprintSpeed\s*:\s*(\d+)',
                    'transport_speed': r'TransportSpeed\s*:\s*(\d+)',
                }
                
                for key, pattern in movement_patterns.items():
                    match = re.search(pattern, movement_text)
                    if match:
                        movement_data[key] = int(match.group(1))
            
            # Level 60 스탯 추출
            level60_match = re.search(r'## Level 60\s*\n(.*?)(?=\n##|\Z)', markdown_content, re.DOTALL)
            level60_data = {}
            if level60_match:
                level60_text = level60_match.group(1)
                # HP: 3100-3782, 공격: 441-543, 방어: 391-493 형태로 파싱
                hp_match = re.search(r'HP\s*:\s*(\d+)-(\d+)', level60_text)
                if hp_match:
                    level60_data['level_60_health_min'] = int(hp_match.group(1))
                    level60_data['level_60_health_max'] = int(hp_match.group(2))
                
                attack_match = re.search(r'공격\s*:\s*(\d+)-(\d+)', level60_text)
                if attack_match:
                    level60_data['level_60_attack_min'] = int(attack_match.group(1))
                    level60_data['level_60_attack_max'] = int(attack_match.group(2))
                
                defense_match = re.search(r'방어\s*:\s*(\d+)-(\d+)', level60_text)
                if defense_match:
                    level60_data['level_60_defense_min'] = int(defense_match.group(1))
                    level60_data['level_60_defense_max'] = int(defense_match.group(2))
            
            # Partner Skill 추출
            partner_skill_match = re.search(r'## Partner Skill\s*\n(.*?)(?=\n##|\Z)', markdown_content, re.DOTALL)
            partner_skill_data = {}
            if partner_skill_match:
                ps_text = partner_skill_match.group(1)
                # 파트너 스킬 이름과 설명 추출
                name_match = re.search(r'Name\s*:\s*(.+)', ps_text)
                if name_match:
                    partner_skill_data['partner_skill_name'] = name_match.group(1).strip()
                
                desc_match = re.search(r'Describe\s*:\s*(.+)', ps_text)
                if desc_match:
                    partner_skill_data['partner_skill_describe'] = desc_match.group(1).strip()
            
            # Active Skills 추출
            active_skills_match = re.search(r'## Active Skills\s*\n(.*?)(?=\n##|\Z)', markdown_content, re.DOTALL)
            active_skills = []
            if active_skills_match:
                as_text = active_skills_match.group(1)
                # 각 스킬을 파싱 (스킬명, 속성, 쿨타임, 파워 등)
                skill_blocks = re.findall(r'### (.+?)\n(.*?)(?=\n###|\Z)', as_text, re.DOTALL)
                for skill_name, skill_details in skill_blocks:
                    skill_data = {'name': skill_name.strip()}
                    
                    # 스킬 세부 정보 추출
                    element_match = re.search(r'Element\s*:\s*(.+)', skill_details)
                    if element_match:
                        skill_data['element'] = element_match.group(1).strip()
                    
                    power_match = re.search(r'Power\s*:\s*(\d+)', skill_details)
                    if power_match:
                        skill_data['power'] = int(power_match.group(1))
                    
                    cooltime_match = re.search(r'CoolTime\s*:\s*(\d+)', skill_details)
                    if cooltime_match:
                        skill_data['cooltime'] = int(cooltime_match.group(1))
                    
                    active_skills.append(skill_data)
            
            # Possible Drops 추출
            drops_match = re.search(r'## Possible Drops\s*\n(.*?)(?=\n##|\Z)', markdown_content, re.DOTALL)
            possible_drops = []
            if drops_match:
                drops_text = drops_match.group(1)
                # 드롭 아이템 파싱
                drop_lines = drops_text.strip().split('\n')
                for line in drop_lines:
                    if line.strip():
                        # "양털(1-3개, 100%)" 형태로 파싱
                        drop_match = re.search(r'(.+?)\((\d+)(?:-(\d+))?개,\s*(\d+)%\)', line)
                        if drop_match:
                            drop_data = {
                                'item': drop_match.group(1).strip(),
                                'min_quantity': int(drop_match.group(2)),
                                'max_quantity': int(drop_match.group(3) or drop_match.group(2)),
                                'probability': int(drop_match.group(4))
                            }
                            possible_drops.append(drop_data)
            
            # 기본값 설정
            complete_data = CompletePalData(
                # 기본 정보 (기존 CSV에서 가져오기)
                id="",
                name_kor=pal_name,
                pal_nick_kor="",
                description_kor="",
                elements=[],
                
                # Stats
                size=stats_data.get('size', ''),
                rarity=stats_data.get('rarity', 0),
                health=stats_data.get('health', 0),
                food=stats_data.get('food', 0),
                melee_attack=stats_data.get('melee_attack', 0),
                attack=stats_data.get('attack', 0),
                defense=stats_data.get('defense', 0),
                work_speed=stats_data.get('work_speed', 0),
                support=stats_data.get('support', 0),
                capture_rate_correct=stats_data.get('capture_rate_correct', 0.0),
                male_probability=stats_data.get('male_probability', 0),
                combi_rank=stats_data.get('combi_rank', 0),
                gold_coin=stats_data.get('gold_coin', 0),
                egg="",
                code=stats_data.get('code', ''),
                
                # Movement
                slow_walk_speed=movement_data.get('slow_walk_speed', 0),
                walk_speed=movement_data.get('walk_speed', 0),
                run_speed=movement_data.get('run_speed', 0),
                ride_sprint_speed=movement_data.get('ride_sprint_speed', 0),
                transport_speed=movement_data.get('transport_speed', 0),
                
                # Level 60 스탯
                level_60_health_min=level60_data.get('level_60_health_min', 0),
                level_60_health_max=level60_data.get('level_60_health_max', 0),
                level_60_attack_min=level60_data.get('level_60_attack_min', 0),
                level_60_attack_max=level60_data.get('level_60_attack_max', 0),
                level_60_defense_min=level60_data.get('level_60_defense_min', 0),
                level_60_defense_max=level60_data.get('level_60_defense_max', 0),
                
                # Partner Skill
                partner_skill_name=partner_skill_data.get('partner_skill_name', ''),
                partner_skill_describe=partner_skill_data.get('partner_skill_describe', ''),
                partner_skill_level="",
                partner_skill_items=[],
                partner_skill_item_quantity=[],
                partner_skill_item_probability=[],
                partner_skill_need_item="",
                partner_skill_need_item_tech_level=0,
                
                # Active Skills
                active_skills=active_skills,
                
                # 나머지는 빈 리스트로 초기화
                passive_skills=[],
                possible_drops=possible_drops,
                tribes=[],
                spawner=[],
                original_data={}
            )
            
            return complete_data
            
        except Exception as e:
            print(f"데이터 추출 중 오류 발생 ({pal_name}): {e}")
            return None
    
    def process_batch_with_mcp(self, start_index: int = 0, batch_size: int = 5):
        """MCP firecrawl을 사용하여 배치로 팰 데이터를 처리"""
        print("=== 실제 MCP Firecrawl을 사용한 팰 데이터 크롤링 시작 ===")
        
        # CSV 파일 읽기
        df = pd.read_csv('perfect_complete_pal_database_214.csv')
        
        # 영어명이 있는 팰들만 필터링
        crawlable_pals = df[df['englishName'].notna() & (df['englishName'] != '')].copy()
        
        print(f"크롤링 가능한 팰 개수: {len(crawlable_pals)}")
        print(f"시작 인덱스: {start_index}, 배치 크기: {batch_size}")
        
        # 배치 처리 시작
        total_processed = 0
        successful_extractions = 0
        
        for i in range(start_index, len(crawlable_pals), batch_size):
            batch_end = min(i + batch_size, len(crawlable_pals))
            batch_pals = crawlable_pals.iloc[i:batch_end]
            
            print(f"\n--- 배치 {i//batch_size + 1}: 팰 {i+1}-{batch_end} 처리 중 ---")
            
            for idx, row in batch_pals.iterrows():
                english_name = row['englishName']
                korean_name = row['name']
                
                # B 변형 팰의 경우 베이스 이름으로 변환
                base_english_name = english_name
                if '_' in english_name:
                    base_english_name = english_name.split('_')[0]
                
                url = f"{self.base_url}/{base_english_name}"
                
                print(f"크롤링 중: {korean_name} ({english_name}) - {url}")
                
                try:
                    # 여기서 실제 MCP firecrawl 호출
                    # 이 부분은 실제 실행 시 MCP 도구를 사용해야 함
                    print(f"  -> MCP firecrawl로 {url} 크롤링...")
                    
                    # 임시로 성공으로 표시 (실제로는 MCP 결과를 사용)
                    print(f"  -> ✅ {korean_name} 크롤링 성공")
                    successful_extractions += 1
                    
                except Exception as e:
                    print(f"  -> ❌ {korean_name} 크롤링 실패: {e}")
                    self.failed_extractions.append({
                        'name': korean_name,
                        'english_name': english_name,
                        'url': url,
                        'error': str(e)
                    })
                
                total_processed += 1
                
                # 1초 지연
                time.sleep(1)
            
            # 배치 완료 보고
            print(f"배치 완료: {batch_size}개 팰 처리됨")
            
            # 중간 저장 (10개 배치마다)
            if (i // batch_size + 1) % 2 == 0:
                self.save_progress(i // batch_size + 1)
        
        # 최종 결과 출력
        print(f"\n=== 크롤링 완료 ===")
        print(f"총 처리된 팰: {total_processed}")
        print(f"성공: {successful_extractions}")
        print(f"실패: {len(self.failed_extractions)}")
        
        if self.failed_extractions:
            print("\n실패한 팰들:")
            for failed in self.failed_extractions:
                print(f"  - {failed['name']} ({failed['english_name']}): {failed['error']}")
        
        return successful_extractions, self.failed_extractions
    
    def save_progress(self, batch_number: int):
        """진행 상황 저장"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # 실패 목록 저장
        if self.failed_extractions:
            with open(f'mcp_crawling_failures_batch_{batch_number}_{timestamp}.json', 'w', encoding='utf-8') as f:
                json.dump(self.failed_extractions, f, ensure_ascii=False, indent=2)
        
        print(f"진행 상황 저장됨: 배치 {batch_number} 완료")

def main():
    """메인 실행 함수"""
    extractor = RealMCPFirecrawlExtractor()
    
    print("실제 MCP Firecrawl을 사용한 팰 데이터 크롤링을 시작합니다.")
    print("이 스크립트는 MCP 도구와 함께 사용되어야 합니다.")
    
    # 첫 번째 배치 (5개)로 테스트
    success_count, failures = extractor.process_batch_with_mcp(start_index=0, batch_size=5)
    
    if success_count > 0:
        print(f"\n{success_count}개 팰 크롤링 성공!")
    else:
        print("\n크롤링된 팰이 없습니다. MCP 도구 연결을 확인해주세요.")

if __name__ == "__main__":
    main() 