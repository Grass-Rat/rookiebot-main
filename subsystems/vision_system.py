import cv2
from photonvision import PhotonCamera
from wpilib import SmartDashboard

class VisionSystem:
    def __init__(self):
        self.cam = PhotonCamera()
        self.target_angle = 0.0
        self.target_distance = 0.0

    def process_images(self):
        # Capture an image from the camera
        ret, frame = self.cam.capture()

        # Process the image using PhotonVision
        result = self.cam.getLatestResult()

        # If a target is detected, update the angle and distance
        if result is not None:
            self.target_angle = result.target.angle
            self.target_distance = result.target.distance

            # Send the angle and distance to the SmartDashboard
            SmartDashboard.putNumber("Target Angle", self.target_angle)
            SmartDashboard.putNumber("Target Distance", self.target_distance)

        else:
            # If no target is detected, send a default value to the SmartDashboard
            SmartDashboard.putNumber("Target Angle", 0.0)
            SmartDashboard.putNumber("Target Distance", 0.0)

        # Display the output
        cv2.imshow('frame', frame)

        # Exit on key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.cam.release()
            cv2.destroyAllWindows()
            exit()

    def get_target_angle(self):
        return self.target_angle

    def get_target_distance(self):
        return self.target_distance

    def shutdown(self):
        self.cam.release()
        cv2.destroyAllWindows()