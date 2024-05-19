from pygame import *
from random import randint
from time import time as timer

back = (200, 225, 225)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-Pong")
window.fill(back)

font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 80)
win = font2.render('MISSION COMPLETED', True, (255, 255, 255))
lose = font1.render('MISSION FAILED', True, (180, 0, 0))

mixer.init()
mixer.music.load('space_war.mp3')
mixer.music.play()

bullets_music = mixer.Sound('fire.ogg')

clock = time.Clock()
FPS = 144

lost = 0
score = 0
max_lost = 3
life = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(bullet)

player = Player('rocket.png', 5, 420, 80, 100, 5)
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        player.reset()
        player.update()
        if score >= 10:
            finish = True
            window.blit(win, (200, 200))
        text_lose = font1.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        text_score = font1.render("Счёт: " + str(score), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))
        window.blit(text_score, (10, 20))
    display.update()
    clock.tick(FPS)