from typing import Any
import pygame, os
import spritesheet
import random
import pygame_textinput
import json
import pickle
from PIL import Image

pygame.init()
#font
def make_font(size, path):
    """
    Function
    Funkcja inicjalizująca font o danym rozmiarze

    Input
    size(int) - rozmiar fontu
    path(str) - scieżka do pliku z fontem

    Output
    font(Font) - font do użycia

    """
    pygame.font.init()
    font = pygame.font.Font(path, size)
    return font

#okno
pygame.display.set_caption("Asteroid City")

#parametry okna
width, height = 1000, 692
window_size = (1000, 692)
window = pygame.display.set_mode((width, height))

#parametry gry
PLAYER_VEL = 7
FPS = 60

#powierzchnia do screenshake'a
display = pygame.Surface((1000, 692))

#tło
background_image = pygame.image.load(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\assets\background_min.jpg")

#grafika pojazdu
sprite_sheet_image = pygame.image.load(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\assets\spr_red_coupe_0 (1).png").convert_alpha()

#rules file
rules_file = open(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\rules.txt", encoding="utf-8")
rules = rules_file.read().splitlines()

#dźwięki
meteor_sound = pygame.mixer.Sound(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\assets\hq-explosion-6288.mp3")
level_up_sound = pygame.mixer.Sound(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\assets\dzwiek_level.mp3")
game_over_sound = pygame.mixer.Sound(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\assets\game-over-38511.mp3")
main_song = pygame.mixer.Sound(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\assets\neon-gaming-128925.mp3")
car_sound = pygame.mixer.Sound(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\assets\silnik.mp3")
sounds = [meteor_sound, level_up_sound, game_over_sound, main_song, car_sound]

#plik z highscorami
highscore_path = r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\highscore.pkl"

def top_scores(highscore_path):
    """
    Function 
    Funkcja wyciągająca z pliku najlepsze wyniki

    Input
    highscore_path(str) - ścieżka do pliku z wynikami

    Output
    top_5_scores(list) - lista najlepszych pięciu wynikow
    False(bool) - jeśli żaden wynik nie jest zapisany

    """
    if os.path.getsize(highscore_path) > 0:
        with open(highscore_path, "rb") as f:
            highscore_list = pickle.load(f)
        scores_list = [str(record["score"]) + "," + record["name"] for record in highscore_list]
        scores_list.sort(reverse = True)
        if len(scores_list) >= 5:
            new_scores = scores_list[:5]
        else:
            new_scores = scores_list[:len(scores_list)]
        top_5_scores = []
        for score in new_scores:
            record = {"name": "", "score": ""}
            splitted = score.split(",")
            for i in range(2):
                record["name"] = splitted[1]
                record["score"] = splitted[0]
            top_5_scores.append(record)
        return top_5_scores
    else:
        return False
    
#plik z opisem autora
author_file = open(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\author.txt", encoding="utf-8").read()

#github qr code
qr = pygame.image.load(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\assets\github_qr.png")
qr = pygame.transform.scale(qr, (220, 220))

#grafika meteora
meteor_img = pygame.image.load(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\assets\flaming_meteor.png").convert_alpha()
meteor_sur = pygame.Surface((32,32), pygame.SRCALPHA, 32)
meteor_sur.blit(meteor_img, (0,0))
meteor_image = pygame.transform.scale(meteor_sur, (32*3, 32*3))

#wycinanie grafik do animacji pojazu
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

#obracanie grafik z prawej strony na lewą
frame_l1 = pygame.transform.flip(frame_p1, flip_x = True, flip_y=False)
frame_l1.set_colorkey((0,0,0))

frame_l2 = pygame.transform.flip(frame_p2, flip_x = True, flip_y=False)
frame_l2.set_colorkey((0,0,0))

frame_l3 = pygame.transform.flip(frame_p3, flip_x = True, flip_y=False)
frame_l3.set_colorkey((0,0,0))

#prawe grafiki do animacji wypadku
img_p4 = pygame.Surface((73,30)).convert_alpha()
img_0.blit(sprite_sheet_image, (0,0), (386, 32, 73, 30))
frame_p4 = pygame.transform.scale(img_p4, (3*73, 3*30))
frame_p4.set_colorkey((0,0,0))

img_p5 = pygame.Surface((66, 26)).convert_alpha()
img_p5.blit(sprite_sheet_image, (0,0), (490, 35, 66, 26))
frame_p5 = pygame.transform.scale(img_p5, (3*66, 3*26))
frame_p5.set_colorkey((0,0,0))

img_p6 = pygame.Surface((77, 33)).convert_alpha()
img_p6.blit(sprite_sheet_image, (0,0), (1, 92, 77, 33))
frame_p6 = pygame.transform.scale(img_p6, (3*77, 3*33))
frame_p6.set_colorkey((0,0,0))

img_p7 = pygame.Surface((77, 37)).convert_alpha()
img_p7.blit(sprite_sheet_image, (0,0), (97, 88, 77, 37))
frame_p7 = pygame.transform.scale(img_p7, (3*77, 3*37))
frame_p7.set_colorkey((0,0,0))

img_p8 = pygame.Surface((77, 33)).convert_alpha()
img_p8.blit(sprite_sheet_image, (0,0), (193, 67, 77, 33))
frame_p8 = pygame.transform.scale(img_p8, (3*77, 3*33))
frame_p8.set_colorkey((0,0,0))

img_p9 = pygame.Surface((77, 37)).convert_alpha()
img_p9.blit(sprite_sheet_image, (0,0), (289, 67, 77, 37))
frame_p9 = pygame.transform.scale(img_p9, (3*77, 3*37))
frame_p9.set_colorkey((0,0,0))

img_p10 = pygame.Surface((77, 33)).convert_alpha()
img_p10.blit(sprite_sheet_image, (0,0), (385, 88, 77, 33))
frame_p10 = pygame.transform.scale(img_p10, (3*77, 3*33))
frame_p10.set_colorkey((0,0,0))

img_p11 = pygame.Surface((66, 26)).convert_alpha()
img_p11.blit(sprite_sheet_image, (0,0), (490, 100, 66, 26))
frame_p11 = pygame.transform.scale(img_p11, (3*66, 3*26))
frame_p11.set_colorkey((0,0,0))

#lewe grafiki do animacji wypadku
frame_l4 = pygame.transform.flip(frame_p4, flip_x = True, flip_y=False)
frame_l4.set_colorkey((0,0,0))

frame_l5 = pygame.transform.flip(frame_p5, flip_x = True, flip_y=False)
frame_l5.set_colorkey((0,0,0))

frame_l6 = pygame.transform.flip(frame_p6, flip_x = True, flip_y=False)
frame_l6.set_colorkey((0,0,0))

frame_l7 = pygame.transform.flip(frame_p7, flip_x = True, flip_y=False)
frame_l7.set_colorkey((0,0,0))

frame_l8 = pygame.transform.flip(frame_p8, flip_x = True, flip_y=False)
frame_l8.set_colorkey((0,0,0))

frame_l9 = pygame.transform.flip(frame_p9, flip_x = True, flip_y=False)
frame_l9.set_colorkey((0,0,0))

frame_l10 = pygame.transform.flip(frame_p10, flip_x = True, flip_y=False)
frame_l10.set_colorkey((0,0,0))

frame_l11 = pygame.transform.flip(frame_p11, flip_x = True, flip_y=False)
frame_l11.set_colorkey((0,0,0))

#listy z grafikami do animacji
frames_left = [frame_0, frame_l1, frame_l2, frame_l3]
frames_right = [frame_0, frame_p1, frame_p2, frame_p3]
frames_left_to_right = [frame_l3, frame_l2, frame_l1, frame_0, frame_p1, frame_p2, frame_p3]
frames_right_to_left = [frame_p3, frame_p2, frame_p1, frame_0, frame_l1, frame_l2, frame_l3]
frames_right_crash = [frame_l4, frame_l5, frame_l6, frame_l7, frame_l8, frame_l9, frame_l10, frame_l11]
frames_left_crash = [frame_p4, frame_p5, frame_p6, frame_p7, frame_p8, frame_p9, frame_p10, frame_p11]
frames_front_crash = [frame_0, frame_p6, frame_p7, frame_p8, frame_p9, frame_p10, frame_p11]


def draw(window, background_image, player, meteors, lives, level, lost=False, level_up=False):
    """
    Function 
    Funkcja wyświetlająca na ekranie elementy gry

    Input
    window(Surface) - powierzchnia, na której będziemy wyświetlać grafiki
    background_image(Surface) - grafika z tłem
    player(Surface) - grafika z pojazdem
    meteors(list) - lista meteorytów
    lives(int) - liczba żyć
    level(int) - aktualny poziom
    lost(bool) - czy gracz przegrał (stracił wszystkie życia)
    level_up(bool) - czy gracz przeszedł poziom

    """
    window.blit(background_image, (0,0))
    player.draw(window)
    for meteor in meteors:
        meteor.draw(window)
    draw_text(window, "LIVES: " + str(lives), 150, 50, 30)
    draw_text(window, "LEVEL: " + str(level), 850, 50, 30)
    if lost:
        draw_text(window, "GAME OVER", width/2, height/2, 50)
    if level_up:
        draw_text(window, "LEVEL " + str(level), width/2, height/2, 50)
    pygame.display.update()

#klasa pojazdu
class Player(pygame.sprite.Sprite):
    """
    Class
    Klasa opisująca pojazd gracza
    
    """
    COLOR = (255, 0, 0)
    SPRITES = {"front": frame_0}
    ANIMATION_DELAY = 10

    def __init__(self, x, y, width, height):
        """
        Function
        Funkcja inicjalizująca obiekt klasy Player 
        
        Input
        x(float) - współrzędna początkowa x pojazdu
        y(float) - współrzędna początkowa y pojazdu
        width(float) - szerokość grafiki pojazdu
        height(float) - wysokość grafiki pojazdu
        
        """
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.mask = None
        self.direction = "front"
        self.previous_direction = "front"
        self.animation_count = 0
        self.crash = False

    def move(self, dx):
        """
        Function
        Funkcja przesuwająca pojazd
        
        Input
        dx(float) - przesunięcie na osi x
        
        """
        if 0 < self.rect.x + dx < width - 54*3:
            self.rect.x += dx

    def move_left(self, vel):
        """
        Function
        Funkcja skręcająca pojazd w lewo
        
        Input
        vel(float) - prędkość pojazdu
        
        """
        self.x_vel = -vel
        if self.direction != "left":
            self.previous_direction = self.direction
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        """
        Function
        Funkcja skręcająca pojazd w prawo
        
        Input
        vel(float) - prędkość pojazdu
        
        """
        self.x_vel = vel
        if self.direction != "right":
            self.previous_direction = self.direction
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        """
        Funkcja aktualizująca stan pojazdu
        
        Input
        fps(int) - liczba klatek na sekundę
        """
        self.move(self.x_vel)
        self.update_sprite()
    
    def draw(self, win):
        """
        Function
        Funkcja rysująca grafikę pojazdu na ekranie
        
        Input
        win(Surface) - ekran, na którym wyświetlana jest gra
        """
        win.blit(self.sprite, (self.rect.x, self.rect.y))

    def update_sprite(self):
        """
        Function
        Funkcja aktualizująca obecnie wyświetlaną grafikę pojazdu
        """
        self.sprite = frame_0
        if self.x_vel != 0:
            frame_index = 0

        if self.crash:
            self.x_vel = 0
            if self.direction == "left":
                frame_index = (self.animation_count // self.ANIMATION_DELAY) % len(frames_left_crash)
                self.sprite = frames_left_crash[frame_index]
                self.animation_count += 1
                if frame_index == len(frames_left_crash) - 1:
                    self.crash = False
                    self.direction = "front"


            elif self.direction == "right":
                frame_index = (self.animation_count // self.ANIMATION_DELAY) % len(frames_right_crash)
                self.sprite = frames_right_crash[frame_index]
                self.animation_count += 1
                if frame_index == len(frames_right_crash) - 1:
                    self.crash = False
                    self.direction = "front"

            elif self.direction == "front":
                frame_index = (self.animation_count // self.ANIMATION_DELAY) % len(frames_front_crash)
                self.sprite = frames_front_crash[frame_index]
                self.animation_count += 1
                if frame_index == len(frames_front_crash) - 1:
                    self.crash = False
                    self.direction = "front"


        else:
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
        """
        Function
        Funkcja aktualizująca pozycję pojazdu
        """
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

class Meteor(pygame.sprite.Sprite):
    """
    Class
    Klasa opisujaca spadające meteoryty
    """

    def __init__(self, x, y, width, height):
        """
        Funkcja inicjalizująca obiekt klasy Meteor
        
        Input
        x(float) - współrzędna początkowa x meteorytu
        y(float) - współrzędna początkowa y meteorytu
        width(float) - szerokość grafiki meteorytu
        height(float) - wysokość grafiki meteorytu
        
        """
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.blit(meteor_image, (0,0))
        self.width = width
        self.height = height
        self.y_vel = 0
        self.mask = pygame.mask.from_surface(self.image)

    def fall(self, dy):
        """
        Funkcja poruszająca meteoryt
        
        Input
        dy(float) - przesunięcie meteorytu
        """
        self.rect.y += dy

    def draw(self, win):
        """
        Function
        Funkcja rysująca meteoryt na ekranie
        
        win(Surface) - ekran gry
        """
        win.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        """
        Funkcja aktualizująca pozycję meteorytu
        """
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

def handle_move(player):
    """
    Function
    Funkcja sprawdzająca kliknięcia gracza na klawiaturze
    
    Input
    player(Player) - pojazd gracza
    """
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and not player.crash:
        player.x_vel = PLAYER_VEL
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT] and not player.crash:
        player.x_vel = PLAYER_VEL
        player.move_right(PLAYER_VEL)

def collision_detection(player, meteor):
    """
    Function
    Funkcja wykrywająca kolizję między pojazdem a meteorytem
    
    Input
    player(Player) - pojazd gracza
    meteor(Meteor) - meteoryt
    
    Output
    True(bool) - jeśli występuje kolizja
    """
    if pygame.sprite.collide_mask(player, meteor) != None:
        return True

def throw_meteor(meteor, vel):
    """
    Function 
    Funkcja zrzucająca meteoryt
    
    Input
    meteor(Meteor) - meteoryt
    vel(float) - prędkość meteorytu
    """
    meteor.fall(vel)
    meteor.update()

def draw_text(window, text, x, y, size):
    """
    Function
    Funkcja wyświetlająca napis na ekranie
    
    Input
    window(Surface) - ekran gry
    text(string) - napis, który chcemy wyświetlić
    x(float) - współrzędna x napisu
    y(float) - współrzędna y napisu
    size(int) - wielkość fontu
    """
    font = make_font(size, r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\PressStart2P-vaV7.ttf")
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    window.blit(text_surface, text_rect)


def main(window):
    """
    Function
    Funkcja startująca grę
    
    Input
    window(Surface) - ekran gry
    """
    run = True
    level = 1
    dif = g.difficulty
    lives = 3

    if dif == "EASY":
        METEOR_VEL = 4
    elif dif == "NORMAL":
        METEOR_VEL = 5
    elif dif == "HARD":
        METEOR_VEL = 6
    
    if dif == "EASY":
        wave = 4
    elif dif == "NORMAL":
        wave = 5
    elif dif == "HARD":
        wave = 6

    meteors = [Meteor(random.randrange(0, 1000 - 32*3), random.randrange(-1500, -100), 32*3, 32*3) for i in range(wave)]
    loss = False
    loss_count = 0
    screen_shake = 0
    level_up = False
    level_up_count = 0

    clock = pygame.time.Clock()

    player = Player(427, 600, 162, 102)
    
    if level % 3 == 0:
        METEOR_VEL += 0.5
        PLAYER_VEL += 0.5

    while run:
        clock.tick(FPS)
        player.loop(FPS)
        handle_move(player) 

        if len(meteors) == 0:
            level_up = True 
            level += 1
            wave += 3
            for i in range(wave):
                met = Meteor(random.randrange(0, 1000 - 32*3), random.randrange(-1500, -100), 32*3, 32*3)
                meteors.append(met)

        if lives == 0:
            loss = True
            loss_count += 1

        if level_up_count == 1:
            level_up_sound.play()

        if loss_count == 1:
            car_sound.stop()
            game_over_sound.play()

        if screen_shake > 0:
            screen_shake -= 1
        
        render_offset = [0,0]
        if screen_shake:
            render_offset[0] = random.randint(0,8) - 4
            render_offset[1] = random.randint(0,8) - 4

        draw(display, background_image, player, meteors, lives, level, loss, level_up)
        window.blit(display, render_offset)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False     
                break

        if loss:
            if loss_count > FPS * 4:
                run = False
            else:
                continue

        if level_up:
            level_up_count += 1
            if level_up_count > FPS * 2:
                level_up = False
                level_up_count = 0

        for meteor in meteors:
            throw_meteor(meteor, METEOR_VEL)
            if collision_detection(player, meteor):
                    meteor_sound.play()
                    meteors.remove(meteor)
                    lives -= 1
                    player.crash = True
                    screen_shake = 30
            if meteor.rect.y > width:
                meteors.remove(meteor)
    g.score = level
    g.current_menu = g.save_score
    main_song.play()
    g.start(window)

class Menu():
    """
    Class
    Klasa opisująca menu główne
    """
    def __init__(self, game):
        """
        Funkcja inicjalizująca obiekt klasy Menu
        
        Input
        game(Game) - gra
        """
        super().__init__()
        self.game = game
        self.cursor1_rect = pygame.Rect(0, 0, 20, 20)
        self.cursor2_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = 50
        self.state = "START"
        self.startx, self.starty = width/2, height/2 + 30
        self.rulesx, self.rulesy = width/2, height/2 + 90
        self.optionsx, self.optionsy = width/2, height/2 + 60
        self.highscorex, self.highscorey = width/2, height/2 + 120
        self.authorx, self.authory = width/2, height/2 + 150
        self.quitx, self.quity = width/2, height/2 + 180
        self.cursor1_rect.midtop = (self.startx - self.offset, self.starty)
        self.cursor2_rect.midtop = (self.startx + 15 + self.offset, self.starty)

    def draw_cursor(self, win):
        """
        Function 
        Funkcja rysująca kursor na ekranie
        
        win(Surface) - ekran gry
        """
        draw_text(win, "<", self.cursor1_rect.x, self.cursor1_rect.y, 15)
        draw_text(win, ">", self.cursor2_rect.x, self.cursor2_rect.y, 15)

    def display_menu(self, win):
        """
        Function
        Funkcja wyświetlająca menu na ekranie
        
        Input
        win(Surface) - ekran gry
        """
        self.run = True
        while self.run:
            win.blit(background_image, (0,0))
            self.draw_cursor(win)
            self.move_cursor()
            draw_text(win, "ASTEROID CITY", width/2, height/2 - 50, 60)
            draw_text(win, "START", self.startx, self.starty, 20)
            draw_text(win, "RULES", self.rulesx, self.rulesy, 20)
            draw_text(win, "OPTIONS", self.optionsx, self.optionsy, 20)
            draw_text(win, "HIGHSCORE", self.highscorex, self.highscorey, 20)
            draw_text(win, "AUTHOR", self.authorx, self.authory, 20)
            draw_text(win, "QUIT", self.quitx, self.quity, 20)
            pygame.display.update()

    def move_cursor(self):
        """
        Function
        Funkcja przesuwająca kursor 
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if self.state == "START":
                        self.cursor1_rect.midtop = (self.optionsx - 20 - self.offset, self.optionsy)
                        self.cursor2_rect.midtop = (self.optionsx + 37 + self.offset, self.optionsy)
                        self.state = "OPTIONS"
                    elif self.state == "OPTIONS":
                        self.cursor1_rect.midtop = (self.rulesx - self.offset, self.rulesy)
                        self.cursor2_rect.midtop = (self.rulesx + 18 + self.offset, self.rulesy)
                        self.state = "RULES"
                    elif self.state == "RULES":
                        self.cursor1_rect.midtop = (self.highscorex - 40 - self.offset, self.highscorey)
                        self.cursor2_rect.midtop = (self.highscorex + 56 + self.offset, self.highscorey)
                        self.state = "HIGHSCORE"
                    elif self.state == "HIGHSCORE":
                        self.cursor1_rect.midtop = (self.authorx - 11 - self.offset, self.authory)
                        self.cursor2_rect.midtop = (self.authorx + 29 + self.offset, self.authory)
                        self.state = "AUTHOR"
                    elif self.state == "AUTHOR":
                        self.cursor1_rect.midtop = (self.quitx + 10 - self.offset, self.quity)
                        self.cursor2_rect.midtop = (self.quitx + 5 + self.offset, self.quity)
                        self.state = "QUIT"
                elif event.key == pygame.K_UP:
                    if self.state == "OPTIONS":
                        self.cursor1_rect.midtop = (self.startx - self.offset, self.starty)
                        self.cursor2_rect.midtop = (self.startx + 15 + self.offset, self.starty)
                        self.state = "START"
                    elif self.state == "RULES":
                        self.cursor1_rect.midtop = (self.optionsx - 20 - self.offset, self.optionsy)
                        self.cursor2_rect.midtop = (self.optionsx + 37 + self.offset, self.optionsy)
                        self.state = "OPTIONS"
                    elif self.state == "HIGHSCORE":
                        self.cursor1_rect.midtop = (self.rulesx - self.offset, self.rulesy)
                        self.cursor2_rect.midtop = (self.rulesx + 18 + self.offset, self.rulesy)
                        self.state = "RULES"
                    elif self.state == "AUTHOR":
                        self.cursor1_rect.midtop = (self.highscorex - 40 - self.offset, self.highscorey)
                        self.cursor2_rect.midtop = (self.highscorex + 56 + self.offset, self.highscorey)
                        self.state = "HIGHSCORE"
                    elif self.state == "QUIT":
                        self.cursor1_rect.midtop = (self.authorx - 11 - self.offset, self.authory)
                        self.cursor2_rect.midtop = (self.authorx + 29 + self.offset, self.authory)
                        self.state = "AUTHOR"
                elif event.key == pygame.K_RETURN:
                    if self.state == "START":
                        main_song.stop()
                        car_sound.play(-1)
                        main(window)
                    elif self.state == "OPTIONS":
                        self.game.current_menu.run = False
                        self.game.current_menu = self.game.options_menu
                    elif self.state == "RULES":
                        self.game.current_menu.run = False
                        self.game.current_menu = self.game.rules_menu
                    elif self.state == "HIGHSCORE":
                        self.game.current_menu.run = False
                        self.game.current_menu = self.game.highscore_menu
                    elif self.state == "AUTHOR":
                        self.game.current_menu.run = False
                        self.game.current_menu = self.game.author_menu
                    elif self.state == "QUIT":
                        pygame.quit()
                        quit()

class OptionsMenu(Menu):
    """
    Class
    Klasa opisująca menu opcji
    """
    def __init__(self, game):
        """
        Function
        Funkcja inicjalizująca obiekt klasy OptionsMenu
        
        game(Game) - gra
        """
        super().__init__(game)
        self.game = game
        self.state = "VOLUME"
        self.optionsx, self.optionsy = width/2, height/2 - 50
        self.volx, self.voly = width/2, height/2 + 30
        self.difx, self.dify = width/2, height/2 + 90
        self.cursor1_rect.midtop = (self.volx - 10 - self.offset, self.voly)
        self.cursor2_rect.midtop = (self.volx + 28 + self.offset, self.voly)
    
    def display_menu(self, win):
        """
        Function
        Funkcja wyświetlająca menu na ekranie
        
        Input
        win(Surface) - ekran gry
        """
        self.run = True
        while self.run:
            win.blit(background_image, (0,0))
            self.draw_cursor(win)
            self.move_cursor()
            draw_text(win, "OPTIONS", self.optionsx, self.optionsy, 60)
            draw_text(win, "VOLUME", self.startx, self.starty, 20)
            draw_text(win, "DIFFICULTY", self.difx, self.dify, 20)
            pygame.display.update()

    def move_cursor(self):
        """
        Function 
        Funkcja poruszająca kursor
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.game.current_menu.run = False
                    self.game.current_menu = self.game.main_menu
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    if self.state == "VOLUME":
                        self.cursor1_rect.midtop = (self.difx - 50 - self.offset, self.dify)
                        self.cursor2_rect.midtop = (self.difx + 67 +self.offset, self.dify)
                        self.state = "DIFFICULTY"
                    elif self.state == "DIFFICULTY":
                        self.cursor1_rect.midtop = (self.volx - 10 - self.offset, self.voly)
                        self.cursor2_rect.midtop = (self.volx + 28 + self.offset, self.voly)
                        self.state = "VOLUME"
                elif event.key == pygame.K_RETURN:
                    if self.state == "VOLUME":
                        self.game.current_menu.run = False
                        self.game.current_menu = self.game.volume_menu
                    elif self.state == "DIFFICULTY":
                        self.game.current_menu.run = False
                        self.game.current_menu = self.game.difficulty_menu

class VolumeMenu(Menu):
    """
    Class
    Klasa opisująca menu dźwięku
    """
    def __init__(self, game):
        """
        Function
        Funkcja inicjalizująca obiekt klasy VolumeMenu
        
        Input
        game(Game) - gra
        """
        super().__init__(game)
        self.game = game
        self.volume = 50
        self.volx, self.voly = width/2, height/2 - 50
        self.switchx, self.switchy = width/2, height/2 + 30
        self.state = "SWITCH"
        self.cursor1_rect.midtop = (self.switchx + 20 - self.offset, self.switchy)
        self.cursor2_rect.midtop = (self.switchx - 3 + self.offset, self.switchy)
    
    def display_menu(self, win):
        """
        Function
        Funkcja wyświetlająca menu na ekranie
        
        Input
        win(Surface) - ekran gry
        """
        self.run = True
        while self.run:
            win.blit(background_image, (0,0))
            self.draw_cursor(win)
            self.move_cursor()
            draw_text(win, "VOLUME", self.volx, self.voly, 40)
            draw_text(win, str(self.volume) + "%", self.switchx, self.switchy, 20)
            pygame.display.update()
     
    def move_cursor(self):
        """
        Funkcja przesuwająca kursor
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.game.current_menu.run = False
                    self.game.current_menu = self.game.options_menu
                    self.game.vol = self.volume / 100
                if event.key == pygame.K_DOWN or event.key == pygame.K_LEFT:
                    if self.volume == 0:
                        continue
                    else:
                        self.volume -= 10
                if event.key == pygame.K_UP or event.key == pygame.K_RIGHT:
                    if self.volume == 100:
                        continue
                    else:
                        self.volume += 10

class DifficultyMenu(Menu):
    """
    Class
    Klasa opisująca menu wyboru poziomu trudności
    """
    def __init__(self, game):
        """
        Function
        Funkcja inicjalizująca obiekt klasy DifficultyMenu
        
        Input
        game(Game) - gra
        """
        super().__init__(game)
        self.game = game
        self.dif = "NORMAL"
        self.difx, self.dify = width/2, height/2 - 50
        self.switchx, self.switchy = width/2, height/2 + 30
        self.cursor1_rect.midtop = (self.switchx - 14 - self.offset, self.switchy)
        self.cursor2_rect.midtop = (self.switchx + 28 + self.offset, self.switchy)
    
    def display_menu(self, win):
        """
        Function
        Funkcja wyświetlająca menu na ekranie
        
        Input
        win(Surface) - ekran gry
        """
        self.run = True
        while self.run:
            win.blit(background_image, (0,0))
            self.draw_cursor(win)
            self.move_cursor()
            draw_text(win, "DIFFICULTY", self.difx, self.dify, 40)
            draw_text(win, self.dif, self.switchx, self.switchy, 20)
            pygame.display.update()
    
    def move_cursor(self):
        """
        Funkcja przesuwająca kursor
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.game.current_menu.run = False
                    self.game.current_menu = self.game.options_menu
                if event.key == pygame.K_DOWN or event.key == pygame.K_LEFT:
                    if self.dif == "NORMAL":
                        self.dif = "EASY"
                        self.game.difficulty = "EASY"
                    elif self.dif == "HARD":
                        self.dif = "NORMAL"
                        self.game.difficulty = "NORMAL"
                    else:
                        continue
                if event.key == pygame.K_UP or event.key == pygame.K_RIGHT:
                    if self.dif == "NORMAL":
                        self.dif = "HARD"
                        self.game.difficulty = "HARD"
                    elif self.dif == "EASY":
                        self.dif = "NORMAL"
                        self.game.difficulty = "NORMAL"
                    else:
                        continue

class RulesMenu(Menu):
    """
    Class
    Klasa opisująca menu z zasadami
    """
    def __init__(self, game):
        """
        Function
        Funkcja inicjalizująca obiekt klasy RulesMenu
        
        Input
        game(Game) - gra
        """
        super().__init__(game)
        self.game = game
        self.rulesx, self.rulesy = width/2, height/2 - 50
        self.rules_text = rules

    def display_menu(self, win):
        """
        Function
        Funkcja wyświetlająca menu na ekranie
        
        Input
        win(Surface) - ekran gry
        """
        self.run = True
        while self.run:
            win.blit(background_image, (0,0))
            self.move_cursor()
            draw_text(win, "RULES", self.rulesx, self.rulesy - 20, 40)
            for i in range(len(self.rules_text)):
                draw_text(win, self.rules_text[i], self.rulesx, self.rulesy + 40 * (i+1), 18)
            pygame.display.update()
    
    def move_cursor(self):
        """
        Function 
        Funkcja przesuwająca kursor
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.game.current_menu.run = False
                    self.game.current_menu = self.game.main_menu

class SaveScore(Menu):
    """
    Class
    Klasa opisująca menu z zapisywaniem wyniku
    """
    def __init__(self, game):
        """
        Function
        Funkcja incjalizująca obiekt klasy SaveScore
        
        Input
        game(Game) - gra
        """
        super().__init__(game)
        self.game = game
        self.labelx, self.labely = self.rulesy = width/2, height/2 - 50
        self.yesx, self.yesy = width/2 + 100, height/2 + 30
        self.nox, self.noy = width/2 - 100, height/2 + 30
        self.cursor1_rect.midtop = (self.nox + 30 - self.offset, self.noy)
        self.cursor2_rect.midtop = (self.nox - 10 + self.offset, self.noy)
        self.state = "NO"
        self.choice = "NO"
        self.write = False
    
    def display_menu(self, win):
        """
        Function
        Funkcja wyświetlająca menu na ekranie
        
        Input
        win(Surface) - ekran gry
        """
        self.run = True
        while self.run:
            win.blit(background_image, (0,0))
            self.draw_cursor(win)
            self.move_cursor()
            draw_text(win, "SAVE MY SCORE", self.labelx, self.labely, 40)
            draw_text(win, "NO", self.nox, self.noy, 20)
            draw_text(win, "YES", self.yesx, self.yesy, 20)
            if self.choice == "YES":
                self.write = True
                draw_text(win, "ENTER YOUR NAME:", self.labelx - 100, self.yesy + 70, 20)
                font = make_font(20, r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 6\PressStart2P-vaV7.ttf")
                textinput = pygame_textinput.TextInputVisualizer(font_object=font)
                textinput.antialias = False
                textinput.font_color = (255, 255, 255)
                data = {"name": "", "score": ""}
                pygame.key.set_repeat(200, 25)
                while self.write:
                    events = pygame.event.get()
                    textinput.update(events)
                    textinput.surface.convert_alpha()
                    textinput.surface.set_colorkey((0,0,0))
                    win.blit(textinput.surface, (self.labelx + 70, self.yesy + 58))
                    for event in events:
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                data["name"] = textinput.value
                                data["score"] = self.game.score
                                if os.path.getsize(highscore_path) == 0:
                                    with open(highscore_path, "wb") as f:
                                        pickle.dump([data], f)
                                else:
                                    with open(highscore_path, "rb") as f:
                                        scores = pickle.load(f)
                                        scores.append(data)
                                    with open(highscore_path, "wb") as f:
                                        pickle.dump(scores, f)
                                self.write = False
                                self.game.current_menu.run = False
                                self.game.current_menu = self.game.main_menu
                    pygame.display.update()
            pygame.display.update()
    
    def move_cursor(self):
        """
        Function
        Funkcja przesuwająca kursor
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if self.state == "NO":
                        self.cursor1_rect.midtop = (self.yesx + 20 - self.offset, self.yesy)
                        self.cursor2_rect.midtop = (self.yesx + self.offset, self.yesy)
                        self.state = "YES"
                    else:
                        continue
                elif event.key == pygame.K_LEFT:
                    if self.state == "YES":
                        self.cursor1_rect.midtop = (self.nox + 25 - self.offset, self.noy)
                        self.cursor2_rect.midtop = (self.nox - 5 + self.offset, self.noy)
                        self.state = "NO"
                    else:
                        continue
                elif event.key == pygame.K_RETURN:
                    if self.state == "NO":
                        self.game.current_menu.run = False
                        self.game.current_menu = self.game.main_menu
                    elif self.state == "YES":
                        self.choice = "YES"

class HighscoreMenu(Menu):
    """
    Class
    Klasa opisująca menu z najlepszymi wynikami
    """
    def __init__(self, game):
        """
        Function
        Funkcja inicjalizująca obiekt klasy HighscoreMenu
        
        Input
        game(Game) - gra
        """
        super().__init__(game)
        self.game = game
        self.labelx, self.labely = width/2, height/2 - 50
        self.scores = top_scores(highscore_path)

    def display_menu(self, win):
        """
        Function
        Funkcja wyśiwetlająca menu na ekranie
        
        Input
        win(Surface) - ekran gry
        """
        self.run = True
        while self.run:
            win.blit(background_image, (0,0))
            self.move_cursor()
            draw_text(win, "TOP 5 SCORES", self.labelx, self.labely - 30, 40)
            if self.scores:
                for i in range(len(self.scores)):
                    username = self.scores[i]["name"]
                    score = self.scores[i]["score"]
                    text1 = str(i+1) + ". " 
                    draw_text(win, text1, self.labelx - 70, self.labely + (i+1)*30, 20)
                    text2 = username + " " + str(score)
                    draw_text(win, text2, self.labelx + 20, self.labely + (i+1)*30, 20)
            pygame.display.update()
    
    def move_cursor(self):
        """
        Function
        Funkcja przesuwająca kursor
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.game.current_menu.run = False
                    self.game.current_menu = self.game.main_menu

class AuthorMenu(Menu):
    """
    Class
    Klasa opisująca menu z notką o autorze
    """
    def __init__(self, game):
        """
        Function
        Funkcja inicjalizująca obiekt klasy AuthorMenu
        
        Input
        game(Game) - gra
        """
        super().__init__(game)
        self.game = game
        self.labelx, self.labely = width/2, height/2 - 150
        self.text_file = author_file
        self.qr_code = qr

    def display_menu(self, win):
        """
        Function
        Funkcja wyświetlająca menu na ekranie
        
        Input
        win(Surface) - ekran gry
        """
        self.run = True
        while self.run:
            win.blit(background_image, (0,0))
            self.move_cursor()
            draw_text(win, "AUTHOR", self.labelx, self.labely - 30, 40)
            splitted = self.text_file.splitlines()
            for i in range(len(splitted)):
                draw_text(win, splitted[i], self.labelx, self.labely + (i+1)*30, 20)
            win.blit(self.qr_code, (390, 400))
            pygame.display.update()

    def move_cursor(self):
        """
        Function
        Funkcja przesuwająca kursor
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.game.current_menu.run = False
                    self.game.current_menu = self.game.main_menu    
            
        
class Game():
    """
    Class
    Klasa opisująca procesy gry
    """
    def __init__(self):
        """
        Funkcja inicjalizująca obiekt klasy Game
        """
        self.main_menu = Menu(self)
        self.options_menu = OptionsMenu(self)
        self.current_menu = self.main_menu
        self.volume_menu = VolumeMenu(self)
        self.difficulty_menu = DifficultyMenu(self)
        self.rules_menu = RulesMenu(self)
        self.save_score = SaveScore(self)
        self.highscore_menu = HighscoreMenu(self)
        self.author_menu = AuthorMenu(self)
        self.playing = True
        self.score = 0
        self.difficulty = "NORMAL"
        self.vol = 0.5

    def start(self, win):
        """
        Function
        Funkcja startująca grę
        
        Input
        win(Surface) - ekran gry
        """
        self.current_menu.display_menu(win)

g = Game()
main_song.play()

while g.playing:
    for sound in sounds:
        sound.set_volume(g.vol)
    g.start(window)

    



