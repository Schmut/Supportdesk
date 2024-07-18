import pygame

vel = 10

class Player(pygame.sprite.Sprite):
    def __init__(self,money,clients, employees,vel,x,y,Company_Name,Player_Name):
        self.money = money
        self.clients = clients
        self.employees = employees
        self.vel = vel
        self.x = x
        self.y = y
        self.vel = vel
        self.Company_Name = Company_Name
        self.Player_Name = Player_Name

class Player_Tile (pygame.sprite.Sprite):
    def __init__ (self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load ('player').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            Player.y -= vel
        if keys[pygame.K_s]:
            Player.y += vel
        if keys[pygame.K_a]:
            Player.x -= vel
        if keys[pygame.K_d]:
            Player.x += vel
        