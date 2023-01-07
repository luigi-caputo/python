'''
Created on 13/gen/2014

@author: GicoPiro
'''
from OpenGL.GL import *
class ShaderLoader(object):
    
    @classmethod
    def loadShader(self, vertPath, fragPath):
        shaderProgram = glCreateProgram()
        vertexShader = glCreateShader(GL_VERTEX_SHADER)
        fragmentShader = glCreateShader(GL_FRAGMENT_SHADER)
    
        vertexReader = file("shaders/"+vertPath)
        fragmentReader = file("shaders/"+fragPath)
        vertexSource = ""
        fragmentSource = ""
    
        for vertexLine in vertexReader:
            vertexSource += vertexLine
            vertexSource += "\n"
        for fragmentLine in fragmentReader:
            fragmentSource += fragmentLine
            fragmentSource += "\n"
    
        glShaderSource(vertexShader, vertexSource)
        glCompileShader(vertexShader)
    
        glShaderSource(fragmentShader, fragmentSource)
        glCompileShader(fragmentShader)
    
        if glGetShaderiv(vertexShader, GL_COMPILE_STATUS) == GL_FALSE:
            print "Vertex shader error !"
        if glGetShaderiv(fragmentShader, GL_COMPILE_STATUS) == GL_FALSE:
            print "Fragment shader error !"
    
        glAttachShader(shaderProgram, vertexShader)
        glAttachShader(shaderProgram, fragmentShader)
    
        glLinkProgram(shaderProgram)
        glValidateProgram(shaderProgram)
        
        return (shaderProgram, vertexShader, fragmentShader)
    
    @classmethod
    def destroy(self, fragmentIds):
        glDeleteProgram(fragmentIds[0])
        glDeleteShader(fragmentIds[1])
        glDeleteShader(fragmentIds[2])
    
    