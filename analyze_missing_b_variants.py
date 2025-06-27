import pandas as pd
import json
import re

def analyze_current_b_variants():
    """현재 CSV의 B variants 분석"""
    
    # 현재 데이터 로드
    df = pd.read_csv('complete_1_to_115_pals.csv')
    
    # B variants 찾기 (id가 B로 끝나는 것들)
    current_b_variants = []
    
    for _, row in df.iterrows():
        pal_id = str(row['id'])
        if 'B' in pal_id or '110B' in pal_id:
            current_b_variants.append({
                'id': row['id'],
                'name_kor': row['name_kor'],
                'elements': row['elements']
            })
    
    print(f"📊 현재 CSV의 B Variants 분석:")
    print(f"  - 전체 팰 수: {len(df)}")
    print(f"  - 현재 B Variants 수: {len(current_b_variants)}")
    
    print(f"\n🔍 현재 보유한 B Variants:")
    for variant in current_b_variants:
        print(f"  - {variant['id']}: {variant['name_kor']} ({variant['elements']})")
    
    return current_b_variants

def get_expected_b_variants():
    """paldb.cc에서 확인된 실제 B variants 목록"""
    
    # 실제 paldb.cc에서 확인된 B variants들 (이전 크롤링 결과 기반)
    expected_b_variants = [
        {'id': '5B', 'name_kor': '아이호', 'name_eng': 'Foxcicle', 'url_name': 'Kitsunebi_Ice'},
        {'id': '6B', 'name_kor': '적부리', 'name_eng': 'Surfent Ignis', 'url_name': 'BluePlatypus_Fire'},
        {'id': '10B', 'name_kor': '뎅키', 'name_eng': 'Pengullet Spark', 'url_name': 'Penguin_Electric'},
        {'id': '11B', 'name_kor': '펭키드', 'name_eng': 'Penking Spark', 'url_name': 'CaptainPenguin_Electric'},
        {'id': '12B', 'name_kor': '코치도치', 'name_eng': 'Bristla Ignis', 'url_name': 'Hedgehog_Ice'},
        {'id': '13B', 'name_kor': '초롱이', 'name_eng': 'Vaelet', 'url_name': 'PlantSlime_Flower'},
        {'id': '21B', 'name_kor': '갈라티트', 'name_eng': 'Lunaris Ignis', 'url_name': 'NightFox_Ice'},
        {'id': '24B', 'name_kor': '칠테트', 'name_eng': 'Katress Spark', 'url_name': 'Bastet_Electric'},
        {'id': '26B', 'name_kor': '시로울프', 'name_eng': 'Chillet', 'url_name': 'Garm_Ice'},
        {'id': '27B', 'name_kor': '알록새B', 'name_eng': 'Sparkit', 'url_name': 'ColorfulBird_Electric'},
        {'id': '30B', 'name_kor': '썬데우', 'name_eng': 'Lyleen Spark', 'url_name': 'LittleBriarRose_Electric'},
        {'id': '32B', 'name_kor': '고릴블랙', 'name_eng': 'Gorirat Terra', 'url_name': 'GorillaBeast_Dark'},
        {'id': '34B', 'name_kor': '설탕양', 'name_eng': 'Sweepa Spark', 'url_name': 'SweetsSheep_Electric'},
        {'id': '37B', 'name_kor': '페어리', 'name_eng': 'Eikthyrdeer Terra', 'url_name': 'Deer_Dark'},
        {'id': '44B', 'name_kor': '코르크로우', 'name_eng': 'Cawgnito Cryst', 'url_name': 'Cawgnito_Ice'},
        {'id': '45B', 'name_kor': '아이스푸크', 'name_eng': 'Leezpunk Cryst', 'url_name': 'Leezpunk_Ice'},
        {'id': '55B', 'name_kor': '천도뇽', 'name_eng': 'Elphidran Aqua', 'url_name': 'WeaselDragon_Pure'},
        {'id': '64B', 'name_kor': '찌르르디노', 'name_eng': 'Dinossom Lux', 'url_name': 'FlowerDinosaur_Electric'},
        {'id': '65B', 'name_kor': '스너펜트', 'name_eng': 'Surfent Terra', 'url_name': 'Serpent_Ground'},
        {'id': '71B', 'name_kor': '시로카바네', 'name_eng': 'Suzaku Aqua', 'url_name': 'BirdDragon_Ice'},
        {'id': '72B', 'name_kor': '어둠무사', 'name_eng': 'Bushi', 'url_name': 'Ronin_Dark'},
        {'id': '75B', 'name_kor': '캐티위자드', 'name_eng': 'Wixen', 'url_name': 'CatMage_Electric'},
        {'id': '76B', 'name_kor': '영마호', 'name_eng': 'Blazamut Ryu', 'url_name': 'FoxMage_Dark'},
        {'id': '80B', 'name_kor': '실티아', 'name_eng': 'Silvera', 'url_name': 'FairyDragon_Dark'},
        {'id': '84B', 'name_kor': '만티코어', 'name_eng': 'Manticore Terra', 'url_name': 'Manticore_Dark'},
        {'id': '85B', 'name_kor': '핑피롱', 'name_eng': 'Relaxaurus Lux', 'url_name': 'LazyDragon_Electric'},
        {'id': '86B', 'name_kor': '스프라돈', 'name_eng': 'Celaray', 'url_name': 'SakuraSaurus_Water'},
        {'id': '88B', 'name_kor': '프로스카노', 'name_eng': 'Volcanus', 'url_name': 'VolcanicMonster_Ice'},
        {'id': '95B', 'name_kor': '포레스키', 'name_eng': 'Quivern Botan', 'url_name': 'SkyDragon_Grass'},
        {'id': '96B', 'name_kor': '마그마 드라고', 'name_eng': 'Blazamut', 'url_name': 'KingBahamut_Fire'},
        {'id': '97B', 'name_kor': '라이가루다', 'name_eng': 'Orserk', 'url_name': 'HadesBird_Electric'},
        {'id': '99B', 'name_kor': '골드 스팅', 'name_eng': 'Menasting Terra', 'url_name': 'DarkScorpion_Ground'},
        {'id': '104B', 'name_kor': '루나퀸', 'name_eng': 'Lyleen Noct', 'url_name': 'LilyQueen_Dark'},
        {'id': '110B', 'name_kor': '그레이섀도우', 'name_eng': 'Frostallion Noct', 'url_name': 'IceHorse_Dark'},
        {'id': '112B', 'name_kor': '벨라루주', 'name_eng': 'Bellanoir Libero', 'url_name': 'NightLady_Libero'}
    ]
    
    print(f"\n📋 예상되는 전체 B Variants 수: {len(expected_b_variants)}")
    
    return expected_b_variants

