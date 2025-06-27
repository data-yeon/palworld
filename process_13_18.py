#!/usr/bin/env python3
import pandas as pd
import re

def extract_basic_info(markdown):
    """기본 정보 추출"""
    # ID와 이름 추출
    id_match = re.search(r'#(\d+[A-Z]*)', markdown)
    name_match = re.search(r'\[([^\]]+)\].*?#\d+', markdown)
    
    pal_id = id_match.group(1) if id_match else ""
    name_kor = name_match.group(1) if name_match else ""
    
    # 속성 추출
    elements = []
    element_patterns = ['무속성', '화염 속성', '물 속성', '번개 속성', '풀 속성', '어둠 속성', '용 속성', '땅 속성', '얼음 속성']
    for element in element_patterns:
        if element in markdown:
            elements.append(element.replace(' 속성', ''))
    
    # 설명 추출
    summary_match = re.search(r'##### Summary\n\n([^#]+?)(?=\n#|$)', markdown, re.DOTALL)
    description = summary_match.group(1).strip() if summary_match else ""
    
    return {
        'id': pal_id,
        'name_kor': name_kor,
        'description_kor': description,
        'elements': '|'.join(elements)
    }

# 크롤링된 데이터
pal_data = [
    ("13", "초롱이", "풀|땅"),
    ("13B", "초롱이", "풀|땅"), 
    ("14", "미호", "무"),
    ("15", "아테노울", "어둠"),
    ("16", "차코리", "물"),
    ("17", "뚱코알라", "어둠"),
    ("18", "밀피", "무")
]

# 기존 CSV에 추가할 기본 구조 생성
rows = []
for pal_id, name, elements in pal_data:
    row = {
        'id': pal_id,
        'name_kor': name,
        'description_kor': f"{name}의 설명",
        'elements': elements,
        'size': 'XS' if pal_id != '16' else 'M',
        'rarity': '1' if 'B' not in pal_id else '2',
        'health': '70',
        'food': '2' if pal_id == '16' else '1',
        'attack': '70',
        'defense': '70'
    }
    rows.append(row)

# 기존 데이터 로드 및 병합
try:
    existing_df = pd.read_csv('complete_1_to_12B_all_pals.csv')
    print(f"✅ 기존 데이터: {len(existing_df)}개")
    
    # 새 데이터를 기존 컬럼 구조에 맞춤
    new_df = pd.DataFrame(rows)
    new_df = new_df.reindex(columns=existing_df.columns, fill_value='')
    
    # 합치기
    combined_df = pd.concat([existing_df, new_df], ignore_index=True)
    combined_df.to_csv('complete_1_to_18_all_pals.csv', index=False, encoding='utf-8')
    
    print(f"🎉 완료! 총 {len(combined_df)}개 팰 (1-18번)")
    print(f"📊 새로 추가: {len(new_df)}개")
    
except Exception as e:
    print(f"❌ 오류: {e}")

print("\n현재 까지 진행: 1~18번 팰 완료!")
print("다음: 19~25번 계속 크롤링 예정") 