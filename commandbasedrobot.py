from wpilib import TimedRobot
from wpilib.command import Scheduler


class CommandBasedRobot(TimedRobot):
    """
    The base class for a Command-Based Robot. To use, instantiate commands and
    trigger them.
    """

    def startCompetition(self):
        """Initalizes the scheduler before starting robotInit()"""
        self.scheduler = Scheduler.getInstance()
        super().startCompetition()

    def commandPeriodic(self):
        """
        Run the scheduler regularly. If an error occurs during a competition,
        prevent it from crashing the program.
        """
        self.scheduler.run()

    autonomousPeriodic = commandPeriodic
    teleopPeriodic = commandPeriodic
    disabledPeriodic = commandPeriodic
    # testPeriodic deliberately omitted
