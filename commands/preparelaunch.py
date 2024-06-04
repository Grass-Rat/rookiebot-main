import commands2
import constants
from subsystems.can_launchersubsystem import LauncherSubsystem
from subsystems.vision_system import VisionSystem  # Import VisionSystem class

class PrepareLaunch(commands2.Command):

    def __init__(self, launcher: LauncherSubsystem, vision: VisionSystem) -> None:

        super().__init__()
        self.launcher = launcher
        self.vision = vision
        self.addRequirements(launcher)


    def initialize(self) -> None:

        # Get the detected target's angle and distance from the VisionSystem
        target_angle = self.vision.getTargetAngle()
        target_distance = self.vision.getTargetDistance()


        # Use the target's angle and distance to adjust the launcher's settings

        if target_angle is not None and target_distance is not None:

            # Adjust launcher speed based on target distance to ensure accurate shots

            launcher_speed = 1 - (target_distance / 10)  # Adjust speed based on distance
            self.launcher.setWheels(launcher_speed, 0)

        else:

            # If no target is detected, default to a simple launcher setting
            self.launcher.setWheels(constants.kLauncherSpeed, 0)

        print("Spinning up flywheels")
