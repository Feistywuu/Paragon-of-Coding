#Load Image Function
import os, sys, random
import pygame
from pygame.locals import *

os.chdir('''C:\\Users\\Philip\\Documents\\Programming\\BasicMovement''')
picture_dir = os.path.join(os.getcwd(), "Pictures")
#Could use os.walk instead
#Check 'Anaconda'

def load_image(name, colorkey=None):
    fullname = os.path.join(picture_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print("Cannot load image:", fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

#Tower Class

ceb = load_image('ceb1.png', -1)            #Normal Surfaces
ana = load_image('ana.png', -1)
flower = load_image('flower.png', -1)
godson = load_image('godson.png', -1)
jerax = load_image('jerax.png', -1)
ceb2 = load_image('ceb1.png', -1)           #Blue Surfaces
ana2 = load_image('ana.png', -1)
flower2 = load_image('flower.png', -1)
godson2 = load_image('godson.png', -1)
jerax2 = load_image('jerax.png', -1)
#Blue Surface list + Normal Surface list
Imgs = ( ceb, ana, flower, godson, jerax)
Imgs2 = ( ceb2, ana2, flower2, godson2, jerax2)

class Tower():
    
    def __init__(self, image):
        #Loading Images
        self.BlueTrue = False   #Key press states
        self.Placed = False
        self.x = 0
        self.y = 0
        self.image = image      #Defined so Surf from Imgs[] can be chosen
        self.BlueSurf = Imgs[image] 
        self.TowerSurf = pygame.Surface((0,0))
        self.TowerList = [ ]
        #self.surf = Imgs2[image]
        
    def ToggleBlue(self):
        '''
        Checks for keypress, then changes state
        :return: Bool
        '''
        if self.BlueTrue == False:
            self.BlueTrue = True
            print('Toggled: Blue == True')
        else: pass

    'Finding Source'
    #How can Toggle happen twice, without == False
    #BlueTrue = False cannot happen, or else TowerPlaced would clear BlueSurf
    #Could be related to instantiation, only then or ToggleBlue can BlueT change
    'Fixing Problem'
    #How does toggling twice, result in 2 BlueSurfs - could solve that
    #Simply don't allow toggle, if BlueTrue == True, make ToggleBlue break
       
    def Blueprint(self):            
        '''
        Fills Tower surface with blue colour if ToggleBlue() is called
        :return: Surf
        '''
        if self.BlueTrue == False:
            self.BlueSurf = pygame.Surface((0,0))       
            pass
        if self.BlueTrue == True:
            print('Should be blue!!!')
            self.BlueSurf = Imgs[self.image]
            self.BlueSurf.fill((0,128,255))
            
    def Build(self):
        '''
        Places Tower at current mouse pos and shows placed
        :return: x, y, bool
        '''
        if self.BlueTrue == True:               #Removes Blueprint
            self.BlueTrue = False
            print('Toggled: Blue == False')
            self.TowerSurf = Imgs2[self.image]
            self.x, self.y = pygame.mouse.get_pos()
            self.TowerList.append( ((self.TowerSurf),((self.x),(self.y))) )
            self.Placed = True
        else:
            print('No Blueprint: Press Q,W,E,R,T')
            pass
        
    def Cancel(self):
        '''
        Upon right click, sets blue surface to clear
        :return: Surf
        '''
        if self.BlueTrue == True:
            self.BlueSurf = pygame.Surface((0,0))
            #self.surf = pygame.Surface((0,0))

    def TowerPlaced(self):
        '''
        Checks if tower has been placed: if yes, provides tower surf;
        if no, provides clear surface
        :return: Surf
        '''
        if self.BlueTrue == False:
            self.BlueSurf = pygame.Surface((0,0))
            #self.surf = pygame.Surface((0,0))
        if self.Placed == True:
            pass
            #Not needed now, maybe for other feature
            #self.TowerSurf = Imgs2[self.image]




#Why is Tower.Surf = blue? When TowerSurf is filled,
#Why is BlueSurf + Surf filled?
#They were referring to same memory, made 2 lists,
#however needed to make 2 sets of images too

#Need to somehow save x, y cooirdnates of each tower placed
# then create surface for each tower placed
#Then have screen blit each type of tower surface.

            
         

        #So BlueTrue == True, but Build doesn't work
        
        
        
            
    
    
