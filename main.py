from pygame import *
font.init()
speed_x = 1
speed_y = 1
w,h = 500,500
window = display.set_mode((w,h))
background = transform.scale(image.load("amogus.png"), (w,h))
font1 = font.Font(None,35)
lose1 = font1.render('ПЕРВЫЙ БОТ СЛИТ',True,(180,0,0))

font2 = font.Font(None,35)
lose2 = font1.render('ВТОРОЙ БОТ СЛИТ',True,(180,0,0))

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x, player_y,size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.size_x = size_x
        self.size_y = size_y

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_RIGHT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_LEFT] and self.rect.y < h - self.size_y - 5:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < h - self.size_y - 5:
            self.rect.y += self.speed

rocket_left = Player("page for igra.jpg",30, 30, 30, 100, 3)
rocket_right = Player("page for igra.jpg", w-30-30, h-100-30,30,100,3)
ball = GameSprite("cgfcbnt.jpg", w/2,h/2,15,15,1)
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        

    if not finish:
        window.blit(background,(0,0))

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > h-15 or ball.rect.y < 0:
            speed_y *= -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))
        if ball.rect.x > w:
            finish = True
            window.blit(lose2,(200,200))

        if sprite.collide_rect(rocket_left,ball) or sprite.collide_rect(rocket_right,ball):
            speed_x *= -1
        
        

        rocket_left.update_l()
        rocket_right.update_r()

        rocket_left.reset()
        rocket_right.reset()
        ball.reset()
    display.update()
    time.delay(2)
