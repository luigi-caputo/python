'''
Created on 29/nov/2013

@author: GicoPiro
'''
from Ship import ship
from baseModel import baseModel
from Controller import Controller
from Vector3d import vec3
from decimal import Decimal

class controllableShip(ship):
    def __init__(self, pos, speed, Type = "CO"):
        ship.__init__(self, "modelBase.obj", pos, Type)
        self.pos = vec3(0,0,0)
        self.speed = speed
        self.rotation.z = 1.
    def update(self, delta):
        self.pos += Controller.camera*delta*self.speed
        self.angle += Controller.rotationAngle*delta*self.speed*2
        if abs(self.angle) >= 30:
            self.angle -= Controller.rotationAngle*delta*self.speed*2
           
        if Controller.rotationAngle == 0:
            if round(self.angle) > 0:
                self.angle -= delta*self.speed*2
            elif round(self.angle) < 0:
                self.angle += delta*self.speed*2
            elif round(self.angle) == 0:
                self.angle = 0
        ship.update(self, delta)