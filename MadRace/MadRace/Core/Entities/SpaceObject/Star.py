'''
Created on 20/gen/2014

@author: GicoPiro
'''
from Planet import Planet
from OpenGL.GL import *

class Star(Planet):
    def __init__(self, pos, scale, color=(0.5,0.5,0.)):
        Planet.__init__(self, pos, scale, color)
        glLight(GL_LIGHT0, GL_DIFFUSE, [1.,1.,1.,1.])
        glLight(GL_LIGHT0, GL_AMBIENT, [0.2,0.2,0.2,1.])
        glLight(GL_LIGHT0, GL_POSITION, [pos.x, pos.y, pos.z,1.])
    def draw(self):
        glMaterial(GL_FRONT, GL_EMISSION, self.color)
        Planet.draw(self)
        glMaterial(GL_FRONT, GL_EMISSION, (0.,0.,0.))