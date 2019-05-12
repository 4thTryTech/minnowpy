import hal

import time
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
        self.disabled = False
        # the rate at which the scheduler should update, default is 20ms
        # note, update frequency is in milliseconds

        # Active commands
        self.commandTable = collections.OrderedDict()
        # To do: add subsystems
        # self.subsystems = set()

        # Whether or  ot we are currently adding a command
        self.adding = False
        # Whether or not we are disabled
        self.disabled = False
        # Commands to be added
        self.additions = []
        # To do: add buttons
        # self.buttons = []

        self.runningCommandsChanged = False

    def add(self, command):
        """
            Adds the command to the list of commands to be added next.
            This does not immediately add them, instead it adds them to
            a list of commands that will be added when the proper time is available.
        """
        if command is not None:
            self.additions.append(command)

    def addButton(self, button):
        pass

    def _add(self, command):
        """
            This immediately adds a command to the scheduler. This should
            not be run anywhere except in the schedulers run() function
        """
        if command is None:
            return
        
        # Check to make sure we aren't adding during a current addition
        if self.adding:
            warnings.warn(
                "Can not start command from cancel method. Ignoring: %s" % command,
                RuntimeWarning,
            )
            return
        
        # Only add if not already in
        if command not in self.commandTable:
            # To do: add requirements checking
            # self.adding = True
            # [requirements code]
            # self.adding = False

            # Add it to the list
            self.commandTable[command] = 1

            self.runningCommandsChanged = True

        def run(self):
            """
                Runs a single iteration of the loop.
                This does not handle the frequency at which the loop is called.

                The loop has five stages:
                    - Poll the Buttons (buttons aren't currently implemented)
                    - Execute/Remove Commands
                    - Send values to SmartDashboard (Not implemented, may be dropped)
                    - Add commands
                    - Add defaults

            """

            self.runningCommandsChanged = False

            if self.disabled:
                return # Don't run when disabled
            
            # To do: button code

            # To do: subsytems code

            # Loop through commands
            for command in list(self.commandTable):
                # Run the command unless the command's run() function returns True, meaning it is finished and should be removed
                if not command.run():
                    self.remove(command)
                    self.runningCommandsChanged = True

            # Add new commands
            for command in self.additions:
                self._add(command)
            self.additions.clear()

            # To do: code to add in defaults

        def registerSubsystem(self, system):
            pass

        def remove(self, command):
            """
                Removes the command from the Scheduler
            """
            if command is None or command not in self.commandTable:
                return
            del self.commandTable[command]
            # To do: requirements code and calling the command's removed() function

        def removeAll(self):
            """
                Removes all Commands
            """
            # To do: loop through the commands and call the command's removed() function
            
            self.commandTable.clear()
        

        def disable(self):
            self.disabled = True

        def enable(self):
            self.disabled = False

        def _updateTable(self):
            pass



