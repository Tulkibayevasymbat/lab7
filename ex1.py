import pygame
from datetime import datetime as dt

pygame.init()
screen = pygame.display.set_mode((1400, 1050))
pygame.display.set_caption("clock")
icon = pygame.image.load(r'c:\Users\АНЭЛ\Downloads\mainclock.png.png')
pygame.display.set_icon(icon)
syma = pygame.image.load(r'c:\Users\АНЭЛ\Downloads\mainclock.png.png')
syma1 = pygame.image.load(r'c:\Users\АНЭЛ\Downloads\rightarm.png')
syma2 = pygame.image.load(r'c:\Users\АНЭЛ\Downloads\leftarm.png')

clock = pygame.time.Clock()

running = True
while running:
    screen.fill((247, 219, 72))
    screen.blit(syma, (10, 10))  

    current_time = dt.now().time()

    seconds_angle = -(current_time.second * 6)
    minutes_angle = -(current_time.minute * 6)

    rotated_leftarm = pygame.transform.rotate(syma2, seconds_angle)
    rotated_rightarm = pygame.transform.rotate(syma1, minutes_angle)

    leftarm_rect = rotated_leftarm.get_rect(center=(700, 525))
    rightarm_rect = rotated_rightarm.get_rect(center=(700, 525))

    screen.blit(rotated_leftarm, leftarm_rect)
    screen.blit(rotated_rightarm, rightarm_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()