"""
Module for voice instructions for correct posture.
"""


def setting_language(engine, language_id):
    """Language setting is changes"""
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[language_id].id)


def instruct_posture(engine, instruct):
    """The instructor will instruct"""
    engine.say(instruct)
    engine.runAndWait()
