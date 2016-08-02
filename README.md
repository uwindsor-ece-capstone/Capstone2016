# Capstone2016
## Introduction 
During the final year of Electrical and Computer Engineering at the University of Windsor, our team was tasked with developing an autonomous vehicle using the Beagle Bone Black (BBB).  Our team took 2 approaches to solving this problem.  

## Project Summary
### The following was implemented
1.	To develop python code to utilize a variety of sensors and XBee 
	1.	Client and Server model to communicate wirelessly between the PC and BBB
		*	Allow the vehicle to function autonomously through the use of sensors and send sensor data to PC 
		*	PC will convert sensor data string into dictionary to allow for extraction of specific sensor data
		*	User will have option to control vehicle manually
		*	User will have ability to shut down vehicle at anytime
2.	To develop a vehicle using ROS to utilize SLAM 
	1.	ROS run across multiple machines, PC and BBB
		*	BBB will send LiDAR and IMU (9DOF) and ROSpy script to control motor function
		*	Two Versions of SLAM tested
			1.	Hector SLAM
			  *	Move_base
			  *	Hector_slam
			  *	Static_transform_tf
			  *	3D model with RVIZ
		  2.	Gmapping
		    *	Move_base
		    *	Laser_scan_matcher
		    *	Static_transorm_tf
		    *	3D model with RVIZ
		*	Map saved from SLAM and run with Localization
			1.	AMCL
			  *	Map_server
			  *	Static_transform_tf
			  *	3D_model with RVIZ
			  *	AMCL

## Team Members
* Affan Rashdi
* Theepan Yoganathan
* Haileab Yoseph

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Dr. Aaron Mavrinac for help throughtout project for giving valuable insight into utilizing ROS
* A Gentle Introduction to ROS by Jason M. O'Kane very helpful in understanding ROS 
* ros.org 
