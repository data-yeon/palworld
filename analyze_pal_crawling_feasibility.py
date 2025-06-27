import pandas as pd
import re

def analyze_pal_crawling_feasibility():
    """
    perfect_complete_pal_database_214.csv 파일을 분석하여 
    크롤링 가능한 팰들을 분류하고 통계를 생성합니다.
    """
    
    # CSV 파일 읽기
    df = pd.read_csv('perfect_complete_pal_database_214.csv')
    
    print(f"총 팰 개수: {len(df)}")
    print(f"컬럼: {list(df.columns)}")
    print("\n" + "="*50)
    
    # 영어명 분석
    has_english_name = df['englishName'].notna() & (df['englishName'] != '')
    no_english_name = ~has_english_name
    
    print(f"영어명이 있는 팰: {has_english_name.sum()}개")
    print(f"영어명이 없는 팰: {no_english_name.sum()}개")
    
    # 영어명이 없는 팰들 확인
    if no_english_name.sum() > 0:
        print("\n영어명이 없는 팰들:")
        missing_english = df[no_english_name][['id', 'name', 'englishName']]
        for _, row in missing_english.iterrows():
            print(f"  ID {row['id']}: {row['name']} ({row['englishName']})")
    
    # B 변형 팰들 분석
    b_variant_pattern = r'.*_(Ice|Fire|Electric|Aqua|Dark|Noct|Terra|Cryst|Lux|Ignis|Gild|Primo|Botan)$'
    
    english_names = df[has_english_name]['englishName'].tolist()
    
    b_variants = []
    normal_pals = []
    special_pals = []
    
    for name in english_names:
        if re.match(b_variant_pattern, name):
            b_variants.append(name)
        elif name.startswith('S') and name[1:].isdigit():
            special_pals.append(name)
        else:
            normal_pals.append(name)
    
    print(f"\n일반 팰: {len(normal_pals)}개")
    print(f"B 변형 팰: {len(b_variants)}개")
    print(f"특수 팰 (S계열): {len(special_pals)}개")
    
    # B 변형 팰들의 베이스명 추출
    print("\nB 변형 팰들 분석:")
    for variant in b_variants[:10]:  # 처음 10개만 출력
        base_name = re.sub(r'_(Ice|Fire|Electric|Aqua|Dark|Noct|Terra|Cryst|Lux|Ignis|Gild|Primo|Botan)$', '', variant)
        variant_type = re.search(r'_(Ice|Fire|Electric|Aqua|Dark|Noct|Terra|Cryst|Lux|Ignis|Gild|Primo|Botan)$', variant).group(1)
        print(f"  {variant} -> 베이스: {base_name}, 타입: {variant_type}")
    
    if len(b_variants) > 10:
        print(f"  ... 외 {len(b_variants) - 10}개")
    
    # 크롤링 전략 제안
    print("\n" + "="*50)
    print("크롤링 전략:")
    print("1. 일반 팰들: 영어명 그대로 사용")
    print("2. B 변형 팰들: 베이스 팰명으로 크롤링 후 변형 정보 추가")
    print("3. 영어명 없는 팰들: 수동 처리 필요")
    
    # 크롤링 우선순위별 분류
    crawlable_normal = [name for name in normal_pals if name and len(name) > 0]
    crawlable_variants = [name for name in b_variants if name and len(name) > 0]
    
    print(f"\n크롤링 가능한 팰:")
    print(f"  - 일반 팰: {len(crawlable_normal)}개")
    print(f"  - B 변형 팰: {len(crawlable_variants)}개")
    print(f"  - 총 크롤링 대상: {len(crawlable_normal) + len(crawlable_variants)}개")
    
    # 결과를 파일로 저장
    result = {
        'total_pals': len(df),
        'crawlable_normal': crawlable_normal,
        'crawlable_variants': crawlable_variants,
        'missing_english': df[no_english_name][['id', 'name']].to_dict('records'),
        'statistics': {
            'normal_count': len(crawlable_normal),
            'variant_count': len(crawlable_variants),
            'missing_count': no_english_name.sum()
        }
    }
    
    import json
    with open('pal_crawling_analysis.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"\n분석 결과가 'pal_crawling_analysis.json'에 저장되었습니다.")
    
    return result

if __name__ == "__main__":
    analyze_pal_crawling_feasibility() 