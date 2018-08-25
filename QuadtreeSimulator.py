import pygame
import sys
import random
from ParticleClass import *
from Quadtree import *

WHITE = (255, 255, 255)
WIDTH = 600
HEIGHT = 600
TILESIZE = 32
LIGHTGREY = (205, 205, 205)

#This is the Game class
#Where the magic begins
class Game:
    def __init__(self):
        #Constuctor for the game object
        pygame.init() #Initilize pygame
        
        #Set the screen to a window size from settings
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
        
        #Set window caption from title in settings
        pygame.display.set_caption("quadtree")
        
        #create the clock
        self.clock = pygame.time.Clock()
        
        #Cal load_data function
        self.load_data()
        
    #load_data is where we define what map is opened
    def load_data(self):
        pass
        
    
    #When new instance
    def new(self):
        #create sprite groups------------------------------------------------
        self.active_sprite_list = pygame.sprite.Group()
        self.particle_list = pygame.sprite.Group()
        
        for i in range(200):
            self.particle = Particle(self, random.randint(0, WIDTH), random.randint(0, HEIGHT))
            
        self.mouseRect = mouseRect(self)       
        
     
    #Game loop. Set self.playing to False to end the game
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(60) / 1000 #Current delta time
            self.events() #Call events
            self.update() #Call updates
            self.draw() #Draw screen
    
    #When game is quit
    def quit(self):
        pygame.quit()
        sys.exit()
        
    #Define what needs to be updated each frame    
    def update(self):
        self.tree = Quadtree(0, pygame.Rect(0,0,WIDTH,HEIGHT), self.particle_list)
        
        #Update all active sprites
        self.active_sprite_list.update()
        
        
       
    #Draw the grid - not for final project.
    #TODO: create toggle in UI for testing enabled
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
    
    #Define how the game is going to draw
    def draw(self):
        #Fill the screen with a background color set in settings
        self.screen.fill(WHITE)
        
        self.tree.update(self.screen)
        
        #if True:
        #    self.draw_grid()
        
        #Draw the rectangle around the mouse to the screen
        self.mouseRect.update()
        pygame.draw.rect(self.screen, (0, 128, 0), self.mouseRect, 2)
        
            
        for sprite in self.active_sprite_list:
            #Draw that sprite to sceen at the location set by the camera 
            self.screen.blit(sprite.image, (sprite.x, sprite.y))
        
        for sprite in self.mouseRect.inRect:
            pygame.draw.rect(self.screen, GREEN, sprite.rect, 3)

               
        #Flip to next frame
        pygame.display.flip()
    
    #Main event listener
    def events(self):
        #For each event returned from pygame.event.get
        for event in pygame.event.get():
            #If the event is a QUIT command
            if event.type == pygame.QUIT:
                #Quit the game
                self.quit()
                
            #If the event is the player pressing a button
            elif event.type == pygame.KEYDOWN:
                #And if that button is Escape
                if event.key == pygame.K_ESCAPE:
                    self.quit() #Quit the game 
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                #when mouse is released, set movePoint to it's most recent location
                x, y = pygame.mouse.get_pos()
                
            if pygame.mouse.get_pressed()[0]:
                #Move to mouse as long as it's pressed.
                x, y = pygame.mouse.get_pos()
                
        
#Create the main game object            
g = Game()

while True:
    g.new() #Create the new instance
    g.run() #Run the main game loop

            

