#!/usr/bin/env python3

def add_batch_10_ultra_mega():
    """새로 발견한 4개 팰(3개 일반 + 1개 B variant)을 기존 CSV에 추가"""
    
    # 새로운 팰들 데이터 (기존 CSV 구조에 맞춘 형태)
    new_rows = [
        # 108 팔라디우스 (Paladius) - 무속성, 3단 점프 탈것
        "108,팔라디우스,원래 켄타나이트의 일종이었다. 나쁜 감정을 제거한 존재로 여겨지나 눈동자 속에선 일말의 증오가 번뜩인다,[무속성],하늘을 나는 성기사,등에 타고 이동할 수 있다. 탑승 중 3단 점프가 가능해진다,팔라디우스 안장,49,1,L,20,130,600,110,120,145,100,100,1,50,80,8810,평범하고 거대한 알,SaintCentaur,50,100,800,1800,450,6317,860,968,파워 샷;얼음 미사일;빙산;파워 폭탄;눈보라 스파이크;창기병 돌격;팰 폭발;프로스트 아웃;신성 폭발,9,전설;성천,2,팰 금속 주괴 10;다이아몬드 1,2,벌목 Lv2;채굴 Lv2,2,,0,,0",
        
        # 112 벨라누아르 (Bellanoir) - 어둠 속성
        "112,벨라누아르,존재도 없이 그저 조용히 세계를 바라볼 뿐이었다. 언제부터인가 누군가의 시선을 갈망하게 됐다. 외부 세계를 적대시하던 욕망의 덩어리는 광란의 숙녀라고 정의되었다,[어둠],악몽의 눈동자,발동하면 목표로 삼은 적을 향해 높은 위력의 악몽의 빛으로 공격한다,,,1,M,20,120,300,100,150,100,100,100,1,10,1,10030,암흑의 거대한 알,NightLady,100,150,600,800,400,5895,1050,683,어둠 대포;어둠 파장;어둠 화살;유령의 불꽃;악몽의 구체;아포칼립스;악몽의 빛,7,,0,,0,수작업 Lv2;제약 Lv4;운반 Lv2,3,,0,,0",
        
        # 112B 벨라루주 (Bellanoir_Libero) - 어둠 속성 B variant  
        "112B,벨라루주,풀려난 욕망은 끝내 가라앉지 못했다. 나를 바라보는 나를 갈망했다. 외부 세계를 적대시하던 응시하는 자매는 결국 구석까지 내몰린 채 서서히 눈을 감게 되었다,[어둠],악몽의 시선,발동하면 목표로 삼은 적을 향해 높은 위력의 악몽의 빛줄기로 공격한다,,,1,M,20,120,300,100,150,100,100,100,1,10,1,10030,암흑의 거대한 알,NightLady_Dark,100,150,600,800,400,5895,1050,683,어둠 대포;어둠 파장;어둠 화살;악몽의 구체;아포칼립스;화염 왈츠;악몽의 빛줄기,7,마녀,1,,0,수작업 Lv2;제약 Lv4;운반 Lv2,3,,0,,0",
        
        # 113 셀레문 (Selyne) - 어둠+무속성, 비행형 탈것
        "113,셀레문,등 뒤에 떠다니는 달처럼 생긴 물체는 세대를 거듭할 때마다 아주 조금씩 원형에 가까워진다고 한다. 그 달이 완전히 찼을 때 무슨 일이 벌어질지는 아무도 모른다,[어둠;무속성],셀레스티얼 다크니스,등에 있는 달을 타고 하늘을 날 수 있다. 탑승 중 무속성 및 어둠 속성 공격이 강화된다,셀레문 안장,53,1,L,9,130,150,100,115,110,100,100,1,20,345,9500,암흑의 거대한 알,MoonQueen,60,150,1000,1600,275,6317,828,747,어둠 대포;어둠 화살;에어 블레이드;신성 폭발;청월의 칼날;스타 마인;월광선,7,,0,천 1-2;사파이어 2-3;귀중한 발톱 1,3,수작업 Lv4;제약 Lv3;운반 Lv3,3,,0,,0"
    ]
    
    print("🚀 Batch 10 ULTRA MEGA 추가 시작...")
    print("🆕 4개의 새로운 팰을 추가합니다:")
    print("- 108 팔라디우스 (일반 팰)")
    print("- 112 벨라누아르 (일반 팰)")
    print("- 112B 벨라루주 (B variant)")
    print("- 113 셀레문 (일반 팰)")
    
    # 기존 CSV 파일 읽기
    try:
        with open('enhanced_complete_pals_batch9_mega.csv', 'r', encoding='utf-8') as f:
            existing_content = f.read()
        print("✅ 기존 CSV 로드 완료")
    except FileNotFoundError:
        print("❌ enhanced_complete_pals_batch9_mega.csv 파일을 찾을 수 없습니다!")
        return
    
    # 새로운 행들 추가
    new_content = existing_content
    for i, row in enumerate(new_rows):
        new_content += "\n" + row
        pal_info = row.split(',')
        print(f"✅ {pal_info[0]} {pal_info[1]} 추가 완료")
    
    # 새로운 파일 저장
    output_filename = 'enhanced_complete_pals_batch10_ultra_mega.csv'
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    # 결과 출력
    total_lines = new_content.count('\n') + 1 - 1  # 헤더 제외
    print(f"\n🎉 Batch 10 ULTRA MEGA 완료!")
    print(f"📊 총 팰 개수: {total_lines}개")
    print(f"💾 파일명: {output_filename}")
    print(f"🆕 이번에 추가된 팰: 4개 (일반 3개 + B variant 1개)")
    
    # 간단한 B variants 개수 확인
    b_count = new_content.count('B,')
    regular_count = total_lines - b_count
    print(f"🔢 일반 팰: {regular_count}개")
    print(f"🔢 B variants: {b_count}개")
    print(f"📈 B variants 완성도 (대략): {b_count}/59 = {b_count/59*100:.1f}%")
    
    print(f"\n🎯 대박 성과!")
    print(f"- 기존 115개 → 현재 {regular_count}개 일반 팰 (+{regular_count-115}개 증가)")
    print(f"- B variants 41개 → {b_count}개 (+{b_count-41}개 증가)")
    print(f"- 전체 데이터베이스가 대폭 확장되었습니다! 🚀")

if __name__ == "__main__":
    add_batch_10_ultra_mega() 