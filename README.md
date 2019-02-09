# minnowpy
A library to mimic portions of WPILIB for teaching FRC robotics programming basics using MicroPython

The goal for MinnowPy is to be able to use cheap micropython control boards with specific, common tasks to allow an FRC team to use these cheap and accessible systems to teach both general programming and FRC specific programming tasks in the off season with minimal hardware and software requirements.  For these common tasks, the code will look and feel like code written using RobotPy WPILib.  

MinnowPy is not intended to be used on competition robots, nor is it intended as a general purpose robotics framework, though it should work fine if the tasks happen to allign with the teaching tasks this project is intended for.

# Why MinnowPy?
"Minnow Is NNOt WPIlib"

In addition to the recusive acronym, a minnow is small and fast, and kids of all ages like to try to catch them - just like this library should be.

# Approach and Structure
MinnowPy will be used to create a simplified, command based robot.  We will be using CommandBasedRobot as the foundation because it provides an excellent teaching method that forces the coder to mentally break the robot down into it's logical parts and functions.

Other robot frameworks that WPILIB and RobotPy provide may allow excellent flexability and creativity, but I believe that the command based structure simplifies teaching people new to programming. A command based robot helps the person visualize how the program functions via the structure of subsystems describing the physical construction of the robot, and the commands that use them.

The code is only intended to mimic WPILIB/RobotPy at the level of what the studen writes, and only for a very limited subset of functionality. Because this is targeted to runon MicroPython boards, the code will agressively change what is done in the background to meet the size/performance needs of the boards. 

Having said that, it is intended that anything written for this could be dropped onto a RoboRio with RobotPy and work (presuming the sensors/actuators used are present) with only a change to which library name being imported.

# What Match Periods, DriverStation, OI, etc...
Initially, MinnowPy will be hardcoded to be in TeleOp, and we will not use the driverstation and NetworkTables, etc...  Nothing outside the robot will initially exist. Our development is being done on an Adafruit Feather Huzzah, and the functionality will be mostly focused on what is directly connected to it.

As we develop, we will experiment with the performance and experience and determine which features to add. 


