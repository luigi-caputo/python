'''
Created on 08/gen/2014

@author: GicoPiro
'''
from Entity import entity
class Planet(entity):
    def __init__(self, pos, scale, color=(0.1,0.1,0.1), name="planet.obj"):
        entity.__init__(self, name, pos, Type = "AI")
        self.pos = pos
        self.scale = scale
        self.color = color
    def draw(self):
        entity.draw(self)