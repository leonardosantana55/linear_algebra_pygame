import sys 
import pygame
import numpy as np

pygame.init()

size = width, height = 800, 600
black = 0, 0, 0
clock = pygame.time.Clock()

font = pygame.font.Font(None, 24)
text = ''

screen = pygame.display.set_mode(size)

blue_ball_position = pygame.Vector2(screen.get_width()/2,screen.get_height()/2)
red_ball_position = pygame.Vector2((screen.get_width()/2),(screen.get_height()/2)) + np.array([0, 172/2])
green_ball_position = pygame.Vector2((screen.get_width()/2),(screen.get_height()/2)) + np.array([0,-172])

angle = 10

x1 = np.cos(np.deg2rad(angle))
x2 = np.sin(np.deg2rad(angle))*-1
w1 = np.sin(np.deg2rad(angle))
w2 = np.cos(np.deg2rad(angle))

transform_m = np.array([[x1,x2],[w1,w2]])
transform_v = np.array([15, 0])

count = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    print(red_ball_position)
    screen.fill(black)
    pygame.draw.circle(screen, 'blue', blue_ball_position, 10)
    pygame.draw.circle(screen, 'red', red_ball_position, 10)
    pygame.draw.circle(screen, 'green', green_ball_position, 10)
    text = str(count)
    rendered_font = font.render(text, True, (255, 155, 155))
    screen.blit(rendered_font, (50,50))
    count += 1
    
    transform_v = np.dot(transform_v,transform_m)
    red_ball_position += transform_v

    pygame.display.flip()    
    clock.tick(30)