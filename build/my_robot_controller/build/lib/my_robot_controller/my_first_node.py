#!/usr/bin/env python3

## don't worry about recognizing import modules
## there is a problem with the vscode extension, not ros2
import rclpy
from rclpy.node import Node

# node classes inherit from default node class in rclpy
class MyNode(Node):
    # create constructor
    def __init__(self):
        super().__init__("first_node") # call the 'Node' class constructor
        self.get_logger().info("Hello from ROS2") # write in logger

def main(args=None):
    rclpy.init(args=args) # intialize ros2 communication
    
    # create the nodes (follow oop)
    node = MyNode()

    # spin node --> keep node alive indefinitely until killed
    rclpy.spin(node)

    # destroy node & all ros2 communications
    rclpy.shutdown

if __name__ == '__main__':
    main()