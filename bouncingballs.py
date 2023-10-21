import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls")

# Ball parameters
ball_radius = 20
balls = []

# Ball class
class Ball:
    def __init__(self, x, y, radius, color, x_speed, y_speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    def check_collision(self):
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.x_speed *= -1
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.y_speed *= -1

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Create initial balls with random colors
for _ in range(5):
    x = random.randint(ball_radius, WIDTH - ball_radius)
    y = random.randint(ball_radius, HEIGHT - ball_radius)
    x_speed = random.choice([-5, 5])
    y_speed = random.choice([-5, 5])
    color = random_color()
    ball = Ball(x, y, ball_radius, color, x_speed, y_speed)
    balls.append(ball)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill the screen with a black background

    for ball in balls:
        ball.move()
        ball.check_collision()
        ball.draw()

    pygame.display.update()
    pygame.time.delay(30)  # Adjust the delay for desired frame rate

pygame.quit()
