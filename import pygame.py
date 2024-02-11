import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
PLAYER_SPEED = 5
PLAYER_JUMP = 10
ENEMY_SPEED = 3
PROJECTILE_SPEED = 8
ENEMY_SPAWN_RATE = 120  # Adjust as needed
MAX_HEALTH = 100
MAX_LIVES = 3

# Camera settings
camera_x = 0  # Initialize camera position
camera_speed = 2  # Adjust camera speed as needed

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Side-Scrolling Game")

# Load images
player_image = pygame.Surface((50, 50))
player_image.fill(RED)
enemy_image = pygame.Surface((50, 50))
enemy_image.fill(WHITE)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT // 2)
        self.health = MAX_HEALTH
        self.lives = MAX_LIVES

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        projectile = Projectile(self.rect.right, self.rect.centery)
        projectiles.add(projectile)
        all_sprites.add(projectile)

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH, HEIGHT // 2)

    def update(self):
        self.rect.x -= ENEMY_SPEED

# Projectile class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x += PROJECTILE_SPEED
        if self.rect.left > WIDTH:
            self.kill()  # Remove projectiles when they go off-screen

# Game loop
player = Player()
enemies = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

clock = pygame.time.Clock()
running = True
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Move the camera
    camera_x += camera_speed

    # Spawn enemies
    if random.randrange(ENEMY_SPAWN_RATE) == 0:
        enemy = Enemy()
        enemies.add(enemy)
        all_sprites.add(enemy)

    # Collision detection
    hits = pygame.sprite.groupcollide(enemies, projectiles, True, True)
    for hit in hits:
        score += 1
        enemy = Enemy()
        enemies.add(enemy)
        all_sprites.add(enemy)

    # Adjust the player's position based on camera movement
    player.rect.x -= camera_speed

    screen.fill((0, 0, 0))

    # Draw all sprites with adjusted positions
    for sprite in all_sprites:
        screen.blit(sprite.image, sprite.rect.move(-camera_x, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
