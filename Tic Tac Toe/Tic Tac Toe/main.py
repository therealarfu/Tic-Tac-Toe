import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 800, 600
board_size = 400
scoreboard_height = 100
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe")
pygame.display.set_icon(pygame.image.load('icon/x.png'))

white = (242, 242, 242)
black = (30, 30, 30)
screen.fill(black)

game = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]

wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6))

TURN = 2

score_x = 0
score_o = 0

font = pygame.font.SysFont('Consolas', 50)
board_y = 0

def checkVictory():
    global game, score_x, score_o, TURN
    for pos in wins:
        if game[pos[0]] == game[pos[1]] == game[pos[2]] and game[pos[0]] != 0:
            if game[pos[0]] == 1:
                score_o += 1
                game = [0, 0, 0, 0, 0, 0, 0, 0, 0].copy()
                TURN = 2
                return 'O won'
            else:
                score_x += 1
                game = [0, 0, 0, 0, 0, 0, 0, 0, 0].copy()
                TURN = 2
                return 'X won'

    for pos in game:
        if pos == 0:
            return 'Continue'

    game = [0, 0, 0, 0, 0, 0, 0, 0, 0].copy()
    return 'Draw'

def play(turn, pos):
    global game, TURN
    if game[pos] == 0:
        if turn == 1:
            game[pos] = 1
            TURN = 2
            pygame.display.set_icon(pygame.image.load('icon/x.png'))
        else:
            game[pos] = 2
            TURN = 1
            pygame.display.set_icon(pygame.image.load('icon/ball.png'))
    else:
        return 'Error'
    checkVictory()

def draw_board():
    cell_size = board_size // 3
    for row in range(3):
        for col in range(3):
            x = col * cell_size
            y = row * cell_size
            pygame.draw.rect(screen, white, (x + board_x, y + scoreboard_height + board_y, cell_size, cell_size), 2)
            if game[row * 3 + col] == 1:
                pygame.draw.circle(screen, white, (x + cell_size // 2 + board_x, y + cell_size // 2 + scoreboard_height + board_y), cell_size // 3, 2)
            elif game[row * 3 + col] == 2:
                pygame.draw.line(screen, white, (x + cell_size // 6 + board_x, y + cell_size // 6 + scoreboard_height + board_y),
                                 (x + cell_size - cell_size // 6 + board_x, y + cell_size - cell_size // 6 + scoreboard_height + board_y), 2)
                pygame.draw.line(screen, white, (x + cell_size - cell_size // 6 + board_x, y + cell_size // 6 + scoreboard_height + board_y),
                                 (x + cell_size // 6 + board_x, y + cell_size - cell_size // 6 + scoreboard_height + board_y), 2)

def draw_scoreboard():
    pygame.draw.rect(screen, black, (0, 0, screen_width, scoreboard_height))
    score_text = f"X: {score_x}   O: {score_o}"
    text_surface = font.render(score_text, True, white)
    text_rect = text_surface.get_rect(center=(screen_width // 2, scoreboard_height // 2))
    screen.blit(text_surface, text_rect)

def get_cell(mouse_pos):
    cell_size = board_size // 3
    row = (mouse_pos[1] - scoreboard_height - board_y) // cell_size
    col = (mouse_pos[0] - board_x) // cell_size
    return row, col

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if scoreboard_height + board_y <= mouse_pos[1] <= scoreboard_height + board_y + board_size:
                row, col = get_cell(mouse_pos)
                if game[row * 3 + col] == 0:
                    play(TURN, row * 3 + col)

    screen.fill(black)

    board_x = (screen_width - board_size) // 2
    board_y = (screen_height - board_size) // 2 - scoreboard_height

    draw_board()
    draw_scoreboard()

    pygame.display.flip()
