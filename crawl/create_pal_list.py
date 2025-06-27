import pandas as pd

def parse_pal_name(full_name):
    """
    '1 Lamball' -> id='1', name_eng='Lamball'
    '11B CaptainPenguin_Black' -> id='11B', name_eng='CaptainPenguin Black'
    """
    parts = full_name.split(' ', 1)  # 첫 번째 공백을 기준으로 분할
    if len(parts) == 2:
        pal_id = parts[0]
        name_eng = parts[1].replace('_', ' ')  # 언더스코어를 공백으로 변환
        return pal_id, name_eng
    else:
        # 공백이 없는 경우 전체를 이름으로 처리
        return full_name, full_name.replace('_', ' ')

def extract_sort_key(full_name):
    """
    정렬을 위한 키 생성
    '1 Lamball' -> (1, '')
    '11B CaptainPenguin_Black' -> (11, 'B')
    """
    pal_id, _ = parse_pal_name(full_name)
    
    # ID에서 숫자와 문자 분리
    import re
    match = re.match(r'(\d+)([A-Za-z]*)', pal_id)
    if match:
        number = int(match.group(1))
        suffix = match.group(2)
        return (number, suffix)
    else:
        # 숫자가 없는 경우 (예상치 못한 케이스)
        return (999999, pal_id)

def create_pal_list():
    """
    크롤링된 브리딩 데이터에서 고유한 팰 목록을 추출하여 pal_list.csv를 생성합니다.
    """
    # 브리딩 데이터 읽기
    print("브리딩 데이터 읽는 중...")
    df = pd.read_csv('paldb_breeding_data_ui_driven.csv')
    
    # Child 컬럼에서 고유한 팰 이름들 추출
    print("고유한 팰 이름들 추출 및 파싱 중...")
    unique_pals = df['Child'].unique()
    
    # 숫자 순서로 정렬
    sorted_pals = sorted(unique_pals, key=extract_sort_key)
    
    # ID와 이름 파싱
    pal_list = []
    for pal_full_name in sorted_pals:
        pal_id, name_eng = parse_pal_name(pal_full_name)
        pal_list.append({
            'id': pal_id,
            'name_eng': name_eng
        })
    
    # DataFrame으로 변환
    pal_df = pd.DataFrame(pal_list)
    
    # CSV로 저장
    output_filename = 'pal_list.csv'
    pal_df.to_csv(output_filename, index=False, encoding='utf-8-sig')
    
    print(f"✅ 성공! 총 {len(pal_df)}마리의 고유한 팰을 '{output_filename}' 파일에 저장했습니다.")
    
    # 처음 10개 결과 출력
    print("\n📋 생성된 팰 목록 (처음 10개):")
    print(pal_df.head(10).to_string(index=False))
    
    return pal_df

if __name__ == '__main__':
    create_pal_list() 