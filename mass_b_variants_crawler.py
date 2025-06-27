import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time
import re
from urllib.parse import urljoin

def extract_active_skills_enhanced(soup):
    """Enhanced active skills extraction"""
    skills = []
    
    # Find the Active Skills section
    skills_section = soup.find('h3', string='Active Skills')
    if not skills_section:
        skills_section = soup.find('h3', string='액티브 스킬')
    
    if skills_section:
        # Get the parent container
        parent = skills_section.find_parent()
        if parent:
            # Find all skill blocks in the parent
            skill_blocks = parent.find_all('div', class_='space-y-2')
            
            for block in skill_blocks:
                # Get all text from the block
                block_text = block.get_text(separator='\n', strip=True)
                
                # Split into lines for processing
                lines = [line.strip() for line in block_text.split('\n') if line.strip()]
                
                for i, line in enumerate(lines):
                    # Look for skill name pattern (Korean name followed by English in parentheses)
                    skill_match = re.match(r'^(.+?)\s*\(([^)]+)\)\s*$', line)
                    if skill_match and not any(keyword in line.lower() for keyword in ['level', 'power', 'cooltime', 'element']):
                        korean_name = skill_match.group(1).strip()
                        english_name = skill_match.group(2).strip()
                        
                        skill = {
                            "name": korean_name,
                            "english_name": english_name,
                            "level": None,
                            "power": None,
                            "cooltime": None,
                            "element": None,
                            "description": None
                        }
                        
                        # Look for details in the following lines
                        for j in range(i+1, min(i+5, len(lines))):
                            detail_line = lines[j]
                            
                            # Extract level
                            level_match = re.search(r'Level\s*(\d+)', detail_line, re.IGNORECASE)
                            if level_match:
                                skill["level"] = int(level_match.group(1))
                            
                            # Extract power
                            power_match = re.search(r'Power\s*(\d+)', detail_line, re.IGNORECASE)
                            if power_match:
                                skill["power"] = int(power_match.group(1))
                            
                            # Extract cooltime
                            cooltime_match = re.search(r'(?:Cooltime|CT)\s*(\d+)', detail_line, re.IGNORECASE)
                            if cooltime_match:
                                skill["cooltime"] = int(cooltime_match.group(1))
                            
                            # Extract element
                            for element in ['Neutral', 'Fire', 'Water', 'Grass', 'Electric', 'Ice', 'Ground', 'Dark', 'Dragon']:
                                if element.lower() in detail_line.lower():
                                    skill["element"] = element
                                    break
                        
                        skills.append(skill)
    
    return skills

def extract_passive_skills(soup):
    """Extract passive skills"""
    passive_skills = []
    
    # Find passive skills section
    passive_section = soup.find('h3', string='Passive Skills')
    if not passive_section:
        passive_section = soup.find('h3', string='패시브 스킬')
    
    if passive_section:
        parent = passive_section.find_parent()
        if parent:
            # Look for skill entries
            skill_elements = parent.find_all(['p', 'div'], string=lambda text: text and ('(' in text and ')' in text))
            
            for element in skill_elements:
                text = element.get_text(strip=True)
                # Match pattern like "Korean Name (English Name)"
                match = re.match(r'^(.+?)\s*\(([^)]+)\)\s*$', text)
                if match:
                    korean_name = match.group(1).strip()
                    english_name = match.group(2).strip()
                    if korean_name and english_name:
                        passive_skills.append({
                            "name": korean_name,
                            "english_name": english_name
                        })
    
    return passive_skills

def crawl_pal_info_enhanced(pal_id, pal_name, retries=3):
    """Enhanced crawling function with better error handling"""
    url = f"https://paldb.cc/ko/{pal_name}"
    
    for attempt in range(retries):
        try:
            print(f"Attempting to crawl {pal_id} ({pal_name}) - Attempt {attempt + 1}")
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract all available data
            pal_data = {
                "pal_id": pal_id,
                "pal_name": pal_name,
                "url": url,
                "activeSkills": extract_active_skills_enhanced(soup),
                "passiveSkills": extract_passive_skills(soup),
                "raw_html_length": len(response.content)
            }
            
            print(f"✅ Successfully crawled {pal_id}: {len(pal_data['activeSkills'])} active skills, {len(pal_data['passiveSkills'])} passive skills")
            return pal_data
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error crawling {pal_id} (attempt {attempt + 1}): {e}")
            if attempt < retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            continue
        except Exception as e:
            print(f"❌ Unexpected error crawling {pal_id}: {e}")
            break
    
    print(f"❌ Failed to crawl {pal_id} after {retries} attempts")
    return None

