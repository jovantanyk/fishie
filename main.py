import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Swimming Fish")
clock = pygame.time.Clock()

background_image = pygame.image.load('background.jpg').convert()
background_width = background_image.get_width()

num_tiles = (screen_width // background_width) + 2

class Fish:
    def __init__(self, x, y, image_path):
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.rect = self.image.get_rect(center=(x, y))
        except Exception as e:
            print(f"Error loading image: {e}")
            sys.exit(1)

        print("Image loaded successfully")
        print(f"Fish position: {self.rect.x}, {self.rect.y}")

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

fish = Fish(screen_width // 2,  screen_height // 2, 'fish.png')

background_offset = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fish.move()

    # Scroll the background
    background_offset -= 2  # Move background left to simulate rightward movement
    if background_offset < -background_width:
        background_offset += background_width

    # Clear the screen
    screen.fill((0, 100, 255))

    # Draw the repeating background
    for i in range(num_tiles):
        screen.blit(background_image, (i * background_width + background_offset, 0))

    screen.blit(fish.image, fish.rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
