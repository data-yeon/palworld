import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time
import re
from urllib.parse import urljoin

def extract_active_skills_korean(soup):
    """Extract active skills from Korean paldb.cc page"""
    skills = []
    
    # Find the Active Skills section header
    active_skills_header = None
    for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5']):
        if header and header.get_text(strip=True) == "Active Skills":
            active_skills_header = header
            break
    
    if active_skills_header:
        # Get the next sibling elements that contain skill data
        current = active_skills_header.find_next_sibling()
        
        while current and not (current.name in ['h1', 'h2', 'h3', 'h4', 'h5'] and current.get_text(strip=True) in ['Passive Skills', '패시브 스킬', 'Possible Drops']):
            if current.name:
                # Look for skill patterns in text
                text = current.get_text(separator=' ', strip=True)
                
                # Pattern: "Lv. X [Korean Name](link)" followed by attributes
                skill_match = re.search(r'Lv\.\s*(\d+)\s*\[([^\]]+)\]', text)
                if skill_match:
                    level = int(skill_match.group(1))
                    korean_name = skill_match.group(2).strip()
                    
                    # Look for English name in the text or linked content
                    english_name = ""
                    
                    # Find power, cooltime, element in the following text
                    power_match = re.search(r'위력:\s*(\d+)', text)
                    cooltime_match = re.search(r'[\u4e00-\u9fff:]\s*(\d+)', text)  # Look for cooltime with icon/symbol
                    
                    # Check for element type - look for specific Korean terms
                    element = None
                    if '얼음 속성' in text or 'Ice' in text:
                        element = "Ice"
                    elif '불 속성' in text or 'Fire' in text:
                        element = "Fire"
                    elif '물 속성' in text or 'Water' in text:
                        element = "Water"
                    elif '전기 속성' in text or 'Electric' in text:
                        element = "Electric"
                    elif '풀 속성' in text or 'Grass' in text:
                        element = "Grass"
                    elif '땅 속성' in text or 'Ground' in text:
                        element = "Ground"
                    elif '어둠 속성' in text or 'Dark' in text:
                        element = "Dark"
                    elif '용 속성' in text or 'Dragon' in text:
                        element = "Dragon"
                    elif '무속성' in text or 'Neutral' in text:
                        element = "Neutral"
                    
                    skill = {
                        "name": korean_name,
                        "english_name": english_name,
                        "level": level,
                        "power": int(power_match.group(1)) if power_match else None,
                        "cooltime": None,  # Will extract from different pattern
                        "element": element,
                        "description": None
                    }
                    
                    # Look for cooltime in a more specific pattern
                    cooltime_lines = text.split('\n')
                    for line in cooltime_lines:
                        if ':' in line and any(char.isdigit() for char in line):
                            # Try to find numeric value after colon
                            parts = line.split(':')
                            if len(parts) > 1:
                                number_match = re.search(r'(\d+)', parts[1])
                                if number_match and not power_match:  # Avoid confusion with power
                                    skill["cooltime"] = int(number_match.group(1))
                                    break
                    
                    skills.append(skill)
            
            current = current.find_next_sibling()
    
    return skills

def extract_passive_skills_korean(soup):
    """Extract passive skills from Korean paldb.cc page"""
    passive_skills = []
    
    # Find the Passive Skills section
    passive_skills_header = None
    for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5']):
        if header and header.get_text(strip=True) == "Passive Skills":
            passive_skills_header = header
            break
    
    if passive_skills_header:
        # Get content after the header until next major section
        current = passive_skills_header.find_next_sibling()
        
        while current and not (current.name in ['h1', 'h2', 'h3', 'h4', 'h5'] and current.get_text(strip=True) in ['Possible Drops', 'Tribes']):
            if current.name and current.get_text(strip=True):
                text = current.get_text(strip=True)
                
                # Look for passive skill patterns
                # Pattern might be different, so we'll look for any text that could be skills
                if text and len(text) > 3 and not text.startswith('Passive Skills'):
                    # This is a simplified approach - you may need to adjust based on actual structure
                    if '(' in text and ')' in text:
                        # Assume it's a skill name pattern
                        match = re.search(r'([^(]+)\(([^)]+)\)', text)
                        if match:
                            korean_name = match.group(1).strip()
                            english_name = match.group(2).strip()
                            passive_skills.append({
                                "name": korean_name,
                                "english_name": english_name
                            })
            
            current = current.find_next_sibling()
    
    return passive_skills

