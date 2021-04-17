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
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.x < win_width - 80:
            self.rect.y += self.speed
#окно игры
back = (85, 255, 113)
win_width = 1280
win_height = 720
window = display.set_mode((win_width, win_height))
window.fill(back)
#переменные
img_rack_l = "rect.png"
#спрайты
rack_l = Player(img_rack_l, 100, 100, 100, 75, 10)
#FPS и обновление
clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    rack_l.reset()
    rack_l.update_l()
    display.update()
    clock.tick(FPS)