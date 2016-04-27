#!/usr/bin/env python


import numpy as np
import roslib
import sys
import rospy
import cv2
import time
from std_msgs.msg import String 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


bridge = CvBridge()

def callback(data):
	rospy.loginfo("SUBSCRIBE--->%s" %data.data)

def callback1(data):
	try:
		cv_image = bridge.imgmsg_to_cv2(data, "8UC1")
		#print "CALLBACK"
	except CvBridgeError as e:
		print e

	cv2.imshow('Telespectator',cv_image)
	cv2.waitKey(3)


def ascultator():
	#rospy.init_node('ascultator', anonymous = True)
	sub = rospy.Subscriber('topic', String, callback)
	rospy.spin()

def telespectator():
	
	rospy.init_node('telespectator', anonymous = True)
	sub = rospy.Subscriber('topic1', Image, callback1)
	print "telespectator"

def main(args):
	
	telespectator()
	ascultator()
	rospy.init_node('ascultator', anonymous = True)

	print "main"
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print "Shut Down"
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main(sys.argv)
