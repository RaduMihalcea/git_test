#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')
import rospy

import tf
import turtlesim.msg

def handle_turtle_pose(msg, turtlename):
    
    br = tf.TransformBroadcaster()
    
    br.sendTransform((msg.x, msg.y, 0),tf.transformations.quaternion_from_euler(0, 0, msg.theta), rospy.Time.now(), turtlename, "world")
    #sendTransform are 5 parametri
        #quaternion = transformarea de rotatie
        #(msg.x, msg.y, 0) transformarea de tranzlatie
        #timpul la care trebuie publicata transformarea rospy.Time.now()
        #numele nodului parinte (base_link)
        #numele nodului fiu (laser_link)
if __name__ == '__main__':
    
    rospy.init_node('turtle_tf_broadcaster')
    #initializarea nodului
    turtlename = rospy.get_param('~turtle')
    #definirea numelui testoasei
    rospy.Subscriber('/%s/pose' % turtlename, turtlesim.msg.Pose, handle_turtle_pose, turtlename)
    #subscriberul care ia datele din turtlename de tip turtlesim.msg.Pose, face callback la handle_turtle_pose
    rospy.spin()