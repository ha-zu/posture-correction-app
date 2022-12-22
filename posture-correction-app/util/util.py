import cv2 as cv
from config import constant_list as const


def put_text(image, landmark_x, landmark_y):
    """Coordinate put screan"""
    image_height, image_width, _ = image.shape
    x = int(landmark_x * image_width)
    y = int(landmark_y * image_height)
    # Put text
    text = f"[x:{round(landmark_x, 3)}, y:{round(landmark_y, 3)}]"
    # print in image
    cv.putText(
        image,
        text,
        (x - 10, y - 10),
        cv.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2,
        cv.LINE_AA,
    )

def put_points(image, landmark_x, landmark_y):
    cv.circle(
        image,
        (
            int(landmark_x * const.VIDEO_FRAME_WIDTH),
            int(landmark_y * const.VIDEO_FRAME_HEIGHT),
        ),
        7,
        (0, 255, 255),
        -1,
        )

def logging_points(txt, landmark_x, landmark_y):
    log_txt = f"[{txt}=X:{landmark_x}, Y:{landmark_y}]"
    print(log_txt)