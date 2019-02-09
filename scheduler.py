import hal

import collections
import warnings

__all__ = ["Scheduler"]


class Scheduler():
    """The Scheduler is a singleton which holds the top-level running commands.
    It is in charge of both calling the command's run() method and to make
    sure that there are no two commands with conflicting requirements running.

    It is fine if teams wish to take control of the Scheduler themselves, all
    that needs to be done is to call Scheduler.getInstance().run() often to
    have Commands function correctly. However, this is already done for you
    if you use the CommandBased Robot template.

    .. seealso:: :class:`.Command`
    """

    @staticmethod
    def _reset():
        try:
            del Scheduler.instance
        except:
            pass

    @staticmethod
    def getInstance():
        """Returns the Scheduler, creating it if one does not exist.

        :returns: the Scheduler
        """
        if not hasattr(Scheduler, "instance"):
            Scheduler.instance = Scheduler()
        return Scheduler.instance

    def __init__(self):
        pass

    def add(self, command):
        pass

    def addButton(self, button):
        pass

    def _add(self, command):
        pass

    def run(self):
        pass

    def registerSubsystem(self, system):
        pass

    def remove(self, command):
        pass

    def removeAll(self):
        pass

    def disable(self):
        pass

    def enable(self):
        pass

    def _updateTable(self):
        pass
