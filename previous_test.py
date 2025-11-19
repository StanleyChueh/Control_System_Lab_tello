import pygame
from djitellopy import Tello
import time

# 初始化 pygame
pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Tello Keyboard Control")

# 建立 tello
tello = Tello()
tello.connect()
print("Battery:", tello.get_battery())

speed = 50
lr = fb = ud = yv = 0

running = True

while running:
    lr = fb = ud = yv = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # 左右
    if keys[pygame.K_LEFT]:  lr = -speed
    if keys[pygame.K_RIGHT]: lr =  speed

    # 前後
    if keys[pygame.K_UP]:    fb =  speed
    if keys[pygame.K_DOWN]:  fb = -speed

    # 上下
    if keys[pygame.K_w]: ud =  speed
    if keys[pygame.K_s]: ud = -speed

    # 旋轉
    if keys[pygame.K_a]: yv = -speed
    if keys[pygame.K_d]: yv =  speed

    # 起飛
    if keys[pygame.K_e]:
        print("Takeoff")
        tello.takeoff()

    # 降落
    if keys[pygame.K_q]:
        print("Land")
        tello.land()
        time.sleep(1)

    tello.send_rc_control(lr, fb, ud, yv)
    time.sleep(0.03)

pygame.quit()
