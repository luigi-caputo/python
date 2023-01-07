'''
Created on 29/nov/2013

@author: GicoPiro
'''
from OpenGL.GL import glRotatef, glTranslatef, GL_TRIANGLES, glPushMatrix, glPopMatrix, glScalef
from objLoader import Loader
from Vector3d import vec3

entities = []
class entity(object):
    def __init__(self, name, pos, Type, obj="models/"):
        self.name = name
        self.speed = 0.
        self.angle = 0.
        self.model = Loader.open(obj, name)
        self.posini = pos
        self.rotation = vec3(0,0,0)
        self.scale = vec3(1.,1.,1.)
        entities.append(self)
        self.Type = Type
    def draw(self):
        glPushMatrix()
        glTranslatef(self.posini.x, self.posini.y, self.posini.z)
        if self.Type == "AI":
            glTranslatef(-entities[0].pos.x, entities[0].pos.y, entities[0].pos.z)
        glRotatef(self.angle, self.rotation.x, self.rotation.y, self.rotation.z)
        glScalef(self.scale.x,self.scale.y,self.scale.z)
        for mesh in self.model:
            mesh.draw(GL_TRIANGLES)
        glPopMatrix()
    def update(self, delta):
        pass
    def unload(self):
        global entities
        for mesh in self.model:
            mesh.destroy()
        entities.remove(self)
    @classmethod
    def unloadall(cls):
        global entities
        for entity in entities:
            for mesh in entity.model:
                mesh.destroy()
        entities = []