#подключаем библиотеки
from pygame import *
#классы
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
#окно игры
back = (85, 255, 113)
win_width = 1280
win_height = 720
window = display.set_mode((win_width, win_height))
window.fill(back)
#переменные
img_ball = "ball.png"
img_rack_l = "rect.png"
speed_x = 3
speed_y = 3
#спрайты
rack_l = Player(img_rack_l, 100, 100, 30, 110, 10)
rack_r = Player(img_rack_l, win_width - 100, 100, 30, 110, 10)
ball = GameSprite(img_ball, 400, 400, 48, 48, 5)
#текст проигрыша и выйгрыша
font.init()
font = font.Font(None, 70)
lose_l = font.render('PLAYER LEFT LOSE!', True, (180, 0, 0))
lose_r = font.render('PLAYER RIGHT LOSE!', True, (180, 0, 0))
#FPS и обновление
clock = time.Clock()
FPS = 60
#игровой цикл
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        rack_l.update_l()
        rack_r.update_r() 
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(rack_l, ball) or sprite.collide_rect(rack_r, ball):
            speed_x *= -1
            speed_y *= -1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose_l, (400, 360))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose_r, (400, 360))

        rack_l.reset()   
        rack_r.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
