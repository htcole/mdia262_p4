import pygame
#import random will be used to randomize platform generation
import random

#starts up the game
pygame.init()

#game window dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

#create window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Platform Hopper')

#limits the fps
clock = pygame.time.Clock()
FPS = 60

#game variables
SCROLL_THRESH = 200
GRAVITY = 1
MAX_PLATFORMS = 10
scroll = 0
bkgrnd_scroll = 0
game_over = False
score = 0

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#fonts
font_small = pygame.font.SysFont('Lucida Sans', 20)
font_big = pygame.font.SysFont('Lucida Sans', 24)

#images
player_img = pygame.image.load('assets/player.png').convert_alpha()
bkgrnd_img = pygame.image.load('assets/background.png').convert_alpha()
platform_img = pygame.image.load('assets/carrot.png').convert_alpha()

#function for showing text
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	window.blit(img, (x, y))


#function for showing background
def draw_bkgrnd(bkgrnd_scroll):
	window.blit(bkgrnd_img, (0, 0 + bkgrnd_scroll))
	#this line allows the background to loop as you get to the end of the SCREEN_HEIGHT
	window.blit(bkgrnd_img, (0, -600 + bkgrnd_scroll))

#player class
class Player():
	def __init__(self, x, y):
		#transforms the player image
		self.image = pygame.transform.scale(player_img, (45, 45))
#collision box size
		self.width = 25
		self.height = 40
#creates collision box
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = (x, y)
		#vertical velocity
		self.vel_y = 0
		#no flip necessary when starting the game
		self.flip = False

	def move(self):
		#resets variables to avoid going off screen
		scroll = 0
		dx = 0
		dy = 0

			#keybinds
		key = pygame.key.get_pressed()
		if key[pygame.K_a]:
					#the 10 adjusts the speed at which the player moves
			dx = -10
			self.flip = False
		if key[pygame.K_d]:
			dx = 10
			#flips the image of the rabbit when you move in the opposite direction
			self.flip = True

			#GRAVITY (how fast the player falls)
		self.vel_y += GRAVITY
		dy += self.vel_y

			#prevents player from going past the SCREEN_WIDTH
		if self.rect.left + dx < 0:
			dx = -self.rect.left
		if self.rect.right + dx > SCREEN_WIDTH:
			dx = SCREEN_WIDTH - self.rect.right

		#collision with platforms
		for platform in platform_group:
			#y axis collision			#collision with player
			if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
				#prevents player from hitting the bottom of the platform
				if self.rect.bottom < platform.rect.centery:
					if self.vel_y > 0:
						self.rect.bottom = platform.rect.top
						dy = 0
						self.vel_y = -20





		#collision with ground beta
		#if self.rect.bottom + dy > SCREEN_HEIGHT:
			#dy = 0
			#the number determines how high the player will bounce
			#self.vel_y = -20




			#checks if player passes SCROLL_THRESH
		if self.rect.top <= SCROLL_THRESH:
			#if player is jumping
			if self.vel_y < 0:
				scroll = -dy

				#update position of collison box
		self.rect.x += dx
		self.rect.y += dy + scroll

		return scroll

	def draw(self):		#shows the player flip when moved in opposite direction		#moves the player to fit in the collision box
		window.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 15, self.rect.y - 5))
#creates a collision box around the player
		#pygame.draw.rect(window, WHITE, self.rect, 2)

#class for the platforms (carrots)
class Platform(pygame.sprite.Sprite):
	def __init__(self, x, y, width):
		pygame.sprite.Sprite.__init__(self)
		#size of platforms
		self.image = pygame.transform.scale(platform_img, (width, 10))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def update(self, scroll):

		#updates platforms vertical position
		self.rect.y += scroll

		#delets platforms that have left the screen
		if self.rect.top > SCREEN_HEIGHT:
			self.kill()




				#player begining position
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

				#create sprite groups
platform_group = pygame.sprite.Group()


#starting platform
platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100)
platform_group.add(platform)



#creates platforms (beta)
#for p in range(MAX_PLATFORMS):
	#randomizes platforms
	#p_w = random.randint(40, 60)
	#p_x = random.randint(0, SCREEN_WIDTH - p_w)
	#space between platforms
	#p_y = p * random.randint(80, 120)
	#platform = Platform(p_x, p_y, p_w)
	#platform_group.add(platform)



#game loop
run = True
while run:

	clock.tick(FPS)

	if game_over == False:
		scroll = player.move()

		#testing if the scroll works, remove # to test
		#print(scroll)

		#shows the background
		bkgrnd_scroll += scroll
		if bkgrnd_scroll >= 600:
			bkgrnd_scroll = 0
		draw_bkgrnd(bkgrnd_scroll)


		#generate platforms
		if len(platform_group) < MAX_PLATFORMS:
			p_w = random.randint(40, 60)
			p_x = random.randint(0, SCREEN_WIDTH - p_w)
			p_y = platform.rect.y - random.randint(80, 120)
			platform = Platform(p_x, p_y, p_w)
			platform_group.add(platform)


	#used for testing amount of platforms shown on screen
		#print(len(platform_group))

	#draws temporary SCROLL_THRESH (here to understand where it will scroll, useless in game)
		#pygame.draw.line(window, WHITE, (0,SCROLL_THRESH), (SCREEN_WIDTH, SCROLL_THRESH))

		#update platforms
		platform_group.update(scroll)

		#shows player
		platform_group.draw(window)
		player.draw()

		#game_over
		if player.rect.top > SCREEN_HEIGHT:
			game_over = True
	else:
		draw_text ('GAME OVER!', font_big, BLACK, 130, 200)
		draw_text('PRESS SPACE TO PLAY AGAIN', font_big, BLACK, 40, 300)
		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE]:
			#resets game
			game_over = False
			score = 0
			scroll = 0
			#reposition player
			player.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
			#resets platforms
			platform_group.empty()
			platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100)
			platform_group.add(platform)



			#testing if game over works
		#print(game_over)

	#events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

			#update display window
	pygame.display.update()



pygame.quit()
