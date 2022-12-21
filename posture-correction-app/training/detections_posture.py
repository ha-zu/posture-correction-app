# ToDo class or dataclass

class DetectionsPosture(object):
    """
    Training posture detection for using MediaPipe
    """

    def __init__(self, training_name):
        pass

    def init_mediapipe(self):
        """Initialize MediaPipe"""
        pass

    def get_nose_points(self):
        """Get nose x and y points."""
        pass

    def get_sholder_points(self):
        """Get sholder x and y points."""
        pass

    def get_hip_points(self):
        """Get hip x and y points."""
        pass

    def get_knee_points(self):
        """Get knee x and y points."""
        pass

    def get_heel_points(self):
        """Get heel x and y points."""
        pass

    def get_foot_idx_points(self):
        """Get foot index x and y points."""
        pass

    def correct_squat(self):
        """Present correct posture for the squat."""
        pass

    def correct_plank(self):
        """Present correct posture for the plank."""
        pass

    def is_correct_posture(self):
        """Correct posture is judge."""
        pass

    def correct_posture_counter(self):
        """Counting correct posture."""
        pass

    def correct_posture_time(self):
        """Counting correct posture time."""
        pass