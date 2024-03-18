### ros2_ws
### ros2 applications
### Last Updated: Mar 17 2024

### Directory Overview (high to low)

1. package: my_robot_controller
2. ros2 executable name: test_node --> installed with colcon build & will be run with the command line (terminal)
3. file name: my_first_node --> where we write our code
4. node name: first_node --> node name in ros2 functionalities

### Tips & Rules
- Tip 1: you can name all three (ros2 executable, file, node) names the same
- Tip 2: use "colcon build --symlink-install" for build convenience

- Rule 1: everytime you want to run a modified python code, you need to use colcon build. similar to "make" command in C.
- Rule 2: node needs to be running for commands "rqt_graph", "ros2 node list" to be effective

### Installing extensions

1. Install python
2. Install pylance
3. Install ros2
===================
if vscode cannot read ros2 modules (i.e rclpy), do the following:

1) Change python extension version to 22.04
2) Change pylance extension version to 22.04