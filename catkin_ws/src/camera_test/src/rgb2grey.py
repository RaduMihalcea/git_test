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



class afisare:
	

	def __init__(self):
		
		self.bridge = CvBridge()
		self.cap = cv2.VideoCapture(0)
		self.cap2 = rospy.Subscriber("/optris/image_color", Image, self.callback)
		self.pub = rospy.Publisher("topic1", Image, queue_size = 5)


	def callback(self, data):
		try:
			self.cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
			gray = cv2.cvtColor(self.cv_image,cv2.COLOR_BGR2GRAY)
		except CvBridgeError as e:
			print (e)
		
		try:
			self.pub.publish(self.bridge.cv2_to_imgmsg(gray, '8UC1'))
		except CvBridgeError as e:
			print (e)


		
		cv2.imshow("Fereastra1", gray)
		cv2.waitKey(3)

		


def ora():
	pub = rospy.Publisher("topic", String, queue_size=10)
	rospy.init_node('ora', anonymous = True)
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		hello="Ora:%s" %time.strftime("%H:%M:%S")
		rospy.loginfo(hello)
		pub.publish(hello)
		rate.sleep()


	

def main(args):
	ic=afisare()
	ora()
	rospy.init_node('afisare', anonymous = True)
	rospy.init_node('ora', anonymous = True)
	print "main"
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print "Shut Down"
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main(sys.argv)
