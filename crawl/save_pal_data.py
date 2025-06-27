import csv
import json
from typing import List, Dict

def save_pal_data_to_csv(pal_data_list: List[Dict], filename: str = "pal_info_crawled.csv"):
    """크롤링된 팰 데이터를 CSV 파일로 저장합니다."""
    
    # CSV 필드명 정의
    fieldnames = [
        'id', 'nickname', 'name', 'description', 'element',
        'hp', 'defense', 'melee_attack', 'ranged_attack',
        'work_skills', 'drops', 'partner_skill_name', 'partner_skill_desc', 'active_skills'
    ]
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for pal in pal_data_list:
            # 스테이터스 분리
            stats = pal.get('stats', {})
            
            # 복잡한 데이터는 JSON 문자열로 변환
            work_skills_json = json.dumps(pal.get('work_skills', {}), ensure_ascii=False)
            drops_json = json.dumps(pal.get('drops', []), ensure_ascii=False)
            active_skills_json = json.dumps(pal.get('active_skills', []), ensure_ascii=False)
            
            # 파트너 스킬 정보
            partner_skill = pal.get('partner_skill', {})
            
            row_data = {
                'id': pal.get('id', ''),
                'nickname': pal.get('nickname', ''),
                'name': pal.get('name', ''),
                'description': pal.get('description', ''),
                'element': pal.get('element', ''),
                'hp': stats.get('hp', ''),
                'defense': stats.get('defense', ''),
                'melee_attack': stats.get('melee_attack', ''),
                'ranged_attack': stats.get('ranged_attack', ''),
                'work_skills': work_skills_json,
                'drops': drops_json,
                'partner_skill_name': partner_skill.get('name', ''),
                'partner_skill_desc': partner_skill.get('description', ''),
                'active_skills': active_skills_json
            }
            
            writer.writerow(row_data)
    
    print(f"총 {len(pal_data_list)}개의 팰 정보가 {filename}에 저장되었습니다.")

