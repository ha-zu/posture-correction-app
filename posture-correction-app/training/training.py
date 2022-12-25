import cv2 as cv
import mediapipe as mp
import math
import os
import pandas as pd
from config import constant_list as const
from util import util


def get_xy_points(landmarks):
    x = landmarks.x
    y = landmarks.y

    return (x, y)

def get_head_points(landmarks):
    pass

def get_traking_landmark(landmarks):
    # Tra
    pass

def train_squat():
    wkdir = os.getcwd()
    # Top right (0, 0)
    mp_pose = mp.solutions.pose
    with mp_pose.Pose(
        model_complexity=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as pose:

        cap = cv.VideoCapture(const.VIDEO_CAMERA_MAC)
        cap.set(cv.CAP_PROP_FRAME_WIDTH, const.VIDEO_FRAME_WIDTH)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, const.VIDEO_FRAME_HEIGHT)
        fmt = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
        writer = cv.VideoWriter(wkdir + '/data/test.mp4', fmt, const.FRAME_RATE, const.VIDEO_SIZE)

        data = []

        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("error can not opened capture.")
                break

            # Image write off
            image.flags.writeable = False
            # Inverted with respect to Y axis
            # Detected inverted right and left
            image = cv.flip(image, 1)
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            points = pose.process(image)
            image.flags.writeable = True
            image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

            landmarks = points.pose_landmarks.landmark
            key_points = mp_pose.PoseLandmark

            if landmarks is not None:
                right_hip = get_xy_points(landmarks[key_points.RIGHT_HIP])
                right_knee = get_xy_points(landmarks[key_points.RIGHT_KNEE])
                right_heel = get_xy_points(landmarks[key_points.RIGHT_HEEL])
                right_foot = get_xy_points(landmarks[key_points.RIGHT_FOOT_INDEX])

                util.put_points(image, right_hip)
                util.put_points(image, right_knee)
                util.put_points(image, right_heel)
                util.put_points(image, right_foot)

                right_hip_x, right_hip_y = right_hip[const.X_COORDINATE], right_hip[const.Y_COORDINATE]
                right_knee_x, right_knee_y = right_knee[const.X_COORDINATE], right_knee[const.Y_COORDINATE]
                right_heel_x, right_heel_y = right_heel[const.X_COORDINATE], right_heel[const.Y_COORDINATE]
                right_foot_x = right_foot[const.X_COORDINATE]

                angle = math.degrees(math.atan2(right_heel_x - right_knee_x, right_heel_y - right_knee_y) - math.atan2(right_hip_x - right_knee_x, right_hip_y - right_knee_y))
                if angle < 0:
                    angle += 360

                util.put_text(image, const.VIDEO_BASE_POINT, round(angle, 0))
                util.put_line(image, right_hip, right_knee, const.COLOR_WHITE)
                util.put_line(image, right_knee, right_heel, const.COLOR_WHITE)

                ded_line = (right_foot[0], right_foot[1] - 0.2)
                if right_knee_x > right_foot_x:
                    util.put_line(image, ded_line, right_foot, const.COLOR_RED)
                else:
                    util.put_line(image, ded_line, right_foot, const.COLOR_GREEN)

                predata = [angle, right_hip[0], right_hip[1],
                            right_knee[0], right_knee[1],
                            right_foot[0], right_foot[1]
                        ]
                data.append(predata)

                cv.imshow("test", image)
                writer.write(image)

                if cv.waitKey(1) == 27:
                    break

        df = pd.DataFrame(data, columns=const.HEADER)
        df.to_csv(wkdir + '/data/data.csv')

        writer.release()
        cap.release()
        cv.destroyAllWindows()


def train_plank():
    pass
