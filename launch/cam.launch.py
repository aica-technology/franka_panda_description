import os
import xacro

from launch import LaunchDescription

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    # robot_description_content = Command(
    #     [
    #         PathJoinSubstitution([FindExecutable(name="xacro")]),
    #         " ",
    #         PathJoinSubstitution([FindPackageShare("franka_panda_description"), "robots/panda_arm_hand_cam.urdf.xacro"]),
    #     ]
    # )
    # robot_description = {"robot_description": robot_description_content}

    pkg_share = FindPackageShare("franka_panda_description").find("franka_panda_description")
    parameters = {"robot_name": "franka"}
    doc = xacro.process_file(os.path.join(pkg_share, "robots/panda_arm_hand_cam.urdf.xacro"),  mappings=parameters)
    robot_description = {"robot_description": doc.toprettyxml(indent="  ")}

    robot_state_pub_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="both",
        parameters=[robot_description],
    )

    joint_state_pub_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        output="both",
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        arguments=["-d", os.path.join(pkg_share, "config/cam.rviz")],
        output="log",
    )

    nodes = [
        robot_state_pub_node,
        joint_state_pub_node,
        rviz_node,
    ]

    return LaunchDescription(nodes)