'''
Created on 03/gen/2014

@author: GicoPiro
'''
from Ship import ship

class baseModel(ship):
    def __init__(self, pos, Type="AI", name="modelBase.obj"):
        ship.__init__(self, name, pos, Type)
        self.speed = 80.
        self.rotation.z = 1.
    def update(self, delta):
        self.angle -= 0.5
        ship.update(self, delta)