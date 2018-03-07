Motion capture feedback and setpoint to Intel Aero drone
========================================================

Here we try to document our road from out of the box Intel Aero drone, to a working motion capture feedback loop used to correct the position of the intel aero drone, and make it hold its pose.

The Optitrack Motion capture software, Motive Tracker, will stream pose data of the registered rigid-bodies over VRPN. This will be received by a VRPN ROS node and redirected to the correct topic. The MAVROS ROS node is used to communicate with the px4 autopilot software in the drone, using the MAVlink protocol. With the QGroundControl, a interface for the px4 software, we will enable the use of motion capture data, and disable the use of  e.g. gyro and gps. This will render the Intel drone completely dependent on the motion capture data for determining its position, as the mocap system is very accurate (< 0.2 mm).

When this is done, we will use our own ROS package, running a c++ script, enabling the px4 flight mode OFFBOARD, arming it and set the Setpoint of the drone.
 
 
Table of contents
-----------------

1. [Prerequisites](#Prerequisites)
2. [Getting started](#)
3. [First autonomous flight]
4. [Results]
 
 
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

#### [Install Ubuntu 16.04](https://help.ubuntu.com/lts/installation-guide/index.html)

#### [Install ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu) and [create catkin workspace.]( http://wiki.ros.org/catkin/Tutorials/create_a_workspace)

#### [Download QGroundControl](https://docs.qgroundcontrol.com/en/getting_started/download_and_install.html)
```sh
# Make it executable and launch QGgroundControl
chmod +x ./QGroundControl.AppImage
./QGroundControl.AppImage  (or double click)
```

#### [Install ROS package VRPN client ROS](http://wiki.ros.org/vrpn_client_ros) 
```sh
sudo apt-get install ros-kinetic-vrpn-client-ros
```

#### [Install ROS package mavros](https://github.com/mavlink/mavros/blob/master/mavros/README.md#installation)
```sh
# Mavros ROS package
sudo apt-get install ros-kinetic-mavros ros-kinetic-mavros-extras

# Mavros is dependent on the GeographicLib datasets
wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh
./install_geographiclib_datasets.sh
```

### 2. Flash and calibrate drone
Intel provides a step by step tutorial of getting the Intel Aero drone up and running. Start by flash and calibration of the drone, https://github.com/intel-aero/meta-intel-aero/wiki/02-Initial-Setup

### 3. Enable and and tune px4 parameters
It is necessary to tune som parameters in the px4 flight control software. This is done from QGroundControl.

* [Switch state estimator to LPE](https://dev.px4.io/en/advanced/switching_state_estimators.html)
* [Enable external pose input](https://dev.px4.io/en/ros/external_position_estimation.html#enabling-external-pose-input)
* [Disable baro fusion](https://dev.px4.io/en/ros/external_position_estimation.html#disabling-barometer-fusion)
* [Tune/reduce parameters](https://dev.px4.io/en/ros/external_position_estimation.html#tuning-noise-parameters)

### 4. Clone and install drone_mocap ROS package
Clone ROS package and build catkin.
```sh
cd ~
git clone https://github.com/mathsten/OsloMet-Digital-Twin.git
cp -a OsloMet-Digital-Twin/drone_mocap/. catkin_ws/src/drone_mocap
cd catkin_ws/
catkin_make
```


First autonomous flight
---------

### 1. Safety measures
#### Map a kill-switch to the RC transmitter
This is an important step since there will always be some uncertainty regarding the real life behaviour of the autonomous system in action. The steps is the same as for [mapping any flight mode.](https://docs.px4.io/en/config/flight_mode.html)

#### Turn off hibernate on ROS computer
In one of our tests, our flight time was so long that the ROS computer began to hibernate. This resulted in instantaneous loss of signal, where the drone crashed, before the the software switch from offboard flight mode to stabilize flight mode (as supposed to) and the quad flew into the air uncontrolable.

#### Physical safety measures
Consider using a net to protect from uncontrolable drones and/or some kind of string from the drone to the ground to limit its range.

### 2. Configure Motive Tracker
Optitrack has a great [OptiTrack Documentation Wiki](https://v20.wiki.optitrack.com/index.php?title=OptiTrack_Documentation_Wiki) with videos and in-depth pages for there system. Calibrating the system, create rigid bodies and enable vrpn streaming will be most important for this project.

* [Calibrate the Optitrack system](https://v20.wiki.optitrack.com/index.php?title=Calibration)
* [Create and track rigid Body](https://v20.wiki.optitrack.com/index.php?title=Rigid_Body_Tracking)
* [Enable VRPN streaming](https://v20.wiki.optitrack.com/index.php?title=Data_Streaming)

### 3. Setup two wifi connections
At this point you will have to connect to both the network the Motive Tracker software is on, and the local network the Intel Aero Drone creates. The Motive Tracker network to receive pose data, and the Intel local network to communicate with the drone.

### 4. Checking QGroundControl parameters


### 5. Run vrpn node, mavros node and drone_mocap node
```sh
# Some parameters: server, fcu_url, gcs_url, drone_setpoint/x, drone_setpoint/y, drone_setpoint/z
roslaunch drone_mocap drone_mocap.launch

```

