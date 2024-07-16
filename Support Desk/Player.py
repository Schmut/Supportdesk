import pygame
money = 0


class User(pygame.sprite.Sprite):
    def __init__(self,money):
        self.money = money