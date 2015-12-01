"""
conway.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life


Reference Morgan's Code Here: https://github.com/morganmeliment/Conway-Life/blob/master/conway.py
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


            
class Sun(Sprite):
    
    asset = ImageAsset("images/sun.png")
    width = 80
    height = 76
    
    def __init__(self, position):
        super().__init__(Sun.asset, position)
        self.fxcenter = 0.5
        self.fycenter = 0.5
        self.circularCollisionModel()
            
            
class Explosion(Sprite):
    
    asset = ImageAsset("images/explosion2.png", Frame(0,0,4800/25,195), 25)
    
    def __init__(self, position):
        super().__init__(ExplosionBig.asset, position)
        self.image = 0
        self.center = (0.5, 0.5)
        
    def step(self):
        self.setImage(self.image//2)  # slow it down
        self.image += 1
        if self.image == 50:
            self.destroy()
            

class spaceship(Sprite)
