import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Flight Simulator")

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)

# Load the plane image
try:
    plane_img = pygame.image.load("assets/plane.png")
    plane_img = pygame.transform.scale(plane_img, (80, 50))  # Resize the plane
    print("✅ Loaded plane image successfully.")
except pygame.error:
    print("❌ Error: Failed to load 'plane.png'. Ensure it's in the 'assets/' directory.")
    sys.exit()

# Load the background image
try:
    background_img = pygame.image.load("assets/background.png")
    bg_width = background_img.get_width()
    bg_height = background_img.get_height()
    print(f"✅ Loaded background image successfully ({bg_width}x{bg_height}).")
except pygame.error:
    print("❌ Error: Failed to load 'background.png'. Ensure it's in the 'assets/' directory.")
    sys.exit()

# Plane properties
plane = pygame.Rect(WIDTH // 2 - 40, HEIGHT - 100, 80, 50)  # Plane starts near bottom center
horizontal_speed = 0
vertical_speed = 0
throttle = 50  # Initial throttle percentage (0–100)
landing_gear_deployed = True  # Start with landing gear deployed

# Max speed for B-2 Bomber in game-units
MAX_SPEED = 628  # B2 Bomber's real-world max speed (~628 mph)
DRAG = 0.02  # Air resistance slows down the plane gradually

# Clock and font for HUD
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# HUD data
altitude = HEIGHT - plane.y  # Relative to the bottom of the screen
bg_x_offset = 0
bg_y_offset = 0


# Function to display the HUD (Heads-Up Display)
def draw_hud():
    # Draw speed
    speed_text = font.render(f"Speed: {int(horizontal_speed)}", True, WHITE)
    screen.blit(speed_text, (10, 10))

    # Draw altitude
    altitude_text = font.render(f"Altitude: {int(altitude)}", True, WHITE)
    screen.blit(altitude_text, (10, 40))

    # Draw throttle
    throttle_text = font.render(f"Throttle: {int(throttle)}%", True, WHITE)
    screen.blit(throttle_text, (10, 70))

    # Draw landing gear status
    gear_status = "Deployed" if landing_gear_deployed else "Retracted"
    landing_gear_text = font.render(f"Landing Gear: {gear_status}", True, WHITE)
    screen.blit(landing_gear_text, (10, 100))


# Main game loop
running = True
print("Starting the game...")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Toggle landing gear with the 'L' key
        if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            landing_gear_deployed = not landing_gear_deployed

    # Key inputs
    keys = pygame.key.get_pressed()

    # Adjust throttle (Page Up / Page Down keys)
    if keys[pygame.K_PAGEUP]:
        throttle = min(100, throttle + 1)  # Increase throttle
    elif keys[pygame.K_PAGEDOWN]:
        throttle = max(0, throttle - 1)  # Decrease throttle

    # Move the plane (horizontal movement tied to throttle, vertical to keys)
    thrust = throttle / 100 * 15  # Throttle-to-thrust conversion
    if keys[pygame.K_RIGHT]:
        horizontal_speed += thrust
    elif keys[pygame.K_LEFT]:
        horizontal_speed -= thrust
    else:
        horizontal_speed -= horizontal_speed * DRAG  # Apply drag (air resistance)

    # Enforce maximum speed limit
    horizontal_speed = max(0, min(horizontal_speed, MAX_SPEED))  # Clamp horizontal speed

    # Handle vertical movement (Ascend/Descend)
    if keys[pygame.K_UP]:
        vertical_speed = -5  # Move visually upward
    elif keys[pygame.K_DOWN]:
        vertical_speed = 5  # Move visually downward
    else:
        vertical_speed = 0  # Stabilize vertical motion

    # Update position
    plane.y += vertical_speed
    bg_y_offset += vertical_speed
    altitude = HEIGHT - plane.y
    altitude = max(0, altitude)  # Prevent altitude from being negative

    bg_x_offset += horizontal_speed

    # Draw the scrolling background (tile seamlessly)
    screen.fill(BLUE)  # Fallback for the sky color
    for x in range(-1, 2):
        for y in range(-1, 2):
            bg_x = (x * bg_width) - (bg_x_offset % bg_width)
            bg_y = (y * bg_height) - (bg_y_offset % bg_height)
            screen.blit(background_img, (bg_x, bg_y))

    # Draw the plane
    screen.blit(plane_img, plane)

    # Draw the HUD
    draw_hud()

    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Cap FPS at 60
