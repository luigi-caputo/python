'''
Created on 05/ago/2013

@author: GicoPiro
'''
import math
class vec3(object):
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return "(%s, %s, %s)"%(self.x, self.y, self.z)
            
    def getMagnitude(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)
    
    def normalize(self):
        magnitude = self.getMagnitude()
        if magnitude == 0: return
        self.x = self.x/magnitude
        self.y = self.y/magnitude
        self.z = self.z/magnitude
    
    def __add__(self, vec):
        return vec3(self.x+vec.x, self.y+vec.y, self.z+vec.z)
    def __sub__(self, vec):
        return vec3(self.x-vec.x, self.y-vec.y, self.z-vec.z)
    def __mul__(self, scalar):
        return vec3(self.x*scalar, self.y*scalar, self.z*scalar)
    def __div__(self, scalar):
        return vec3(self.x/scalar, self.y/scalar, self.z/scalar)
    def __neg__(self):
        return vec3(-self.x, -self.y, -self.z)
    def to_tuple(self):
        return (self.x, self.y, self.z)
    @classmethod
    def fromPoints(cls, vecA, vecB):
        return vec3(vecB.x-vecA.x, vecB.y-vecA.y, vecB.z-vecA.z)
    @classmethod
    def getAngle(cls, vec):
        if vec.x == 0:return 0
        return math.degrees(math.atan(vec.y/vec.x))