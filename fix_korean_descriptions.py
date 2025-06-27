import csv
import json

def fix_korean_descriptions():
    """영어로 된 팰 설명을 한국어로 수정합니다."""
    
    # 한국어 번역 데이터
    korean_translations = {
        "131": {
            "name": "스모키",
            "englishName": "Smokie", 
            "description": "검은 불꽃은 만져도 따뜻할 뿐이지만, 계속 접촉하면 안에서부터 천천히 녹아내린다. 치즈를 그 위에 올리면 진정한 별미가 된다.",
            "type1": "화염",
            "partnerSkill": "파헤쳐라! 활성화시 예리한 후각으로 근처의 크로마이트를 탐지한다. 함께 싸우는 동안 대량의 크로마이트를 획득한다.",
            "workSkills": "채집 Lv. 2",
            "activeSkills": "파이어 샷, 다크 볼, 플레임 버스트, 파이어 브레스, 인페르노",
            "dropItems": "뼈, 원유",
            "hp": "80",
            "attack": "90", 
            "defense": "75"
        },
        "132": {
            "name": "셀레스디르",
            "englishName": "Celesdir",
            "description": "고대 문헌에서는 구원의 짐승이라고 언급한다. 셀레스디르가 내뿜는 빛은 모든 것을 정화하여 흔적도 없이 존재에서 사라지게 만든다.",
            "type1": "용",
            "type2": "번개", 
            "partnerSkill": "정화의 축복 - 탈 수 있다. 탑승 중 플레이어의 자동 회복 속도를 증가시킨다.",
            "workSkills": "벌목 Lv. 4, 채집 Lv. 1",
            "activeSkills": "파워 샷, 용 대포, 성스러운 폭발, 정화 광선, 천상의 화염",
            "dropItems": "헥솔라이트 쿼츠, 뿔",
            "hp": "4400",
            "attack": "743",
            "defense": "635"
        },
        "133": {
            "name": "오마스쿨", 
            "englishName": "Omascul",
            "description": "가면은 그의 얼굴이 아니라고들 한다. 앞에 있는 것 같지만 거기에는 없고, 그림자 깊숙한 곳에서 밤낮으로 지켜본다. 시선을 돌리면 더 가까이 다가온다.",
            "type1": "어둠",
            "partnerSkill": "그림자 추적자 - 적의 위치를 파악하고 은밀하게 접근한다.",
            "workSkills": "수작업 Lv. 2, 운반 Lv. 1", 
            "activeSkills": "다크 볼, 섀도우 버스트, 악몽의 구체, 그림자 분신, 어둠의 돌격",
            "dropItems": "작은 팰 영혼, 어둠의 파편",
            "hp": "85",
            "attack": "95",
            "defense": "90"
        }
    }
    
    # CSV 파일 읽기
    input_file = 'crawled_pals_118_to_133.csv'
    output_file = 'crawled_pals_118_to_133_korean.csv'
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)
    
    # 번역 적용
    for row in rows:
        pal_id = row['id']
        if pal_id in korean_translations:
            translation = korean_translations[pal_id]
            row['description'] = translation['description']
            row['type1'] = translation['type1'] 
            row['partnerSkill'] = translation['partnerSkill']
            # work1에만 workSkills 적용 (work2, work3는 비워둠)
            row['work1'] = translation['workSkills']
            row['work2'] = ''
            row['work3'] = ''
            row['activeSkills'] = translation['activeSkills']
            # dropItem1, dropItem2로 분리
            drop_items = translation['dropItems'].split(', ')
            row['dropItem1'] = drop_items[0] if len(drop_items) > 0 else ''
            row['dropItem2'] = drop_items[1] if len(drop_items) > 1 else ''
            row['hp'] = translation['hp']
            row['attack'] = translation['attack']
            row['defense'] = translation['defense']
            
            if 'type2' in translation:
                row['type2'] = translation['type2']
    
    # 수정된 CSV 파일 저장
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        if rows:
            writer = csv.DictWriter(outfile, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
    
    print(f"✅ 한국어 번역 완료: {output_file}")
    print("🔄 수정된 팰들:")
    for pal_id, data in korean_translations.items():
        print(f"  {pal_id}. {data['name']} ({data['englishName']}) - 설명 한국어로 수정")

if __name__ == "__main__":
    fix_korean_descriptions() 