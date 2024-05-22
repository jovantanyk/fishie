import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Swimming Fish")
clock = pygame.time.Clock()

# Load and scale the background image
background_image = pygame.image.load('background.jpg').convert()
background_width = background_image.get_width()

# Calculate how many times the background needs to be repeated
num_tiles = (screen_width // background_width) + 2  # +2 to ensure full coverage

class Fish:
    def __init__(self, x, y, image_path, mass=1.0):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(x, y))
        self.mass = mass
        self.net_force = 10  # Initial net force in Newtons
        self.velocity = 0  # Initial velocity in m/s

    def update_physics(self):
        # Calculate acceleration from F = ma
        acceleration = self.net_force / self.mass
        # Update velocity
        self.velocity += acceleration * (1/60)  # Update velocity based on frame rate
        # Update horizontal position based on velocity
        self.rect.x += self.velocity * (1/60)  # Convert velocity to displacement per frame

    def modify_resistance(self, change):
        self.net_force += change  # Increment or decrement net force based on resistance change

# Instantiate the fish centered horizontally
fish = Fish(screen_width // 2, screen_height // 2, 'fish.png')

background_offset = 0  # Initial background position

font = pygame.font.Font(None, 36)  # Font for displaying text

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        fish.modify_resistance(-1)  # Increase resistance, decrease net force
    if keys[pygame.K_DOWN]:
        fish.modify_resistance(1)  # Decrease resistance, increase net force

    # Update fish physics
    fish.update_physics()

    # Scroll the background proportional to fish velocity
    background_offset -= fish.velocity
    if background_offset < -background_width:
        background_offset += background_width

    # Clear the screen
    screen.fill((0, 100, 255))

    # Draw the repeating background
    for i in range(num_tiles):
        screen.blit(background_image, (i * background_width + background_offset, 0))

    # Draw the fish at the center
    screen.blit(fish.image, fish.rect)

    # Display the speed and net force counters
    speed_text = font.render(f"Speed: {fish.velocity:.2f} m/s", True, (255, 255, 255))
    force_text = font.render(f"Net Force: {fish.net_force} N", True, (255, 255, 255))
    screen.blit(speed_text, (10, 10))
    screen.blit(force_text, (10, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
