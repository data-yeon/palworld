import pandas as pd
import json
import time
import asyncio
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
import logging
from pathlib import Path
import csv
import re

@dataclass
class PalDetailedData:
    """read.md 요구사항에 맞는 팰 상세 데이터 클래스"""
    # 기본 정보 (기존 CSV에서 가져옴)
    id: str
    name_kor: str
    pal_nick_kor: str = ""
    description_kor: str = ""
    elements: str = ""
    
    # Stats
    size: str = ""
    rarity: str = ""
    health: str = ""
    food: str = ""
    melee_attack: str = ""
    attack: str = ""
    defense: str = ""
    work_speed: str = ""
    support: str = ""
    capture_rate_correct: str = ""
    male_probability: str = ""
    combi_rank: str = ""
    gold_coin: str = ""
    egg: str = ""
    code: str = ""
    
    # Movement
    slow_walk_speed: str = ""
    walk_speed: str = ""
    run_speed: str = ""
    ride_sprint_speed: str = ""
    transport_speed: str = ""
    
    # Level 60 스탯
    health_lv60: str = ""
    attack_lv60: str = ""
    defense_lv60: str = ""
    
    # Partner Skill 상세
    partner_skill_name: str = ""
    partner_skill_describe: str = ""
    partner_skill_level: str = ""
    partner_skill_items: str = ""
    partner_skill_item_quantity: str = ""
    partner_skill_item_probability: str = ""
    partner_skill_need_item: str = ""
    partner_skill_need_item_tech_level: str = ""
    
    # Active Skills 상세 (JSON 문자열로 저장)
    active_skills_detailed: str = ""
    
    # Passive Skills
    passive_skills: str = ""
    
    # Possible Drops 상세
    possible_drops_detailed: str = ""
    
    # Tribes
    tribes: str = ""
    
    # Spawner
    spawner: str = ""
    
    # Work (기존 데이터 유지)
    work1: str = ""
    work2: str = ""
    work3: str = ""
    
    # 기타
    image_file: str = ""

