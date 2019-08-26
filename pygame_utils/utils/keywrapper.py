import pygame
from pygame.locals import *

class KeyWrapper(object):
    def __init__(self, wm):
        self.wm = wm

    def getKey(self, key):
        return self.wm.get(key, key)