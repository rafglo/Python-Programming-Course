from typing import Any
import pygame, os
import spritesheet
import random


#font
pygame.font.init()

#screen
pygame.display.set_caption("Asteroid City")
width, height = 1000, 692
window = pygame.display.set_mode((width, height))
PLAYER_VEL = 5
FPS = 60

sprite_sheet_image = pygame.image.load(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\assets\spr_red_coupe_0 (1).png").convert_alpha()


meteor_img = pygame.image.load(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\assets\flaming_meteor.png").convert_alpha()
meteor_sur = pygame.Surface((32,32), pygame.SRCALPHA, 32)
meteor_sur.blit(meteor_img, (0,0))
meteor_image = pygame.transform.scale(meteor_sur, (32*3, 32*3))


img_0 = pygame.Surface((50,34)).convert_alpha()
img_0.blit(sprite_sheet_image, (0,0), (8, 30, 50, 34))
frame_0 = pygame.transform.scale(img_0, (3*50, 3*34))
frame_0.set_colorkey((0,0,0))

img_p1 = pygame.Surface((49,34)).convert_alpha()
img_p1.blit(sprite_sheet_image, (0,0), (103, 30, 49, 34))
frame_p1 = pygame.transform.scale(img_p1, (3*49, 3*34))
frame_p1.set_colorkey((0,0,0))

img_p2 = pygame.Surface((50,34)).convert_alpha()
img_p2.blit(sprite_sheet_image, (0,0), (199, 30, 50, 34))
frame_p2 = pygame.transform.scale(img_p2, (3*50, 3*34))
frame_p2.set_colorkey((0,0,0))

img_p3 = pygame.Surface((54,34)).convert_alpha()
img_p3.blit(sprite_sheet_image, (0,0), (294, 30, 54, 34))
frame_p3 = pygame.transform.scale(img_p3, (3*54, 3*34))
frame_p3.set_colorkey((0,0,0))

img_l1 = pygame.Surface((49,34)).convert_alpha()
img_l1.blit(sprite_sheet_image, (0,0), (422, 158, 49, 34))
frame_l1 = pygame.transform.scale(img_l1, (3*49, 3*34))
frame_l1.set_colorkey((0,0,0))

img_l2 = pygame.Surface((50,34)).convert_alpha()
img_l2.blit(sprite_sheet_image, (0,0), (325, 158, 50, 34))
frame_l2 = pygame.transform.scale(img_l2, (3*50, 3*34))
frame_l2.set_colorkey((0,0,0))

img_l3 = pygame.Surface((54,34)).convert_alpha()
img_l3.blit(sprite_sheet_image, (0,0), (226, 158, 54, 34))
frame_l3 = pygame.transform.scale(img_l3, (3*54, 3*34))
frame_l3.set_colorkey((0,0,0))

frames_left = [frame_0, frame_l1, frame_l2, frame_l3]
frames_right = [frame_0, frame_p1, frame_p2, frame_p3]
frames_left_to_right = [frame_l3, frame_l2, frame_l1, frame_0, frame_p1, frame_p2, frame_p3]
frames_right_to_left = [frame_p3, frame_p2, frame_p1, frame_0, frame_l1, frame_l2, frame_l3]

#background
def draw(window, bg_path, player, meteors, lives, level, lost=False):

    background_image = pygame.image.load(os.path.join(bg_path))
    window.blit(background_image, (0,0))
    player.draw(window)
    for meteor in meteors:
        meteor.draw(window)
    draw_text(window, "LIVES: " + str(lives), 150, 50, 30)
    draw_text(window, "LEVEL: " + str(level), 850, 50, 30)
    if lost:
        draw_text(window, "GAME OVER", width/2, height/2, 50)
    
    pygame.display.update()


class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    SPRITES = {"front": frame_0}
    ANIMATION_DELAY = 10

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.mask = None
        self.direction = "front"
        self.previous_direction = "front"
        self.animation_count = 0

    def move(self, dx):
        if 0 < self.rect.x + dx < width - 54*3:
            self.rect.x += dx

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.previous_direction = self.direction
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.previous_direction = self.direction
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.move(self.x_vel)
        self.update_sprite()
    
    def draw(self, win):
        win.blit(self.sprite, (self.rect.x, self.rect.y))

    def update_sprite(self):
        self.sprite = frame_0
        if self.x_vel != 0:
            frame_index = 0

            if self.previous_direction == "front" and self.direction == "left":
                frame_index = (self.animation_count // self.ANIMATION_DELAY) % len(frames_left)
                if frame_index == 3:
                    self.sprite = frame_l3
                else:
                    self.sprite = frames_left[frame_index]
                    self.animation_count += 1


            if self.previous_direction == "front" and self.direction == "right":
                frame_index = (self.animation_count // self.ANIMATION_DELAY) % len(frames_right)
                if frame_index == 3:
                    self.sprite = frame_p3
                else:
                    self.sprite = frames_right[frame_index]
                    self.animation_count += 1
                


            if self.previous_direction == "right" and self.direction == "left":

                frame_index = (self.animation_count // self.ANIMATION_DELAY) % len(frames_right_to_left)
                if frame_index == 3:
                    self.sprite = frame_l3
                else:
                    self.sprite = frames_left[frame_index]
                    self.animation_count += 1


            elif self.previous_direction == "left" and self.direction == "right":

                frame_index = (self.animation_count // self.ANIMATION_DELAY) % len(frames_left_to_right)
                if frame_index == 3:
                    self.sprite = frame_p3
                else:
                    self.sprite = frames_right[frame_index]
                    self.animation_count += 1

        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

class Meteor(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.blit(meteor_image, (0,0))
        self.width = width
        self.height = height
        self.y_vel = 0
        self.mask = pygame.mask.from_surface(self.image)

    def fall(self, dy):
        self.rect.y += dy

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

def handle_move(player):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VEL)

def collision_detection(player, meteor):
    if pygame.sprite.collide_mask(player, meteor) != None:
        return True

def throw_meteor(meteor, vel):
    meteor.fall(vel)
    meteor.update()

def lose(loss):
    loss = True

def draw_text(window, text, x, y, size):
    font = pygame.font.Font(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\PressStart2P-vaV7.ttf", size)
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    window.blit(text_surface, text_rect)
    pygame.display.update()

def main(window):
    run = True
    level = 1
    lives = 3
    METEOR_VEL = 5
    wave = 0
    meteors = []
    loss = False
    loss_count = 0

    clock = pygame.time.Clock()

    player = Player(427, 600, 162, 102)
    
    if len(meteors) == 0:
        level += 1
        wave += 5
        for i in range(wave):
            meteors.append(Meteor(random.randrange(0, 1000 - 32*3), random.randrange(-1500, -100), 32*3, 32*3))

    while run:
        clock.tick(FPS)
        player.loop(FPS)
        handle_move(player) 
        
        if lives == 0:
            loss = True
            loss_count += 1

        draw(window, r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\assets\background_min.jpg", player, meteors, lives, level, loss)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False     
                break

        if loss:
            if loss_count > FPS * 5:
                run = False
            else:
                continue

        for meteor in meteors:
            throw_meteor(meteor, METEOR_VEL)
            if collision_detection(player, meteor):
                    lives -= 1
            if meteor.rect.y > width:
                meteors.remove(meteor)

    pygame.quit()
    quit()   

if __name__ == "__main__":
    main(window)

