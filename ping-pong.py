from pygame import *

back = (255, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping-Pong")
window.fill(back)

font.init()
font = font.SysFont('Arial', 36)

lose1 = font.render('FAILED player 1', True, (180, 0, 0))
lose2 = font.render('FAILED player 2', True, (180, 0, 0))
#mixer.init()
#mixer.music.load('space_war.mp3')
#mixer.music.play()

clock = time.Clock()
FPS = 60

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
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

speed_x = 3
speed_y = 3

player1 = Player('Racket.png', 30, 200, 20, 100, 10)
player2 = Player('Racket.png', 520, 200, 20, 100, 10)
ball = GameSprite('ball.png', 200, 200, 50, 50, 50)
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        player1.update_l()
        player2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game = True
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game = True
        player1.reset()
        player2.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
