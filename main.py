import pygame
import math
import sys

pygame.init()

screenSize = (600, 450)
screen = pygame.display.set_mode(screenSize)

pygame.display.set_caption("Display")

fps = 240
clock = pygame.time.Clock()
pygame.key.set_repeat(1)


mapCord = []
n = 100
for i in range(n + 1):
    for j in range(n + 1):
        mapCord.append([i - n / 2, j - n / 2, 0])


def dist(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2 + (pos1[2] - pos2[2]) ** 2)


class Camera:
    def __init__(self):
        self.pos = [0, 0, 60]
        self.angleX = math.pi / 180 * 30  # x 시야각
        self.angleY = math.atan(math.tan(self.angleX / 2) * screenSize[1] / screenSize[0]) * 2  # y 시야각

    def display(self):
        for i in mapCord:
            angleX = math.asin(i[0] / dist(i, self.pos))
            if angleX <= math.pi:
                x = screenSize[0] / self.angleX * angleX
            else:
                x = screenSize[0] / self.angleX * (angleX - 2 * math.pi)

            angleY = math.asin(i[1] / dist(i, self.pos))
            if angleY <= math.pi:
                y = screenSize[1] / self.angleY * angleY
            else:
                y = screenSize[1] / self.angleY * (angleY - 2 * math.pi)
            pygame.draw.circle(screen, (0, 0, 0), [x + screenSize[0] / 2, y + screenSize[1] / 2], 1)

    def move(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.pos[2] += 0.1
                print(self.pos[2])
            if event.key == pygame.K_s:
                self.pos[2] -= 0.1
                print(self.pos[2])


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
