import pygame
from pygame import Vector2

from settings import *


class Blob:
    def __init__(self, maze_size, tile_size):
        self.tile_size = tile_size
        self.SCALEDOWN = self.tile_size / 5 + 2
        self.image = pygame.image.load('blob.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, [self.tile_size - self.SCALEDOWN, self.tile_size - self.SCALEDOWN])
        
        self.pos = Vector2(maze_size, maze_size)
        self.accel = Vector2()
        self.animation_speed = BLOB_ANIMATION_SPEED * maze_size
        self.max_accel = BLOB_MAX_ACCELERATION

        self.move_queue = []
        self.in_animation = False

    def display(self, maze_surface, dt):
        if self.in_animation:
            if self.move_queue[0][0] == 'left':
                if self.accel.x > -self.max_accel:
                    self.accel.x -= self.animation_speed * dt
                self.pos += self.accel

                if self.pos.x <= self.move_queue[0][1] - 1:
                    self.pos.x = self.move_queue[0][1] - 1
                    self.accel.x = 0
                    self.move_queue.pop(0)

            elif self.move_queue[0][0] == 'right':
                if self.accel.x < self.max_accel:
                    self.accel.x += self.animation_speed * dt
                self.pos += self.accel

                if self.pos.x >= self.move_queue[0][1] + 1:
                    self.pos.x = self.move_queue[0][1] + 1
                    self.accel.x = 0
                    self.move_queue.pop(0)

            elif self.move_queue[0][0] == 'up':
                if self.accel.y > -self.max_accel:
                    self.accel.y -= self.animation_speed * dt
                self.pos += self.accel

                if self.pos.y <= self.move_queue[0][1] - 1:
                    self.pos.y = self.move_queue[0][1] - 1
                    self.accel.y = 0
                    self.move_queue.pop(0)

            elif self.move_queue[0][0] == 'down':
                if self.accel.y < self.max_accel:
                    self.accel.y += self.animation_speed * dt
                self.pos += self.accel

                if self.pos.y >= self.move_queue[0][1] + 1:
                    self.pos.y = self.move_queue[0][1] + 1
                    self.accel.y = 0
                    self.move_queue.pop(0)

        maze_surface.blit(self.image, [self.tile_size * self.pos.x + self.SCALEDOWN / 2, self.tile_size * self.pos.y + self.SCALEDOWN / 2])

    def update(self, events, maze):
        for event in events:
            if event.type == pygame.KEYDOWN:

                if len(self.move_queue) == 1:
                    if self.move_queue[0][0] == 'left':
                        x = self.move_queue[0][1] - 1
                        y = self.pos.y
                    elif self.move_queue[0][0] == 'right':
                        x = self.move_queue[0][1] + 1
                        y = self.pos.y
                    elif self.move_queue[0][0] == 'up':
                        x = self.pos.x
                        y = self.move_queue[0][1] - 1
                    elif self.move_queue[0][0] == 'down':
                        x = self.pos.x
                        y = self.move_queue[0][1] + 1

                elif len(self.move_queue) == 0:
                    x = self.pos.x
                    y = self.pos.y

                if len(self.move_queue) <= 1:
                    if event.key == pygame.K_LEFT:
                        if x != 0 and maze[int(y) * 2][int(x) * 2 - 1] != 1:
                            self.move_queue.append(['left', x])

                    if event.key == pygame.K_RIGHT:
                        if x != (len(maze) + 1) / 2 - 1 and maze[int(y) * 2][int(x) * 2 + 1] != 1:
                            self.move_queue.append(['right', x])

                    if event.key == pygame.K_UP:
                        if y != 0 and maze[int(y) * 2 - 1][int(x) * 2] != 1:
                            self.move_queue.append(['up', y])

                    if event.key == pygame.K_DOWN:
                        if y != (len(maze) + 1) / 2 - 1 and maze[int(y) * 2 + 1][int(x) * 2] != 1:
                            self.move_queue.append(['down', y])

        if self.move_queue:
            self.in_animation = True
        else:
            self.in_animation = False
