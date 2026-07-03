import pygame
import sys
import math

pygame.init()

# Window settings
WIDTH, HEIGHT = 600, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe AI")

# Colors
BACKGROUND = (20, 25, 45)
GRID_COLOR = (220, 230, 255)
X_COLOR = (255, 100, 120)
O_COLOR = (90, 210, 255)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (80, 120, 220)
BUTTON_HOVER = (110, 150, 255)

FONT = pygame.font.SysFont("arial", 32, bold=True)
SMALL_FONT = pygame.font.SysFont("arial", 22, bold=True)

CELL_SIZE = 200
BOARD_HEIGHT = 600

board = [" " for _ in range(9)]
game_over = False
winner = None
ai_thinking = False
animation_marks = []


def draw_board():
    SCREEN.fill(BACKGROUND)

    # Title
    title = FONT.render("TIC-TAC-TOE AI", True, TEXT_COLOR)
    SCREEN.blit(title, (WIDTH // 2 - title.get_width() // 2, 620))

    # Grid lines
    for i in range(1, 3):
        pygame.draw.line(
            SCREEN, GRID_COLOR,
            (i * CELL_SIZE, 20),
            (i * CELL_SIZE, BOARD_HEIGHT - 20),
            5
        )
        pygame.draw.line(
            SCREEN, GRID_COLOR,
            (20, i * CELL_SIZE),
            (WIDTH - 20, i * CELL_SIZE),
            5
        )

    # Draw X and O with growing animation
    for index, mark, progress in animation_marks:
        row = index // 3
        col = index % 3
        center_x = col * CELL_SIZE + CELL_SIZE // 2
        center_y = row * CELL_SIZE + CELL_SIZE // 2

        size = int(65 * min(progress, 1))

        if mark == "X":
            pygame.draw.line(
                SCREEN, X_COLOR,
                (center_x - size, center_y - size),
                (center_x + size, center_y + size),
                10
            )
            pygame.draw.line(
                SCREEN, X_COLOR,
                (center_x + size, center_y - size),
                (center_x - size, center_y + size),
                10
            )

        elif mark == "O":
            pygame.draw.circle(SCREEN, O_COLOR, (center_x, center_y), size, 10)

    # Result message
    if game_over:
        if winner == "X":
            message = "You Win! Amazing!"
        elif winner == "O":
            message = "AI Wins!"
        else:
            message = "It's a Draw!"

        result = FONT.render(message, True, TEXT_COLOR)
        SCREEN.blit(result, (WIDTH // 2 - result.get_width() // 2, 620))

        draw_restart_button()


def draw_restart_button():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    button_rect = pygame.Rect(220, 650, 160, 40)

    color = BUTTON_HOVER if button_rect.collidepoint(mouse_x, mouse_y) else BUTTON_COLOR
    pygame.draw.rect(SCREEN, color, button_rect, border_radius=12)

    text = SMALL_FONT.render("Play Again", True, TEXT_COLOR)
    SCREEN.blit(
        text,
        (button_rect.centerx - text.get_width() // 2,
         button_rect.centery - text.get_height() // 2)
    )


def check_winner(current_board):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if current_board[a] == current_board[b] == current_board[c] != " ":
            return current_board[a]

    if " " not in current_board:
        return "Draw"

    return None


# Minimax AI algorithm
def minimax(current_board, is_maximizing):
    result = check_winner(current_board)

    if result == "O":
        return 1
    elif result == "X":
        return -1
    elif result == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if current_board[i] == " ":
                current_board[i] = "O"
                score = minimax(current_board, False)
                current_board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if current_board[i] == " ":
                current_board[i] = "X"
                score = minimax(current_board, True)
                current_board[i] = " "
                best_score = min(score, best_score)

        return best_score


def best_ai_move():
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


def add_mark(index, mark):
    board[index] = mark
    animation_marks.append([index, mark, 0])


def reset_game():
    global board, game_over, winner, animation_marks, ai_thinking

    board = [" " for _ in range(9)]
    game_over = False
    winner = None
    animation_marks = []
    ai_thinking = False


clock = pygame.time.Clock()

while True:
    clock.tick(60)

    # Update animation progress
    for item in animation_marks:
        if item[2] < 1:
            item[2] += 0.08

    draw_board()
    pygame.display.update()

    # AI move after human move
    if ai_thinking and not game_over:
        pygame.time.delay(350)

        move = best_ai_move()
        if move is not None:
            add_mark(move, "O")

        ai_thinking = False
        winner = check_winner(board)

        if winner is not None:
            game_over = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Restart button
            if game_over:
                restart_rect = pygame.Rect(220, 650, 160, 40)
                if restart_rect.collidepoint(mouse_x, mouse_y):
                    reset_game()

            # Human move
            elif not ai_thinking and mouse_y < BOARD_HEIGHT:
                col = mouse_x // CELL_SIZE
                row = mouse_y // CELL_SIZE
                index = row * 3 + col

                if board[index] == " ":
                    add_mark(index, "X")

                    winner = check_winner(board)
                    if winner is not None:
                        game_over = True
                    else:
                        ai_thinking = True