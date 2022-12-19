"""
Detecting Bad posture in Squats and Planks and improve your posture.
Might add training Push-Up, Sit-Up, Others...
"""

import pyttsx3
from config import constant_list as const
from training import instructions as ins


def main():
    """Detection posture"""
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("rate", const.VOICE_SPEED)
    engine.setProperty("volume", const.VOICE_VOLUME)
    engine.setProperty("voice", voices[const.VOICE_NUMBER_OF_JP].id)

    ins.instruct_posture(engine, const.BACKWORD_POSTURE)


if __name__ == "__main__":
    main()
