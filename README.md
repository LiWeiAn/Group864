# OMTP Course repository - Group 864

# Description
This is the README file for the OMTP Course repository created by Group 864.
It is assumed that the user operating system is Ubuntu 18.04.
All exercises can be found in the "exercise" branch of this repository.

### Prerequisites
#### ROS Melodic: 
Follow instructions in: http://wiki.ros.org/melodic/Installation/Ubuntu

#### catkin toolbox

#### Gazebo 9.12 with dependensies: 
```
$ sudo apt install ros-melodic-gazebo-ros-control
$ sudo apt install ros-melodic-gazebo-msgs
$ sudo apt install ros-melodic-gazebo-plugins
$ sudo apt install ros-melodic-ros-controllers
```

#### MoveIt with other plugins and packages: 
```
$ sudoapt install ros-melodic-moveit
$ sudoapt install ros-melodic-trac-ik-kinematics-plugin
```

#### rosdep with dependensies:
```
$ rosdep update
```

From the root of your catkin workspace run: 
```
$ rosdep check--from-paths . --ignore-src --rosdistromelodic
$ rosdep install--from-paths . --ignore-src --rosdistromelodic
```

### Installing
In order to test the files, follow the following procedure
* Create a catkin workspace (`mkdir G864catkin_ws/src -p`)
* Clone the repository into the src folder of your catkin workspace
* Build the catkin workspace (`catkin build` inside the `G864catkin_ws` folder)
* Source the catkin workspace (`source devel/setup.bash` inside the `G864catkin_ws` folder)



## Authors
Daniela Pinto - danielapinto

Giorgio Frego - Gekogio

Vivian Li - LiWeiAn
