Motion capture feedback and setpoint to Intel Aero drone
========================================================

Here we try to document our road from out of the box Intel Aero drone, to a working motion capture feedback loop used to correct the position of the intel aero drone, and make it hold its pose.

The Optitrack Motion capture software, Motive Tracker, will stream pose data of the registered rigid-bodies over VRPN. This will be received by a VRPN ROS node and redirected to the correct topic. The MAVROS ROS node is used to communicate with the px4 autopilot software in the drone, using the MAVlink protocol. With the QGroundControl, a interface for the px4 software, we will enable the use of motion capture data, and disable the use of  e.g. gyro and gps. This will render the Intel drone completely dependent on the motion capture data for determining its position, as the mocap system is very accurate (< 0.2 mm).

When this is done, we will use our own ROS package, running a c++ script, enabling the px4 flight mode OFFBOARD, arming it and set the Setpoint of the drone.

Prerequisites
-------------

### Hardware
* Intel Aero Ready To Fly Drone
* Optitrack Motion Capture System
* Two wifi adapters

### Software
* Motive tracker (for optitrack)
* Ubuntu 16.04
* ROS Kinetic

### ROS packages
* VPRN Client ROS 
* Mavros


Getting started
---------------

For in-depth description and explanation regarding Intel Aero Drone, its systems and the physical drone, see their comprehensive wiki-page, https://github.com/intel-aero/meta-intel-aero/wiki. For tutorials on ROS, see http://wiki.ros.org/ROS/Tutorials

### 1. Install required software
* [Install Ubuntu 16.04](https://help.ubuntu.com/lts/installation-guide/index.html)
* [Install ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu) and [create catkin workspace.]( http://wiki.ros.org/catkin/Tutorials/create_a_workspace)
* [Install QGroundControl](https://docs.qgroundcontrol.com/en/getting_started/download_and_install.html)
* [Install ROS package VRPN client ROS](http://wiki.ros.org/vrpn_client_ros)
* [Install ROS package mavros](https://github.com/mavlink/mavros/blob/master/mavros/README.md#installation)

### 2. Flash and calibrate drone
Intel provides a step by step tutorial of getting the Intel Aero drone up and running. Start by flash and calibration of the drone, https://github.com/intel-aero/meta-intel-aero/wiki/02-Initial-Setup

### 3. Enable and and tune px4 parameters
* [Switch state estimator to LPE](https://dev.px4.io/en/advanced/switching_state_estimators.html)
* [Enable external pose input](https://dev.px4.io/en/ros/external_position_estimation.html#enabling-external-pose-input)
* [Disable baro fusion](https://dev.px4.io/en/ros/external_position_estimation.html#disabling-barometer-fusion)
* [Tune/reduce parameters](https://dev.px4.io/en/ros/external_position_estimation.html#tuning-noise-parameters)

### 4. Clone and install drone_mocap ROS package
Clone ROS package and build catkin.
```
cd ~/catkin/src
git clone https://github.com/mathsten/OsloMet-Bachelorproject-1811
cd ..
catkin_make
```

First autonomous flight
---------
### 1. Map a kill-switch to the RC transmitter

### 2. Configure Motive Tracker
#### Calibrate the Optitrack system

#### Create rigid body

#### Enable VRPN streaming

### 3. VPRN Client ROS node

### 4. Mavros node

### Forward motion capture data

### 5. Drone_mocap node