# 지금까지 크롤링한 팰 데이터
crawled_pals = [
    # 첫 번째 배치
    {
        "id": "Anubis",
        "name": "아누비스",
        "drops": ["뼈3~5", "대형 팰 영혼1", "혁신적인 기술서15%", "고대 문명의 부품4~6", "귀중한 내장4~6", "땅 저항 반지+2"],
        "stats": {"hp": "120", "defense": "100", "melee_attack": "130", "ranged_attack": "130"},
        "element": "Earth",
        "nickname": "저무는 태양의 수호자",
        "description": "그 풍모 덕택에 일찍이 고귀한 자의 상징이었다. 부와 권력을 멀리하는 이에게도 귀감이었으나 언제부턴가 아누비스은(는) 죽음의 상징이 되었다.",
        "work_skills": {"관개": "LV.0", "냉각": "LV.0", "목장": "LV.0", "발전": "LV.0", "벌목": "LV.0", "운반": "LV.2", "제약": "LV.0", "채굴": "LV.3", "채집": "LV.0", "파종": "LV.0", "수작업": "LV.4", "불 피우기": "LV.0"},
        "active_skills": ["바위 폭발", "파워 폭탄", "모래 폭풍", "스핀 레그 러쉬", "포스 드라이브", "그라운드 스매셔", "바위 창"],
        "partner_skill": {"name": "사막의 수호신", "description": "함께 싸우는 동안 플레이어의 공격이 땅 속성(으)로 변화한다. 전투 중에 가끔씩 고속 스텝으로 공격을 회피한다."}
    },
    {
        "id": "Alpaca",
        "name": "멜파카",
        "drops": ["양털", "가죽"],
        "stats": {"hp": "90", "defense": "90", "melee_attack": "90", "ranged_attack": "75"},
        "element": "Normal",
        "nickname": "늘씬한 다리를 자랑하는",
        "description": "복슬복슬한 털을 보고 방심해선 안 된다. 긴 다리로 가하는 초고속 발차기에 맞으면 지구 반대편까지 날아간다.",
        "work_skills": {"관개": "LV.0", "냉각": "LV.0", "목장": "LV.1", "발전": "LV.0", "벌목": "LV.0", "운반": "LV.0", "제약": "LV.0", "채굴": "LV.0", "채집": "LV.0", "파종": "LV.0", "수작업": "LV.0", "불 피우기": "LV.0"},
        "active_skills": ["공기 대포", "푹신 태클", "모래 돌풍", "파워 샷", "전기 파장", "파워 폭탄", "팰 폭발"],
        "partner_skill": {"name": "털파카파카", "description": "등에 타고 이동할 수 있다. 가축 목장에 배치하면 양털을(를) 떨어뜨리기도 한다."}
    },
    {
        "id": "AmaterasuWolf",
        "name": "불이리",
        "drops": ["발화 기관2~3100%", "가죽2~3100%"],
        "stats": {"hp": "100", "defense": "100", "melee_attack": "70", "ranged_attack": "115"},
        "element": "Fire",
        "nickname": "푸른 불꽃의 수호신",
        "description": "기질이 워낙 예민해 기분이 상하면 동굴에 숨어 버린다. 옛 사람들은 불이리이(가) 숨으면 흉조로 여겼다.",
        "work_skills": {"관개": "LV.0", "냉각": "LV.0", "목장": "LV.0", "발전": "LV.0", "벌목": "LV.0", "운반": "LV.0", "제약": "LV.0", "채굴": "LV.0", "채집": "LV.0", "파종": "LV.0", "수작업": "LV.0", "불 피우기": "LV.2"},
        "active_skills": ["파이어 샷", "스피릿 파이어", "유령의 불꽃", "풍림화산", "화염 폭풍", "인페르노", "화염구"],
        "partner_skill": {"name": "무념무상", "description": "등에 타고 이동할 수 있다. 탑승 중에는 추위나 더위의 영향을 받지 않는다."}
    },
    # 두 번째 배치
    {
        "id": "BadCatgirl",
        "name": "멀보냥",
        "drops": ["가죽", "고대 문명의 부품", "귀중한 동물 털", "어둠 저항 반지+1"],
        "stats": {"hp": "110", "defense": "100", "melee_attack": "100", "ranged_attack": "100"},
        "element": "Dark",
        "nickname": "남에게 양쪽 눈을 보여주는 것을 극도로 싫어한다",
        "description": "남에게 양쪽 눈을 보여주는 것을 극도로 싫어한다. 억지로 확인해 보려 하면 갑자기 울음을 터뜨리고 적어도 2주 동안은 상대조차 안 해준다.",
        "work_skills": {"관개": "LV.0", "냉각": "LV.0", "목장": "LV.0", "발전": "LV.0", "벌목": "LV.2", "운반": "LV.2", "제약": "LV.0", "채굴": "LV.0", "채집": "LV.2", "파종": "LV.0", "수작업": "LV.3", "불 피우기": "LV.0"},
        "active_skills": ["독 안개", "독 사격", "바위 폭발", "그림자 폭발", "포이즌 샤워", "악몽의 구체", "어둠의 레이저"],
        "partner_skill": {"name": "산탄냥 모드", "description": "발동하면 일정 시간 동안 멀보냥이(가) 근처 적에게 산탄총을 난사한다."}
    },
    {
        "id": "Baphomet",
        "name": "헬고트",
        "drops": ["뿔", "가죽", "고대 문명의 부품", "귀중한 발톱", "화염 저항 반지+1"],
        "stats": {"hp": "95", "defense": "85", "melee_attack": "150", "ranged_attack": "100"},
        "element": "Fire, Dark",
        "nickname": "밤에 사냥감을 잡아 자기 영역에 돌아온다",
        "description": "밤에 사냥감을 잡아 자기 영역에 돌아온다. 잡힌 팰이 그 후 어떤 일을 당할지는 불 보듯 뻔하다.",
        "work_skills": {"관개": "LV.0", "냉각": "LV.0", "목장": "LV.0", "발전": "LV.0", "벌목": "LV.0", "운반": "LV.2", "제약": "LV.0", "채굴": "LV.1", "채집": "LV.0", "파종": "LV.0", "수작업": "LV.2", "불 피우기": "LV.1"},
        "active_skills": ["파이어 샷", "스피릿 파이어", "불화살", "지옥불 할퀴기", "그림자 폭발", "화염구", "인페르노"],
        "partner_skill": {"name": "화염 발톱의 사냥꾼", "description": "발동하면 목표로 삼은 적을 향해 높은 위력의 지옥불 할퀴기(으)로 공격한다."}
    },
    {
        "id": "Bastet",
        "name": "냐옹테트",
        "drops": ["금화100~200", "고대 문명의 부품1~2", "귀중한 발톱1~2", "어둠 저항 반지"],
        "stats": {"hp": "70", "defense": "70", "melee_attack": "70", "ranged_attack": "60"},
        "element": "Dark",
        "nickname": "단단한 꼬리 조직은 잘라도 그대로이다",
        "description": "단단한 꼬리 조직은 잘라도 그대로이다. 그 꼬리가 재물을 불러온다는 미신이 성행해 대량의 냐옹테트이(가) 목숨을 잃었다.",
        "work_skills": {"관개": "LV.0", "냉각": "LV.0", "목장": "LV.1", "발전": "LV.0", "벌목": "LV.0", "운반": "LV.0", "제약": "LV.0", "채굴": "LV.0", "채집": "LV.0", "파종": "LV.0", "수작업": "LV.0", "불 피우기": "LV.0"},
        "active_skills": ["모래 돌풍", "암흑구", "그림자 폭발", "모래 폭풍", "유령의 불꽃", "악몽의 구체", "어둠의 레이저"],
        "partner_skill": {"name": "금화 수집", "description": "가축 목장에 배치하면 지면에서 금화을(를) 파내기도 한다."}
    },
    {
        "id": "BerryGoat",
        "name": "베리고트",
        "drops": ["베리고트 향초 고기", "빨간 열매", "뿔", "고대 문명의 부품", "귀중한 동물 털", "풀 저항 반지+1"],
        "stats": {"hp": "100", "defense": "90", "melee_attack": "70", "ranged_attack": "70"},
        "element": "Leaf",
        "nickname": "걸어 다니는 농장",
        "description": "밥을 잘 먹이면 등의 덤불에 열매가 맺힌다. 마음에 드는 상대에게 그 열매를 먹여 입맛을 사로잡으면 한 쌍의 커플이 된다.",
        "work_skills": {"관개": "LV.0", "냉각": "LV.0", "목장": "LV.1", "발전": "LV.0", "벌목": "LV.0", "운반": "LV.0", "제약": "LV.0", "채굴": "LV.0", "채집": "LV.0", "파종": "LV.2", "수작업": "LV.0", "불 피우기": "LV.0"},
        "active_skills": ["바람의 칼날", "공기 대포", "모래 돌풍", "파워 샷", "초록 폭풍", "가시덩굴", "태양 폭발"],
        "partner_skill": {"name": "열매 채집", "description": "가축 목장에 배치하면 등에서 빨간 열매을(를) 떨어뜨리기도 한다."}
    },
    {
        "id": "BirdDragon",
        "name": "버드래곤",
        "drops": ["뼈1~2100%", "루비1~21%", "금화10~4010%", "고대 문명의 부품4~6100%", "귀중한 깃털4~6100%", "화염 저항 반지+113%", "프레데터 코어1100%", "극한 팰 영혼1100%"],
        "stats": {"hp": "90", "defense": "90", "melee_attack": "100", "ranged_attack": "115"},
        "element": "Fire, Dark",
        "nickname": "하늘에서 온 습격자",
        "description": "버드래곤의 외골격으로 만든 피리 소리는 천 개의 봉우리를 건넌다고 한다. 고대 전쟁에선 공격 신호로 사용했다.",
        "work_skills": {"관개": "LV.0", "냉각": "LV.0", "목장": "LV.0", "발전": "LV.0", "벌목": "LV.0", "운반": "LV.3", "제약": "LV.0", "채굴": "LV.0", "채집": "LV.0", "파종": "LV.0", "수작업": "LV.0", "불 피우기": "LV.1"},
        "active_skills": ["공기 대포", "파이어 샷", "스피릿 파이어", "파이어 브레스", "플라잉 브레스", "악몽의 구체", "화염구", "어둠의 레이저"],
        "partner_skill": {"name": "하늘에서 온 습격자", "description": "등에 타고 하늘을 날 수 있다. 탑승 중 플레이어가 적의 약점 부위를 공격할 때 주는 피해량이 증가한다."}
    }
]

if __name__ == "__main__":
    # CSV 파일로 저장
    save_pal_data_to_csv(crawled_pals)
    print("팰 데이터가 성공적으로 저장되었습니다!")
    
    # 저장된 데이터 통계
    print(f"\n=== 저장된 팰 데이터 통계 ===")
    print(f"총 팰 수: {len(crawled_pals)}")
    
    # 속성별 분포
    elements = {}
    for pal in crawled_pals:
        element = pal.get('element', 'Unknown')
        elements[element] = elements.get(element, 0) + 1
    
    print(f"속성별 분포:")
    for element, count in elements.items():
        print(f"  {element}: {count}개") 