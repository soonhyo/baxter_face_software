#!/usr/bin/env python

"""
@Author: Bilgehan NAL
This file has a class which defines the mouth of the baxter's face.
"""

from PIL import Image
import rospkg

class Eyebrow:

    indexOfEyebrow = 0  # choosen element of the array

    def __init__(self, initEyebrow):
        default_path = rospkg.RosPack().get_path('baxter_face')

        # This array keeps the diffirent shape of eyebrow
        self.eyebrows = [
            Image.open(default_path+"/scripts/data/eyebrow/baxter_eyebrow_0.png"),
            Image.open(default_path+"/scripts/data/eyebrow/baxter_eyebrow_1.png"),
            Image.open(default_path+"/scripts/data/eyebrow/baxter_eyebrow_2.png"),
            Image.open(default_path+"/scripts/data/eyebrow/baxter_eyebrow_3.png"),
            Image.open(default_path+"/scripts/data/eyebrow/baxter_eyebrow_4.png")
        ]

        self.indexOfEyebrow = initEyebrow
    

    # Encapsulation

    def setEyebrow(self, eyebrow):
        self.indexOfEyebrow = eyebrow

    def getEyebrow(self):
        return self.eyebrows[self.indexOfEyebrow]
