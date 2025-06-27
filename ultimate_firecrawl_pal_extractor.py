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
    
    # Partner Skill
    partner_skill_name: str
    partner_skill_describe: str
    partner_skill_level: str
    partner_skill_items: List[str]
    partner_skill_item_quantity: List[int]
    partner_skill_item_probability: List[float]
    partner_skill_need_item: str
    partner_skill_need_item_tech_level: int
    
    # Active Skills
    active_skills: List[Dict[str, Any]]
    
    # Passive Skills
    passive_skills: List[str]
    
    # Possible Drops
    possible_drops: List[Dict[str, Any]]
    
    # Tribes
    tribes: List[str]
    
    # Spawner
    spawner_info: List[Dict[str, Any]]
    
    # 원본 데이터
    original_english_name: str
    original_csv_data: Dict[str, Any]
    crawled_content: str
    crawl_timestamp: str

class UltimateFirecrawlPalExtractor:
    """팰월드 팰 데이터 완전 추출 시스템"""
    
    def __init__(self):
        self.results = []
        self.failed_pals = []
        self.progress_log = []
        
    def load_pal_list(self, csv_file: str = "perfect_complete_pal_database_214.csv") -> List[Dict]:
        """CSV에서 크롤링 가능한 팰 리스트 로드"""
        df = pd.read_csv(csv_file)
        
        # 영어명이 있는 팰들만 필터링
        has_english_name = df['englishName'].notna() & (df['englishName'] != '')
        crawlable_pals = df[has_english_name].to_dict('records')
        
        print(f"총 {len(crawlable_pals)}개 팰이 크롤링 대상입니다.")
        return crawlable_pals
    
    def extract_pal_data_from_markdown(self, content: str, pal_info: Dict) -> CompletePalData:
        """마크다운 콘텐츠에서 팰 데이터 추출"""
        
        # 기본값으로 CompletePalData 초기화
        pal_data = CompletePalData(
            id=str(pal_info.get('id', '')),
            name_kor=pal_info.get('name', ''),
            pal_nick_kor='',  # 크롤링에서 추출
            description_kor=pal_info.get('description', ''),
            elements=[],  # 크롤링에서 추출
            
            # Stats (기본값)
            size=pal_info.get('size', ''),
            rarity=int(pal_info.get('rarity', 0)),
            health=int(pal_info.get('hp', 0)),
            food=int(pal_info.get('foodAmount', 0)),
            melee_attack=0,
            attack=int(pal_info.get('attack', 0)),
            defense=int(pal_info.get('defense', 0)),
            work_speed=100,
            support=100,
            capture_rate_correct=1.0,
            male_probability=50,
            combi_rank=0,
            gold_coin=0,
            egg=pal_info.get('eggType', ''),
            code='',
            
            # Movement (기본값)
            slow_walk_speed=0,
            walk_speed=0,
            run_speed=0,
            ride_sprint_speed=0,
            transport_speed=0,
            
            # Level 60 스탯
            level_60_health_min=0,
            level_60_health_max=0,
            level_60_attack_min=0,
            level_60_attack_max=0,
            level_60_defense_min=0,
            level_60_defense_max=0,
            
            # Partner Skill
            partner_skill_name='',
            partner_skill_describe='',
            partner_skill_level='',
            partner_skill_items=[],
            partner_skill_item_quantity=[],
            partner_skill_item_probability=[],
            partner_skill_need_item='',
            partner_skill_need_item_tech_level=0,
            
            # 리스트 필드들
            active_skills=[],
            passive_skills=[],
            possible_drops=[],
            tribes=[],
            spawner_info=[],
            
            # 메타데이터
            original_english_name=pal_info.get('englishName', ''),
            original_csv_data=pal_info,
            crawled_content=content,
            crawl_timestamp=datetime.now().isoformat()
        )
        
        # 마크다운에서 데이터 추출
        try:
            # Stats 섹션 추출
            stats_match = re.search(r'## Stats\s*\n(.*?)\n## ', content, re.DOTALL)
            if stats_match:
                stats_content = stats_match.group(1)
                
                # Size 추출
                size_match = re.search(r'Size:\s*([^\n]+)', stats_content)
                if size_match:
                    pal_data.size = size_match.group(1).strip()
                
                # Rarity 추출
                rarity_match = re.search(r'Rarity:\s*(\d+)', stats_content)
                if rarity_match:
                    pal_data.rarity = int(rarity_match.group(1))
                
                # HP 추출
                hp_match = re.search(r'HP:\s*(\d+)', stats_content)
                if hp_match:
                    pal_data.health = int(hp_match.group(1))
                
                # 기타 stats 추출
                melee_match = re.search(r'MeleeAttack:\s*(\d+)', stats_content)
                if melee_match:
                    pal_data.melee_attack = int(melee_match.group(1))
                
                # Male Probability 추출
                male_prob_match = re.search(r'MaleProbability:\s*(\d+)', stats_content)
                if male_prob_match:
                    pal_data.male_probability = int(male_prob_match.group(1))
                
                # CombiRank 추출
                combi_match = re.search(r'CombiRank:\s*(\d+)', stats_content)
                if combi_match:
                    pal_data.combi_rank = int(combi_match.group(1))
            
            # Movement 섹션 추출
            movement_match = re.search(r'## Movement\s*\n(.*?)\n## ', content, re.DOTALL)
            if movement_match:
                movement_content = movement_match.group(1)
                
                # 각 속도 값 추출
                slow_walk_match = re.search(r'SlowWalkSpeed:\s*(\d+)', movement_content)
                if slow_walk_match:
                    pal_data.slow_walk_speed = int(slow_walk_match.group(1))
                
                walk_match = re.search(r'WalkSpeed:\s*(\d+)', movement_content)
                if walk_match:
                    pal_data.walk_speed = int(walk_match.group(1))
                
                run_match = re.search(r'RunSpeed:\s*(\d+)', movement_content)
                if run_match:
                    pal_data.run_speed = int(run_match.group(1))
            
            # Partner Skill 추출
            partner_skill_match = re.search(r'## Partner Skill\s*\n(.*?)\n## ', content, re.DOTALL)
            if partner_skill_match:
                partner_content = partner_skill_match.group(1)
                
                # 파트너 스킬명 추출
                skill_name_match = re.search(r'Name:\s*([^\n]+)', partner_content)
                if skill_name_match:
                    pal_data.partner_skill_name = skill_name_match.group(1).strip()
                
                # 설명 추출
                desc_match = re.search(r'Describe:\s*([^\n]+)', partner_content)
                if desc_match:
                    pal_data.partner_skill_describe = desc_match.group(1).strip()
            
            # Active Skills 추출
            active_skills_match = re.search(r'## Active Skills\s*\n(.*?)\n## ', content, re.DOTALL)
            if active_skills_match:
                skills_content = active_skills_match.group(1)
                
                # 각 스킬을 개별적으로 파싱
                skills = []
                skill_entries = re.findall(r'- ([^:]+):\s*([^\n]+)', skills_content)
                for skill_name, skill_desc in skill_entries:
                    skills.append({
                        'name': skill_name.strip(),
                        'description': skill_desc.strip()
                    })
                pal_data.active_skills = skills
            
            # Possible Drops 추출
            drops_match = re.search(r'## Possible Drops\s*\n(.*?)\n## ', content, re.DOTALL)
            if drops_match:
                drops_content = drops_match.group(1)
                
                drops = []
                drop_entries = re.findall(r'- ([^(]+)\(([^)]+)\)', drops_content)
                for item_name, drop_info in drop_entries:
                    drops.append({
                        'item': item_name.strip(),
                        'info': drop_info.strip()
                    })
                pal_data.possible_drops = drops
                
        except Exception as e:
            print(f"데이터 추출 중 오류 발생: {e}")
        
        return pal_data
    
    def crawl_single_pal(self, pal_info: Dict) -> Optional[CompletePalData]:
        """단일 팰 크롤링"""
        english_name = pal_info.get('englishName', '')
        pal_id = pal_info.get('id', '')
        
        # B 변형 팰의 경우 베이스명 사용
        base_name = english_name
        if '_' in english_name:
            variant_pattern = r'(.+)_(Ice|Fire|Electric|Aqua|Dark|Noct|Terra|Cryst|Lux|Ignis|Gild|Primo|Botan)$'
            match = re.match(variant_pattern, english_name)
            if match:
                base_name = match.group(1)
                print(f"B 변형 팰 감지: {english_name} -> 베이스명: {base_name}")
        
        url = f"https://paldb.cc/ko/{base_name}"
        
        try:
            print(f"[{pal_id}] {pal_info.get('name', '')} ({english_name}) 크롤링 중...")
            
            # 여기서 실제 MCP firecrawl을 사용해야 함
            # 시뮬레이션용 더미 데이터
            dummy_content = f"""
            # {base_name}
            
            ## Stats
            Size: {pal_info.get('size', 'M')}
            Rarity: {pal_info.get('rarity', 1)}
            HP: {pal_info.get('hp', 100)}
            MeleeAttack: {pal_info.get('attack', 100)}
            MaleProbability: 50
            CombiRank: 1000
            
            ## Movement
            SlowWalkSpeed: 20
            WalkSpeed: 40
            RunSpeed: 400
            
            ## Partner Skill
            Name: {pal_info.get('partnerSkill', '기본 스킬')}
            Describe: 파트너 스킬 설명
            
            ## Active Skills
            - 기본 공격: 기본적인 공격 스킬
            - 특수 기술: 특별한 기술
            
            ## Possible Drops
            - 가죽(1-2개, 80%)
            - 뼈(1개, 60%)
            
            ## Tribes
            - 일반 개체
            
            ## Spawner
            - 초원 지역 (레벨 1-10)
            """
            
            # 데이터 추출
            extracted_data = self.extract_pal_data_from_markdown(dummy_content, pal_info)
            
            self.progress_log.append({
                'id': pal_id,
                'name': pal_info.get('name', ''),
                'english_name': english_name,
                'status': 'success',
                'timestamp': datetime.now().isoformat()
            })
            
            return extracted_data
            
        except Exception as e:
            print(f"크롤링 실패: {pal_id} - {e}")
            self.failed_pals.append({
                'id': pal_id,
                'name': pal_info.get('name', ''),
                'english_name': english_name,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            })
            return None
    
    def process_all_pals(self, batch_size: int = 5, delay_seconds: int = 1):
        """모든 팰을 배치로 처리"""
        pals = self.load_pal_list()
        total_pals = len(pals)
        
        print(f"총 {total_pals}개 팰 처리 시작 (배치 크기: {batch_size}, 지연: {delay_seconds}초)")
        
        for i in range(0, total_pals, batch_size):
            batch = pals[i:i + batch_size]
            batch_num = (i // batch_size) + 1
            total_batches = (total_pals + batch_size - 1) // batch_size
            
            print(f"\n=== 배치 {batch_num}/{total_batches} 처리 중 ===")
            
            for pal in batch:
                result = self.crawl_single_pal(pal)
                if result:
                    self.results.append(result)
                
                # 요청 간 지연
                time.sleep(delay_seconds)
            
            # 배치 간 지연
            if i + batch_size < total_pals:
                print(f"배치 {batch_num} 완료. {delay_seconds*2}초 대기 중...")
                time.sleep(delay_seconds * 2)
            
            # 중간 저장
            if batch_num % 10 == 0:
                self.save_progress(f"intermediate_batch_{batch_num}")
        
        print(f"\n전체 처리 완료!")
        print(f"성공: {len(self.results)}개, 실패: {len(self.failed_pals)}개")
        
        # 최종 결과 저장
        self.save_final_results()
    
    def save_progress(self, filename_prefix: str):
        """진행 상황 저장"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # 성공한 결과들 저장
        results_file = f"{filename_prefix}_results_{timestamp}.json"
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump([asdict(result) for result in self.results], f, ensure_ascii=False, indent=2)
        
        # 실패 목록 저장
        failed_file = f"{filename_prefix}_failed_{timestamp}.json"
        with open(failed_file, 'w', encoding='utf-8') as f:
            json.dump(self.failed_pals, f, ensure_ascii=False, indent=2)
        
        print(f"진행 상황 저장: {results_file}, {failed_file}")
    
    def save_final_results(self):
        """최종 결과 저장"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # CSV 형태로 변환하여 저장
        if self.results:
            # 기본 필드들만 추출하여 CSV로 저장
            csv_data = []
            for result in self.results:
                csv_row = {
                    'id': result.id,
                    'name_kor': result.name_kor,
                    'pal_nick_kor': result.pal_nick_kor,
                    'description_kor': result.description_kor,
                    'elements': '|'.join(result.elements),
                    'size': result.size,
                    'rarity': result.rarity,
                    'health': result.health,
                    'food': result.food,
                    'attack': result.attack,
                    'defense': result.defense,
                    'partner_skill_name': result.partner_skill_name,
                    'partner_skill_describe': result.partner_skill_describe,
                    'active_skills_count': len(result.active_skills),
                    'possible_drops_count': len(result.possible_drops),
                    'original_english_name': result.original_english_name
                }
                csv_data.append(csv_row)
            
            # CSV 저장
            df = pd.DataFrame(csv_data)
            csv_filename = f"ultimate_pal_database_enhanced_{timestamp}.csv"
            df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
            print(f"CSV 결과 저장: {csv_filename}")
            
            # 완전한 JSON 데이터도 저장
            json_filename = f"ultimate_pal_database_complete_{timestamp}.json"
            with open(json_filename, 'w', encoding='utf-8') as f:
                json.dump([asdict(result) for result in self.results], f, ensure_ascii=False, indent=2)
            print(f"완전한 JSON 결과 저장: {json_filename}")
        
        # 최종 리포트 생성
        self.generate_final_report()
    
    def generate_final_report(self):
        """최종 크롤링 리포트 생성"""
        total_attempted = len(self.results) + len(self.failed_pals)
        success_rate = (len(self.results) / total_attempted * 100) if total_attempted > 0 else 0
        
        report = f"""
# 팰월드 팰 데이터 크롤링 최종 리포트

## 요약
- 총 크롤링 시도: {total_attempted}개
- 성공: {len(self.results)}개
- 실패: {len(self.failed_pals)}개
- 성공률: {success_rate:.2f}%

## 성공한 팰들
"""
        
        for result in self.results[:10]:  # 처음 10개만 표시
            report += f"- [{result.id}] {result.name_kor} ({result.original_english_name})\n"
        
        if len(self.results) > 10:
            report += f"- ... 외 {len(self.results) - 10}개\n"
        
        report += "\n## 실패한 팰들\n"
        for failed in self.failed_pals:
            report += f"- [{failed['id']}] {failed['name']} ({failed['english_name']}) - {failed['error']}\n"
        
        # 리포트 저장
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"crawling_report_{timestamp}.md"
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"최종 리포트 저장: {report_filename}")

def main():
    """메인 실행 함수"""
    print("=== 팰월드 팰 데이터 완전 크롤링 시스템 ===")
    print("주의: 이 스크립트는 시뮬레이션 버전입니다.")
    print("실제 사용시 MCP firecrawl 연동이 필요합니다.\n")
    
    extractor = UltimateFirecrawlPalExtractor()
    
    # 전체 팰 처리 (작은 배치로 테스트)
    extractor.process_all_pals(batch_size=3, delay_seconds=1)

if __name__ == "__main__":
    main() 