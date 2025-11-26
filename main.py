import sys
import os

# 현재 폴더 경로를 파이썬이 인식하도록 설정
sys.path.append(os.getcwd())

from simple_cam import camera

if __name__ == "__main__":
    print("=== 나만의 필터 카메라 과제 ===")
    try:
        # [과제 요구사항] 패키지 실행
        camera.run()
    except Exception as e:
        # [과제 요구사항] 예외 처리
        print(f"[오류 발생] {e}")
        input("엔터를 누르면 종료합니다...")
