import random
import sys

import pygame

# ---------- Settings ----------
CELL = 20                 # size of one grid cell in pixels
COLS, ROWS = 30, 20       # grid size
WIDTH, HEIGHT = CELL * COLS, CELL * ROWS
FPS = 10                  # game speed (higher = faster)

BLACK = (20, 20, 20)
GREEN = (50, 200, 80)
DARK_GREEN = (30, 140, 50)
RED = (220, 50, 50)
WHITE = (240, 240, 240)

KEYS = {
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
}

# ---------- Setup ----------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 24)
big_font = pygame.font.SysFont("consolas", 48)


def random_food(snake):
    """Pick a random cell that is not on the snake."""
    while True:
        pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        if pos not in snake:
            return pos


def draw_cell(pos, color):
    x, y = pos
    pygame.draw.rect(screen, color, (x * CELL, y * CELL, CELL - 1, CELL - 1))


def draw_text(text, fnt, color, center):
    surface = fnt.render(text, True, color)
    screen.blit(surface, surface.get_rect(center=center))


def reset():
    """Start a new game: snake in the middle, moving right."""
    cx, cy = COLS // 2, ROWS // 2
    snake = [(cx, cy), (cx - 1, cy), (cx - 2, cy)]
    return snake, (1, 0), random_food(snake), 0


def main():
    snake, direction, food, score = reset()
    next_direction = direction
    game_over = False

    while True:
        # ---- 1. Handle input ----
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if game_over and event.key == pygame.K_SPACE:
                    snake, direction, food, score = reset()
                    next_direction = direction
                    game_over = False
                elif event.key in KEYS:
                    new_dir = KEYS[event.key]
                    # block reversing directly into yourself
                    if new_dir != (-direction[0], -direction[1]):
                        next_direction = new_dir

        # ---- 2. Update game ----
        if not game_over:
            direction = next_direction
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])

            hit_wall = not (0 <= new_head[0] < COLS and 0 <= new_head[1] < ROWS)
            hit_self = new_head in snake[:-1]

            if hit_wall or hit_self:
                game_over = True
            else:
                snake.insert(0, new_head)
                if new_head == food:
                    score += 1
                    food = random_food(snake)   # grow: don't remove tail
                else:
                    snake.pop()                 # normal move

        # ---- 3. Draw ----
        screen.fill(BLACK)
        draw_cell(food, RED)
        for i, part in enumerate(snake):
            draw_cell(part, GREEN if i == 0 else DARK_GREEN)

        screen.blit(font.render(f"Score: {score}", True, WHITE), (10, 10))

        if game_over:
            draw_text("GAME OVER", big_font, RED, (WIDTH // 2, HEIGHT // 2 - 20))
            draw_text("Press SPACE to restart", font, WHITE, (WIDTH // 2, HEIGHT // 2 + 30))

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()