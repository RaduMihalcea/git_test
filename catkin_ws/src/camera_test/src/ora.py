#!/usr/bin/env python

import rospy	
import time

from std_msgs.msg import String


def ora():
	pub = rospy.Publisher("topic", String, queue_size=10)
	rospy.init_node('ora', anonymous = True)
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		hello="Ora:%s" %time.strftime("%H:%M:%S")
		rospy.loginfo(hello)
		pub.publish(hello)
		rate.sleep()

if __name__ == '__main__':
	try:
		ora()
	except rospy.ROSInterruptException:
		pass
