'''
Created on 22/nov/2013

@author: GicoPiro
'''

import sys
sys.path.append("Entities/")
sys.path.append("Entities/Starships/")
sys.path.append("Entities/SpaceObject/")
sys.path.append("Utils/")
sys.path.append("Controller/")
sys.path.append("Physics/")

from Screen import screen
main_screen = screen("MadRace - GPSoft", 1080, 720, 80.)
main_screen.setUpOpenGL()
main_screen.mainLoop()