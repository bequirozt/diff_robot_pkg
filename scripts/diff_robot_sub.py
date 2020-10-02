#!/usr/bin/python

from diff_robot_model import Model
from std_msgs.msg import Float32MultiArray
import numpy as np
from diff_robot_model import Model
import rospy
from rospy.numpy_msg import numpy_msg

class WheelsVelPub():

    def __init__(self):
        rospy.Subscriber("wheels_vel", numpy_msg(Float32MultiArray), self.callback)
        self.pub = rospy.Publisher("wheels_vel_procesed", Float32MultiArray)

    def callback(self,data):
        m = Model()
        data = data.data
        n = m.wheels_speed(data[0],data[1],data[2])
        arr = Float32MultiArray()
        arr.data = n
        self.pub.publish(arr)
        