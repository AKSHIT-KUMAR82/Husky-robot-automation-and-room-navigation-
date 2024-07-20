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
5.   ```bash
     cd ~/catkin_ws/src
     catkin_make
     source devel/setup.bash
     ```
   **Launch Gazebo with Husky**
     ```bash
     roslaunch husky_gazebo husky_playpen.launch
     ```
   **Control Husky with a Keyboard or Xbox Controller**
   ## Keyboard Control
     ```bash
     sudo apt-get install ros-noetic-teleop-twist-keyboard
     rosrun teleop_twist_keyboard teleop_twist_keyboard.py
     ```
   ## Xbox Controller
     ```bash
     rosrun joy joy_node
     rosrun teleop_twist_joy teleop_node
     ```
**Record the Trajectory**
## Create a ROS node to record the trajectory data
      Link to the python script for that node to record the trajectory : https://github.com/AKSHIT-KUMAR82/Husky-robot-automation-and-room-navigation-/blob/origin/scripts/record_trajectory.py

## Note: Create this python file in your custom package only, Once you add this file in the custom package then make sure to make it executable through the below command :
     ```bash
     chmod +x path/to/your/package/scrpits/trajectory_recorder.py
     ```
## Update CMakeLists.txt and package.xml to include the new script then build the workspace again using the commands :
     ```bash
     cd ~/catkin_ws
     catkin_make
     source devel/setup.bash
     ```
## Run the recorder node and move your husky along any trajectory in gazebo through xbox or keyboard 
     ```bash
     rosrun husky_trajectory_recorder trajectory_recorder.py
     ```
**Train a DMP Model**
## Use Python to train a DMP model. Install necessary libraries:
     ```bash
     pip install numpy pandas dmp
     ```
## Create a script to train the DMP model: 
     Link of the DMP algorithm and generic algorithm is used to find the best hypertuning parameters : https://github.com/AKSHIT-KUMAR82/Husky-robot-automation-and-room-navigation-/blob/origin/scripts/DMP_trajectory_training.py
## Note : After,Applying this algorithm,Our DMP will be trained for that trajectory to be followed by husky.You will get best hypertuning parameters after this algorithm get executed,which will be used further for it's simulation in gazebo

**Simulate a trained Dynamic Movement Primitive (DMP) trajectory in Gazebo**
## Generate the Trajectory using DMP Parameters:
     ## Now,You have to create a that will generate a trajectory given the best parameters produced above....
     Link for that python script : https://github.com/AKSHIT-KUMAR82/Husky-robot-automation-and-room-navigation-/blob/origin/scripts/generate_traj.py 

## Publish the Trajectory as ROS Messages:
     ## Create a ROS node to publish the trajectory:
     Link for the node to publish the trajectory : https://github.com/AKSHIT-KUMAR82/Husky-robot-automation-and-room-navigation-/blob/origin/scripts/publish_trajectory.py

## Execute the Trajectory in Gazebo:
     ## Create a ROS node that subscribes to the /husky/dmp_trajectory topic and sends appropriate movement commands to the robot in Gazebo:
     Link for the node to execute that trajectory in your virtual environment of gazebo : https://github.com/AKSHIT-KUMAR82/Husky-robot-automation-and-room-navigation-/blob/origin/scripts/TrainedDMP_trajectory_execute.py

## Note : After, This you will see your husky robot moving in your gazebo environment and you can adjust the speed through some changes in Execute node created just in above step.......