class BatchFirecrawlProcessor:
    """Firecrawl MCP를 사용한 전체 팰 데이터 배치 크롤링 및 처리 클래스"""
    
    def __init__(self, input_csv_path: str, output_csv_path: str):
        self.input_csv_path = input_csv_path
        self.output_csv_path = output_csv_path
        self.base_url = "https://paldb.cc/ko/"
        self.processed_pals = []
        self.failed_pals = []
        self.success_count = 0
        self.error_count = 0
        
        # 로깅 설정
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('batch_firecrawl_processing.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def load_existing_pal_data(self) -> List[Dict]:
        """기존 CSV 파일에서 팰 데이터 로드"""
        try:
            df = pd.read_csv(self.input_csv_path)
            return df.to_dict('records')
        except Exception as e:
            self.logger.error(f"CSV 파일 로드 실패: {e}")
            return []
    
    def extract_pal_details_from_markdown(self, markdown_content: str) -> Dict[str, str]:
        """마크다운 콘텐츠에서 팰 상세 정보 추출"""
        details = {}
        
        try:
            # Stats 섹션 추출 - 다양한 패턴으로 시도
            stats_patterns = {
                'size': [r'크기[:\s]*([^\n]+)', r'Size[:\s]*([^\n]+)', r'사이즈[:\s]*([^\n]+)'],
                'rarity': [r'레어도[:\s]*([^\n]+)', r'Rarity[:\s]*([^\n]+)', r'등급[:\s]*([^\n]+)'],
                'health': [r'체력[:\s]*(\d+)', r'Health[:\s]*(\d+)', r'HP[:\s]*(\d+)'],
                'food': [r'식료량[:\s]*(\d+)', r'Food[:\s]*(\d+)', r'먹이[:\s]*(\d+)'],
                'melee_attack': [r'근접\s*공격[:\s]*(\d+)', r'Melee\s*Attack[:\s]*(\d+)', r'격투[:\s]*(\d+)'],
                'attack': [r'원거리\s*공격[:\s]*(\d+)', r'Attack[:\s]*(\d+)', r'공격력[:\s]*(\d+)'],
                'defense': [r'방어력[:\s]*(\d+)', r'Defense[:\s]*(\d+)', r'방어[:\s]*(\d+)'],
                'work_speed': [r'작업\s*속도[:\s]*(\d+)', r'Work\s*Speed[:\s]*(\d+)', r'작업력[:\s]*(\d+)'],
                'support': [r'서포트[:\s]*(\d+)', r'Support[:\s]*(\d+)', r'지원[:\s]*(\d+)'],
                'capture_rate_correct': [r'포획율[:\s]*([^\n]+)', r'Capture\s*Rate[:\s]*([^\n]+)', r'포획[:\s]*([^\n]+)'],
                'male_probability': [r'수컷\s*확률[:\s]*([^\n]+)', r'Male\s*Probability[:\s]*([^\n]+)', r'♂[:\s]*([^\n]+)'],
                'combi_rank': [r'조합\s*랭크[:\s]*([^\n]+)', r'Combi\s*Rank[:\s]*([^\n]+)', r'브리딩[:\s]*([^\n]+)'],
                'gold_coin': [r'금화[:\s]*(\d+)', r'Gold[:\s]*(\d+)', r'골드[:\s]*(\d+)'],
                'egg': [r'알[:\s]*([^\n]+)', r'Egg[:\s]*([^\n]+)', r'타마고[:\s]*([^\n]+)'],
                'code': [r'코드[:\s]*([^\n]+)', r'Code[:\s]*([^\n]+)', r'ID[:\s]*([^\n]+)']
            }
            
            for key, patterns in stats_patterns.items():
                for pattern in patterns:
                    match = re.search(pattern, markdown_content, re.IGNORECASE)
                    if match:
                        details[key] = match.group(1).strip()
                        break
            
            # Movement 섹션 추출
            movement_patterns = {
                'slow_walk_speed': [r'천천히\s*걷기[:\s]*(\d+)', r'Slow\s*Walk[:\s]*(\d+)', r'느린\s*이동[:\s]*(\d+)'],
                'walk_speed': [r'걷기[:\s]*(\d+)', r'Walk[:\s]*(\d+)', r'보행[:\s]*(\d+)'],
                'run_speed': [r'달리기[:\s]*(\d+)', r'Run[:\s]*(\d+)', r'러닝[:\s]*(\d+)'],
                'ride_sprint_speed': [r'라이딩\s*질주\s*속도[:\s]*(\d+)', r'Ride\s*Sprint[:\s]*(\d+)', r'승마\s*질주[:\s]*(\d+)'],
                'transport_speed': [r'운반\s*속도[:\s]*(\d+)', r'Transport[:\s]*(\d+)', r'운송[:\s]*(\d+)']
            }
            
            for key, patterns in movement_patterns.items():
                for pattern in patterns:
                    match = re.search(pattern, markdown_content, re.IGNORECASE)
                    if match:
                        details[key] = match.group(1).strip()
                        break
            
            # Level 60 스탯 추출
            lv60_patterns = {
                'health_lv60': [r'레벨\s*60.*?체력[:\s]*(\d+)', r'Level\s*60.*?Health[:\s]*(\d+)', r'Lv\.?\s*60.*?HP[:\s]*(\d+)'],
                'attack_lv60': [r'레벨\s*60.*?공격[:\s]*(\d+)', r'Level\s*60.*?Attack[:\s]*(\d+)', r'Lv\.?\s*60.*?ATK[:\s]*(\d+)'],
                'defense_lv60': [r'레벨\s*60.*?방어[:\s]*(\d+)', r'Level\s*60.*?Defense[:\s]*(\d+)', r'Lv\.?\s*60.*?DEF[:\s]*(\d+)']
            }
            
            for key, patterns in lv60_patterns.items():
                for pattern in patterns:
                    match = re.search(pattern, markdown_content, re.IGNORECASE | re.DOTALL)
                    if match:
                        details[key] = match.group(1).strip()
                        break
            
            # 파트너 스킬 상세 정보 추출
            partner_skill_patterns = [
                r'파트너\s*스킬[:\s]*([^\n]+)',
                r'Partner\s*Skill[:\s]*([^\n]+)',
                r'동료\s*스킬[:\s]*([^\n]+)'
            ]
            
            for pattern in partner_skill_patterns:
                match = re.search(pattern, markdown_content, re.IGNORECASE)
                if match:
                    details['partner_skill_name'] = match.group(1).strip()
                    break
            
            # 파트너 스킬 설명 추출
            partner_desc_patterns = [
                r'파트너\s*스킬.*?설명[:\s]*([^\n]+)',
                r'Partner\s*Skill.*?Description[:\s]*([^\n]+)',
                r'스킬\s*효과[:\s]*([^\n]+)'
            ]
            
            for pattern in partner_desc_patterns:
                match = re.search(pattern, markdown_content, re.IGNORECASE | re.DOTALL)
                if match:
                    details['partner_skill_describe'] = match.group(1).strip()
                    break
            
            # 액티브 스킬 목록 추출
            active_skills = []
            skill_patterns = [
                r'(?:액티브\s*스킬|Active\s*Skills?|기술)[:\s]*([^\n]+(?:\n[^\n#]+)*)',
                r'공격\s*스킬[:\s]*([^\n]+(?:\n[^\n#]+)*)',
                r'특수\s*공격[:\s]*([^\n]+(?:\n[^\n#]+)*)'
            ]
            
            for pattern in skill_patterns:
                skill_matches = re.findall(pattern, markdown_content, re.IGNORECASE)
                for skill_text in skill_matches:
                    # 각 스킬의 상세 정보 파싱
                    skill_lines = skill_text.strip().split('\n')
                    for line in skill_lines:
                        if line.strip() and not line.strip().startswith('#'):
                            active_skills.append(line.strip())
            
            if active_skills:
                details['active_skills_detailed'] = json.dumps(active_skills, ensure_ascii=False)
            
            # 패시브 스킬 추출
            passive_patterns = [
                r'패시브\s*스킬[:\s]*([^\n]+)',
                r'Passive\s*Skills?[:\s]*([^\n]+)',
                r'특성[:\s]*([^\n]+)'
            ]
            
            for pattern in passive_patterns:
                match = re.search(pattern, markdown_content, re.IGNORECASE)
                if match:
                    details['passive_skills'] = match.group(1).strip()
                    break
            
            # 드롭 아이템 추출
            drops_patterns = [
                r'드롭[:\s]*([^\n]+(?:\n[^\n#]+)*)',
                r'Drop[:\s]*([^\n]+(?:\n[^\n#]+)*)',
                r'아이템\s*드롭[:\s]*([^\n]+(?:\n[^\n#]+)*)'
            ]
            
            for pattern in drops_patterns:
                drops_match = re.search(pattern, markdown_content, re.IGNORECASE)
                if drops_match:
                    details['possible_drops_detailed'] = drops_match.group(1).strip()
                    break
            
            # Tribes 정보 추출
            tribes_patterns = [
                r'부족[:\s]*([^\n]+)',
                r'Tribes?[:\s]*([^\n]+)',
                r'종족[:\s]*([^\n]+)'
            ]
            
            for pattern in tribes_patterns:
                tribes_match = re.search(pattern, markdown_content, re.IGNORECASE)
                if tribes_match:
                    details['tribes'] = tribes_match.group(1).strip()
                    break
            
            # Spawner 정보 추출
            spawner_patterns = [
                r'스포너[:\s]*([^\n]+)',
                r'Spawner[:\s]*([^\n]+)',
                r'출현\s*위치[:\s]*([^\n]+)'
            ]
            
            for pattern in spawner_patterns:
                spawner_match = re.search(pattern, markdown_content, re.IGNORECASE)
                if spawner_match:
                    details['spawner'] = spawner_match.group(1).strip()
                    break
        
        except Exception as e:
            self.logger.error(f"마크다운 파싱 오류: {e}")
        
        return details
    
    def create_enhanced_pal_data(self, original_pal: Dict, crawled_details: Dict[str, str]) -> PalDetailedData:
        """원본 팰 데이터와 크롤링된 상세 정보를 결합하여 확장된 팰 데이터 생성"""
        
        # 기본 정보는 원본 데이터에서 가져옴
        enhanced_data = PalDetailedData(
            id=str(original_pal.get('id', '')),
            name_kor=original_pal.get('name', ''),
            pal_nick_kor='',  # 별명은 별도로 추출 필요
            description_kor=original_pal.get('description', ''),
            elements=f"{original_pal.get('type1', '')},{original_pal.get('type2', '')}".strip(','),
            
            # 기존 스탯 정보 (원본에서) - 크롤링된 정보가 있으면 우선
            health=crawled_details.get('health', str(original_pal.get('hp', ''))),
            attack=crawled_details.get('attack', str(original_pal.get('attack', ''))),
            defense=crawled_details.get('defense', str(original_pal.get('defense', ''))),
            rarity=crawled_details.get('rarity', str(original_pal.get('rarity', ''))),
            size=crawled_details.get('size', str(original_pal.get('size', ''))),
            food=crawled_details.get('food', str(original_pal.get('foodAmount', ''))),
            
            # Work 정보
            work1=original_pal.get('work1', ''),
            work2=original_pal.get('work2', ''),
            work3=original_pal.get('work3', ''),
            
            # 이미지 파일
            image_file=original_pal.get('imageFile', ''),
            
            # 크롤링된 상세 정보로 업데이트
            **{k: v for k, v in crawled_details.items() if k not in ['health', 'attack', 'defense', 'rarity', 'size', 'food']}
        )
        
        return enhanced_data
    
    def save_to_csv(self):
        """처리된 데이터를 CSV로 저장"""
        if not self.processed_pals:
            self.logger.warning("저장할 데이터가 없습니다.")
            return
        
        try:
            # 데이터프레임으로 변환
            data_dicts = [asdict(pal) for pal in self.processed_pals]
            df = pd.DataFrame(data_dicts)
            
            # CSV 저장
            df.to_csv(self.output_csv_path, index=False, encoding='utf-8-sig')
            self.logger.info(f"데이터 저장 완료: {self.output_csv_path}")
            
            # 실패 목록도 별도 저장
            if self.failed_pals:
                failed_df = pd.DataFrame(self.failed_pals)
                failed_path = self.output_csv_path.replace('.csv', '_failed.csv')
                failed_df.to_csv(failed_path, index=False, encoding='utf-8-sig')
                self.logger.info(f"실패 목록 저장: {failed_path}")
                
        except Exception as e:
            self.logger.error(f"CSV 저장 실패: {e}")
    
    def generate_processing_report(self):
        """처리 결과 리포트 생성"""
        total_processed = len(self.processed_pals)
        total_failed = len(self.failed_pals)
        total_attempts = total_processed + total_failed
        
        success_rate = (total_processed / total_attempts * 100) if total_attempts > 0 else 0
        
        report = f"""
=== 팰 데이터 확장 크롤링 결과 리포트 ===

총 처리 시도: {total_attempts}
성공: {total_processed} ({success_rate:.1f}%)
실패: {total_failed}

생성된 파일:
- 메인 데이터: {self.output_csv_path}
"""
        
        if self.failed_pals:
            report += f"- 실패 목록: {self.output_csv_path.replace('.csv', '_failed.csv')}\n"
            report += "\n실패한 팰들:\n"
            for failed in self.failed_pals[:10]:  # 처음 10개만 표시
                report += f"  - ID {failed['id']}: {failed['name']} ({failed['error']})\n"
            if len(self.failed_pals) > 10:
                report += f"  ... 및 {len(self.failed_pals) - 10}개 더\n"
        
        print(report)
        
        # 리포트 파일로도 저장
        report_path = self.output_csv_path.replace('.csv', '_report.txt')
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)

# 이 스크립트는 실제 MCP firecrawl 호출을 위해 사용될 템플릿입니다
def show_usage():
    """사용법 안내"""
    print("=== 팰 데이터 확장 크롤링 스크립트 ===")
    print()
    print("이 스크립트는 firecrawl MCP를 사용하여 214개 팰의 상세 정보를 크롤링합니다.")
    print()
    print("실행 전 준비사항:")
    print("1. perfect_complete_pal_database_214.csv 파일이 있어야 합니다")
    print("2. firecrawl MCP 도구가 연결되어 있어야 합니다")
    print("3. 인터넷 연결이 안정적이어야 합니다")
    print()
    print("예상 소요 시간: 약 5-10분 (214개 팰, 배치 크기 5, 1초 지연)")
    print()
    print("실제 실행을 위해서는 이 템플릿을 기반으로")
    print("MCP firecrawl 호출 부분을 구현해야 합니다.")

if __name__ == "__main__":
    show_usage() 