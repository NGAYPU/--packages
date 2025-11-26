# Simple Cam Package (hw7)

OpenCV를 활용하여 웹캠 영상을 흑백으로 필터링해주는 패키지입니다.

## 1. 패키지 구조
- `main.py`: 프로그램 진입점 및 예외 처리
- `simple_cam`:
    - `camera.py`: `cv2.VideoCapture`를 이용한 영상 캡처 및 리소스 관리 (`try-finally`)
    - `filters.py`: 영상 처리(Grayscale) 모듈

## 2. 설치 및 실행 방법
1. **가상환경 생성 및 활성화** (강의 p.30 참고)
   ```bash
   conda create -n my_cam python=3.10
   conda activate my_cam
