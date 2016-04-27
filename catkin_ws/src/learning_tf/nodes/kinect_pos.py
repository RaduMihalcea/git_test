#!/usr/bin/env python

import roslib
roslib.load_manifest('learning_tf')
import rospy

import tf
import turtlesim.msg

class Kinect_tf:

	def __init__(self):
		self.sub = rospy.Subscriber('coordinates_topic', PoseStamped, pose_callback, Kinect)

	def pose_callback(msg, turtlename):
    
    	br = tf.TransformBroadcaster()
    
    	br.sendTransform((msg.x, msg.y, 0),
    		tf.transformations.quaternion_from_euler(0, 0, msg.theta), 
    		rospy.Time.now(), turtlename, "world")
	    #sendTransform are 5 parametri
	        #quaternion = transformarea de rotatie
	        #(msg.x, msg.y, 0) transformarea de tranzlatie
	        #timpul la care trebuie publicata transformarea rospy.Time.now()
	        #numele nodului parinte (base_link)
	        #numele nodului fiu (laser_link)

def main(args):
	ic = Kinect_tf()
	rospy.init_node('Kinect_tf', anonymous = True)

	try:
		rospy.spin()
	except KeyboardInterrupt:
		print 'Shutting down'

if __name__ == '__main__':
    
	main(sys.argv)