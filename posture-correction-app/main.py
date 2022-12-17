"""
Detecting Bad posture in Squats and Planks and improve your posture.
Might add training Push-Up, Sit-Up, Others...
"""

from config import constant_list as const
from training import instructions as ins


def main():
    """ Detection posture """
    engine = ins.instructor_init()
    ins.instruct_posture(engine, const.BACKWORD_POSTURE)


if __name__ == '__main__':
    main()
