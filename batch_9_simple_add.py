#!/usr/bin/env python3

def add_batch_9_simple():
    """4개의 새로운 B variants를 기존 CSV에 간단하게 추가"""
    
    # 새로운 B variants 데이터 (기존 CSV 구조에 맞춘 형태)
    new_rows = [
        "40B,아비스고트,어린 팰만 노려 자기 구역에 데리고 간다. 아이를 빼앗긴 부모 팰이 얼마나 절망에 빠졌을지 상상도 안 된다,[어둠],암흑 발톱의 사냥꾼,발동하면 목표로 삼은 적을 향해 높은 위력의 지옥불 할퀴기로 공격한다,,,1,M,5,95,300,150,105,85,100,100,1,50,580,4870,암흑의 대형 알,Baphomet_Dark,80,160,700,960,320,4838,765,588,파이어 샷;스피릿 파이어;불화살;지옥불 할퀴기;그림자 폭발;화염구;인페르노,7,,0,뿔 1;가죽 1,2,수작업 Lv2;채굴 Lv1;운반 Lv2,3,,0,,0",
        "58B,사라블랙,정체불명의 암흑 물질을 태워 에너지로 삼으며 남은 어둠의 입자를 전신에서 방출한다. 누군가 탑승하면 그가 어둠에 물들지 않도록 눈치 있게 배려하는 면도 있다,[화염;어둠],흑토마,등에 타고 이동할 수 있다. 탑승 중 플레이어의 공격이 어둠 속성으로 변화한다,사라블랙 안장,34,1,L,7,100,350,110,95,90,100,100,1,50,240,7270,열기 나는 대형 알,FireKirin_Dark,100,150,850,1300,500,5050,702,620,파이어 샷;그림자 폭발;파이어 브레스;유령의 불꽃;어둠의 돌격;인페르노;어둠의 레이저,7,,0,발화 기관 4-5;가죽 2-3,2,불 피우기 Lv2;벌목 Lv1,2,,0,,0",
        "85B,핑피롱,헤로롱은 생각했다. 슬슬 자신을 바꿀 때라고. 그 순간 전신에 전기가 흘렀다!,[용;번개],미사일 파티,등에 타고 이동할 수 있다. 탑승 중 미사일 발사기 연사가 가능해진다,핑피롱의 미사일 발사기,46,1,XL,9,110,475,110,110,75,100,100,1,50,270,10380,용의 거대한 알,LazyDragon_Electric,40,60,650,1000,150,5472,797,525,스파크 샷;용 대포;전기 파장;라인 썬더;용의 숨결;번개 일격;전기 볼트,7,,0,고급 팰 기름 1-4;발전 기관 2-3;사파이어 1,3,발전 Lv3;운반 Lv1,2,,0,,0",
        "99B,골드 스팅,본체는 에너지 덩어리로 속이 비었다. 토사나 광물을 외피 속에 채워 압도적인 질량을 보여준다. 공격한 상대는 지옥 같은 신음을 내지를 수밖에 없다,[땅],스틸 스콜피온,함께 싸우는 동안 플레이어의 방어력이 증가하고 번개 속성 팰을 쓰러뜨렸을 때 드롭 아이템 획득량이 증가한다,,,1,L,10,100,475,100,105,130,100,100,1,50,250,8050,거친 느낌의 거대한 알,DarkScorpion_Ground,100,200,1000,1200,600,5050,765,873,모래 돌풍;바위 폭발;바위 대포;모래 폭풍;점프 찌르기;바위 창;암석 폭발,7,,0,원유 1;발화 기관 1-2,2,벌목 Lv2;채굴 Lv3,2,,0,,0"
    ]
    
    print("🚀 Batch 9 간단 추가 시작...")
    
    # 기존 CSV 파일 읽기
    try:
        with open('enhanced_complete_pals_batch8_mega.csv', 'r', encoding='utf-8') as f:
            existing_content = f.read()
        print("✅ 기존 CSV 로드 완료")
    except FileNotFoundError:
        print("❌ enhanced_complete_pals_batch8_mega.csv 파일을 찾을 수 없습니다!")
        return
    
    # 새로운 행들 추가
    new_content = existing_content
    for i, row in enumerate(new_rows):
        new_content += "\n" + row
        print(f"✅ {i+1}번째 B variant 추가 완료")
    
    # 새로운 파일 저장
    output_filename = 'enhanced_complete_pals_batch9_mega.csv'
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    # 결과 출력
    total_lines = new_content.count('\n') + 1 - 1  # 헤더 제외
    print(f"\n🎉 Batch 9 완료!")
    print(f"📊 총 팰 개수: {total_lines}개")
    print(f"💾 파일명: {output_filename}")
    print(f"🆕 이번에 추가된 B variants: 4개")
    
    # 간단한 B variants 개수 확인
    b_count = new_content.count('B,')
    print(f"🔢 총 B variants (대략): {b_count}개")
    print(f"📈 완성도 (대략): {b_count}/59 = {b_count/59*100:.1f}%")

if __name__ == "__main__":
    add_batch_9_simple() 