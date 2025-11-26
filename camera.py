import cv2
from . import filters

def run(cam_index=0):
    vid = cv2.VideoCapture(cam_index)
    
    # [과제 요구사항] 예외 발생 (raise)
    if not vid.isOpened():
        raise RuntimeError(f"카메라(Index {cam_index})를 찾을 수 없습니다. 연결을 확인하세요.")

    print("카메라가 실행되었습니다. 종료하려면 'q'를 누르세요.")

    try:
        while True:
            ret, frame = vid.read()
            if not ret:
                raise ValueError("프레임을 읽어올 수 없습니다.")

            # 필터 모듈 사용
            gray_frame = filters.to_gray(frame)

            cv2.imshow("Original", frame)
            cv2.imshow("Gray Filter", gray_frame)

            if cv2.waitKey(1) == ord("q"):
                break
    finally:
        # [과제 요구사항] 자원 해제 (finally)
        vid.release()
        cv2.destroyAllWindows()
        print("카메라가 종료되었습니다.")
