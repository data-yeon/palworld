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

# Firecrawl MCP 도구 가정 (실제 환경에서는 MCP 연결 사용)
# 여기서는 시뮬레이션을 위한 플레이스홀더 함수들

def simulate_firecrawl_scrape(url: str) -> Dict[str, Any]:
    """
    Firecrawl MCP를 시뮬레이션하는 함수
    실제로는 mcp_firecrawl-mcp_firecrawl_scrape를 사용해야 함
    """
    return {
        "markdown": f"# Simulated content for {url}\n\n이것은 시뮬레이션된 콘텐츠입니다.",
        "success": True
    }

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

class EnhancedFirecrawlPalBatchProcessor:
    """전체 팰 데이터 배치 크롤링 및 처리 클래스"""
    
    def __init__(self, input_csv_path: str, output_csv_path: str):
        self.input_csv_path = input_csv_path
        self.output_csv_path = output_csv_path
        self.base_url = "https://paldb.cc/ko/"
        self.processed_pals = []
        self.failed_pals = []
        
        # 로깅 설정
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('enhanced_pal_batch_processing.log'),
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
            # Stats 섹션 추출
            stats_patterns = {
                'size': r'크기[:\s]*([^\n]+)',
                'rarity': r'레어도[:\s]*([^\n]+)',
                'health': r'체력[:\s]*(\d+)',
                'food': r'식료량[:\s]*(\d+)',
                'melee_attack': r'근접공격[:\s]*(\d+)',
                'attack': r'원거리공격[:\s]*(\d+)',
                'defense': r'방어력[:\s]*(\d+)',
                'work_speed': r'작업속도[:\s]*(\d+)',
                'support': r'서포트[:\s]*(\d+)',
                'capture_rate_correct': r'포획율[:\s]*([^\n]+)',
                'male_probability': r'수컷확률[:\s]*([^\n]+)',
                'combi_rank': r'조합랭크[:\s]*([^\n]+)',
                'gold_coin': r'금화[:\s]*(\d+)',
                'egg': r'알[:\s]*([^\n]+)',
                'code': r'코드[:\s]*([^\n]+)'
            }
            
            for key, pattern in stats_patterns.items():
                match = re.search(pattern, markdown_content, re.IGNORECASE)
                if match:
                    details[key] = match.group(1).strip()
            
            # Movement 섹션 추출
            movement_patterns = {
                'slow_walk_speed': r'천천히걷기[:\s]*(\d+)',
                'walk_speed': r'걷기[:\s]*(\d+)',
                'run_speed': r'달리기[:\s]*(\d+)',
                'ride_sprint_speed': r'라이딩질주속도[:\s]*(\d+)',
                'transport_speed': r'운반속도[:\s]*(\d+)'
            }
            
            for key, pattern in movement_patterns.items():
                match = re.search(pattern, markdown_content, re.IGNORECASE)
                if match:
                    details[key] = match.group(1).strip()
            
            # Level 60 스탯 추출
            lv60_patterns = {
                'health_lv60': r'레벨\s*60.*?체력[:\s]*(\d+)',
                'attack_lv60': r'레벨\s*60.*?공격[:\s]*(\d+)',
                'defense_lv60': r'레벨\s*60.*?방어[:\s]*(\d+)'
            }
            
            for key, pattern in lv60_patterns.items():
                match = re.search(pattern, markdown_content, re.IGNORECASE | re.DOTALL)
                if match:
                    details[key] = match.group(1).strip()
            
            # 파트너 스킬 상세 정보 추출
            partner_skill_match = re.search(r'파트너\s*스킬[:\s]*([^\n]+)', markdown_content, re.IGNORECASE)
            if partner_skill_match:
                details['partner_skill_name'] = partner_skill_match.group(1).strip()
            
            # 파트너 스킬 설명 추출
            partner_desc_match = re.search(r'파트너\s*스킬.*?설명[:\s]*([^\n]+)', markdown_content, re.IGNORECASE | re.DOTALL)
            if partner_desc_match:
                details['partner_skill_describe'] = partner_desc_match.group(1).strip()
            
            # 액티브 스킬 목록 추출
            active_skills = []
            skill_pattern = r'(?:액티브\s*스킬|기술)[:\s]*([^\n]+(?:\n[^\n#]+)*)'
            skill_matches = re.findall(skill_pattern, markdown_content, re.IGNORECASE)
            
            for skill_text in skill_matches:
                # 각 스킬의 상세 정보 파싱
                skill_lines = skill_text.strip().split('\n')
                for line in skill_lines:
                    if line.strip():
                        active_skills.append(line.strip())
            
            if active_skills:
                details['active_skills_detailed'] = json.dumps(active_skills, ensure_ascii=False)
            
            # 패시브 스킬 추출
            passive_match = re.search(r'패시브\s*스킬[:\s]*([^\n]+)', markdown_content, re.IGNORECASE)
            if passive_match:
                details['passive_skills'] = passive_match.group(1).strip()
            
            # 드롭 아이템 추출
            drops_pattern = r'드롭[:\s]*([^\n]+(?:\n[^\n#]+)*)'
            drops_match = re.search(drops_pattern, markdown_content, re.IGNORECASE)
            if drops_match:
                details['possible_drops_detailed'] = drops_match.group(1).strip()
            
            # Tribes 정보 추출
            tribes_match = re.search(r'부족[:\s]*([^\n]+)', markdown_content, re.IGNORECASE)
            if tribes_match:
                details['tribes'] = tribes_match.group(1).strip()
            
            # Spawner 정보 추출
            spawner_match = re.search(r'스포너[:\s]*([^\n]+)', markdown_content, re.IGNORECASE)
            if spawner_match:
                details['spawner'] = spawner_match.group(1).strip()
        
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
            
            # 기존 스탯 정보 (원본에서)
            health=str(original_pal.get('hp', '')),
            attack=str(original_pal.get('attack', '')),
            defense=str(original_pal.get('defense', '')),
            rarity=str(original_pal.get('rarity', '')),
            size=original_pal.get('size', ''),
            food=str(original_pal.get('foodAmount', '')),
            
            # Work 정보
            work1=original_pal.get('work1', ''),
            work2=original_pal.get('work2', ''),
            work3=original_pal.get('work3', ''),
            
            # 이미지 파일
            image_file=original_pal.get('imageFile', ''),
            
            # 크롤링된 상세 정보로 업데이트
            **crawled_details
        )
        
        return enhanced_data
    
    async def process_single_pal(self, pal_data: Dict) -> Optional[PalDetailedData]:
        """단일 팰 처리"""
        english_name = pal_data.get('englishName', '')
        pal_id = pal_data.get('id', '')
        pal_name = pal_data.get('name', '')
        
        if not english_name:
            self.logger.warning(f"팰 ID {pal_id} ({pal_name})의 영어 이름이 없습니다.")
            return None
        
        try:
            # URL 구성
            url = f"{self.base_url}{english_name}"
            self.logger.info(f"크롤링 시작: {pal_name} ({english_name}) - {url}")
            
            # Firecrawl로 크롤링 (실제 환경에서는 MCP 호출)
            result = simulate_firecrawl_scrape(url)
            
            if not result.get('success', False):
                self.logger.error(f"크롤링 실패: {pal_name} - {url}")
                self.failed_pals.append({'id': pal_id, 'name': pal_name, 'error': 'crawl_failed'})
                return None
            
            # 마크다운에서 상세 정보 추출
            markdown_content = result.get('markdown', '')
            crawled_details = self.extract_pal_details_from_markdown(markdown_content)
            
            # 확장된 팰 데이터 생성
            enhanced_pal = self.create_enhanced_pal_data(pal_data, crawled_details)
            
            self.logger.info(f"크롤링 완료: {pal_name}")
            return enhanced_pal
            
        except Exception as e:
            self.logger.error(f"팰 처리 오류 {pal_name}: {e}")
            self.failed_pals.append({'id': pal_id, 'name': pal_name, 'error': str(e)})
            return None
    
    async def process_all_pals(self, batch_size: int = 5, delay: float = 1.0):
        """모든 팰을 배치로 처리"""
        # 기존 팰 데이터 로드
        original_pals = self.load_existing_pal_data()
        total_pals = len(original_pals)
        
        self.logger.info(f"총 {total_pals}개 팰 처리 시작")
        
        # 배치 단위로 처리
        for i in range(0, total_pals, batch_size):
            batch = original_pals[i:i+batch_size]
            batch_number = (i // batch_size) + 1
            total_batches = (total_pals + batch_size - 1) // batch_size
            
            self.logger.info(f"배치 {batch_number}/{total_batches} 처리 중...")
            
            # 배치 내 각 팰 처리
            batch_tasks = []
            for pal_data in batch:
                task = self.process_single_pal(pal_data)
                batch_tasks.append(task)
            
            # 배치 실행
            batch_results = await asyncio.gather(*batch_tasks, return_exceptions=True)
            
            # 결과 수집
            for result in batch_results:
                if isinstance(result, PalDetailedData):
                    self.processed_pals.append(result)
                elif isinstance(result, Exception):
                    self.logger.error(f"배치 처리 중 예외: {result}")
            
            # 지연
            if i + batch_size < total_pals:  # 마지막 배치가 아니면
                self.logger.info(f"다음 배치까지 {delay}초 대기...")
                await asyncio.sleep(delay)
        
        self.logger.info(f"전체 처리 완료: 성공 {len(self.processed_pals)}개, 실패 {len(self.failed_pals)}개")
    
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

async def main():
    """메인 실행 함수"""
    # 입력/출력 파일 경로
    input_csv = "perfect_complete_pal_database_214.csv"
    output_csv = "enhanced_complete_pal_database_214_detailed.csv"
    
    # 배치 프로세서 생성
    processor = EnhancedFirecrawlPalBatchProcessor(input_csv, output_csv)
    
    print("=== 팰 데이터 확장 크롤링 시작 ===")
    print(f"입력 파일: {input_csv}")
    print(f"출력 파일: {output_csv}")
    print("배치 크기: 5개씩")
    print("배치 간 지연: 1초")
    print()
    
    # 전체 팰 처리
    await processor.process_all_pals(batch_size=5, delay=1.0)
    
    # 결과 저장
    processor.save_to_csv()
    
    # 리포트 생성
    processor.generate_processing_report()

if __name__ == "__main__":
    # 실행
    asyncio.run(main()) 