def find_missing_b_variants():
    """누락된 B variants 찾기"""
    
    current = analyze_current_b_variants()
    expected = get_expected_b_variants()
    
    # 현재 가지고 있는 ID들
    current_ids = {variant['id'] for variant in current}
    
    # 누락된 B variants 찾기
    missing = []
    for variant in expected:
        if variant['id'] not in current_ids:
            missing.append(variant)
    
    print(f"\n❌ 누락된 B Variants ({len(missing)}개):")
    for variant in missing:
        print(f"  - {variant['id']}: {variant['name_kor']} ({variant['name_eng']}) -> {variant['url_name']}")
    
    print(f"\n✅ 현재 보유한 B Variants ({len(current)}개):")
    for variant in current:
        print(f"  - {variant['id']}: {variant['name_kor']}")
    
    print(f"\n📊 완성도: {len(current)}/{len(expected)} ({len(current)/len(expected)*100:.1f}%)")
    
    return missing

def main():
    print("🔍 Analyzing B Variants in Current Dataset...")
    missing_variants = find_missing_b_variants()
    
    # 누락된 아종들을 우선순위별로 정렬 (ID 순서대로)
    missing_variants.sort(key=lambda x: int(re.findall(r'\d+', x['id'])[0]))
    
    print(f"\n🎯 크롤링 대상 B Variants (우선순위 순):")
    for i, variant in enumerate(missing_variants[:10], 1):
        print(f"  {i:2d}. {variant['id']:3s}: {variant['name_kor']:8s} -> https://paldb.cc/ko/{variant['url_name']}")
    
    if len(missing_variants) > 10:
        print(f"     ... 그리고 {len(missing_variants)-10}개 더")

if __name__ == "__main__":
    main() 