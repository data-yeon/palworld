#!/usr/bin/env python3
import os
import csv
import shutil

def main():
    # CSV 파일에서 ID-이름 매핑 읽기
    id_to_name = {}
    name_to_id = {}
    
    with open('assets/data/pal_list.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 헤더 스킵
        
        for row in reader:
            if len(row) >= 2:
                pal_id = row[0].strip()
                pal_name = row[1].strip()
                id_to_name[pal_id] = pal_name
                name_to_id[pal_name] = pal_id
    
    # 이미지 폴더 경로
    image_dir = 'assets/images/pals'
    
    # 백업 폴더 생성
    backup_dir = 'assets/images/pals_backup'
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        print(f"백업 폴더 생성: {backup_dir}")
    
    # 현재 이미지 파일들 목록
    image_files = [f for f in os.listdir(image_dir) if f.endswith('.webp')]
    
    renamed_count = 0
    not_found_count = 0
    
    print(f"총 {len(image_files)}개의 이미지 파일 처리 중...")
    
    for image_file in image_files:
        # 파일명에서 팰 이름 추출 (확장자와 _menu 제거)
        base_name = image_file.replace('_menu.webp', '')
        
        # 공백을 언더스코어로 바꾼 이름들을 원래 이름으로 변환 시도
        possible_names = [
            base_name,
            base_name.replace('_', ' '),
        ]
        
        found_id = None
        found_name = None
        
        # 가능한 이름들로 ID 찾기
        for possible_name in possible_names:
            if possible_name in name_to_id:
                found_id = name_to_id[possible_name]
                found_name = possible_name
                break
        
        if found_id:
            # 원본 파일 경로와 새 파일 경로
            old_path = os.path.join(image_dir, image_file)
            new_filename = f"{found_id}_menu.webp"
            new_path = os.path.join(image_dir, new_filename)
            backup_path = os.path.join(backup_dir, image_file)
            
            # 백업 생성
            shutil.copy2(old_path, backup_path)
            
            # 파일명 변경
            if old_path != new_path:  # 이름이 실제로 다른 경우만
                os.rename(old_path, new_path)
                print(f"✅ {image_file} → {new_filename} (ID: {found_id}, Name: {found_name})")
                renamed_count += 1
            else:
                print(f"⏭️  {image_file} (이미 올바른 이름)")
        else:
            print(f"❌ {image_file} - 매칭되는 팰을 찾을 수 없음")
            not_found_count += 1
    
    print(f"\n작업 완료!")
    print(f"✅ 이름 변경: {renamed_count}개")
    print(f"❌ 매칭 실패: {not_found_count}개")
    print(f"💾 백업 위치: {backup_dir}")
    
    if not_found_count > 0:
        print(f"\n매칭되지 않은 파일들을 수동으로 확인해주세요.")

if __name__ == "__main__":
    main() 