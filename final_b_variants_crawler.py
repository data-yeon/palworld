import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time
import re
from urllib.parse import urljoin

def extract_skills_from_text(html_content):
    """Extract skills directly from HTML text using regex patterns"""
    active_skills = []
    passive_skills = []
    
    # Convert to text for easier regex matching
    text = html_content
    
    # Pattern for Active Skills: "Lv. X [Skill Name]" followed by attributes
    # Example: "Lv. 1 [얼음 미사일]...얼음 속성...위력: 30"
    
    active_skill_pattern = r'Lv\.\s*(\d+)\s*\[([^\]]+)\][^L]*?(?:얼음|불|물|전기|풀|땅|어둠|용|무속성)\s*속성[^L]*?위력:\s*(\d+)'
    
    matches = re.findall(active_skill_pattern, text, re.DOTALL)
    
    for match in matches:
        level = int(match[0])
        name = match[1].strip()
        power = int(match[2])
        
        # Extract element and cooltime from the full match
        full_match = re.search(
            rf'Lv\.\s*{level}\s*\[{re.escape(name)}\][^L]*?(?P<element>얼음|불|물|전기|풀|땅|어둠|용|무속성)\s*속성[^L]*?위력:\s*{power}[^L]*?(?::\s*(?P<cooltime>\d+))?',
            text, re.DOTALL
        )
        
        element_map = {
            '얼음': 'Ice',
            '불': 'Fire', 
            '물': 'Water',
            '전기': 'Electric',
            '풀': 'Grass',
            '땅': 'Ground',
            '어둠': 'Dark',
            '용': 'Dragon',
            '무속성': 'Neutral'
        }
        
        element = None
        cooltime = None
        
        if full_match:
            korean_element = full_match.group('element')
            element = element_map.get(korean_element, korean_element)
            if full_match.group('cooltime'):
                cooltime = int(full_match.group('cooltime'))
        
        active_skills.append({
            "name": name,
            "english_name": "",
            "level": level,
            "power": power,
            "cooltime": cooltime,
            "element": element,
            "description": None
        })
    
    # Alternative pattern if the first one doesn't work
    if not active_skills:
        # More flexible pattern
        alt_pattern = r'Lv\.\s*(\d+)[^[]*\[([^\]]+)\]'
        alt_matches = re.findall(alt_pattern, text)
        
        for alt_match in alt_matches:
            level = int(alt_match[0])
            name = alt_match[1].strip()
            
            # Look for power near this skill
            power_search = re.search(rf'{re.escape(name)}[^위]*위력:\s*(\d+)', text)
            power = int(power_search.group(1)) if power_search else None
            
            if power:  # Only add if we found power
                active_skills.append({
                    "name": name,
                    "english_name": "",
                    "level": level,
                    "power": power,
                    "cooltime": None,
                    "element": None,
                    "description": None
                })
    
    # Look for passive skills (usually after "Passive Skills" header)
    passive_section = re.search(r'Passive Skills(.*?)(?:Possible Drops|Tribes|$)', text, re.DOTALL | re.IGNORECASE)
    
    if passive_section:
        passive_text = passive_section.group(1)
        # Look for patterns like "Korean Name (English Name)"
        passive_matches = re.findall(r'([^(]+)\(([^)]+)\)', passive_text)
        
        for passive_match in passive_matches:
            korean_name = passive_match[0].strip()
            english_name = passive_match[1].strip()
            
            # Filter out obvious non-skill text
            if len(korean_name) > 1 and len(english_name) > 1 and not any(word in korean_name.lower() for word in ['http', 'www', 'image', 'icon']):
                passive_skills.append({
                    "name": korean_name,
                    "english_name": english_name
                })
    
    return active_skills, passive_skills

def crawl_pal_info_final(pal_id, pal_name, retries=3):
    """Final attempt at crawling with direct text analysis"""
    url = f"https://paldb.cc/ko/{pal_name}"
    
    for attempt in range(retries):
        try:
            print(f"Attempting to crawl {pal_id} ({pal_name}) - Attempt {attempt + 1}")
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'ko-KR,ko;q=0.9,en;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
            }
            
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            # Get the raw text content
            raw_content = response.text
            
            # Extract skills using direct text analysis
            active_skills, passive_skills = extract_skills_from_text(raw_content)
            
            pal_data = {
                "pal_id": pal_id,
                "pal_name": pal_name,
                "url": url,
                "activeSkills": active_skills,
                "passiveSkills": passive_skills,
                "raw_html_length": len(raw_content),
                "parsing_method": "direct_text_regex"
            }
            
            print(f"✅ Successfully crawled {pal_id}: {len(pal_data['activeSkills'])} active skills, {len(pal_data['passiveSkills'])} passive skills")
            
            # Debug output
            if active_skills:
                print(f"   First active skill: {active_skills[0]['name']} (Lv.{active_skills[0]['level']}, Power: {active_skills[0]['power']}, Element: {active_skills[0]['element']})")
            
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
    # Test with the same variants
    test_variants = [
        ("5B", "Foxparks_Cryst"),
        ("6B", "Fuack_Ignis"), 
        ("10B", "Pengullet_Lux"),
        ("11B", "Penking_Lux"),
        ("12B", "Jolthog_Cryst")
    ]
    
    print(f"Testing final crawler with {len(test_variants)} B variants...")
    
    all_results = []
    successful_crawls = 0
    
    for i, (pal_id, pal_name) in enumerate(test_variants, 1):
        print(f"\n[{i}/{len(test_variants)}] Processing {pal_id} - {pal_name}")
        
        result = crawl_pal_info_final(pal_id, pal_name)
        if result:
            all_results.append(result)
            successful_crawls += 1
        
        time.sleep(2)
    
    # Save test results
    print(f"\n🎉 Final test completed! Successfully crawled {successful_crawls}/{len(test_variants)} B variants")
    
    with open('final_b_variants_test.json', 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    
    # Summary
    total_active = sum(len(r['activeSkills']) for r in all_results)
    total_passive = sum(len(r['passiveSkills']) for r in all_results)
    
    print(f"📊 Final Test Summary:")
    print(f"  - Total Active Skills: {total_active}")
    print(f"  - Total Passive Skills: {total_passive}")
    print(f"  - Success Rate: {successful_crawls/len(test_variants)*100:.1f}%")
    
    if total_active > 0:
        print(f"✅ Final crawler is working! Ready to run on all B variants.")
        return True
    else:
        print(f"❌ Still need to debug the parsing logic.")
        
        # Debug: Show sample of raw content
        if all_results:
            sample_result = all_results[0]
            print(f"\n🔍 Debug info for {sample_result['pal_id']}:")
            print(f"   - Raw HTML length: {sample_result['raw_html_length']}")
            print(f"   - URL: {sample_result['url']}")
        
        return False

if __name__ == "__main__":
    main() 