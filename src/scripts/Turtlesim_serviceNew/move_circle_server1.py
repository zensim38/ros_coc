#!/usr/bin/env python
import rospy
from ros_coc.srv import MoveCirclenew
from ros_coc.srv import MoveCirclenewRequest
from ros_coc.srv import MoveCirclenewResponse
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
x=0
y=0
yaw=0
PI = 3.1415926535897


def poseCallback(pose_message):
	global x
	global y, yaw
	x= pose_message.x
	y= pose_message.y
	yaw = pose_message.theta

 

def handle_move_circle(req):
	global x, y
        x0=x
        y0=y
	
	vel_msg = Twist()
	speed = req.s
	radius = req.r
	distance = req.d

	print "Proceeding to move Turtle in circle"
	


	vel_msg.linear.x = speed
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = radius

 	distance_moved = 0.0
        loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    
        cmd_vel_topic='/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        while True :
                rospy.loginfo("Turtlesim moves forwards")
                velocity_publisher.publish(vel_msg)

                loop_rate.sleep()
                
                #rospy.Duration(1.0)
                
                distance_moved = abs(0.5 * math.sqrt(((x-x0) ** 2) + ((y-y0) ** 2)))
                print  distance_moved               
                if  not (distance_moved<distance):
                    rospy.loginfo("reached")
		    return MoveCirclenewResponse('reached home') 

                    break
        
        #finally, stop the robot when the distance is moved
        vel_msg.linear.x =0
        velocity_publisher.publish(vel_msg)
    	

def move_circle_server():
	rospy.init_node('move_circle_server')
	s = rospy.Service( 'move_circle', MoveCirclenew, handle_move_circle )
	rospy.spin()

if __name__ == "__main__":
        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback) 
	move_circle_server()

