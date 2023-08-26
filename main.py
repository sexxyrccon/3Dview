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


mapCord = []
n = 200
for j in range(n + 1):
    for i in range(n + 1):
        mapCord.append([i - n / 2, j - n / 2])


def dist(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)


class Camera:
    def __init__(self):
        self.pos = [0, 0, -100]
        self.angle = [0, 0]
        self.focalLength = -100
        self.pov = math.pi / 180 * 120

    def display(self):
        for i in mapCord:
            d = [0, 0]
            cor = [0, 0]
            tan = [0, 0]
            condition = [0, 0]

            for j in range(2):
                d[j] = i[j] - self.pos[j]
                if self.angle[j] > math.pi:
                    self.angle[j] = math.pi * -1
                elif self.angle[j] < math.pi * -1:
                    self.angle[j] = math.pi
                tan[j] = math.atan(d[j] / self.pos[2]) + self.angle[j]
                if self.pov / 2 >= tan[j] >= self.pov / -2:
                    condition[j] = 1
                    cor[j] = self.focalLength * math.tan(tan[j])

            if 0 in condition:
                continue
            pygame.draw.circle(screen, (0, 0, 0), [cor[0] + screenSize[0] / 2, cor[1] * -1 + screenSize[1] / 2], 1)

    def move(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.angle[0] += math.pi / 180 * 1
            if event.key == pygame.K_a:
                self.angle[0] -= math.pi / 180 * 1
            if event.key == pygame.K_w:
                self.angle[1] += math.pi / 180 * 1
            if event.key == pygame.K_s:
                self.angle[1] -= math.pi / 180 * 1
            if event.key == pygame.K_0:
                self.pos[2] += 1
            if event.key == pygame.K_9:
                self.pos[2] -= 1


James = Camera()

while True:
    clock.tick(fps)
    screen.fill((255, 255, 255))

    James.display()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        James.move()

    pygame.display.update()
