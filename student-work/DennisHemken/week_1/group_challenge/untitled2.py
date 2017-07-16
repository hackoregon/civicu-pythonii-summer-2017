# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 19:06:49 2017

@author: Dennis
"""

#An example of a class that makes bicycles
class Bicycle:
    def __init__(self, size, color, noise):
        self.size = size
        self.color = color
        self.noise = noise
        
    def ring_bell(self):
        return self.noise
        
# making an instance of the Bicycle class
bike_1 = Bicycle(5, "blue", "Clang")

# calling the ring_bell method
bike_1.ring_bell() 

# output: "Clang"