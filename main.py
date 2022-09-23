#Name : Radhesham Nemade
#Subject : Fourier convolutionSystem
import pygame
import os
import math
import random
from formulae import *
from colors import *

os.environ["SDL_VIDEO_CENTERED"] = '1'
pygame.init()

width, height = 1396, 1080
SIZE = (width, height)
pygame.display.set_caption("Double Pendulum")
fps = 60
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
cam_x = width/2
cam_y = height/2

mass1 = 10
mass2 = 10
length1 = 100
length2 = 100

angle1 = [math.pi*1/2] * 72
angle2 = [math.pi*1/2] * 72

starting_point = (int(width / 2), int(height / 2))
x1 = [0] * 72
y1 = [0] * 72

matrix = [[0]*5]*12000000
for i in range(12000000):
    for j in range(5):
        matrix[i][j] = [0,0]
kount_matrix = 0

x_offset = starting_point[0]
y_offset = starting_point[1]

x1[0] = x_offset
y1[0] = y_offset
x1[1] = x_offset
y1[1] = y_offset

running = True
while running:
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    i = 2
    j = 1
    length1 = 100
    x_offset = starting_point[0]
    y_offset = starting_point[1]
    while(i<=71):
        x1[i] = float(length1 * math.sin(angle1[j]) + x1[j])
        y1[i] = float(length1 * math.cos(angle1[j]) + y1[j])
        pygame.draw.line(screen, a[i], (int(x1[i]),int(y1[i])), (int(x1[j]), int(y1[j])), 1)
        pygame.draw.circle(screen,(150,150,150),(int(x1[j]), int(y1[j])), 2)
        x_offset += x1[j]
        y_offset += y1[j]
        length1 /= 1.04
        angle1[j] += ((j)*(j)*(0.00005))*(-1)**i
        i+=1
        j+=1
        print(length1)
    matrix[kount_matrix].insert(0, (x1[71], y1[71]))
    count = 0
    for point in matrix[kount_matrix]:
        plot = Points(point[0], point[1], screen, a[28], matrix[kount_matrix])
        plot.draw()
        pygame.display.update()
        count+=1
    if len(matrix[kount_matrix]) > 5:
        kount_matrix+=1
        matrix[kount_matrix].pop()
pygame.quit()