def main():
    # Complete list of all B variants (아종) from paldb.cc
    b_variants = [
        ("5B", "Foxparks_Cryst"),
        ("6B", "Fuack_Ignis"), 
        ("10B", "Pengullet_Lux"),
        ("11B", "Penking_Lux"),
        ("12B", "Jolthog_Cryst"),
        ("23B", "Killamari_Primo"),
        ("24B", "Mau_Cryst"),
        ("25B", "Celaray_Lux"),
        ("31B", "Gobfin_Ignis"),
        ("32B", "Hangyu_Cryst"),
        ("33B", "Mossanda_Lux"),
        ("35B", "Caprity_Noct"),
        ("37B", "Eikthyrdeer_Terra"),
        ("39B", "Ribbuny_Botan"),
        ("40B", "Incineram_Noct"),
        ("43B", "Dumud_Gild"),
        ("45B", "Leezpunk_Ignis"),
        ("46B", "Loupmoon_Cryst"),
        ("48B", "Robinquill_Terra"),
        ("49B", "Gorirat_Terra"),
        ("55B", "Chillet_Ignis"),
        ("58B", "Pyrin_Noct"),
        ("61B", "Kitsun_Noct"),
        ("62B", "Dazzi_Noct"),
        ("64B", "Dinossom_Lux"),
        ("65B", "Surfent_Terra"),
        ("71B", "Vanwyrm_Cryst"),
        ("72B", "Bushi_Noct"),
        ("75B", "Katress_Ignis"),
        ("76B", "Wixen_Noct"),
        ("80B", "Elphidran_Aqua"),
        ("81B", "Kelpsea_Ignis"),
        ("82B", "Azurobe_Cryst"),
        ("83B", "Cryolinx_Terra"),
        ("84B", "Blazehowl_Noct"),
        ("85B", "Relaxaurus_Lux"),
        ("86B", "Broncherry_Aqua"),
        ("88B", "Reptyro_Cryst"),
        ("89B", "Kingpaca_Cryst"),
        ("90B", "Mammorest_Cryst"),
        ("91B", "Wumpo_Botan"),
        ("92B", "Warsect_Terra"),
        ("93B", "Fenglope_Lux"),
        ("95B", "Quivern_Botan"),
        ("96B", "Blazamut_Ryu"),
        ("97B", "Helzephyr_Lux"),
        ("99B", "Menasting_Terra"),
        ("101B", "Jormuntide_Ignis"),
        ("102B", "Suzaku_Aqua"),
        ("104B", "Lyleen_Noct"),
        ("105B", "Faleris_Aqua"),
        ("110B", "Frostallion_Noct"),
        ("112B", "Bellanoir_Libero"),
        ("114B", "Croajiro_Noct"),
        ("116B", "Shroomer_Noct"),
        ("148B", "Turtacle_Terra"),
        ("152B", "Finsider_Ignis"),
        ("153B", "Ghangler_Ignis"),
        ("154B", "Whalaska_Ignis")
    ]
    
    print(f"Starting to crawl {len(b_variants)} B variants...")
    
    all_results = []
    successful_crawls = 0
    
    for i, (pal_id, pal_name) in enumerate(b_variants, 1):
        print(f"\n[{i}/{len(b_variants)}] Processing {pal_id} - {pal_name}")
        
        result = crawl_pal_info_enhanced(pal_id, pal_name)
        if result:
            all_results.append(result)
            successful_crawls += 1
        
        # Add delay between requests
        time.sleep(1)
        
        # Save progress every 10 pals
        if i % 10 == 0:
            print(f"\n💾 Saving progress... ({successful_crawls}/{i} successful)")
            with open(f'b_variants_progress_{i}.json', 'w', encoding='utf-8') as f:
                json.dump(all_results, f, ensure_ascii=False, indent=2)
    
    # Save final results
    print(f"\n🎉 Crawling completed! Successfully crawled {successful_crawls}/{len(b_variants)} B variants")
    
    # Save JSON
    with open('complete_b_variants_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    
    # Create summary
    summary = {
        "total_b_variants": len(b_variants),
        "successful_crawls": successful_crawls,
        "failed_crawls": len(b_variants) - successful_crawls,
        "total_active_skills": sum(len(r['activeSkills']) for r in all_results),
        "total_passive_skills": sum(len(r['passiveSkills']) for r in all_results),
        "crawled_variants": [r['pal_id'] for r in all_results]
    }
    
    with open('b_variants_summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    print(f"📊 Summary:")
    print(f"  - Total Active Skills: {summary['total_active_skills']}")
    print(f"  - Total Passive Skills: {summary['total_passive_skills']}")
    print(f"  - Success Rate: {successful_crawls/len(b_variants)*100:.1f}%")

if __name__ == "__main__":
    main() 