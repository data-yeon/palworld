import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

def scrape_paldb_via_ui_interaction():
    """
    드롭다운 UI를 직접 클릭하고 제어하는 방식으로 교배 데이터를 크롤링합니다.
    """
    url = 'https://paldb.cc/en/Breed'
    output_filename = 'paldb_breeding_data_ui_driven.csv'
    all_breeding_data = []
    driver = None

    try:
        print("크롬 드라이버 설정 중...")
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless') # 디버깅 시에는 주석 처리하여 브라우저를 직접 보세요.
        options.add_argument('--log-level=3')
        driver = webdriver.Chrome(service=service, options=options)
        wait = WebDriverWait(driver, 20)
        
        print(f"'{url}' 사이트에 접속 중...")
        driver.get(url)

        # 1. 조작할 드롭다운의 컨테이너를 먼저 찾습니다.
        print("Select2 드롭다운 컨테이너를 찾는 중...")
        select2_container = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span[aria-labelledby*='select2-child']"))
        )
        
        # 2. 드롭다운을 열어 총 몇 개의 팰이 있는지 확인합니다.
        select2_container.click()
        time.sleep(1)  # 로딩 대기
        
        options_ul = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.select2-results__options")))
        
        # 스크롤을 끝까지 내려서 모든 옵션을 로드
        last_height = driver.execute_script("return arguments[0].scrollHeight", options_ul)
        while True:
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", options_ul)
            time.sleep(0.5)
            new_height = driver.execute_script("return arguments[0].scrollHeight", options_ul)
            if new_height == last_height:
                break
            last_height = new_height
        
        initial_options = options_ul.find_elements(By.TAG_NAME, "li")
        pal_names_list = [opt.text.strip() for opt in initial_options if opt.text.strip()]
        total_pals = len(pal_names_list)
        print(f"총 {total_pals}마리의 팰을 확인했습니다. UI 제어 크롤링을 시작합니다.")
        print(f"팰 목록 예시: {pal_names_list[:5]}...")
        
        # 드롭다운을 닫고 시작
        driver.find_element(By.TAG_NAME, 'body').click()
        time.sleep(1)
        print("-" * 50)

        # 3. 인덱스(순서)를 기준으로 모든 팰을 순회합니다.
        for i in range(total_pals):
            pal_name_for_log = ""
            try:
                # --- 매 루프마다 드롭다운을 새로 열고 i번째 옵션을 선택 ---
                # 컨테이너를 다시 찾아 클릭
                select2_container = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "span[aria-labelledby*='select2-child']"))
                )
                select2_container.click()
                
                # 옵션 목록이 나타날 때까지 기다림
                options_ul = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.select2-results__options")))
                
                # 옵션 목록을 새로 가져와서 i번째 요소를 클릭 (Stale 에러 방지)
                current_options = options_ul.find_elements(By.TAG_NAME, "li")
                
                # 비어있지 않은 실제 옵션만 대상으로 인덱싱
                actual_options = [opt for opt in current_options if opt.text.strip()]
                if i >= len(actual_options):
                    print(f"오류: {i}번째 옵션을 찾을 수 없습니다.")
                    continue

                option_to_click = actual_options[i]
                pal_name_for_log = option_to_click.text
                print(f"({i+1}/{total_pals}) '{pal_name_for_log}' 선택 중...")
                
                option_to_click.click() # 옵션 클릭 (드롭다운이 자동으로 닫힘)

                # --- 결과 데이터 수집 ---
                # 잠시 기다린 후 결과 카드를 찾음
                time.sleep(2)
                
                try:
                    # 카드 형태의 결과를 찾음
                    result_container = driver.find_element(By.CSS_SELECTOR, "div.card-body.row")
                    print(f"    결과 컨테이너 찾음!")
                    
                    # 각 브리딩 조합 (col div)을 찾음
                    breeding_cols = result_container.find_elements(By.CSS_SELECTOR, "div.col")
                    
                    count = 0
                    for col in breeding_cols:
                        try:
                            # 각 col에서 텍스트를 가져와서 파싱
                            col_text = col.text.strip()
                            if '+' in col_text and '=' in col_text:
                                # "부모1+부모2=자식" 형식에서 부모1, 부모2 추출
                                parts = col_text.split('=')
                                if len(parts) == 2:
                                    parents_part = parts[0].strip()
                                    if '+' in parents_part:
                                        parent_names = parents_part.split('+')
                                        if len(parent_names) == 2:
                                            parent1 = parent_names[0].strip()
                                            parent2 = parent_names[1].strip()
                                            
                                            if parent1 and parent2:
                                                all_breeding_data.append({
                                                    'Child': pal_name_for_log, 
                                                    'Parent1': parent1, 
                                                    'Parent2': parent2
                                                })
                                                count += 1
                        except Exception as e:
                            print(f"      조합 처리 중 오류: {e}")
                            continue
                    
                    print(f"  └─ {count}개의 조합을 수집했습니다.")
                    
                except Exception as e:
                    print(f"    결과 컨테이너를 찾을 수 없습니다: {e}")

            except TimeoutException:
                print(f"  └─ '{pal_name_for_log}' 처리 중 시간 초과. 다음으로 넘어갑니다.")
            except StaleElementReferenceException:
                print(f"  └─ Stale Element 에러 발생. 다음 순번으로 재시도합니다.")
            except Exception as e:
                print(f"  └─ '{pal_name_for_log}' 처리 중 예상치 못한 오류 발생: {e}")
        
        print("-" * 50)
        print("크롤링 완료!")

    except Exception as e:
        print(f"스크립트 실행 중 오류가 발생했습니다: {e}")
    finally:
        if driver:
            driver.quit()

    if all_breeding_data:
        df = pd.DataFrame(all_breeding_data)
        df.to_csv(output_filename, index=False, encoding='utf-8-sig')
        print(f"\n성공! 총 {len(df)}개의 교배 조합을 '{output_filename}' 파일에 저장했습니다.")
    else:
        print("수집된 데이터가 없습니다. 파일이 생성되지 않았습니다.")

if __name__ == '__main__':
    scrape_paldb_via_ui_interaction()