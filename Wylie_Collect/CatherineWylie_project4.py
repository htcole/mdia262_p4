#Catherine Wylie
#JRL 262
#Nov. 13, 2020
#PYGAME

#imports
import pygame
import random

#initialize Pygame
pygame.init()

#sets up window
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Collect the planets!")

pygame.mixer.music.load("space.mp3")
pygame.mixer.music.play(loops = 1, start = 0.0, fade_ms = 1)
background_image = pygame.image.load("sky.jpg").convert()

#colors
black = (0,0,0)
white = (255,255,255)

#creates Sprites
class Play(pygame.sprite.Sprite):
    
    def __init__(self, filename):
        super().__init__() 
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()

planet_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

#displays a certain amount of planets
for i in range(10):
    
    #represents a planet object
    planet = Play("planet.png")
 
    #sets a random location for the planet object
    planet.rect.x = random.randrange(screen_width)
    planet.rect.y = random.randrange(screen_height)
     
    #add the planets to the list of objects
    planet_list.add(planet)
    all_sprites_list.add(planet)
     
#creates the player 
player = Play("ufo.png")
all_sprites_list.add(player)

done = False

font = pygame.font.Font(None, 20)

score = 0
level = 1
 
#-------- MAIN-----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
  
    #gets the current mouse position
    pos = pygame.mouse.get_pos()
       
    #sets the player to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]
     
    #sees if the player block has collided with anything
    collect = pygame.sprite.spritecollide(player, planet_list, True)

    for planets in collect:
        score += 1

    if len(planet_list) == 0:
        level += 1
        
        #adds more planets depending on the level
        for i in range(level * 10):
            planet = Play("planet.png")
            planet.rect.x = random.randrange(screen_width)
            planet.rect.y = random.randrange(screen_height)
    
            planet_list.add(planet)
            all_sprites_list.add(planet)

    screen.blit(background_image, [0,0])
          
    #draws all the spites
    all_sprites_list.draw(screen)

    text = font.render("Score: " + str(score), True, white)
    screen.blit(text, [10,10])

    text = font.render("Level: " + str(level), True, white)
    screen.blit(text, [10,40])
 
    pygame.display.flip()
 
pygame.quit()
