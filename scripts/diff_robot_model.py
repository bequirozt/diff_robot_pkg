#!/usr/bin/python

import numpy as np

class Model():
    def __init__(self, r=0.0125, l=0.1):
        self.r = r
        self.l = l
        self.J = self.jacobian(self.r, self.l)

    def jacobian(self, r, l):
        J1 = np.array([[0, -1,  l*np.sqrt(2)/2],
                       [0,  1, -l*np.sqrt(2)/2]])
        J2 = np.linalg.inv(r*np.eye(2))
        return np.dot(J2,J1)

    def wheels_speed(self,x,y,th):
        return np.dot(self.J,np.array([[x],[y],[th]]))