"""
Module for voice instructions for correct posture.
"""

import pyttsx3

from config import constant_list as const


def instructor_init() -> object:
    """ Instructor initialization """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', const.VOICE_SPEED)
    engine.setProperty('volume', const.VOICE_VOLUME)
    engine.setProperty('voice', voices[const.VOICE_NUMBER_OF_JP].id)

    return engine


def setting_language(engine, language_id):
    """ Language setting is changes """
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[language_id].id)


def instruct_posture(engine, instruct):
    """ The instructor will instruct """
    engine.say(instruct)
    engine.runAndWait()
