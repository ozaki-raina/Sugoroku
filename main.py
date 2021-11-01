import pygame
from pygame.locals import *
#from Screen_abc import Screen
from TestScreen import TestScreen
from TestScreen2 import TestScreen2
from StartScreen import StratScreen
import Screen_abc as SC
from MainScreen import MainScreen

#screen = [StratScreen()]
#screen = [StratScreen(),TestScreen(),TestScreen2()]
screen = [MainScreen()]

if __name__ == '__main__':
    while True:
        screen[SC.ScreenNum].display()
        screen[SC.ScreenNum].getEvent()


