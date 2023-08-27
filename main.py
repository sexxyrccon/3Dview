import pygame
import math
import sys

pygame.init()

screenSize = (600, 450)
screen = pygame.display.set_mode(screenSize)

pygame.display.set_caption("Display")

fps = 240
clock = pygame.time.Clock()
pygame.key.set_repeat(10)

objects = []


def cube(n,i):
    objects.append([[1 + n, 1 + i, -1], [1 + n, 1 + i, 1], [1 + n, -1 + i, 1], [1 + n, -1 + i, -1], [1 + n, 1 + i, -1]])
    objects.append([[-1 + n, 1 + i, -1], [-1 + n, 1 + i, 1], [-1 + n, -1 + i, 1], [-1 + n, -1 + i, -1], [-1 + n, 1 + i, -1]])
    objects.append([[-1  + n, -1 + i, -1], [-1 + n, -1 + i, 1], [1 + n, -1 + i, 1], [1 + n, -1 + i, -1], [-1 + n, -1 + i, -1]])
    objects.append([[-1 + n, 1 + i, -1], [-1 + n, 1 + i, 1], [1 + n, 1 + i, 1], [1 + n, 1 + i, -1], [-1 + n, 1 + i, -1]])


for i in range(10):
    cube(2, i * 4)
    cube(-2, i * 4)



class Camera:
    def __init__(self):
        self.pos = [0, -4, 0]
        self.depth = 600
        self.angle = 0

    def display(self):
        for j in objects:
            for i in range(len(j) - 1):
                dx1 = j[i][0] - self.pos[0]
                dy1 = j[i][1] - self.pos[1]
                dz1 = j[i][2] - self.pos[2]
                dx2 = j[i + 1][0] - self.pos[0]
                dy2 = j[i + 1][1] - self.pos[1]
                dz2 = j[i + 1][2] - self.pos[2]

                translatedx1 = dx1 * math.cos(-1 * self.angle) + dy1 * math.sin(-1 * self.angle)
                translatedy1 = dy1 * math.cos(-1 * self.angle) - dx1 * math.sin(-1 * self.angle)
                translatedx2 = dx2 * math.cos(-1 * self.angle) + dy2 * math.sin(-1 * self.angle)
                translatedy2 = dy2 * math.cos(-1 * self.angle) - dx2 * math.sin(-1 * self.angle)

                if translatedy1 <= 0 and translatedy2 <= 0:
                    continue

                if translatedy1 < 0:
                    translatedy1 *= -1
                if translatedy2 < 0 :
                    translatedy2 *= -1

                pygame.draw.line(screen, (0, 0, 0),
                                 (self.depth * translatedx1 / translatedy1 + screenSize[0] / 2, self.depth * dz1 / translatedy1 * -1 + screenSize[1] / 2),
                                 (self.depth * translatedx2 / translatedy2 + screenSize[0] / 2, self.depth * dz2 / translatedy2 * -1 + screenSize[1] / 2))


    def move(self):
        if event.key == pygame.K_a:
            self.angle -= math.pi / 180 * 1
            print(self.angle / math.pi * 180)
        if event.key == pygame.K_d:
            self.angle += math.pi / 180 * 1
            print(self.angle / math.pi * 180)
        if event.key == pygame.K_w:
            self.pos[1] += 0.1 * math.cos(self.angle)
            self.pos[0] += 0.1 * math.sin(self.angle)
        if event.key == pygame.K_s:
            self.pos[1] -= 0.1 * math.cos(self.angle)
            self.pos[0] -= 0.1 * math.sin(self.angle)
        if event.key == pygame.K_0:
            self.pos[2] += 0.1
        if event.key == pygame.K_9:
            self.pos[2] -= 0.1


James = Camera()


while True:
    clock.tick(fps)
    screen.fill((255, 255, 255))

    James.display()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            James.move()

    pygame.display.update()
