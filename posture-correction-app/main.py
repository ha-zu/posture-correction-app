"""
Detecting Bad posture in Squats and Planks and improve your posture.
Might add training Push-Up, Sit-Up, Others...
"""


import cv2 as cv
import mediapipe as mp
from config import constant_list as const
from training import instructions as ins
from util import util


def sample_pose():
    """
    Using MediaPipe for posture detections.
    sample code.
    """
    mp_pose = mp.solutions.pose
    with mp_pose.Pose(
        model_complexity=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as pose:

        cap = cv.VideoCapture(0)
        cap.set(cv.CAP_PROP_FRAME_WIDTH, const.VIDEO_FRAME_WIDTH)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, const.VIDEO_FRAME_HEIGHT)

        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("error can not opened capture.")
                break

            image.flags.writeable = False
            # Inverted with respect to Y axis
            image = cv.flip(image, 1)
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

            # Get pose landmarks
            results = pose.process(image)
            image.flags.writeable = True
            image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

            # Get pose landmarks
            pose_lands = results.pose_landmarks
            pose_pos = mp_pose.PoseLandmark

            if results is not None:
                # Nose
                nose_x = pose_lands.landmark[pose_pos.NOSE].x
                nose_y = pose_lands.landmark[pose_pos.NOSE].y
                cv.circle(
                    image,
                    (
                        int(nose_x * const.VIDEO_FRAME_WIDTH),
                        int(nose_y * const.VIDEO_FRAME_HEIGHT),
                    ),
                    7,
                    (0, 255, 255),
                    -1,
                )
                util.put_text(image, nose_x, nose_y)
                print("Nose:", nose_x, nose_y)

                # Sholders
                left_point = pose_pos.LEFT_SHOULDER
                right_point = pose_pos.RIGHT_SHOULDER
                left_sholder_x = pose_lands.landmark[left_point].x
                left_sholder_y = pose_lands.landmark[left_point].y
                right_sholder_x = pose_lands.landmark[right_point].x
                right_sholder_y = pose_lands.landmark[right_point].y
                central_sholder_x = (left_sholder_x + right_sholder_x) / 2
                central_sholder_y = (left_sholder_y + right_sholder_y) / 2
                cv.circle(
                    image,
                    (
                        int(left_sholder_x * const.VIDEO_FRAME_WIDTH),
                        int(left_sholder_y * const.VIDEO_FRAME_HEIGHT),
                    ),
                    7,
                    (0, 255, 255),
                    -1,
                )
                cv.circle(
                    image,
                    (
                        int(right_sholder_x * const.VIDEO_FRAME_WIDTH),
                        int(right_sholder_y * const.VIDEO_FRAME_HEIGHT),
                    ),
                    7,
                    (0, 255, 255),
                    -1,
                )
                cv.circle(
                    image,
                    (
                        int(central_sholder_x * const.VIDEO_FRAME_WIDTH),
                        int(central_sholder_y * const.VIDEO_FRAME_HEIGHT),
                    ),
                    7,
                    (0, 255, 255),
                    -1,
                )
                util.put_text(image, left_sholder_x, left_sholder_y)
                util.put_text(image, right_sholder_x, right_sholder_y)
                util.put_text(image, central_sholder_x, central_sholder_y)
                print(
                    "Sholder=LX:{0}, LY:{1}, RX:{2}, RY:{3}".format(
                        left_sholder_x,
                        left_sholder_y,
                        right_sholder_x,
                        right_sholder_y
                    )
                )

                # Hips
                left_hip_x = pose_lands.landmark[pose_pos.LEFT_HIP].x
                left_hip_y = pose_lands.landmark[pose_pos.LEFT_HIP].y
                right_hip_x = pose_lands.landmark[pose_pos.RIGHT_HIP].x
                right_hip_y = pose_lands.landmark[pose_pos.RIGHT_HIP].y
                central_hip_x = (left_hip_x + right_hip_x) / 2
                central_hip_y = (left_hip_y + right_hip_y) / 2
                cv.circle(
                    image,
                    (
                        int(left_hip_x * const.VIDEO_FRAME_WIDTH),
                        int(left_hip_y * const.VIDEO_FRAME_HEIGHT),
                    ),
                    7,
                    (0, 255, 255),
                    -1,
                )
                cv.circle(
                    image,
                    (
                        int(right_hip_x * const.VIDEO_FRAME_WIDTH),
                        int(right_hip_y * const.VIDEO_FRAME_HEIGHT),
                    ),
                    7,
                    (0, 255, 255),
                    -1,
                )
                cv.circle(
                    image,
                    (
                        int(central_hip_x * const.VIDEO_FRAME_WIDTH),
                        int(central_hip_y * const.VIDEO_FRAME_HEIGHT),
                    ),
                    7,
                    (0, 255, 255),
                    -1,
                )
                util.put_text(image, left_hip_x, left_hip_y)
                util.put_text(image, right_hip_x, right_hip_y)
                util.put_text(image, central_hip_x, central_hip_y)
                print(
                    "Hip=LX:{0}, LY:{1}, RX:{2}, RY:{3}".format(
                        left_hip_x,
                        left_hip_y,
                        right_hip_x,
                        right_hip_y
                    )
                )

                cv.line(
                    image,
                    (int(central_sholder_x * const.VIDEO_FRAME_WIDTH), int(central_sholder_y * const.VIDEO_FRAME_HEIGHT)),
                    (int(central_hip_x * const.VIDEO_FRAME_WIDTH), int(central_hip_y * const.VIDEO_FRAME_HEIGHT)),
                    (0, 255, 0),
                    3,
                    cv.LINE_4,
                    0
                    )

                cv.line(
                    image,
                    (int(nose_x * const.VIDEO_FRAME_WIDTH), int(nose_y * const.VIDEO_FRAME_HEIGHT)),
                    (int(central_sholder_x * const.VIDEO_FRAME_WIDTH), int(central_sholder_y * const.VIDEO_FRAME_HEIGHT)),
                    (0, 255, 0),
                    3,
                    cv.LINE_4,
                    0
                    )

                # Knee
                left_knee_x = pose_lands.landmark[pose_pos.LEFT_KNEE].x
                left_knee_y = pose_lands.landmark[pose_pos.LEFT_KNEE].y
                right_knee_x = pose_lands.landmark[pose_pos.RIGHT_KNEE].x
                right_knee_y = pose_lands.landmark[pose_pos.RIGHT_KNEE].y
                cv.circle(
                    image,
                    (
                        int(left_knee_x * const.VIDEO_FRAME_WIDTH),
                        int(left_knee_y * const.VIDEO_FRAME_HEIGHT),
                    ),
                    7,
                    (0, 255, 255),
                    -1,
                )
                cv.circle(
                    image,
                    (
                        int(right_knee_x * const.VIDEO_FRAME_WIDTH),
                        int(right_knee_y * const.VIDEO_FRAME_HEIGHT),
                    ),
                    7,
                    (0, 255, 255),
                    -1,
                )
                util.put_text(image, left_knee_x, left_knee_y)
                util.put_text(image, right_knee_x, right_knee_y)
                print(
                    "Hip=LX:{0}, LY:{1}, RX:{2}, RY:{3}".format(
                        left_knee_x,
                        left_knee_y,
                        right_knee_x,
                        right_knee_y
                    )
                )

            cv.imshow("Detection posture App", image)

            if cv.waitKey(1) == 27:
                break

        cap.release()
        cv.destroyAllWindows()


def main():
    """Detection posture"""
    sample_pose()


if __name__ == "__main__":
    main()