import pygame, os
import spritesheet

pygame.font.init()
width, height = 1000, 692
screen = pygame.display.set_mode((width, height))
background = pygame.image.load(os.path.join(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\background_min.jpg"))
sprite_sheet_image = pygame.image.load(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\spr_red_coupe_1.png").convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
meteor = pygame.image.load(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\flaming_meteor.png")
meteor = pygame.transform.scale(meteor, (3 * 32, 3 * 32))

frame_0 = sprite_sheet.get_image(0, 96, 64, 3, (0,0,0))
frame_l1 = sprite_sheet.get_image(16, 96, 64, 3, (0,0,0))
frame_l2 = sprite_sheet.get_image(15, 96, 64, 3, (0,0,0))
frame_l3 = sprite_sheet.get_image(14, 96, 64, 3, (0,0,0))
frame_l4 = sprite_sheet.get_image(13, 96, 64, 3, (0,0,0))
frame_p1 = sprite_sheet.get_image(1, 96, 64, 3, (0,0,0))
frame_p2 = sprite_sheet.get_image(2, 96, 64, 3, (0,0,0))
frame_p3 = sprite_sheet.get_image(3, 96, 64, 3, (0,0,0))
frame_p4 = sprite_sheet.get_image(4, 96, 64, 3, (0,0,0))

class Car():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.car_img = frame_0

    def draw(self, window):
        window.blit(self.car_img, (self.x, self.y))
        
            

def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    labels_font = pygame.font.SysFont("comicsans", 50)
    car_velocity = 5
    clock = pygame.time.Clock()

    car = Car(410,491)

    def redraw_window():
        level_label = labels_font.render(f"Level: {level}", 1, (0,0,0))
        lives_label = labels_font.render(f"Lives: {lives}", 1, (0,0,0))
        screen.blit(background, (0,0))
        screen.blit(meteor, (100,100))
        screen.blit(level_label, (15,10))
        screen.blit(lives_label, (width - lives_label.get_width() - 15, 10))
        car.draw(screen)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and car.x - car_velocity > 0:
            car.x -= car_velocity
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and car.x + car_velocity + 50 < width:
            car.x += car_velocity
main()
