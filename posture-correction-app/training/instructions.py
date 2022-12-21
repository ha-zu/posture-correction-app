import pyttsx3
from config import constant_list as const


class VoiceInstructionPosture(object):
    """
    Module for voice instructions for correct posture.
    """

    def __init__(self):
        """Voice instructions for correct posture setting"""
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("rate", const.VOICE_SPEED)
        self.engine.setProperty("volume", const.VOICE_VOLUME)
        self.engine.setProperty("voice",
                                self.voices[const.VOICE_NUMBER_OF_JP].id)

    def setting_language(self, language_id):
        """Language setting is changes"""
        self.engine.setProperty("voice", self.voices[language_id].id)

    def instruct_posture(self, instruct):
        """Voice instructions for correct posture"""
        self.engine.say(instruct)
        self.engine.runAndWait()