def crawl_pal_info_improved(pal_id, pal_name, retries=3):
    """Improved crawling function for Korean pages"""
    url = f"https://paldb.cc/ko/{pal_name}"
    
    for attempt in range(retries):
        try:
            print(f"Attempting to crawl {pal_id} ({pal_name}) - Attempt {attempt + 1}")
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
            }
            
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract skills using improved methods
            active_skills = extract_active_skills_korean(soup)
            passive_skills = extract_passive_skills_korean(soup)
            
            # If no skills found, try alternative parsing
            if not active_skills:
                # Try to find any text containing "Lv." and skill patterns
                all_text = soup.get_text()
                lv_patterns = re.findall(r'Lv\.\s*(\d+)\s*\[([^\]]+)\][^위]*위력:\s*(\d+)', all_text)
                for pattern in lv_patterns:
                    level, name, power = pattern
                    active_skills.append({
                        "name": name.strip(),
                        "english_name": "",
                        "level": int(level),
                        "power": int(power),
                        "cooltime": None,
                        "element": None,
                        "description": None
                    })
            
            pal_data = {
                "pal_id": pal_id,
                "pal_name": pal_name,
                "url": url,
                "activeSkills": active_skills,
                "passiveSkills": passive_skills,
                "raw_html_length": len(response.content),
                "parsing_method": "improved_korean"
            }
            
            print(f"✅ Successfully crawled {pal_id}: {len(pal_data['activeSkills'])} active skills, {len(pal_data['passiveSkills'])} passive skills")
            
            # Debug: print first skill if found
            if active_skills:
                print(f"   First active skill: {active_skills[0]['name']} (Lv.{active_skills[0]['level']}, Power: {active_skills[0]['power']})")
            
            return pal_data
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error crawling {pal_id} (attempt {attempt + 1}): {e}")
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
            continue
        except Exception as e:
            print(f"❌ Unexpected error crawling {pal_id}: {e}")
            break
    
    print(f"❌ Failed to crawl {pal_id} after {retries} attempts")
    return None

def main():
    # Test with a few B variants first
    test_variants = [
        ("5B", "Foxparks_Cryst"),
        ("6B", "Fuack_Ignis"), 
        ("10B", "Pengullet_Lux"),
        ("11B", "Penking_Lux"),
        ("12B", "Jolthog_Cryst")
    ]
    
    print(f"Testing improved crawler with {len(test_variants)} B variants...")
    
    all_results = []
    successful_crawls = 0
    
    for i, (pal_id, pal_name) in enumerate(test_variants, 1):
        print(f"\n[{i}/{len(test_variants)}] Processing {pal_id} - {pal_name}")
        
        result = crawl_pal_info_improved(pal_id, pal_name)
        if result:
            all_results.append(result)
            successful_crawls += 1
        
        time.sleep(2)  # Be respectful to the server
    
    # Save test results
    print(f"\n🎉 Test completed! Successfully crawled {successful_crawls}/{len(test_variants)} B variants")
    
    with open('improved_b_variants_test.json', 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    
    # Summary
    total_active = sum(len(r['activeSkills']) for r in all_results)
    total_passive = sum(len(r['passiveSkills']) for r in all_results)
    
    print(f"📊 Test Summary:")
    print(f"  - Total Active Skills: {total_active}")
    print(f"  - Total Passive Skills: {total_passive}")
    print(f"  - Success Rate: {successful_crawls/len(test_variants)*100:.1f}%")
    
    if total_active > 0:
        print(f"✅ Improved crawler is working! Ready to run on all B variants.")
    else:
        print(f"❌ Still need to improve the parsing logic.")

if __name__ == "__main__":
    main() 