from typing import Any
import pygame, os
import spritesheet

#font
pygame.font.init()

#screen
pygame.display.set_caption("Asteroid City")
width, height = 1000, 692
window = pygame.display.set_mode((width, height))
PLAYER_VEL = 5
FPS = 60

sprite_sheet_image = pygame.image.load(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\assets\spr_red_coupe_1.png").convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
meteor = pygame.image.load(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\assets\flaming_meteor.png")
meteor = pygame.transform.scale(meteor, (3 * 32, 3 * 32))


frame_0 = sprite_sheet.get_image(0, 96, 64, 3, (0,0,0))
frame_l1 = sprite_sheet.get_image(16, 96, 64, 3, (0,0,0))
frame_l2 = sprite_sheet.get_image(15, 96, 64, 3, (0,0,0))
frame_l3 = sprite_sheet.get_image(14, 96, 64, 3, (0,0,0))
frame_p1 = sprite_sheet.get_image(1, 96, 64, 3, (0,0,0))
frame_p2 = sprite_sheet.get_image(2, 96, 64, 3, (0,0,0))
frame_p3 = sprite_sheet.get_image(3, 96, 64, 3, (0,0,0))

"""frames_left = [frame_0, frame_l1, frame_l2, frame_l3]
frames_right = [frame_0, frame_p1, frame_p2, frame_p3]
frames = [frame_l3, frame_l2, frame_l1, frame_0, frame_p1, frame_p2, frame_p3]
"""
frame_l2_flipped = pygame.transform.flip(frame_l2, True, False).convert_alpha()
#background
def draw(window, bg_path, player):
    background_image = pygame.image.load(os.path.join(bg_path))
    window.blit(background_image, (0,0))
    player.draw(window)
    pygame.display.update()


class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    SPRITES = {"left": frame_l2, "right": frame_l2_flipped, "front": frame_0}
    ANIMATION_DELAY = 5

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.mask = None
        self.direction = "front"
        self.frame_count = 0

    def move(self, dx):
        self.rect.x += dx

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.move(self.x_vel)
        self.update_sprite()
    
    def draw(self, win):
        self.sprite = self.SPRITES[self.direction]
        win.blit(self.sprite, (self.rect.x, self.rect.y))
        window.blit(meteor, (400, 200))

    def update_sprite(self):
        if self.x_vel == 0:
            self.sprite = frame_0
        else:
            self.sprite = self.SPRITES[self.direction] 
        """if self.x_vel == 0:
            self.sprite = frame_0
        else:
            if self.direction == "right":
                if (self.frame_count + 1) > 6:
                    self.sprite = frames[5]
                else:
                    self.sprie = frames[self.frame_count + 1]
            else:
                if (self.frame_count - 1) < 0:
                    self.sprite = frames[0]
                else:
                    self.sprie = frames[self.frame_count - 1]"""
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)


def handle_move(player):
    keys = pygame.key.get_pressed()
    player.x_vel = 0

    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VEL)

def main(window):
    run = True
    clock = pygame.time.Clock()

    player = Player(410, 491, 288, 192)


    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False     
                break
        
        player.loop(FPS)
        handle_move(player)
        draw(window, r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\assets\background_min.jpg", player) 

    pygame.quit()
    quit()   

if __name__ == "__main__":
    main(window)
