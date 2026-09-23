import random
import sys

import pygame

# ---------- Settings ----------
WIDTH, HEIGHT = 400, 600
FPS = 60
GRAVITY = 0.5          # how fast the bird falls
FLAP = -8              # jump strength (negative = up)
BIRD_SIZE = 30
PIPE_WIDTH = 70
PIPE_GAP = 160         # space between top and bottom pipe
PIPE_SPEED = 3
PIPE_EVERY = 90        # frames between new pipes

SKY = (120, 200, 240)
YELLOW = (250, 210, 40)
GREEN = (60, 180, 75)
WHITE = (255, 255, 255)
RED = (220, 50, 50)

# ---------- Setup ----------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 28)
big_font = pygame.font.SysFont("consolas", 48)


def draw_text(text, fnt, color, center):
    surface = fnt.render(text, True, color)
    screen.blit(surface, surface.get_rect(center=center))


def new_pipe():
    gap_y = random.randint(80, HEIGHT - 80 - PIPE_GAP)
    return {"x": WIDTH, "gap_y": gap_y, "scored": False}


def pipe_rects(pipe):
    top = pygame.Rect(pipe["x"], 0, PIPE_WIDTH, pipe["gap_y"])
    bottom_y = pipe["gap_y"] + PIPE_GAP
    bottom = pygame.Rect(pipe["x"], bottom_y, PIPE_WIDTH, HEIGHT - bottom_y)
    return top, bottom


def reset():
    return HEIGHT / 2, 0, [], 0, 0   # bird_y, velocity, pipes, score, frame


def main():
    bird_y, velocity, pipes, score, frame = reset()
    state = "ready"   # ready -> playing -> over

    while True:
        # ---- 1. Input ----
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pressed = (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) \
                or event.type == pygame.MOUSEBUTTONDOWN
            if pressed:
                if state == "over":
                    bird_y, velocity, pipes, score, frame = reset()
                    state = "ready"
                else:
                    state = "playing"
                    velocity = FLAP

        bird = pygame.Rect(80, int(bird_y), BIRD_SIZE, BIRD_SIZE)

        # ---- 2. Update ----
        if state == "playing":
            velocity += GRAVITY
            bird_y += velocity
            bird.y = int(bird_y)

            frame += 1
            if frame % PIPE_EVERY == 0:
                pipes.append(new_pipe())

            for pipe in pipes:
                pipe["x"] -= PIPE_SPEED
                top, bottom = pipe_rects(pipe)
                if bird.colliderect(top) or bird.colliderect(bottom):
                    state = "over"
                if not pipe["scored"] and pipe["x"] + PIPE_WIDTH < bird.x:
                    pipe["scored"] = True
                    score += 1

            pipes = [p for p in pipes if p["x"] + PIPE_WIDTH > 0]   # drop off-screen pipes

            if bird.top < 0 or bird.bottom > HEIGHT:
                state = "over"

        # ---- 3. Draw ----
        screen.fill(SKY)
        for pipe in pipes:
            for rect in pipe_rects(pipe):
                pygame.draw.rect(screen, GREEN, rect)
        pygame.draw.ellipse(screen, YELLOW, bird)

        draw_text(str(score), big_font, WHITE, (WIDTH // 2, 50))
        if state == "ready":
            draw_text("Press SPACE to flap", font, WHITE, (WIDTH // 2, HEIGHT // 2 + 80))
        elif state == "over":
            draw_text("GAME OVER", big_font, RED, (WIDTH // 2, HEIGHT // 2 - 20))
            draw_text("SPACE to restart", font, WHITE, (WIDTH // 2, HEIGHT // 2 + 30))

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()