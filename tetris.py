import pygame
import random
import pygame.transform

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 600
WINDOW_SIZE = (WIDTH, HEIGHT)
GRID_SIZE = 30
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tetrominoes
tetrominoes = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]]
]

# Tetromino colors
tetromino_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (128, 0, 128)]

# Initialize the game window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tetris")

# Game variables
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
current_tetromino = None
current_tetromino_color = None
x, y = 0, 0

# Functions

def rotate_tetromino():
    global current_tetromino
    current_tetromino = [list(row) for row in zip(*current_tetromino[::-1])]


def draw_grid():
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if grid[row][col]:
                pygame.draw.rect(screen, tetromino_colors[grid[row][col] - 1],
                                 pygame.Rect(col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
    for row in range(len(current_tetromino)):
        for col in range(len(current_tetromino[row])):
            if current_tetromino[row][col]:
                pygame.draw.rect(screen, current_tetromino_color,
                                 pygame.Rect((x + col) * GRID_SIZE, (y + row) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)

def new_tetromino():
    global current_tetromino, current_tetromino_color, x, y
    current_tetromino = random.choice(tetrominoes)
    current_tetromino_color = random.choice(tetromino_colors)
    x = GRID_WIDTH // 2 - len(current_tetromino[0]) // 2
    y = 0

def collide():
    for row in range(len(current_tetromino)):
        for col in range(len(current_tetromino[row])):
            if current_tetromino[row][col]:
                if x + col < 0 or x + col >= GRID_WIDTH or y + row >= GRID_HEIGHT or grid[y + row][x + col]:
                    return True
    return False

def place_tetromino():
    for row in range(len(current_tetromino)):
        for col in range(len(current_tetromino[row])):
            if current_tetromino[row][col]:
                grid[y + row][x + col] = tetromino_colors.index(current_tetromino_color) + 1

def check_lines():
    full_lines = []
    for row in range(GRID_HEIGHT):
        if all(grid[row]):
            full_lines.append(row)
    for row in full_lines:
        del grid[row]
        grid.insert(0, [0] * GRID_WIDTH)

# Main game loop
clock = pygame.time.Clock()
new_tetromino()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                if collide():
                    x += 1
            if event.key == pygame.K_RIGHT:
                x += 1
                if collide():
                    x -= 1
            if event.key == pygame.K_DOWN:
                y += 1
                if collide():
                    y -= 1
            if event.key == pygame.K_UP:  # Rotate the Tetromino when the UP arrow key is pressed
                rotate_tetromino()
                if collide():
                    rotate_tetromino()

    y += 1
    if collide():
        y -= 1
        place_tetromino()
        check_lines()
        new_tetromino()
        if collide():
            game_over = True

    screen.fill(WHITE)
    draw_grid()
    pygame.display.update()
    clock.tick(5)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                if collide():
                    x += 1
            if event.key == pygame.K_RIGHT:
                x += 1
                if collide():
                    x -= 1
            if event.key == pygame.K_DOWN:
                y += 1
                if collide():
                    y -= 1
            if event.key == pygame.K_UP:  # Rotate the Tetromino when the UP arrow key is pressed
                rotate_tetromino()
                if collide():
                    rotate_tetromino()




pygame.quit()
