# Assignments for Lecture 7
This assignment is for lecture 7 of the OMTP course. The topic of the assignment is about using state machines to control a robot (in a simulation), by creating different behaviors(states) in the program FlexBE. The robot performs a sequence of behaviors to perform a task. 
Assignmet 1 is about designing a robot behaviors in FlexBE, and creating a sequence of behviors (state machine). The task is to make a robot pick up an object, which is detected by a camera. The object is spawned on a conveyor belt, which moves the object towards the robot. When the object is detected by the camera, the robot knows the position of the object, and it is able to pick it up.

## Assignment 1 - Overall description:
To install FlexBE run 
```
$ sudoapt install ros-$ROS_DISTRO-flexbe-behavior-engine
```
To get the FlexBE app, clone git to workspace: 
```
$ git clone https://github.com/FlexBE/flexbe_app.git
```
To get the more states, clone git to workspace: 
```
$ git clone https://github.com/FlexBE/generic_flexbe_states
```
* Choose one student's assignment folder and clone the folders to your workspace
* Replace/overwrite the "omtp_gazebo" and "omtp_utilities" folders with the existing ones

* To load the environment run 
```
$ roslaunch omtp_gazebo omtp_pick_demo.launch 
```
* To load the FlexBe app run 
```
$ roslaunch flexbe_app flexbe_full.launch 
```
* To spawn an object run 
```
$ rosservice call /start_spawn 
```


## Assignment 1 - Vivian
* Clone folders/files and replace/overwrite folders (as described above) 
* Run `$ roslaunch omtp_gazebo omtp_pick_demo.launch `
* Run `$ roslaunch flexbe_app flexbe_full.launch `
* Load the behavior `"grasp_an_object_with_robot1"` in the FlexBE app and press "execute"
* When the robot reaches the state "Detect object on conveyor" run `$ rosservice call /start_spawn`

Video link: https://drive.google.com/open?id=1lLtQJJzJCLXGn5u6Oca1Uk3hT1vpd9JK 



## Assignment 1 - Daniela


## Assignment 1 - Giorgio
* Clone folders/files and replace/overwrite folders (as described above)
* Run `$ roslaunch omtp_gazebo omtp_pick_demo.launch`
* unpause the simulation
* Run `$ rosservice call /start_spawn`
* Run `$ roslaunch flexbe_app flexbe_full.launch `
* Load the behavior `"pick_and_release_part_from_conveyor_with_robot1"` in the FlexBE app and press "execute"

Video link: https://drive.google.com/file/d/1BfeUnjDWuPcq25mKfeV3sDsb-3Fh6wVL/view?usp=sharing
