import pygame
from djitellopy import Tello
import time

pygame.init()
win = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Tello Keyboard Controller")

font = pygame.font.SysFont("Arial", 20)

# Connect to Tello
tello = Tello()
tello.connect()
battery = tello.get_battery()
print("Battery:", battery)

# Button class
class Button:
    def __init__(self, label, x, y, cmd):
        self.label = label
        self.x = x
        self.y = y
        self.cmd = cmd
        self.rect = pygame.Rect(x, y, 40, 40)

    def draw(self):
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()[0]

        # Hover highlight
        color = (100, 100, 100)
        if self.rect.collidepoint(mouse):
            color = (0, 120, 0)
            if clicked:
                self.execute()

        pygame.draw.rect(win, color, self.rect, border_radius=6)
        t = font.render(self.label, True, (255, 255, 255))
        win.blit(t, (self.x + 10, self.y + 8))

    def execute(self):
        print("Button:", self.label)
        self.cmd()

# Movement functions
speed = 50
is_stopped = True
def forward(): 
        tello.send_rc_control(0,  speed, 0, 0)

def stop(): 
    tello.send_rc_control(0, 0, 0, 0)

def backward(): 
    tello.send_rc_control(0, -speed, 0, 0)

def left(): 
    tello.send_rc_control(-speed, 0, 0, 0)

def right(): 
    tello.send_rc_control(speed,  0, 0, 0)

def up(): 
    tello.send_rc_control(0, 0, speed, 0)

def down(): 
    tello.send_rc_control(0, 0, -speed, 0)

def yaw_left(): 
    tello.send_rc_control(0, 0, 0, -speed)

def yaw_right(): 
    tello.send_rc_control(0, 0, 0,  speed)

def takeoff():
    global is_stopped

    # FULL STOP BEFORE TAKEOFF
    tello.send_rc_control(0,0,0,0)
    time.sleep(0.1)

    print("Takeoff starting...")

    tello.takeoff()

    # FULL STOP AFTER TAKEOFF (VERY IMPORTANT)
    tello.send_rc_control(0,0,0,0)

    is_stopped = True   # Reset toggle state
    print("Takeoff: STOP mode fully reset")


def land(): 
    tello.land()

# Create buttons
buttons = [
    Button("W", 180, 80, forward),
    Button("A", 130,130, left),
    Button("S", 180,130, stop),         # S now STOP
    Button("D", 230,130, right),
    Button("X", 180,180, backward),     # X now backward

    Button("UP", 180,230, up),
    Button("YL", 130,280, yaw_left),
    Button("DW", 180,280, down),
    Button("YR", 230,280, yaw_right),

    Button("E", 330, 80, takeoff),
    Button("Q", 330,130, land)
]

# Keyboard mapping
def handle_keyboard():
    keys = pygame.key.get_pressed()

    # STOP (S key)
    if keys[pygame.K_s]:
        print("STOP")
        stop()
        time.sleep(0.1)
        return

    # Backward (X key)
    if keys[pygame.K_x]:
        print("BACKWARD")
        backward()
        return

    # Normal movement keys
    if keys[pygame.K_w]:     forward()
    if keys[pygame.K_a]:     left()
    if keys[pygame.K_d]:     right()
    if keys[pygame.K_UP]:    up()
    if keys[pygame.K_DOWN]:  down()
    if keys[pygame.K_LEFT]:  yaw_left()
    if keys[pygame.K_RIGHT]: yaw_right()

    # Takeoff / Land
    if keys[pygame.K_e]:     takeoff()
    if keys[pygame.K_q]:     land()

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tello.end()
            pygame.quit()
            exit()

    win.fill((30, 30, 30))

    # Draw battery
    battery_text = font.render(f"Battery: {battery}%", True, (255, 255, 0))
    win.blit(battery_text, (10, 10))

    # Draw all buttons
    for b in buttons:
        b.draw()

    # Keyboard control
    handle_keyboard()

    pygame.display.update()
    time.sleep(0.05)
