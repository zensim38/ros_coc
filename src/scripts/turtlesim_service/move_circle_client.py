#!/usr/bin/env python

import rospy
from ros_coc.srv import MoveCircle

def move_circle_client():
    rospy.wait_for_service('move_circle')
    try:
        radius = float(input("Enter Radius (0 - 2.5) : "))
        speed = float(input("Enter Speed : "))
        move_circle = rospy.ServiceProxy('move_circle', MoveCircle)
        move_circle(speed,radius)
        #return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    print "Turtlesim moves in Circle"
    move_circle_client()
