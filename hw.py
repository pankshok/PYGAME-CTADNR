import pygame
import sys
from pygame.locals import *

AQUA      =  (  0, 255, 255)
BLACK     =  (  0,   0,   0)
BLUE      =  (  0,   0, 255)
FUCHSIA   =  (255,   0, 255)
GRAY      =  (128, 128, 128)
GREEN     =  (  0, 128,   0)
LIME      =  (  0, 255,   0)
MAROON    =  (128,   0,   0)
NAVYBLUE  =  (  0,   0, 128)
OLIVE     =  (128, 128,   0)
PURPLE    =  (128,   0, 128)
RED       =  (255,   0,   0)
SILVER    =  (192, 192, 192)
TEAL      =  (  0, 128, 128)
WHITE     =  (255, 255, 255)
YELLOW    =  (255, 255,   0)

class Coord(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        print "({0}; {1})".format(self.x, self.y)
    
    def getXY(self):
        return (self.x, self.y)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def setXY(self, x, y):
        self.x = x
        self.y = y

class Entity(object):
    def __init__(self):
        self.coord = Coord(None, None)
        self.type = None
        self.visible = True #?
        self.image = None
        
    def getX(self):
        return self.coord.getX()
    def getY(self):
        return self.coord.getY()
    def getXY(self):
        return self.coord.getXY()
    
    def setX(self, x):
        self.coord.setX(x)
    def setY(self, y):
        self.coord.setY(y)
    def setXY(self, x, y):
        self.coord.setXY(x, y)

    def setImage(self, path):
        self.image = pygame.image.load(path)
    def getImage(self):
        return self.image

    def get_height(self):
        return self.image.get_height()
    def get_width(self):
        return self.image.get_width()

class PlayerShip(Entity):
    def __init__(self, startX, startY):
        self.coord = Coord(startX, startY)
        self.type = "PlayerShip"
        self.direction = None
        


class game(object):

    def __init__(self):
        self.FPS = 60
        self.fpsClock = pygame.time.Clock()
        
        pygame.init()
        self.width = 640
        self.height = 480
        self.fullscreen = 0
        self.depth = 32
        self.display = pygame.display.set_mode((self.width, self.height), self.fullscreen, self.depth)
        pygame.display.set_caption('Animation')
        self.playerShip = PlayerShip(0,0)
        self.playerShip.setImage('res/image 17.png')
        self.playerShip.setXY(self.display.get_width() / 2 - self.playerShip.get_width() / 2, self.display.get_height() - self.playerShip.get_height())
        #self.catImg = pygame.image.load('res/image 17.png')
        
        #self.catCoord = Coord(10, 10)
#        self.fontObj = pygame.font.Font('freesansbold.ttf', 16)
#        self.mytext = self.fontObj.render("L", True, RED)
#        self.mytextRect = self.mytext.get_rect()
#        self.mytextRect.center = (self.mycat.get_width() / 2, self.mycat.get_height() / 2)
#        self.textSurfaceObj = self.fontObj.render(self.direction, True, BLACK, WHITE)
#        self.textRectObj = self.textSurfaceObj.get_rect()
#        self.textRectObj.center = (200, 150)

        pygame.mixer.music.load('res/runaway.mp3')
        pygame.mixer.music.play(-1, 0.0)
        
        self.keyToDir = {
            273: "up",
            119: "up",
            274: "down",
            115: "down",
            275: "right",
            100: "right",
            276: "left",
            97: "left"
            }
#        self.direction = None
        
    def init(self):
        pass

    def quit(self):
        pass

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key in self.keyToDir.keys():
                print "KEY {0} MOD {1}".format(event.key, event.mod)
                self.playerShip.direction = self.keyToDir[event.key]
            else:
                print(event)

    def updateState(self):
        if self.playerShip.direction == "up":
            self.playerShip.setY(self.playerShip.getY() - 25)
            if self.playerShip.getY() < 0:
                self.playerShip.setY(0)
            self.playerShip.direction = None
        elif self.playerShip.direction == "down":
            self.playerShip.setY(self.playerShip.getY() + 25)
            if self.playerShip.getY() + self.playerShip.get_height() >= self.display.get_height():
                self.playerShip.setY(self.display.get_height() - self.playerShip.get_height())
            self.playerShip.direction = None
        elif self.playerShip.direction == "right":
            self.playerShip.setX(self.playerShip.getX() + 25)
            if self.playerShip.getX() + self.playerShip.get_width() >= self.display.get_width():
                self.playerShip.setX(self.display.get_width() - self.playerShip.get_width())
            self.playerShip.direction = None
        elif self.playerShip.direction == "left":

            self.playerShip.setX(self.playerShip.getX() - 25)
            if self.playerShip.getX() <= 0:
                self.playerShip.setX(0)
            self.playerShip.direction = None
        else:
            pass
        

    def drawScreen(self):
        self.display.fill(BLACK)
        #self.display.blit(self.catImg, self.catCoord.getXY())
        self.display.blit(self.playerShip.getImage(), self.playerShip.getXY())
        pygame.display.update()
        self.fpsClock.tick(self.FPS)


catgame = game()

while True:
    catgame.handleEvents()
    catgame.updateState()
    catgame.drawScreen()
