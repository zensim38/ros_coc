#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

from ros_coc.msg import turtledata
def turtle_callback(turtle_m):
    vel_m = Twist()
    r = turtle_m.radius
    s = turtle_m.speed
    rospy.loginfo("radius & speed of turtlesim received: (%.2f,%.2f)",r,s)
    
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
    
    vel_m.linear.x = s
    vel_m.angular.z = r
    while not rospy.is_shutdown():
        pub.publish(vel_m)
	
    vel_ms.linear.x = 0	
    vel_ms.linear.z = 0
    pub.publish(vel_m)
def listener():
    rospy.init_node('turtlesim_subscriber_node', anonymous=True)

    rospy.Subscriber("turtlesim_topic", turtledata, turtle_callback)
# spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
