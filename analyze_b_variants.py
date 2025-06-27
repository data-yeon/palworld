import pandas as pd
import re

def analyze_current_b_variants():
    """Analyze current B variants in the CSV"""
    
    # Load current data
    df = pd.read_csv('complete_1_to_115_pals.csv')
    
    # Find B variants (check if id ends with 'B')
    current_b_variants = []
    
    for _, row in df.iterrows():
        if str(row['id']).endswith('B'):
            current_b_variants.append({
                'id': row['id'],
                'name_kor': row['name_kor'],
                'elements': row['elements']
            })
    
    print(f"📊 Current B Variants Analysis:")
    print(f"  - Total Pals in CSV: {len(df)}")
    print(f"  - Current B Variants: {len(current_b_variants)}")
    
    print(f"\n🔍 Current B Variants:")
    for variant in current_b_variants:
        print(f"  - {variant['id']}: {variant['name_kor']} ({variant['elements']})")
    
    return current_b_variants

def get_known_b_variants():
    """List of all known B variants from paldb.cc based on our earlier crawling"""
    
    # Based on the paldb.cc list we scraped earlier, here are all the B variants
    known_b_variants = [
        ('5B', '아이호', 'Ice'),  # Kitsunebi_Ice
        ('6B', '적부리', 'Water|Fire'),  # BluePlatypus_Fire
        ('10B', '뎅키', 'Water|Electric'),  # Penguin_Electric
        ('11B', '펭키드', 'Water|Electric'),  # CaptainPenguin_Black
        ('12B', '코치도치', 'Ice'),  # Hedgehog_Ice
        ('13B', '초롱이', 'Grass|Ground'),  # PlantSlime_Flower
        ('21B', '갈라티트', 'Ice'),  # NightFox_Ice
        ('24B', '칠테트', 'Electric'),  # Bastet_Electric
        ('26B', '시로울프', 'Ice'),  # Garm_Ice
        ('27B', '알록새B', 'Electric'),  # ColorfulBird_Electric
        ('30B', '썬데우', 'Electric'),  # LittleBriarRose_Electric
        ('32B', '고릴블랙', 'Dark'),  # GorillaBeast_Dark
        ('34B', '설탕양', 'Electric'),  # SweetsSheep_Electric
        ('37B', '페어리', 'Dark'),  # Deer_Dark
        ('44B', '코르크로우', 'Ice'),  # Cawgnito_Ice
        ('45B', '아이스푸크', 'Ice'),  # Leezpunk_Ice
        ('55B', '천도뇽', 'Dragon'),  # WeaselDragon_Pure
        ('64B', '찌르르디노', 'Electric'),  # FlowerDinosaur_Electric
        ('65B', '스너펜트', 'Ground'),  # Serpent_Ground
        ('71B', '시로카바네', 'Ice'),  # BirdDragon_Ice
        ('72B', '어둠무사', 'Dark'),  # Ronin_Dark
        ('75B', '캐티위저드', 'Electric'),  # CatMage_Electric
        ('76B', '영마호', 'Dark'),  # FoxMage_Dark
        ('80B', '실티아', 'Ice'),  # FairyDragon_Ice
        ('88B', '프로스카노', 'Ice'),  # VolcanicMonster_Ice
        ('95B', '포레스키', 'Grass'),  # SkyDragon_Grass
        ('96B', '마그마 드라고', 'Dark'),  # KingBahamut_Dark
        ('97B', '라이가루다', 'Electric'),  # HadesBird_Electric
        ('99B', '골드 스팅', 'Ground'),  # DarkScorpion_Ground
        ('110B', '그레이섀도우', 'Dark'),  # IceHorse_Dark
        ('112B', '벨라루주', 'Electric'),  # NightLady_Electric
    ]
    
    return known_b_variants

def find_missing_b_variants():
    """Find B variants that are missing from the current CSV"""
    
    current_variants = analyze_current_b_variants()
    known_variants = get_known_b_variants()
    
    # Extract current variant IDs
    current_ids = {v['id'] for v in current_variants}
    
    # Find missing variants
    missing_variants = []
    for variant_id, name_kor, elements in known_variants:
        if variant_id not in current_ids:
            missing_variants.append((variant_id, name_kor, elements))
    
    print(f"\n🔥 Missing B Variants ({len(missing_variants)}):")
    for variant_id, name_kor, elements in missing_variants:
        print(f"  - {variant_id}: {name_kor} ({elements})")
    
    print(f"\n📈 Summary:")
    print(f"  - Current B variants: {len(current_variants)}")
    print(f"  - Known B variants: {len(known_variants)}")
    print(f"  - Missing B variants: {len(missing_variants)}")
    print(f"  - Coverage: {len(current_variants)}/{len(known_variants)} ({len(current_variants)/len(known_variants)*100:.1f}%)")
    
    return missing_variants

if __name__ == "__main__":
    missing = find_missing_b_variants() 