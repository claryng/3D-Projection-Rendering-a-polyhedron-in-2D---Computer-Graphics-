#!/usr/bin/env python

'''graphics.py: 3D projection onto 2D screen'''
__author__ : "Clary Nguyen"
__version__ : "Aug 10 2022"


# import modules
import pygame
import numpy as np
from math import *

# Screen setup
white = [255,255,255]
black = [0,0,0]
red = [255,0,0]
yellow = [255,255,0]
green = [0,255,0]
blue = [0,0,255]
purple = [255,0,255]

width, height = 800,800
pygame.display.set_caption("Projection")
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

# Clock object to control framerate
clock = pygame.time.Clock()

# Scale to increase size of the shape to match with the screen
scale = 100

# Points
points = []

points.append(np.matrix([0,3,0]))
points.append(np.matrix([1,1,0]))
points.append(np.matrix([3,0,0]))
points.append(np.matrix([1,-1,0]))
points.append(np.matrix([0,3,0]))
points.append(np.matrix([-1,-1,0]))
points.append(np.matrix([-3,0,0]))
points.append(np.matrix([-1,1,0]))

points.append(np.matrix([0,1,1]))
points.append(np.matrix([0,0,3]))
points.append(np.matrix([0,-1,1]))
points.append(np.matrix([0,1,-1]))
points.append(np.matrix([0,-3,0]))

points.append(np.matrix([0,1,-1]))

points.append(np.matrix([0,0,-3]))
points.append(np.matrix([1,0,1]))
points.append(np.matrix([0,-1,-1]))


points.append(np.matrix([-1,0,1]))
points.append(np.matrix([-1,0,-1]))

points.append(np.matrix([1,0,-1]))

# Angle for rotation
angle = 0

projection_matrix = np.matrix([
    [1,0,0],
    [0,1,0],
    [0,0,0]
])

# Move the shape to the center of the screen
point_pos = [(width/2),(height/2)]

# list to later store 2s coordinates
projected_point2d = [
    [n,n] for n in range(len(points))
]

# Connect points
def connection (i,j,point):
    pygame.draw.line(
        screen, blue, (point[i][0], point[i][1]), (point [j] [0], point [j] [1])
    )

while True:
	# framerate 60
    clock.tick(60)

	# close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_Q:
                pygame.quit()
                exit()
    
    screen.fill(black)
    
	# rotation matrix
    rotation_x = np.matrix([
        [1,0,0],
        [0,cos(angle), -sin(angle)],
        [0,sin(angle), cos(angle)]
    ])

    rotation_y = np.matrix([
        [cos(angle), 0,sin(angle)],
        [0,1,0],
        [-sin(angle), 0, cos(angle)]
    ])

    rotation_z = np.matrix([
        [cos(angle), -sin(angle),0],
        [sin(angle), cos(angle),0],
        [0,0,1]
    ])

	# increase angle after each rotation
    angle += 0.01

    i = 0

	# convert 3d points to 2d and project onto thw screen
    for point in points:
        rotation2d = np.dot(rotation_x, point.reshape((3,1)))
        rotation2d = np.dot(rotation_y, rotation2d)
        rotation2d = np.dot(rotation_z,rotation2d)

        projected_point = np.dot(projection_matrix, rotation2d)

        x = int(projected_point [0] [0] * scale) + point_pos [0]

        y = int(projected_point [1] [0] * scale) + point_pos [1]
        
        pygame.draw.circle(screen, red, (x,y), 5)

        projected_point2d [i] = [x,y]
        i += 1

	# connect the points
    connection(0,1,projected_point2d)
    connection(1,2,projected_point2d)
    connection(2,3,projected_point2d)
    connection(5,12,projected_point2d)
    connection(4,8,projected_point2d)
    connection(5,6,projected_point2d)
    connection(6,7,projected_point2d)
    connection(7,0,projected_point2d)
    connection(3,12,projected_point2d)
    connection(10,12,projected_point2d)
    connection(9,10,projected_point2d)
    connection(8,9,projected_point2d)
    connection(4,13,projected_point2d)
    connection(14,13,projected_point2d)
    connection(14,16,projected_point2d)
    connection(12,16,projected_point2d)
    connection(12,17,projected_point2d)
    connection(0,17,projected_point2d)
    connection(18,12,projected_point2d)
    connection(18,0,projected_point2d)
    connection(12,19,projected_point2d)
    connection(0,19,projected_point2d)
    connection(12,15,projected_point2d)
    connection(15,0,projected_point2d)
    connection(6,17,projected_point2d)
    connection(6,18,projected_point2d)
    connection(2,15,projected_point2d)
    connection(2,19,projected_point2d)
    connection(14,19,projected_point2d)
    connection(14,18,projected_point2d)
    connection(9,17,projected_point2d)
    connection(9,15,projected_point2d)
    connection(10,15,projected_point2d)
    connection(10,17,projected_point2d)
    connection(13,18,projected_point2d)
    connection(13,19,projected_point2d)
    connection(8,17,projected_point2d)
    connection(8,15,projected_point2d)
    connection(5,18,projected_point2d)
    connection(5,17,projected_point2d)
    connection(19,1,projected_point2d)
    connection(1,15,projected_point2d)
    connection(6,17,projected_point2d)
    connection(6,18,projected_point2d)
    connection(3,15,projected_point2d)
    connection(3,19,projected_point2d)
    connection(7,18,projected_point2d)
    connection(7,17,projected_point2d)
    connection(16,18,projected_point2d)
    connection(16,19,projected_point2d)
	
	# update the screen
    pygame.display.update()



