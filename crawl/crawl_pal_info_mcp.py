import csv
import re
import json
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict

@dataclass
class PalInfo:
    id: str
    nickname: str  # 간략한 수식어
    name: str      # 이름
    description: str  # 자세한 도감설명
    element: str   # 속성
    work_skills: str  # 작업적성 (JSON 문자열)
    stats: str     # 스테이터스 (JSON 문자열)
    drops_normal: str  # 일반 드롭 아이템 (JSON 문자열)
    partner_skill_name: str  # 파트너 스킬 이름
    partner_skill_desc: str  # 파트너 스킬 설명
    active_skills: str  # 공격 스킬 (JSON 문자열)

def parse_pal_info(markdown_content: str, pal_id: str) -> PalInfo:
    """마크다운 콘텐츠에서 팰 정보를 파싱합니다."""
    lines = markdown_content.split('\n')
    
    # 기본 정보 초기화
    nickname = ""
    name = ""
    description = ""
    element = ""
    
    # 이름과 수식어, 설명 추출
    text_lines = []
    for line in lines:
        stripped = line.strip()
        if (stripped and 
            not stripped.startswith('![') and 
            not stripped.startswith('[') and
            not stripped.startswith('#') and
            not stripped.startswith('체력') and
            '서식지' not in stripped and
            '부모 조합' not in stripped):
            text_lines.append(stripped)
    
    # 첫 번째 의미 있는 텍스트들을 찾기
    for i, line in enumerate(text_lines[:10]):  # 처음 10개 라인만 확인
        if not nickname and len(line) > 2 and len(line) < 50:
            nickname = line
        elif not name and len(line) > 1 and len(line) < 30 and line != nickname:
            name = line
        elif not description and len(line) > 20:
            description = line
            break
    
    # 속성 추출
    for line in lines:
        if 'Normal](https://palworld.shwa.space/assets/UI/InGame/T_Icon_element_s_00.webp)' in line:
            element = "Normal"
        elif 'Fire](https://palworld.shwa.space/assets/UI/InGame/T_Icon_element_s_01.webp)' in line:
            element = "Fire"
        elif 'Water](https://palworld.shwa.space/assets/UI/InGame/T_Icon_element_s_02.webp)' in line:
            element = "Water"
        elif 'Electricity](https://palworld.shwa.space/assets/UI/InGame/T_Icon_element_s_03.webp)' in line:
            element = "Electricity"
        elif 'Earth](https://palworld.shwa.space/assets/UI/InGame/T_Icon_element_s_07.webp)' in line:
            element = "Earth"
        elif 'Grass](https://palworld.shwa.space/assets/UI/InGame/T_Icon_element_s_04.webp)' in line:
            element = "Grass"
        elif 'Ice](https://palworld.shwa.space/assets/UI/InGame/T_Icon_element_s_05.webp)' in line:
            element = "Ice"
        elif 'Dark](https://palworld.shwa.space/assets/UI/InGame/T_Icon_element_s_06.webp)' in line:
            element = "Dark"
        elif 'Dragon](https://palworld.shwa.space/assets/UI/InGame/T_Icon_element_s_08.webp)' in line:
            element = "Dragon"
    
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
                if stat_name and stat_name not in ['느린 걷기 속도', '걷기 속도', '달리기 속도']:
                    stats[stat_name] = stat_value
    
    # 작업 적성 파싱
    work_skills = {}
    in_work_section = False
    current_work = ""
    for line in lines:
        if "### 작업 적성" in line:
            in_work_section = True
            continue
        elif in_work_section and line.startswith("###"):
            break
        elif in_work_section:
            if "LV." in line:
                level_match = re.search(r'LV\.(\d+)', line)
                if level_match and current_work:
                    work_skills[current_work] = int(level_match.group(1))
            else:
                # 작업명 추출
                work_names = ['불 피우기', '관개', '파종', '발전', '수작업', '채집', '벌목', '채굴', '제약', '냉각', '운반', '목장']
                for work in work_names:
                    if work in line:
                        current_work = work
                        break
    
    # 드롭 아이템 파싱
    drops_normal = []
    in_drops_section = False
    for line in lines:
        if "### 드롭하는 아이템" in line:
            in_drops_section = True
            continue
        elif in_drops_section and "### 스킬" in line:
            break
        elif in_drops_section and "100%" in line:
            # 한글 아이템명 추출
            item_matches = re.findall(r'([가-힣\s]+)\d+~?\d*100%', line)
            for item in item_matches:
                item_name = item.strip()
                if item_name and len(item_name) > 1:
                    drops_normal.append(item_name)
    
    # 파트너 스킬 파싱
    partner_skill_name = ""
    partner_skill_desc = ""
    in_partner_section = False
    skill_desc_lines = []
    
    for line in lines:
        if "### 파트너" in line:
            in_partner_section = True
            continue
        elif in_partner_section and line.startswith("###"):
            break
        elif in_partner_section and line.strip():
            if not line.startswith("![") and not partner_skill_name:
                partner_skill_name = line.strip()
            elif not line.startswith("![") and partner_skill_name and line.strip():
                skill_desc_lines.append(line.strip())
    
    partner_skill_desc = " ".join(skill_desc_lines)
    
    # 액티브 스킬 파싱
    active_skills = []
    in_active_section = False
    for line in lines:
        if "### 액티브" in line:
            in_active_section = True
            continue
        elif in_active_section and line.startswith("###"):
            break
        elif in_active_section and "Lv." in line and "](" in line:
            # 스킬 정보 파싱 시도
            try:
                # 스킬명 추출
                if "\\\\n\\\\" in line:
                    parts = line.split("\\\\n\\\\")
                    if len(parts) >= 3:
                        skill_name = parts[2].strip()
                        level_part = parts[1].strip() if len(parts) > 1 else ""
                        if skill_name:
                            active_skills.append({
                                "name": skill_name,
                                "level": level_part
                            })
            except:
                continue
    
    return PalInfo(
        id=pal_id,
        nickname=nickname,
        name=name,
        description=description,
        element=element,
        work_skills=json.dumps(work_skills, ensure_ascii=False),
        stats=json.dumps(stats, ensure_ascii=False),
        drops_normal=json.dumps(drops_normal, ensure_ascii=False),
        partner_skill_name=partner_skill_name,
        partner_skill_desc=partner_skill_desc,
        active_skills=json.dumps(active_skills, ensure_ascii=False)
    )

