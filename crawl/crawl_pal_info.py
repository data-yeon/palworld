import csv
import re
import time
import requests
from typing import List, Dict, Optional
from dataclasses import dataclass
import json

@dataclass
class PalInfo:
    id: str
    nickname: str  # 간략한 수식어
    name: str      # 이름
    description: str  # 자세한 도감설명
    work_skills: Dict[str, int]  # 작업적성
    stats: Dict[str, str]  # 스테이터스
    drops_normal: List[str]  # 일반 드롭 아이템
    drops_boss: List[str]    # 보스 드롭 아이템
    partner_skill: str       # 파트너 스킬
    active_skills: List[Dict[str, str]]  # 공격 스킬

class PalCrawler:
    def __init__(self):
        self.base_url = "https://palworld.shwa.space"
        self.pals_url = f"{self.base_url}/pals"
        
    def get_pal_list(self) -> List[str]:
        """팰 목록을 가져옵니다."""
        print("팰 목록을 가져오는 중...")
        
        # Firecrawl을 사용하여 팰 목록 페이지 맵핑
        from mcp_firecrawl_mcp import FirecrawlMCPServer
        firecrawl = FirecrawlMCPServer()
        
        try:
            # 팰 목록 페이지 맵핑
            map_result = firecrawl.map_website(self.pals_url, limit=200)
            
            # 팰 개별 페이지 URL 추출
            pal_urls = []
            for url in map_result:
                if '/pals/' in url and url != self.pals_url:
                    pal_urls.append(url)
            
            print(f"총 {len(pal_urls)}개의 팰을 찾았습니다.")
            return pal_urls[:10]  # 테스트를 위해 처음 10개만
            
        except Exception as e:
            print(f"팰 목록 가져오기 실패: {e}")
            return []
    
    def parse_pal_info(self, markdown_content: str, pal_url: str) -> PalInfo:
        """마크다운 콘텐츠에서 팰 정보를 파싱합니다."""
        lines = markdown_content.split('\n')
        
        # ID 추출 (URL에서)
        pal_id = pal_url.split('/')[-1]
        
        # 이름과 수식어 추출
        nickname = ""
        name = ""
        description = ""
        
        for i, line in enumerate(lines):
            if line.strip() and not line.startswith('![') and not line.startswith('['):
                if not nickname and line.strip():
                    nickname = line.strip()
                elif not name and line.strip():
                    name = line.strip()
                elif not description and len(line.strip()) > 20:  # 긴 설명문
                    description = line.strip()
                    break
        
        # 스테이터스 파싱
        stats = {}
        in_stats_section = False
        for line in lines:
            if "### 스테이터스" in line:
                in_stats_section = True
                continue
            elif in_stats_section and line.startswith("###"):
                break
            elif in_stats_section and line.strip():
                # 한글과 숫자가 붙어있는 패턴 파싱
                matches = re.findall(r'([가-힣\s]+)(\d+)', line)
                for match in matches:
                    stat_name = match[0].strip()
                    stat_value = match[1]
                    if stat_name:
                        stats[stat_name] = stat_value
        
        # 작업 적성 파싱
        work_skills = {}
        in_work_section = False
        for line in lines:
            if "### 작업 적성" in line:
                in_work_section = True
                continue
            elif in_work_section and line.startswith("###"):
                break
            elif in_work_section and "LV." in line:
                # 작업명과 레벨 추출
                if ")" in line:
                    work_name = line.split(")")[-1].split("LV.")[0].strip()
                    level = line.split("LV.")[-1].strip()
                    if work_name:
                        work_skills[work_name] = int(level) if level.isdigit() else 0
        
        # 드롭 아이템 파싱
        drops_normal = []
        drops_boss = []
        in_drops_section = False
        for i, line in enumerate(lines):
            if "### 드롭하는 아이템" in line:
                in_drops_section = True
                continue
            elif in_drops_section and line.startswith("###"):
                break
            elif in_drops_section and "100%" in line:
                # 아이템명 추출
                item_matches = re.findall(r'([가-힣\s]+)\d+~?\d*100%', line)
                for item in item_matches:
                    drops_normal.append(item.strip())
        
        # 파트너 스킬 파싱
        partner_skill = ""
        in_partner_section = False
        for line in lines:
            if "### 파트너" in line:
                in_partner_section = True
                continue
            elif in_partner_section and line.startswith("###"):
                break
            elif in_partner_section and line.strip() and not line.startswith("!["):
                if not partner_skill:
                    partner_skill = line.strip()
                else:
                    partner_skill += " " + line.strip()
        
        # 액티브 스킬 파싱
        active_skills = []
        in_active_section = False
        for line in lines:
            if "### 액티브" in line:
                in_active_section = True
                continue
            elif in_active_section and line.startswith("###"):
                break
            elif in_active_section and "Lv." in line and "\\\\n\\\\" in line:
                # 스킬 정보 파싱
                parts = line.split("\\\\n\\\\")
                if len(parts) >= 3:
                    skill_name = parts[2].strip() if len(parts) > 2 else ""
                    if skill_name:
                        active_skills.append({"name": skill_name})
        
        return PalInfo(
            id=pal_id,
            nickname=nickname,
            name=name,
            description=description,
            work_skills=work_skills,
            stats=stats,
            drops_normal=drops_normal,
            drops_boss=drops_boss,
            partner_skill=partner_skill,
            active_skills=active_skills
        )
    
    def crawl_pal(self, pal_url: str) -> Optional[PalInfo]:
        """개별 팰 정보를 크롤링합니다."""
        print(f"크롤링 중: {pal_url}")
        
        try:
            # Firecrawl을 직접 API 호출로 사용
            api_key = "fc-your-api-key"  # 실제 API 키로 교체 필요
            
            response = requests.post(
                "https://api.firecrawl.dev/v1/scrape",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "url": pal_url,
                    "formats": ["markdown"],
                    "onlyMainContent": True
                }
            )
            
            if response.status_code == 200:
                data = response.json()
                if "data" in data and "markdown" in data["data"]:
                    return self.parse_pal_info(data["data"]["markdown"], pal_url)
                else:
                    print(f"마크다운 데이터를 찾을 수 없습니다: {pal_url}")
            else:
                print(f"크롤링 실패 ({response.status_code}): {pal_url}")
                
        except Exception as e:
            print(f"크롤링 에러: {e}")
        
        return None
    
    def save_to_csv(self, pal_data: List[PalInfo], filename: str = "pal_info.csv"):
        """팰 정보를 CSV 파일로 저장합니다."""
        print(f"CSV 파일로 저장 중: {filename}")
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'id', 'nickname', 'name', 'description',
                'stats_hp', 'stats_defense', 'stats_attack', 'stats_ranged_attack',
                'work_skills', 'drops_normal', 'drops_boss', 'partner_skill', 'active_skills'
            ]
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for pal in pal_data:
                # 스테이터스에서 주요 값들 추출
                stats_hp = pal.stats.get('체력', '')
                stats_defense = pal.stats.get('방어', '')
                stats_attack = pal.stats.get('근접 공격', '')
                stats_ranged = pal.stats.get('원거리 공격', '')
                
                # 복잡한 데이터는 JSON 문자열로 변환
                work_skills_json = json.dumps(pal.work_skills, ensure_ascii=False)
                drops_normal_json = json.dumps(pal.drops_normal, ensure_ascii=False)
                drops_boss_json = json.dumps(pal.drops_boss, ensure_ascii=False)
                active_skills_json = json.dumps(pal.active_skills, ensure_ascii=False)
                
                writer.writerow({
                    'id': pal.id,
                    'nickname': pal.nickname,
                    'name': pal.name,
                    'description': pal.description,
                    'stats_hp': stats_hp,
                    'stats_defense': stats_defense,
                    'stats_attack': stats_attack,
                    'stats_ranged_attack': stats_ranged,
                    'work_skills': work_skills_json,
                    'drops_normal': drops_normal_json,
                    'drops_boss': drops_boss_json,
                    'partner_skill': pal.partner_skill,
                    'active_skills': active_skills_json
                })
        
        print(f"총 {len(pal_data)}개의 팰 정보가 {filename}에 저장되었습니다.")
    
    def run(self):
        """전체 크롤링 프로세스를 실행합니다."""
        print("팰월드 팰 정보 크롤링을 시작합니다...")
        
        # 팰 목록 가져오기
        pal_urls = self.get_pal_list()
        if not pal_urls:
            print("팰 목록을 가져올 수 없습니다.")
            return
        
        # 각 팰 정보 크롤링
        pal_data = []
        for i, url in enumerate(pal_urls, 1):
            print(f"진행률: {i}/{len(pal_urls)}")
            pal_info = self.crawl_pal(url)
            if pal_info:
                pal_data.append(pal_info)
            
            # API 요청 제한을 위한 대기
            time.sleep(1)
        
        # CSV 파일로 저장
        if pal_data:
            self.save_to_csv(pal_data)
        else:
            print("크롤링된 데이터가 없습니다.")

if __name__ == "__main__":
    crawler = PalCrawler()
    crawler.run()
