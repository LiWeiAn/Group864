# Assignments for Lecture 6
This is the assignments for lecture 6 of the OMTP course. The topic of this assignment is about object detection and grasping. The task for this assignment is to place cameras in the simulation environment, which gives information about the object's position. The robot is able to grasp the object by knowing its position.

## Assignment 1
* Run `$ roslaunch omtp_lecture6 lecture6_assignment1.launch`

## Assignment 2
* Run  `$ rosrun tf view_frames`
![](gifs/frames.png)

## Assignment 3
* Run `$ roslaunch omtp_lecture6 lecture6_assignment3.launch` 
* Run `$ rosrun omtp_lecture6 lecture6_assignment3.py` 

## Assignment 4
Replace the launch file `spawn_static_world_objects.launch` with the same file, in folder `omtp_gazebo/launch`
You need to spawn the object by running the rosservice `rosservice call /spawn_object_once`  
* To launch the simulation environment run `$ roslaunch omtp_lecture6 lecture6_assignment1.launch`
* To execute the assignment run `$ rosrun omtp_lecture6 assign4.py`

![](gifs/assignment4.gif)