def save_to_csv(pal_data: List[PalInfo], filename: str = "pal_info_complete.csv"):
    """팰 정보를 CSV 파일로 저장합니다."""
    print(f"CSV 파일로 저장 중: {filename}")
    
    fieldnames = [
        'id', 'nickname', 'name', 'description', 'element',
        'work_skills', 'stats', 'drops_normal', 
        'partner_skill_name', 'partner_skill_desc', 'active_skills'
    ]
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for pal in pal_data:
            writer.writerow(asdict(pal))
    
    print(f"총 {len(pal_data)}개의 팰 정보가 {filename}에 저장되었습니다.")

# 테스트용 데이터
if __name__ == "__main__":
    # 이미 크롤링된 데이터로 테스트
    test_markdown = """
저무는 태양의 수호자

아누비스

![Earth](https://palworld.shwa.space/assets/UI/InGame/T_Icon_element_s_07.webp)

그 풍모 덕택에 일찍이 고귀한 자의 상징이었다.
부와 권력을 멀리하는 이에게도 귀감이었으나
언제부턴가 아누비스은(는) 죽음의 상징이 되었다.

### 스테이터스

체력120
방어100
근접 공격130
원거리 공격130

### 작업 적성

수작업
LV.4

채굴
LV.3

### 드롭하는 아이템

뼈3~5100%

### 파트너

사막의 수호신

함께 싸우는 동안 플레이어의 공격이
땅 속성(으)로 변화한다.
"""
    
    pal_info = parse_pal_info(test_markdown, "Anubis")
    print("파싱 결과:")
    print(f"ID: {pal_info.id}")
    print(f"수식어: {pal_info.nickname}")
    print(f"이름: {pal_info.name}")
    print(f"설명: {pal_info.description}")
    print(f"속성: {pal_info.element}")
    print(f"스테이터스: {pal_info.stats}")
    print(f"작업 적성: {pal_info.work_skills}")
    print(f"드롭 아이템: {pal_info.drops_normal}")
    print(f"파트너 스킬: {pal_info.partner_skill_name}")
    
    # CSV 저장 테스트
    save_to_csv([pal_info], "test_pal_info.csv") 