'''
Created on 23/nov/2013

@author: GicoPiro
'''
from OpenGL.GL import *
from OpenGL.GLU import *
from numpy import array, float32, ushort

class Drawer(object):
    
    def __init__(self, vertices, normals, indices, normalIndices, colors, textureCoordinates, textureIndices, textureHandle):
        
        self.textureHandle = textureHandle
        
        self.verticesSize = len(vertices[0])
        self.normalsSize = len(normals[0])
        self.colorsSize = len(colors[0])
        
        self.indicesLen = len(indices)
        self.normalIndicesLen = len(normalIndices)
        self.textureCoordinates = textureCoordinates
        
        if textureHandle != None:
            self.textureCoordinatesSize = len(textureCoordinates)
            self.textureIndices = textureIndices
            self.textureIndicesLen = len(textureIndices)
        
        self.verticesBuffer = array(vertices, dtype=float32)
        self.colorsBuffer = array(colors, dtype=float32)
        self.indicesBuffer = array(indices, dtype=ushort)
        
        self.normalIndicesBuffer = array(normalIndices, dtype=ushort)
        self.normalsBuffer = array(normals, dtype=float32)
        
        if textureHandle != None:
            self.textureCoordinatesBuffer = array(textureCoordinates, dtype=float32)
            self.textureIndicesBuffer = array(textureIndices, dtype=ushort)
        
        self.verticesHandle = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.verticesHandle)
        glBufferData(GL_ARRAY_BUFFER, self.verticesBuffer, GL_DYNAMIC_DRAW);
        
        self.normalsHandle = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.normalsHandle)
        glBufferData(GL_ARRAY_BUFFER, self.normalsBuffer, GL_DYNAMIC_DRAW);
        
        self.colorsHandle = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.colorsHandle)
        glBufferData(GL_ARRAY_BUFFER, self.colorsBuffer, GL_DYNAMIC_DRAW);
        
        if textureHandle != None:
            self.textureCoordHandle = glGenBuffers(1)
            glBindBuffer(GL_ARRAY_BUFFER, self.textureCoordHandle)
            glBufferData(GL_ARRAY_BUFFER, self.textureCoordinatesBuffer, GL_DYNAMIC_DRAW);
        
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def destroy(self):
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glDeleteBuffers(1, self.verticesBuffer)
        glDeleteBuffers(1, self.normalsBuffer)
        glDeleteBuffers(1, self.colorsBuffer)
        if self.textureHandle != None:
            glDeleteTextures(self.textureHandle)
        
    def draw(self, method):
        if self.textureHandle != None:
            glBindTexture(GL_TEXTURE_2D, self.textureHandle)
        
        #LOAD Vertices
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)
        
        glBindBuffer(GL_ARRAY_BUFFER, self.verticesHandle)
        glVertexPointer(self.verticesSize, GL_FLOAT, 0, None)
        
        glBindBuffer(GL_ARRAY_BUFFER, self.colorsHandle)
        glColorPointer(self.colorsSize, GL_FLOAT, 0, None)
        
        if self.textureHandle != None:
            glEnableClientState(GL_TEXTURE_COORD_ARRAY)
            glBindBuffer(GL_ARRAY_BUFFER, self.textureCoordHandle)
            glTexCoordPointer(2, GL_FLOAT, 0, None)
        
        glDrawElements(method, self.indicesLen, GL_UNSIGNED_SHORT, self.indicesBuffer);
        
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_COLOR_ARRAY)
        glDisableClientState(GL_TEXTURE_COORD_ARRAY)
        
        ###LOAD Normals
        glEnableClientState(GL_NORMAL_ARRAY)
        
        glBindBuffer(GL_ARRAY_BUFFER, self.normalsHandle)
        glNormalPointer(GL_FLOAT, 0, None)
        
        glDrawElements(GL_TRIANGLES, self.normalIndicesLen, GL_UNSIGNED_SHORT, self.normalIndicesBuffer);
        
        glDisableClientState(GL_NORMAL_ARRAY)
        if self.textureHandle != None:
            glBindTexture(GL_TEXTURE_2D, 0)