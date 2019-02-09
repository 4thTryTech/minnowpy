import hal
__all__ = ["TimedRobot"]


class TimedRobot():
    """TimedRobot framework.
    periodic() functions from the base class are called on an interval by a Notifier instance.
    """

    kDefaultPeriod = 0.02

    def __init__(self, period=TimedRobot.kDefaultPeriod):
        self.period = period
        pass

    def free(self) -> None:
        pass

    def startCompetition(self) -> None:
        """Provide an alternate "main loop" via startCompetition()"""
        pass

    def getPeriod(self) -> float:
        """Get time period between calls to Periodic() functions."""
        return self.period

    def _updateAlarm(self) -> None:
        """Update the alarm hardware to reflect the next alarm."""
        pass
