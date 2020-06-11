# Assignments for Lecture 5
This is the assignments for lecture 5 of the OMTP course. The topic of this assignment is about enabling the robots in the OMTP factory simulation, to do object manipulation with MoveIt. The task of the assignment is to create a MoveIt package with the MoveIt Setup Assistant and use MoveIt to control/manipulate the robot. 


## Assignment 1
* Create a MoveIt package using MoveIt Setup Assistant. (we are missing the folder with the package ??)
* Clone this repositiory to get the MoveIt package `omtp_moveit_config` created by the authors.


## Assignment 2
* Start the demo simulation `$ roslaunch omtp_moveit_config demo.launch`
* Start the MoveIt command line `$ rosrun moveit_commander moveit_commander_cmdline.py`
* Execute the `moveit_commander_assign2` script by using the command `load moveit_commander_test` in the MoveIt command line.

## Assignment 3
* Start the factory simulation in gazebo `$ roslaunch omtp_lecture5 omtp_lecture5_environment.launch`
* Launch the script by running `$ roslaunch omtp_lecture5 lecture5_assignment3.launch´
![](gifs/assignment3.gif)


