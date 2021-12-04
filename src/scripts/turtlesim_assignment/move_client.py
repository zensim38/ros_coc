#!/usr/bin/env python

import rospy
from ros_coc.srv import Move

def move_client():
    rospy.wait_for_service('move')
    try:
        d = float(input("Enter distance : "))
        s = float(input("Enter speed : "))
	flag = bool(input("Enter if 'is forward'(True or False) : "))
        move = rospy.ServiceProxy('move', Move)
        move(d,s,flag)
        #return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    print "Turtlesim Moves"
    move_client()
