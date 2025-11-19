import pygame
from djitellopy import Tello
import time

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Tello Keyboard Control")

# Create Tello object
tello = Tello()
tello.connect()
print("Battery:", tello.get_battery())

speed = 50
lr = fb = ud = yv = 0

running = True

while running:
    lr = fb = ud = yv = 0
    
    # When window is closed(x), stop the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Left and Right
    # pygame.K_LEFT => left arrow key
    if keys[pygame.K_LEFT]:  lr = -speed
    if keys[pygame.K_RIGHT]: lr =  speed

    # Forward and Backward
    # pygame.K_UP => up arrow key
    if keys[pygame.K_UP]:    fb =  speed
    if keys[pygame.K_DOWN]:  fb = -speed

    # Up and Down
    # pygame.K_w => W key
    if keys[pygame.K_w]: ud =  speed
    if keys[pygame.K_s]: ud = -speed

    # Rotation
    # pygame.K_a => A key
    if keys[pygame.K_a]: yv = -speed
    if keys[pygame.K_d]: yv =  speed

    # Takeoff
    # pygame.K_e => E key
    if keys[pygame.K_e]:
        print("Takeoff")
        tello.takeoff()

    # Land
    # pygame.K_q => Q key
    if keys[pygame.K_q]:
        print("Land")
        tello.land()
        time.sleep(1)

    tello.send_rc_control(lr, fb, ud, yv)
    time.sleep(0.03)

pygame.quit()