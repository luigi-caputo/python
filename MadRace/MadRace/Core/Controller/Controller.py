'''
Created on 27/dic/2013

@author: GicoPiro
'''
from Vector3d import vec3
import pygame

class Controller(object):
    
    camera = vec3(0,0,0)
    rotationAngle = 0.
    
    @classmethod
    def eventsUpdate(self):
        keys = pygame.key.get_pressed()
        self.camera.x = 0; self.camera.z = 0
        self.rotationAngle = 0.
        if keys[pygame.K_w]:
            self.camera.z=+1
        if keys[pygame.K_s]:
            self.camera.z=-1
        if keys[pygame.K_a]:
            self.camera.x=-1
            self.rotationAngle = +1.
        if keys[pygame.K_d]:
            self.camera.x=+1
            self.rotationAngle = -1.