Motion capture feedback and setpoint to Intel Aero drone
========================================================

Here we try to document our road from out of the box Intel Aero drone, to a working motion capture feedback loop used to correct the position of the intel aero drone, and make it hold its pose.

The Optitrack Motion capture software, Motive Tracker, will stream pose data over the VRPN protocol (Virtual Reality 

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

Getting started
---------------

For in-depth description and explanation regarding Intel Aero Drone, its systems and the physical drone, see their [comprehensive wiki-page](https://github.com/intel-aero/meta-intel-aero/wiki)

For tutorials on ROS, see http://wiki.ros.org/ROS/Tutorials

### 1. Install required software
* Install Ubuntu 16.04 https://help.ubuntu.com/lts/installation-guide/index.html
* Install ROS Kinetic http://wiki.ros.org/kinetic/Installation/Ubuntu and create catkin workspace http://wiki.ros.org/catkin/Tutorials/create_a_workspace
* Install QGroundControl

### 2. Flashing and calibrating drone
Intel provides a step by step tutorial of getting the Intel Aero drone up and running. [Start by flash and calibration of the drone.](https://github.com/intel-aero/meta-intel-aero/wiki/02-Initial-Setup)

### 3. 
