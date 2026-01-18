import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Flight Simulator")

# Colors
WHITE = (255, 255, 255)

# Load assets
plane_img = pygame.image.load("assets/plane.png")
plane_img = pygame.transform.scale(plane_img, (80, 50))  # Resize the plane
cloud_img = pygame.image.load("assets/cloud.png")
background_img = pygame.image.load("assets/background.png")

# Background dimensions
bg_width = background_img.get_width()
bg_height = background_img.get_height()

# Plane properties
plane = pygame.Rect(WIDTH // 2 - 40, HEIGHT - 100, 80, 50)  # Start on the ground (bottom of the screen)
plane_rotation = 0
thrust = 0.4
lift = -0.6
drag = 0.01
gravity = 0.5
MAX_SPEED = 628  # Max horizontal speed in the game (B2 Bomber max speed)

horizontal_speed = 0
vertical_speed = 0
camera_offset_x = 0
camera_offset_y = 0

# Cloud settings
clouds = []
for _ in range(10):
    cloud_x = random.randint(0, WIDTH * 2)
    cloud_y = random.randint(50, HEIGHT - 150)
    clouds.append(pygame.Rect(cloud_x, cloud_y, 70, 50))

# Font for HUD
font = pygame.font.Font(None, 36)
hud_color = WHITE

# Game clock
clock = pygame.time.Clock()

# Game variables
distance = 0
altitude = 0
on_ground = True  # This flag ensures the plane starts on the ground

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get input
    keys = pygame.key.get_pressed()

    # Handle movement mechanics
    if on_ground:
        # Plane is on the ground; it cannot move vertically but can move horizontally
        if keys[pygame.K_RIGHT]:  # Increase forward speed
            horizontal_speed += thrust
        elif keys[pygame.K_LEFT]:  # Decrease forward speed
            horizontal_speed -= thrust

        # Apply drag to horizontal movement
        if horizontal_speed > 0:
            horizontal_speed -= drag
        elif horizontal_speed < 0:
            horizontal_speed += drag

        # Clamp horizontal speed to prevent extreme values
        horizontal_speed = max(0, min(MAX_SPEED, horizontal_speed))  # Clamp to MAX_SPEED

        # Update camera offset (simulate forward movement)
        camera_offset_x += horizontal_speed

        # Check takeoff condition
        if horizontal_speed > 4 and keys[pygame.K_UP]:  # Sufficient speed + lift key pressed
            on_ground = False  # Enable flight
            vertical_speed = lift * 2  # Apply initial lift
            plane_rotation = -15
    else:
        # In flight mechanics
        if keys[pygame.K_RIGHT]:  # Increase forward speed in the air
            horizontal_speed += thrust
        elif keys[pygame.K_LEFT]:  # Decrease forward speed in the air
            horizontal_speed -= thrust

        if keys[pygame.K_UP]:  # Tilt upward
            vertical_speed += lift
            plane_rotation = -15
        elif keys[pygame.K_DOWN]:  # Tilt downward
            vertical_speed -= lift
            plane_rotation = 15
        else:
            vertical_speed += gravity  # Apply gravity
            plane_rotation = 0

        # Apply drag to horizontal speed (slows plane during flight)
        if horizontal_speed > 0:
            horizontal_speed -= drag
        elif horizontal_speed < 0:
            horizontal_speed += drag

        # Clamp horizontal speed to MAX_SPEED
        horizontal_speed = max(0, min(MAX_SPEED, horizontal_speed))

        # Update vertical speed limits
        vertical_speed = max(-8, min(8, vertical_speed))  # Limit vertical speed

        # Update camera offset (simulate forward movement in flight)
        camera_offset_x += horizontal_speed
        camera_offset_y += vertical_speed  # Enable vertical scrolling after takeoff

    # Transition plane from bottom to center after takeoff
    if not on_ground:
        if plane.y > HEIGHT // 2 - plane.height // 2:  # Move the plane upward to center
            plane.y += vertical_speed
        else:
            plane.y = HEIGHT // 2 - plane.height // 2  # Keep it centered after reaching the middle
            camera_offset_y += vertical_speed  # Start moving the camera offset

    # Prevent altitude from going below 0 (ground level)
    if on_ground:
        plane.y = HEIGHT - plane.height - 50  # Keep plane at the bottom before takeoff
    if camera_offset_y > 0:
        camera_offset_y = 0  # Reset camera at ground level
        vertical_speed = 0  # Stop downward movement at ground level

    # Draw moving background (camera scrolls)
    for x in range(-1, 2):  # Infinite scrolling horizontally
        for y in range(-1, 2):  # Infinite scrolling vertically
            bg_x = (x * bg_width) - (camera_offset_x % bg_width)
            bg_y = (y * bg_height) - (camera_offset_y % bg_height)
            screen.blit(background_img, (bg_x, bg_y))

    # Draw the plane, either on the ground or centered
    rotated_plane = pygame.transform.rotate(plane_img, plane_rotation)
    screen.blit(rotated_plane, plane)

    # Update and draw clouds (relative to the camera)
    for cloud in clouds:
        cloud_world_x = cloud.x - camera_offset_x
        cloud_world_y = cloud.y - camera_offset_y

        if -100 < cloud_world_x < WIDTH + 100 and -100 < cloud_world_y < HEIGHT + 100:
            screen.blit(cloud_img, (cloud_world_x, cloud_world_y))

        # Recycle clouds that go offscreen
        if cloud_world_x < -100:
            cloud.x = random.randint(int(camera_offset_x), int(camera_offset_x) + 800)
            cloud.y = random.randint(50, HEIGHT - 150)

    # HUD information
    altitude = -camera_offset_y
    distance = camera_offset_x
    speed_text = font.render(f"Speed: {int(horizontal_speed)}", True, hud_color)
    altitude_text = font.render(f"Altitude: {int(max(altitude, 0))}", True, hud_color)
    distance_text = font.render(f"Distance: {int(distance)}", True, hud_color)

    # Render HUD
    screen.blit(speed_text, (10, 10))
    screen.blit(altitude_text, (10, 40))
    screen.blit(distance_text, (10, 70))

    pygame.display.flip()
    clock.tick(60)  # Limit FPS

pygame.quit()
sys.exit()