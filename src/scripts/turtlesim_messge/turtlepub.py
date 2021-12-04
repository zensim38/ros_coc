#!/usr/bin/env python

import rospy

from ros_coc.msg import turtledata

#create a new publisher. we specify the topic name, then type of message then the queue size
pub = rospy.Publisher('turtlesim_topic', turtledata, queue_size=10)

#we need to initialize the node
rospy.init_node('turtlesim_publisher_node', anonymous=True)

#set the loop rate
rate = rospy.Rate(1) # 1hz

radius = float(input("Enter Radius (0 - 2.5) : "))
speed = float(input("Enter Speed : "))
td = turtledata()
td.radius = radius
td.speed = speed
rospy.loginfo("I publish:")
rospy.loginfo(td)
pub.publish(td)

rate.sleep()

  
