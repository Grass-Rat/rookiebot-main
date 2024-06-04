import commands2
import constants
from subsystems.can_launchersubsystem import LauncherSubsystem
from subsystems.vision_system import VisionSystem  # Import VisionSystem class

class StopIntakeAndShooter(commands2.Command):

    def __init__(self, launcher: LauncherSubsystem, vision: VisionSystem) -> None:

        super().__init__()
        self.launcher = launcher
        self.vision = vision
        self.addRequirements(launcher)


    def initialize(self) -> None:

        # Get the detected target's angle and distance from the VisionSystem
        target_angle = self.vision.getTargetAngle()
        target_distance = self.vision.getTargetDistance()


        # Use the target's angle and distance to decide whether to stop the intake and shooter
        if target_angle is None and target_distance is None:

            # If no target is detected, stop the intake and shooter to conserve energy
            self.launcher.stop()
            self.launcher.shooting = False

        print("STOOPPPIING")