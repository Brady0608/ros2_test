from launch import LaunchDescription
import os
from ament_index_python.packages import get_package_share_path
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node

def generate_launch_description():

    urdf_path = os.path.join(get_package_share_path('my_robot_description'), 'urdf', 'my_robot.urdf.xacro')
    rviz_config_path = os.path.join(get_package_share_path('my_robot_bringup'),'rviz', 'urdf_config.rviz')
    world_path = os.path.join(get_package_share_path('my_robot_bringup'), 'worlds', 'first_worlds.world')




    robot_description= ParameterValue(Command(['xacro ', urdf_path]), value_type=str)

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters= [{'robot_description' : robot_description}],
    )


    joint_state_publisher_gui_node = Node(
    package="joint_state_publisher_gui",
    executable="joint_state_publisher_gui",
    )

    jrviz2_node = Node(
    package="rviz2",
    executable="rviz2",
    arguments=['-d',rviz_config_path]
    )


    gazebo_node = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-topic", "robot_description" ,"-entity", "my_robot"],
        output="screen",
        # prefix="gnome-terminal --",
    )
    
    

    return LaunchDescription([
        robot_state_publisher_node,
        gazebo_node,
        joint_state_publisher_gui_node,
        jrviz2_node,
    ])