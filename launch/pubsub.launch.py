from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="ros2_launch_demo",
                executable="talker",
                parameters=[{"message_prefix": "ROS2"}],
                output="screen",
            ),
            Node(
                package="ros2_launch_demo",
                executable="listener",
                output="screen",
            ),
        ]
    )




