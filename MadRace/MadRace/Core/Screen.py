'''
Created on 22/nov/2013

@author: GicoPiro
'''
import pygame
from pygame.locals import *
from sys import exit
from OpenGL.GL import *
from OpenGL.GLU import *
from Controller import Controller
from controllableShip import controllableShip
from Vector3d import vec3
from Space import Space
from baseModel import baseModel
from Planet import Planet
from Star import Star
from ShaderLoader import ShaderLoader

class screen(object):
    
    def __init__(self, title, width, height, fov):
        self.width = width
        self.height = height
        self.title = title
        self.fov = fov
        pygame.init()
        self.display = pygame.display.set_mode((width, height), HWSURFACE|DOUBLEBUF|OPENGL, 32)
        pygame.display.set_caption(title)
        self.time = pygame.time.Clock()
        self.stars = Space(100, vec3(1000,100,3000), 2)
        
    def setUpOpenGL(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.fov, float(self.width)/self.height, 0.3, 10000.)
        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        pos = vec3(0.,-3.2,-6.5)
        
        self.truck1 = controllableShip(pos, 40.)            ##--->> ALWAYS AS FIRST INSTANCE
        self.test = baseModel(vec3(20.,-3.2,-30))
        self.test_planet = Planet(vec3(-20.,-3.2,-50),vec3(20.,20.,20.))
        self.star = Star(vec3(-20.,-3.2,-10000),vec3(450.,450.,450.))
        
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        
    def tick(self):
        currentTime = self.time.tick()
        currentTimeInSec = currentTime / 1000.
        return currentTimeInSec
    
    def input(self):
        for event in pygame.event.get():
                if event.type == QUIT:
                    self.truck1.unload()
                    self.test.unload()
                    self.stars.destroy()
                    self.test_planet.unload()
                    self.star.unload()
                    exit()
    def mainLoop(self):
        while True:
            self.input()
            self.update()
            self.render()
            pygame.display.flip()
    def update(self):
        delta = self.tick()
        Controller.eventsUpdate()
        self.truck1.update(delta)
        self.test.update(delta)
        self.test_planet.update(delta)
        self.star.update(delta)
    def render(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT|GL_STENCIL_BUFFER_BIT)
        self.truck1.draw()
        self.test.draw()
        self.test_planet.draw()
        self.star.draw()
        self.stars.draw(self.truck1)