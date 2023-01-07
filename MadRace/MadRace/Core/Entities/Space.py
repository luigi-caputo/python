'''
Created on 29/dic/2013

@author: GicoPiro
'''
from vboDrawer import Drawer
from OpenGL.GL import GL_POINTS, glTranslatef, glRotatef, glPopMatrix, glPushMatrix
import random
from Controller import Controller
from Vector3d import vec3
#from Entity import entity
import math

class Space(Drawer):
    def __init__(self, starn, spaceRange, density):
        vertices = []
        colors = []
        for _ in xrange(starn):
            for _ in xrange(density):
                vertices.append([random.uniform(-spaceRange.x,spaceRange.x), random.uniform(-spaceRange.y,spaceRange.y), random.uniform(-spaceRange.z,spaceRange.z)])
                if random.randint(0,1) == 1:
                    colors.append([1.,1.,random.uniform(0,1)])
                else:
                    colors.append([random.uniform(0,1),1.,1.])
        indices = range(starn)
        Drawer.__init__(self, vertices, vertices, indices, indices, colors, vertices, vertices, None)
    def draw(self, controllableShip):
        glPushMatrix()
        glTranslatef(-controllableShip.pos.x, controllableShip.pos.y, controllableShip.pos.z)
        glRotatef(-controllableShip.speed,0,1,0)
        Drawer.draw(self, GL_POINTS)
        glPopMatrix()
        #for e in entity.entities:
        #    if e.Type != "CO":
        #        print "ok"