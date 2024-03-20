###### tags: `ROS2` `Humble` `Gazebo`

# Ros 2

This project is about how to use ROS2 on Gazebo simulation with differential drive configuration.

![gazebo-and-ros-687x319](https://hackmd.io/_uploads/HJdUtXP06.jpg)
![螢幕擷取畫面 2024-03-20 202923](https://hackmd.io/_uploads/S1s1vUuRa.png)


## Index

[TOC]

## Information

- Software
  - Operating System: [Ubuntu 22.04](https://developer.nvidia.cn/zh-cn/embedded/downloads)
  - Framework:
    - Robot Operating System 2 (ROS2) - Humble
  - Simulation: Rivz2 Gazebo
  - Python: 3.10.12
  - Source code: [Brady0608/ros2_test](https://github.com/Brady0608/ros2_test) 

##  Developer

- Tsung-Meng Guo(a800608a@gmail.com)


## 0. Setup environment
### 0-1. Set locale
Make sure you have a locale which supports UTF-8. If you are in a minimal environment (such as a docker container), the locale may be something minimal like POSIX. We test with the following settings. However, it should be fine if you’re using a different UTF-8 supported locale.!

```
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8
```

### 0-2. Setup Sources
You will need to add the ROS 2 apt repository to your system.

First ensure that the Ubuntu Universe repository is enabled.

```
sudo apt install software-properties-common
sudo add-apt-repository universe
```

Now add the ROS 2 GPG key with apt.

```
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

### 0-3. Install ROS 2 packages
Update your apt repository caches after setting up the repositories.

``sudo apt update``

ROS 2 packages are built on frequently updated Ubuntu systems. It is always recommended that you ensure your system is up to date before installing new packages.

``sudo apt upgrade``

Desktop Install (Recommended): ROS, RViz, demos, tutorials.

``sudo apt install ros-humble-desktop``

Development tools: Compilers and other tools to build ROS packages

``sudo apt install ros-dev-tools``

### 0-4 Environment setup
Set up your environment by sourcing the following file.
``source /opt/ros/humble/setup.bash``


## 1. Ros2 and Gazebo

### 1-1 Download the project ros2_test

Please download the project ros2_test through the command below:
``` git clone https://github.com/Brady0608/ros2_test ```

![螢幕擷取畫面 2024-03-20 161611](https://hackmd.io/_uploads/HyJqszOCp.png)


### 1-2. Install teleop-twist-keyborad

The package "teleop-twist-keyboard" is a generic keyboard teleop for twist robots. Please ckeck the [ROS Wiki](http://wiki.ros.org/teleop_twist_keyboard) to install.

### 1-3. Build the Package
Navigate to your ROS 2 workspace and build the package using colcon.![螢幕擷取畫面 2024-03-20 165426](https://hackmd.io/_uploads/r1MK4mu06.png)

### 1-4. Source the Workspace Source the ROS 2 workspace to set the environment for the package.

Source the setup.bash through the command below:
``` source ~/ros2_test/install/setup.bash ```

### 1-5. Run the launch file You can now run the Rivz2 and Gazebo.

```
ros2 launch my_robot_bringup my_robot_gazebo.launch.xml
```

![螢幕擷取畫面 2024-03-20 200311](https://hackmd.io/_uploads/SJPqx8u06.png)


![螢幕擷取畫面 2024-03-20 200146](https://hackmd.io/_uploads/S1nagIdAT.png)

![螢幕擷取畫面 2024-03-20 200217](https://hackmd.io/_uploads/Sy6AxUdRa.png)


### 1-6. Control the Robot

Now, you have two methods to control this robot.

#### 1. Use comand line publish parameters to the topic "cmd_vel", the interface "geometry_msgs/msg/Twist"

```
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0}, angular: {z: 0}}"
```

#### 2. Use teleop-twist-keyborad package

Open another terminal through the command below:

```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

![螢幕擷取畫面 2024-03-20 202336](https://hackmd.io/_uploads/BkHvB8O0a.png)

Now you can follow the information on the terminal to control the Robot!


