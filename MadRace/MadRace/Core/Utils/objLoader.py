'''
Created on 26/nov/2013

@author: GicoPiro
'''
from vboDrawer import Drawer
from OpenGL.GL import *
import pygame

class Loader(object):
    vectors = [];colors = []
    colorPerVertex = {}; tcoordPerVertex = {}
    textureCoordinates = []
    textures = {}
    textureHandle = None
    indices = []; normalIndices = []; textureIndices = []
    normals = []
    
    @classmethod
    def clear(self):
        self.vectors = [];self.colors = []
        self.textureCoordinates = []
        self.indices = []; self.normalIndices = []; self.textureIndices = []
        self.normals = []
        self.textureHandle = None
    @classmethod
    def open(self, path, name):
        mtls = {}
        current_color = []
        mtlpath = ""
        reader = file(path + name)
        meshes = []; start = False
        count = [0,0,0]
        meshn = 0
        subv=0;subn=0;subt=0
        for line in reader:
            if len(line) != 1:
                raw_line = line.split()
                command = raw_line[0]
                data = raw_line[1:]
                if command == "o":
                    meshn += 1
                    if start == False:
                        start = True
                    else:
                        subv, subn, subt = count
                        self.loadColorsAndTextures()
                        meshes.append(Drawer(self.vectors, self.normals, self.indices, self.normalIndices, self.colors, self.textureCoordinates, self.textureIndices, self.textureHandle))
                        self.clear()
                elif command == "mtllib":
                    mtlpath = data[0]
                    mtls = self.readMaterial(path, mtlpath)
                elif command == "v":
                    count[0] += 1
                    self.vectors.append([float(data[0]), float(data[1]), float(data[2])])
                elif command == "vn":
                    count[1] += 1
                    self.normals.append([float(data[0]), float(data[1]), float(data[2])])
                elif command == "vt":
                    count[2] += 1
                    self.textureCoordinates.append([float(data[0]), float(data[1])])
                elif command == "usemtl":
                    mtl = data[0]
                    current_color = mtls[mtl]
                    try:
                        self.textureHandle = self.textures[mtl]
                    except KeyError:
                        self.textureHandle = None
                elif command == "f":
                    self.indices.append(int(data[0].split("/")[0])-1-subv)
                    self.indices.append(int(data[1].split("/")[0])-1-subv)
                    self.indices.append(int(data[2].split("/")[0])-1-subv)
                    
                    self.normalIndices.append(int(data[0].split("/")[2])-1-subn)
                    self.normalIndices.append(int(data[1].split("/")[2])-1-subn)
                    self.normalIndices.append(int(data[2].split("/")[2])-1-subn)
                    
                    self.colorPerVertex[str(self.vectors[self.indices[-1]])] = current_color
                    self.colorPerVertex[str(self.vectors[self.indices[-2]])] = current_color
                    self.colorPerVertex[str(self.vectors[self.indices[-3]])] = current_color
                    
                    if data[0].split("/")[1] != "":
                        self.textureIndices.append(int(data[0].split("/")[1])-1-subt)
                        self.textureIndices.append(int(data[1].split("/")[1])-1-subt)
                        self.textureIndices.append(int(data[2].split("/")[1])-1-subt)
                        
                        self.tcoordPerVertex[str(self.vectors[self.indices[-1]])] = self.textureCoordinates[self.textureIndices[-1]]
                        self.tcoordPerVertex[str(self.vectors[self.indices[-2]])] = self.textureCoordinates[self.textureIndices[-2]]
                        self.tcoordPerVertex[str(self.vectors[self.indices[-3]])] = self.textureCoordinates[self.textureIndices[-3]]
                        
        self.loadColorsAndTextures()
        meshes.append(Drawer(self.vectors, self.normals, self.indices, self.normalIndices, self.colors, self.textureCoordinates, self.textureIndices, self.textureHandle))
        self.clear()
        return meshes
    
    @classmethod
    def loadColorsAndTextures(self):
        self.textureCoordinates = []
        for vector in self.vectors:
            try:
                self.colors.append(self.colorPerVertex[str(vector)])
                self.textureCoordinates.append(self.tcoordPerVertex[str(vector)])
            except KeyError:
                pass
    
    @classmethod
    def loadTexture(self, texture):
        image = pygame.image.load(texture).convert_alpha()
        width, height = image.get_size()
        imageBuffer = pygame.image.tostring(image, "RGBA", True)
        glPixelStorei(GL_PACK_ALIGNMENT, 1)
        textureHandle = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, textureHandle)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, imageBuffer)
        glBindTexture(GL_TEXTURE_2D, 0)
        return textureHandle
    
    @classmethod
    def readMaterial(self, path, mtlpath):
        materials = {}
        mtl_reader = file(path+mtlpath)
        current_material = ""
        for mtl_line in mtl_reader:
            if len(mtl_line) != 1:
                raw_line_mtl = mtl_line.split()
                command_mtl = raw_line_mtl[0]
                data_mtl = raw_line_mtl[1:]
                if command_mtl == "newmtl":
                    current_material = data_mtl[0]
                elif command_mtl == "Kd":
                    materials[current_material] = [float(data_mtl[0]), float(data_mtl[1]), float(data_mtl[2])]
                elif command_mtl == "d":
                    materials[current_material].append(float(data_mtl[0]))
                elif command_mtl == "map_Kd":
                    self.textures[current_material] = self.loadTexture(path+data_mtl[0])
        return materials
                