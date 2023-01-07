'''
Created on 29/nov/2013

@author: GicoPiro
'''
from Entity import entity

class ship(entity):
    def __init__(self, name, pos, Type = "AI"):
        entity.__init__(self, name, pos, Type)
    def update(self, delta):
        entity.update(self, delta)