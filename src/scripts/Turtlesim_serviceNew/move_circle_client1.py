#!/usr/bin/env python

import rospy
from ros_coc.srv import MoveCirclenew
from ros_coc.srv import MoveCirclenewRequest
from ros_coc.srv import MoveCirclenewResponse

def move_circle_client():
    rospy.wait_for_service('move_circle')
    try:
        radius = float(input("Enter Radius (0 - 2.5) : "))
        speed = float(input("Enter Speed : "))
	distance =float(input("Enter distance : "))
        move_circle = rospy.ServiceProxy('move_circle', MoveCirclenew)
        resp = move_circle(speed,radius,distance)
        return resp.str
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    print "Turtlesim moves"
    response=move_circle_client()
    print response
