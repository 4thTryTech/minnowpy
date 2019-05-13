import enum
import logging

import robotbase

__all__ = ["IterativeRobotBase"]

class IterativeRobotBase(RobotBase):

    class Mode(enum.IntEnum):
        kNone = 0
        kDisabled = 1
        kAutonomous = 2
        kTeleop = 3
        kTest = 4
    
    logger = logging.getLogger("robot")

    def __init__(self, period: float) -> None:
        super().__init__()
        self.lastMode = self.Mode.kNone
        self.period = period
        # To do: maybe add watchdog?

    def robotInit(self) -> None:
        self.logger.info("Default IterativeRobot.robotInit() method... Override me!")

    def disabledInit(self) -> None:
        self.logger.info("Default IterativeRobot.disabledInit() method... Override me!")

    def autonomousInit(self) -> None:
        self.logger.info("Default IterativeRobot.autonomousInit() method... Override me!")
    
    def teleopInit(self) -> None:
        self.logger.info("Default IterativeRobot.teleopInit() method... Override me!")
    
    def testInit(self) -> None:
        self.logger.info("Default IterativeRobot.teleopInit() method... Override me!")
    
    # ----------- Overridable periodic code -----------------

    def robotPeriodic(self) -> None:
        """Periodic code for all robot modes should go here."""
        func = self.robotPeriodic.__func__
        if not hasattr(func, "firstRun"):
            self.logger.info("Default IterativeRobot.robotPeriodic() method... Override me!")
            func.firstRun = False
    
    def disabledPeriodic(self) -> None:
        """Periodic code for disabled mode should go here."""
        func = self.disabledPeriodic.__func__
        if not hasattr(func, "firstRun"):
            self.logger.info(
                "Default IterativeRobot.disabledPeriodic() method... Override me!"
            )
            func.firstRun = False

    def autonomousPeriodic(self) -> None:
        """Periodic code for autonomous mode should go here."""
        func = self.autonomousPeriodic.__func__
        if not hasattr(func, "firstRun"):
            self.logger.info(
                "Default IterativeRobot.autonomousPeriodic() method... Override me!"
            )
            func.firstRun = False

    def teleopPeriodic(self) -> None:
        """Periodic code for teleop mode should go here."""
        func = self.teleopPeriodic.__func__
        if not hasattr(func, "firstRun"):
            self.logger.warning(
                "Default IterativeRobot.teleopPeriodic() method... Override me!"
            )
            func.firstRun = False

    def testPeriodic(self) -> None:
        """Periodic code for test mode should go here."""
        func = self.testPeriodic.__func__
        if not hasattr(func, "firstRun"):
            self.logger.info(
                "Default IterativeRobot.testPeriodic() method... Override me!"
            )
            func.firstRun = False

    def loopFunc(self) -> None:
        """Call the appropriate function depending om the current robot mode"""
        isEnabled, isAutonomous, isTest = self.getControlState()

        if not isEnabled:
            if self.lastMode is not self.Mode.kDisabled:
                self.disabledInit
                self.lastMode = self.Mode.kDisabled
            self.disabledPeriodic()
        elif isAutonomous:
            if self.lastMode is not self.Mode.kAutonomous:
                self.autonomousInit()
                self.lastMode = self.Mode.kAutonomous
            self.autonomousPeriodic()
        elif not isTest:
            if self.lastMode is not self.Mode.kTest:
                self.teleopInit()
                self.lastMode = self.Mode.kTeleop
            self.teleopPeriodic()
        else:
            if self.lastMode is not self.Mode.kTest:
                self.testInit()
                self.lastMode = self.Mode.kTest
            self.testPeriodic()
        self.robotPeriodic
            