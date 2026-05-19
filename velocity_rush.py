import pygame
import random
import json

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Runner Final")

clock = pygame.time.Clock()

# Load assets
bg = pygame.image.load("WEB Sem2/bg.png").convert()

player_img = pygame.image.load("WEB Sem2/player1.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (120, 120))

player_jump = pygame.image.load("WEB Sem2/jump.png").convert_alpha()
player_jump = pygame.transform.scale(player_jump, (120, 120))

obstacle_img = pygame.image.load("WEB Sem2/obstacle.png").convert_alpha()
obstacle_img = pygame.transform.scale(obstacle_img, (70, 90))

coin_img = pygame.image.load("WEB Sem2/coin.png").convert_alpha()
coin_img = pygame.transform.scale(coin_img, (30, 30))

jump_sound = pygame.mixer.Sound("WEB Sem2/jump.wav")
coin_sound = pygame.mixer.Sound("WEB Sem2/coin.wav")
hit_sound = pygame.mixer.Sound("WEB Sem2/hit.wav")

player_rect = player_img.get_rect(midbottom=(80, 300))
player_hitbox = pygame.Rect(0, 0, 30, 45)
obstacles = []
coins = []

gravity = 0
score = 0
coin_count = 0
speed = 6

font = pygame.font.SysFont(None, 36)

bg_x = 0
game_active = True

try:
    with open("highscore.json", "r") as f:
        data = json.load(f)
        highscore = data["highscore"]
except:
    highscore = 0

def save_highscore(score):
    with open("highscore.json", "w") as f:
        json.dump({"highscore": score}, f)

class Obstacle:
    def __init__(self, img, speed):
        self.image = img
        self.rect = pygame.Rect(0, 0, 30, 45)
        self.rect.midbottom = (800, 265)
        self.speed = speed

        # random type
        self.type = random.choice(["normal", "fast"])

    def move(self):
        #polymorphism behavior
        if self.type == "normal":
            self.rect.x -= self.speed
        elif self.type == "fast":
            self.rect.x -= self.speed * 1.5   # faster obstacle

    def draw(self, screen):
        screen.blit(self.image, self.rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    gravity = -15
                    jump_sound.play()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                obstacles.clear()
                coins.clear() 
                player_rect.midbottom = (80, 300)
                gravity = 0
                score = 0
                coin_count = 0   
                speed = 6


    if game_active:
        # Background scroll
        bg_x -= 2
        if bg_x <= -WIDTH:
            bg_x = 0
        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (bg_x + WIDTH, 0))        

        # Player physics
        player_hitbox.midbottom = player_rect.midbottom

        gravity += 1
        player_rect.y += gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        player_hitbox.width = 30
        player_hitbox.height = 45
        player_hitbox.midbottom = player_rect.midbottom

        # Choose image (jump or run)
        if player_rect.bottom < 300:
            player_surface = player_jump
        else:
            player_surface = player_img

        # Spawn obstacles
        if len(obstacles) == 0 or obstacles[-1].rect.x < 500:
            if random.randint(1, 60) == 1:
                obstacles.append(Obstacle(obstacle_img, speed))

            if random.randint(1, 80) == 1:
                coin = coin_img.get_rect(midbottom=(800, 250))
                coins.append(coin)
            

        # Move obstacles
        for obstacle in obstacles:
            obstacle.move()

        for coin in coins:
            coin.x -= speed

        obstacles = [obs for obs in obstacles if obs.rect.x > -50]
        coins = [c for c in coins if c.x > -50]

        # Collision
        player_hitbox.center = player_rect.center

        for obstacle in obstacles:
            if player_hitbox.colliderect(obstacle.rect):
                hit_sound.play()
                if score > highscore:
                    highscore = score
                    save_highscore(highscore)
                game_active = False

        for coin in coins:
            if player_hitbox.colliderect(coin):
                coins.remove(coin)
                score += 50
                coin_count +=1
                coin_sound.play()
                
        # Draw
        screen.blit(player_surface, player_rect)
        for obstacle in obstacles:
            obstacle.draw(screen)

        for coin in coins:
            screen.blit(coin_img, coin)
 

        # Score + difficulty
        score += 1
        speed += 0.002

        score_surf = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_surf, (10, 10))

        high_surf = font.render(f"High Score: {highscore}", True, (0,0,0))
        screen.blit(high_surf, (10,70))

        coin_surf = font.render(f"Coins: {coin_count}", True, (0, 0, 0))
        screen.blit(coin_surf, (10, 40))

    else:
        screen.fill((255, 255, 255))
        text = font.render("GAME OVER - Press SPACE", True, (255, 0, 0))
        screen.blit(text, (200, 180))

    pygame.display.update()
    clock.tick(60)