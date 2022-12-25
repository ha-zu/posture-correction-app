import cv2 as cv
from config import constant_list as const


def put_text(image, points, angle = None):
    """Coordinate put screan"""
    image_height, image_width, _ = image.shape
    x = int(points[const.X_COORDINATE] * image_width)
    y = int(points[const.Y_COORDINATE] * image_height)
    # Put text
    if angle is None:
        text = f"[x:{round(points[0], 3)}, y:{round(points[1], 3)}]"
    else:
        text = f"[x:{round(points[0], 3)}, y:{round(points[1], 3)}, angle:{round(angle, 1)}]"

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


def put_points(image, points):
    cv.circle(
        image,
        (
            int(points[const.X_COORDINATE] * const.VIDEO_FRAME_WIDTH),
            int(points[const.Y_COORDINATE] * const.VIDEO_FRAME_HEIGHT),
        ),
        7,
        (0, 255, 255),
        5,
        )


def put_line(image, pt1, pt2, color):
    cv.line(
        image,
        (
            int(pt1[const.X_COORDINATE] * const.VIDEO_FRAME_WIDTH),
            int(pt1[const.Y_COORDINATE] * const.VIDEO_FRAME_HEIGHT)
        ),
        (
            int(pt2[const.X_COORDINATE] * const.VIDEO_FRAME_WIDTH),
            int(pt2[const.Y_COORDINATE] * const.VIDEO_FRAME_HEIGHT)
        ),
        color,
        2,
        cv.LINE_4,
        0
    )

def logging_points(txt, landmark_x, landmark_y):
    log_txt = f"[{txt}=X:{landmark_x}, Y:{landmark_y}]"
    print(log_txt)
