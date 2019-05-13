from typing import Tuple, Type

import logging

logger = logging.getLogger("robotpy")

__all__ = ["RobotBase"]


class RobotBase():
    """
        Implements a base robot framework.
    """

    def __init__(self) -> None:
        # python specific optimization, attach ds methods to object to reduce function calls
        pass
    
    def close() -> None:
        pass
    
    def getGetControlState(self) -> Tuple[bool, bool, bool]:
        """
            More efficient way to determine what state the robot is in.

            returns booleans representing enabled, isautonomous, istest
        """
        # To do: write get controlstate function
        pass
    
    def isDisabled(self) -> bool:
        pass
    
    def isEnabled(self) -> bool:
        pass
    
    def isAutonomousEnabled(self) -> bool:
        pass
    
    def isOperaterControlEnabled(self) -> bool:
        pass
    
    def startCompetition(self) -> None:
        pass
    
    @staticmethod
    def main(robot_cls: Type["RobotBase"]) -> bool:
        """Starting point for the application"""

        try:
            robot = robot_cls()
        except:
            logger.exception("Unhandled exception")
            return False
        
        # Add a check to see if the user forgot to call super().__init__()
        # to do ------

        try:
            robot.startCompetition()
        except KeyboardInterrupt
            logger.exception(
                "THIS IS NOT AN ERROR: The user hit CTRL-C to kill the robot"
            )
            logger.info("Exiting because of keyboard interrupt")
            return True
        except:
            logger.exception("Unhandled exception")
            return False
        else:
            # startCompetition never returns unless an exception occurs
            logger.exception("Robots should not quit, but yours did!")
            logger.exception("Unexpected return from startCompetition() method")
            return False

