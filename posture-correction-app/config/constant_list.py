"""
Detection posture settings
"""
VIDEO_FRAME_WIDTH = 1280
VIDEO_FRAME_HEIGHT = 720
VIDEO_CAMERA_MAC = 0
VIDEO_CAMERA_USEB = 1
FRAME_RATE = 10
VIDEO_SIZE = (VIDEO_FRAME_WIDTH, VIDEO_FRAME_HEIGHT)
VIDEO_BASE_POINT = (0, 0.05)

"""
Coordinate X and Y
"""
X_COORDINATE = 0
Y_COORDINATE = 1

"""
Training detected points
"""
HEADER = ['Angle', 'Right Hip X', 'Right Hip Y',
            'Right Knee X', 'Right Knee Y',
            'Right Foot X', 'Right Foot Y'
        ]

"""
Detected connect line and point color
(B, G, R)
"""
COLOR_YELLOW = (41, 255, 252)
COLOR_GREEN = (49, 255, 36)
COLOR_BLUE = (247, 36, 8)
COLOR_RED = (51, 51, 255)
COLOR_WHITE = (255, 255, 255)

"""
Voice settings
"""
# Voice List Number 18=ja_JP in Mac.
VOICE_NUMBER_OF_JP = 18
VOICE_NUMBER_OF_US = 0
VOICE_SPEED = 180
VOICE_VOLUME = 0.7

"""
Instructions correct posture
"""
# squat
FORWORD_POSTURE = "姿勢を前に倒してください"
BACKWORD_POSTURE = "姿勢を後ろに倒してください"
FORWORD_KNEE = "膝をつま先より後ろにしてください"
BUTTOCKS_UP = "お尻を上げてください"
BUTTOCKS_DOWN = "お尻を下げてください"

# plank
UP_HEAD = "顔を上げてください"
UP_WAIST = "腰を上げてください"
DOWN_WAIST = "腰を下げてください"
UP_CHEST = "胸を上げてください"
DOWN_CHEST = "胸を下げてください"
