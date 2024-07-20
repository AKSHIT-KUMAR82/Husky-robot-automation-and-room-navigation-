# Husky-robot-automation-and-room-navigation

## Overview
This project is used for navigating a husky robot through some environment, Which involves map generation of the environment, Gazebo simulation, and DMP algorithm for trajectory training then we will execute the trained DMP trajectory in the gazebo virtual environment, and accordingly at the end we'll provide it different coordinates then correspondingly it will follow that path. This will be used to create a robust robot for room navigation.


## Setup Instructions
### Prerequisites
Ubuntu (preferably 20.04)
ROS Noetic
Gazebo
husky_simulator package
ros_control and controller_manager
rosbag for recording data
numpy and pandas for data processing
Python libraries for DMP (such as dmp)

### Step-by-Step Guide
1. **Install Required Packages**
    ```bash
    sudo apt-get update
    sudo apt-get install ros-noetic-husky-simulator ros-noetic-husky-desktop ros-noetic-joy ros-noetic-teleop- 
    twist-joy ros-noetic-ros-control ros-noetic-controller-manager
    ```
2. **Create your package for husky_trajectory**
3.   ```bash
     cd ~/catkin_ws/src
     catkin_create_pkg Husky_trajectory std_msgs rospy 
     ```
4. **Set Up the Workspace**
5. ```bash
     cd ~/catkin_ws/src
     catkin_make
     source devel/setup.bash
     ```
   **Launch Gazebo with Husky**
   ```bash
     roslaunch husky_gazebo husky_playpen.launch
     ```
   **Control Husky with a Keyboard or Xbox Controller**
   -> Keyboard Control
  ```bash
     sudo apt-get install ros-noetic-teleop-twist-keyboard
     rosrun teleop_twist_keyboard teleop_twist_keyboard.py
     ```
   -> Xbox Controller
   ```bash
     rosrun joy joy_node
     rosrun teleop_twist_joy teleop_node
     ```
    **Record the Trajectory**
