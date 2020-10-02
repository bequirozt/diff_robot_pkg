#!/usr/bin/python

import rospy
import numpy as np
from std_msgs.msg import Float32MultiArray
from diff_robot_sub import WheelsVelPub

def talker():
    pub = rospy.Publisher("wheels_vel",Float32MultiArray, queue_size=1)
    WheelsVelPub()
    rospy.init_node("diff_robot_node", anonymous=True)
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        velocities = Float32MultiArray()
        velocities.data = np.array([1,2,3],dtype=np.float32) 
        pub.publish(velocities)
        rate.sleep()

if __name__ == "__main__":
    talker()