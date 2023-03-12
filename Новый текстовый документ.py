from pygame import *

window = display.set_mode((700, 500))
display.set_caption('PP')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))

#ракетки
class GameSprite(sprite.Sprite):
    def __init__(self, image_1, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(image_1), (32, 132))#переписать размеры для мяча (через переменные)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def dvig_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 1:
            self.rect.y = self.rect.y - self.speed
        if keys_pressed[K_s] and self.rect.y < 370:
            self.rect.y = self.rect.y + self.speed
    def dvig_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 1:
            self.rect.y = self.rect.y - self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 370:
            self.rect.y = self.rect.y + self.speed
r_1 = Player('R1.png', 6, 50, 200) 
r_2 = Player('R2.png', 6, 610, 200) 


class Enemy(GameSprite):
    def update(self):
        pass

b = Enemy('B.png', 6, 250, 250)

clock = time.Clock()
FPS = 60
finish = False
game = True
while game:
    window.blit(background, (0, 0))
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        #функц
        r_1.reset()
        r_1.dvig_1()
        r_2.reset()
        r_2.dvig_2()
        #b.reset()

    display.update()
    clock.tick(FPS)  