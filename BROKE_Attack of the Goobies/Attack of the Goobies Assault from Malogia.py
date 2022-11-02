"""
Attack of the Goobies: Assault from Malogia

Artwork and some SFX used is all free use content except the goobies and the
death sounds featured in this game, which were created by DECA Games for their bullet hell MMO
'Realm of the Mad God'

The super secret is a reference to the popular YouTuber and Twitch streamer,
"Jerma985" and references this famous moment in his Silly Putty Car Circus!
video: https://youtu.be/f7cyaC8Q1f8?t=306

"""
import time
import sys
import os
import random
import math
import arcade
from PIL import ImageFont

SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_enemy = 0.5
SPRITE_SCALING_LASER = 0.8
SPRITE_SCALING_boss = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Attack of the Goobies: Assault from Malogia"

BULLET_SPEED = 5
ENEMY_SPEED = 2
BOSS_SPEED = 2
MAX_PLAYER_BULLETS = 3

# This margin controls how close the enemy gets to the left or right side
# before reversing direction.
BOSS_HORIZONTAL_MARGIN = 15
BOSS_VERTICAL_MARGIN = 15
ENEMY_VERTICAL_MARGIN = 15
RIGHT_ENEMY_BORDER = SCREEN_WIDTH - ENEMY_VERTICAL_MARGIN
RIGHT_BOSS_BORDER = SCREEN_WIDTH - BOSS_VERTICAL_MARGIN
LEFT_ENEMY_BORDER = ENEMY_VERTICAL_MARGIN
LEFT_BOSS_BORDER = BOSS_VERTICAL_MARGIN
BOTTOM_BOSS_BORDER = BOSS_HORIZONTAL_MARGIN 
# How many pixels to move the enemy down when reversing
ENEMY_MOVE_DOWN_AMOUNT = 30
BOSS_MOVE_DOWN_AMOUNT = 0.5
# Game state
GAME_OVER = 1
PLAY_GAME = 0

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_list = None
        self.boss_list = []
        self.enemy_list = []
        self.player_bullet_list = None
        self.enemy_bullet_list = None
        self.shield_list = None

        self.background = None

        # Textures for the enemies
        self.enemy_textures = None
        self.boss_textures = None
        
        #Sounds

        self.PLAYER_LASER_SOUND= "player_laser.mp3"
        self.PLAYER_LASER_SOUND= arcade.load_sound(self.PLAYER_LASER_SOUND)
        self.PLAYER_DEATH_SOUND= "player_death.wav"
        self.PLAYER_DEATH_SOUND= arcade.load_sound(self.PLAYER_DEATH_SOUND)

        self.ENEMY_DEATH_SOUND= "gooby_death.mp3"
        self.ENEMY_DEATH_SOUND= arcade.load_sound(self.ENEMY_DEATH_SOUND)
        self.BOSS_DEATH_SOUND= "boss_death.mp3"
        self.BOSS_DEATH_SOUND= arcade.load_sound(self.BOSS_DEATH_SOUND)

        self.BACKGROUND_MUSIC= "background_music.mp3"
        self.BACKGROUND_MUSIC= arcade.load_sound(self.BACKGROUND_MUSIC)

        self.SECRET_MUSIC= "giant_enemy_spider.mp3"
        self.SECRET_MUSIC= arcade.load_sound(self.SECRET_MUSIC)
        self.EASY_SOUND= "easy.wav"
        self.EASY_SOUND= arcade.load_sound(self.EASY_SOUND)

        def stop_sound(self):
            self.BACKGROUND_MUSIC.stop
        self.stop_sound= self.BACKGROUND_MUSIC.stop

        def stop_sound2(self):
            self.SECRET_MUSIC.stop
        self.stop_sound2= self.SECRET_MUSIC.stop

        # State of the game
        self.game_state = PLAY_GAME

        #Boss sprite
        self.boss_sprite = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Enemy movement
        self.enemy_change_x = -ENEMY_SPEED
        self.boss_change_x = -BOSS_SPEED
        self.boss_change_y = -BOSS_SPEED
        
        # Don't show the mouse cursor
        self.set_mouse_visible(False)

    def setup_level_one(self):
        # Load the textures for the enemies, one facing left, one right
            self.boss_textures = []
            texture = arcade.load_texture("spider.png")
            self.boss_textures.append(texture)
            boss = arcade.Sprite()
            boss.center_x = 400
            boss.center_y = 900
            boss.scale = SPRITE_SCALING_boss
            boss.texture = self.boss_textures[0]
            self.boss_list.append(boss)

            self.enemy_textures = []
            texture = arcade.load_texture("shred.png")
            self.enemy_textures.append(texture)
            texture = arcade.load_texture("shred.png", mirrored=True)
            self.enemy_textures.append(texture)

            # Create rows and columns of enemies
            x_count = 7
            x_start = 380
            x_spacing = 60
            y_count = 5
            y_start = 420
            y_spacing = 40
            for x in range(x_start, x_spacing * x_count + x_start, x_spacing):
                for y in range(y_start, y_spacing * y_count + y_start, y_spacing):

                    # Create the enemy instance
                    enemy = arcade.Sprite()
                    enemy.scale = SPRITE_SCALING_enemy
                    enemy.texture = self.enemy_textures[1]

                    # Position the enemy
                    enemy.center_x = x
                    enemy.center_y = y

                    # Add the enemy to the lists
                    self.enemy_list.append(enemy)
                    

    def make_shield(self, x_start):
        """
        Make a shield, which is just a 2D grid of solid color sprites
        stuck together with no margin so you can't tell them apart.
        """
        shield_block_width = 5
        shield_block_height = 10
        shield_width_count = 20
        shield_height_count = 5
        y_start = 150
        for x in range(x_start, x_start + shield_width_count * shield_block_width, shield_block_width):
            for y in range(y_start, y_start + shield_height_count * shield_block_height, shield_block_height):
                shield_sprite = arcade.SpriteSolidColor(shield_block_width, shield_block_height, arcade.color.RED)
                shield_sprite.center_x = x
                shield_sprite.center_y = y
                self.shield_list.append(shield_sprite)

        """
        Set up the game and initialize the variables.
        """
    def setup(self):
        self.boss_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.player_bullet_list = arcade.SpriteList()
        self.shield_list = arcade.SpriteList(is_static=True)

        #Background image
        self.background = arcade.load_texture("space.jpg")

        # Image for player sprite
        self.player_sprite = arcade.Sprite("spaceship.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 40
        self.player_list.append(self.player_sprite)

        # Make each of the shields
        for x in range(75, 800, 190):
            self.make_shield(x)

        #Background music
        arcade.play_sound(self.BACKGROUND_MUSIC)

        self.setup_level_one()    

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()
        self.shield_list = arcade.SpriteList(is_static=True)

        # Set up the player
        self.score = 0

        #Background image
        self.background = arcade.load_texture("space.jpg")

        # Image for player sprite
        self.player_sprite = arcade.Sprite("spaceship.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 40
        self.player_list.append(self.player_sprite)

        # Make each of the shields
        for x in range(75, 800, 190):
            self.make_shield(x)

        self.setup_level_one()

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        arcade.start_render()

        #Draw background image
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # Draw all the sprites.
        self.enemy_list.draw()
        self.player_bullet_list.draw()
        self.enemy_bullet_list.draw()
        self.shield_list.draw()
        self.player_list.draw()
        self.player_bullet_list.draw()
        self.shield_list.draw()
        self.player_list.draw()
        self.boss_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 570, arcade.color.WHITE, font_name="space", font_size=14)

        # Draw game over if the game state is such
        if self.game_state == GAME_OVER:
            self.stop_sound()
            arcade.draw_text(f"GAME OVER", 250, 300, arcade.color.WHITE, font_name="space", font_size=55)
            self.set_mouse_visible(True)

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """

        # Don't move the player if the game is over
        if self.game_state == GAME_OVER:
            return

        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """

        # Only allow the user so many bullets on screen at a time to prevent
        # them from spamming bullets.
        if len(self.player_bullet_list) < MAX_PLAYER_BULLETS:

            #Create a bullet
            bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)

            #Create sound
            arcade.play_sound(self.PLAYER_LASER_SOUND)

            # The image points to the right, and we want it to point up. So
            # rotate it.
            bullet.angle = 90

            # Give the bullet a speed
            bullet.change_y = BULLET_SPEED

            # Position the bullet
            bullet.center_x = self.player_sprite.center_x
            bullet.bottom = self.player_sprite.top

            # Add the bullet to the appropriate lists
            self.player_bullet_list.append(bullet)
    
    def update_boss(self):
        move_down = False
        for boss in self.boss_list:
            boss.center_x += self.boss_change_x
        for boss in self.boss_list:
            if boss.center_y > BOTTOM_BOSS_BORDER:
                move_down = True
            if boss.right > RIGHT_BOSS_BORDER and self.boss_change_x > 0:
                self.boss_change_x *= -1
                move_down = True
            if boss.left < LEFT_BOSS_BORDER and self.boss_change_x < 0:
                self.boss_change_x *= -1
                move_down = True
                
        if move_down:
            for boss in self.boss_list:
                boss.center_y -= BOSS_MOVE_DOWN_AMOUNT
                
    def on_key_press(self, key, modifiers):
        if key == arcade.key.S:
            self.BACKGROUND_MUSIC = False
            self.stop_sound()
            arcade.play_sound(self.SECRET_MUSIC)
            for i in range(6):
                for enemy in self.enemy_list:
                    enemy.remove_from_sprite_lists()
            self.update_boss()

        if key == arcade.key.SPACE:
            self.setup_level_one()

        if key == arcade.key.M:
            self.stop_sound()

    
        

    def update_enemies(self):
        # Move the enemy vertically
        for enemy in self.enemy_list:
            enemy.center_x += self.enemy_change_x

        # Check every enemy to see if any hit the edge. If so, reverse the
        # direction and flag to move down.
        move_down = False
        for enemy in self.enemy_list:
            if enemy.right > RIGHT_ENEMY_BORDER and self.enemy_change_x > 0:
                self.enemy_change_x *= -1
                move_down = True
            if enemy.left < LEFT_ENEMY_BORDER and self.enemy_change_x < 0:
                self.enemy_change_x *= -1
                move_down = True

        # Did we hit the edge above, and need to move the enemy down?
        if move_down:
            # Yes
            for enemy in self.enemy_list:
                # Move enemy down
                enemy.center_y -= ENEMY_MOVE_DOWN_AMOUNT
                # Flip texture on enemy so it faces the other way
                if self.enemy_change_x > 0:
                    enemy.texture = self.enemy_textures[0]
                else:
                    enemy.texture = self.enemy_textures[1]

    def allow_enemies_to_fire(self):
        """
        See if any enemies will fire this frame.
        """
        # Track which x values have had a chance to fire a bullet.
        # Since enemy list is build from the bottom up, we can use
        # this to only allow the bottom row to fire.
        if self.game_state == PLAY_GAME:
            x_spawn = []
            for enemy in self.enemy_list:
                # Adjust the chance depending on the number of enemies. Fewer
                # enemies, more likely to fire.
                chance = 4 + len(self.enemy_list) * 4

                # Fire if we roll a zero, and no one else in this column has had
                # a chance to fire.
                if random.randrange(chance) == 0 and enemy.center_x not in x_spawn:
                    # Create a bullet
                    bullet = arcade.Sprite(":resources:images/space_shooter/laserRed01.png", SPRITE_SCALING_LASER)

                    # Angle down.
                    bullet.angle = 180

                    # Give the bullet a speed
                    bullet.change_y = -BULLET_SPEED

                    # Position the bullet so its top id right below the enemy
                    bullet.center_x = enemy.center_x
                    bullet.top = enemy.bottom

                    # Add the bullet to the appropriate list
                    self.enemy_bullet_list.append(bullet)

                # Ok, this column has had a chance to fire. Add to list so we don't
                # try it again this frame.
                x_spawn.append(enemy.center_x)

    def process_enemy_bullets(self):

        if self.game_state == PLAY_GAME:
            # Move the bullets
            self.enemy_bullet_list.update()

            # Loop through each bullet
            for bullet in self.enemy_bullet_list:
                # Check this bullet to see if it hit a shield
                hit_list = arcade.check_for_collision_with_list(bullet, self.shield_list)

                # If it did, get rid of the bullet and shield blocks
                if len(hit_list) > 0:
                    bullet.remove_from_sprite_lists()
                    for shield in hit_list:
                        shield.remove_from_sprite_lists()
                        continue

                # See if the player got hit with a bullet
                if arcade.check_for_collision_with_list(self.player_sprite, self.enemy_bullet_list):
                    arcade.play_sound(self.PLAYER_DEATH_SOUND)
                    self.game_state = GAME_OVER

                # If the bullet falls off the screen get rid of it
                if bullet.top < 0:
                    bullet.remove_from_sprite_lists()

    def process_player_bullets(self):

        # Move the bullets
        self.player_bullet_list.update()

        # Loop through each bullet
        for bullet in self.player_bullet_list:

            # Check this bullet to see if it hit a shield
            hit_list = arcade.check_for_collision_with_list(bullet, self.shield_list)
            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                for shield in hit_list:
                    shield.remove_from_sprite_lists()
                continue

            # Check this bullet to see if it hit a enemy
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                
            # For every enemy we hit, add to the score and remove the enemy
            for enemy in hit_list:
                enemy.remove_from_sprite_lists()
                arcade.play_sound(self.ENEMY_DEATH_SOUND)
                self.score += 1
            #Check this bullet to see if it hit the boss
            hit_list = arcade.check_for_collision_with_list(bullet, self.boss_list)    

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                
            for boss in hit_list:
                boss.remove_from_sprite_lists()
                self.stop_sound2()
                arcade.play_sound(self.BOSS_DEATH_SOUND)
                self.score += 1
                arcade.play_sound(self.EASY_SOUND)
                
            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

    def on_update(self, delta_time):
        """ Movement and game logic """

        if self.game_state == GAME_OVER:
            return
    
        self.update_enemies()
        self.allow_enemies_to_fire()
        self.process_enemy_bullets()
        self.process_player_bullets()   

        if self.BACKGROUND_MUSIC == False:
            self.update_boss()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
