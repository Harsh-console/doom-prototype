# Chess board with turn-based play and castling (simplified: no check/checkmate/en passant).
# Uppercase = white pieces, lowercase = black pieces.

import pygame
import sys

# Constants
TILE_SIZE = 80
BOARD_SIZE = 8
WIDTH, HEIGHT = TILE_SIZE * BOARD_SIZE, TILE_SIZE * BOARD_SIZE
WHITE = (240, 217, 181)
BROWN = (181, 136, 99)
HIGHLIGHT = (0, 255, 0, 100)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess with Castling & Turn")
font = pygame.font.SysFont(None, 44)

chess_board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p'] * 8,
    [' '] * 8,
    [' '] * 8,
    [' '] * 8,
    [' '] * 8,
    ['P'] * 8,
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
]

selected_pos = None
possible_moves = []
turn = 'white'  # white starts
castling_rights = {
    'white_king': True,
    'white_kingside': True,
    'white_queenside': True,
    'black_king': True,
    'black_kingside': True,
    'black_queenside': True,
}

def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            color = WHITE if (row + col) % 2 == 0 else BROWN
            pygame.draw.rect(screen, color, rect)

            piece = chess_board[row][col]
            if piece != ' ':
                color = (0, 0, 0) if piece.islower() else (255, 255, 255)
                text = font.render(piece.upper(), True, color)
                screen.blit(text, (col * TILE_SIZE + 25, row * TILE_SIZE + 20))

    for move in possible_moves:
        row, col = move
        highlight_rect = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
        highlight_rect.fill(HIGHLIGHT)
        screen.blit(highlight_rect, (col * TILE_SIZE, row * TILE_SIZE))

def is_inside_board(row, col):
    return 0 <= row < 8 and 0 <= col < 8

def get_moves_for_piece(row, col):
    piece = chess_board[row][col]
    if piece == ' ':
        return []

    color = 'white' if piece.isupper() else 'black'
    if color != turn:
        return []

    piece_type = piece.lower()
    directions = []

    if piece_type == 'p':
        moves = []
        step = -1 if color == 'white' else 1
        start_row = 6 if color == 'white' else 1

        if is_inside_board(row + step, col) and chess_board[row + step][col] == ' ':
            moves.append((row + step, col))
            if row == start_row and chess_board[row + 2*step][col] == ' ':
                moves.append((row + 2*step, col))

        for dc in [-1, 1]:
            r, c = row + step, col + dc
            if is_inside_board(r, c):
                target = chess_board[r][c]
                if target != ' ' and target.isupper() != piece.isupper():
                    moves.append((r, c))
        return moves

    elif piece_type == 'r':
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    elif piece_type == 'b':
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    elif piece_type == 'q':
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]
    elif piece_type == 'n':
        moves = []
        jumps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                 (1, -2), (1, 2), (2, -1), (2, 1)]
        for dr, dc in jumps:
            r, c = row + dr, col + dc
            if is_inside_board(r, c):
                target = chess_board[r][c]
                if target == ' ' or target.isupper() != piece.isupper():
                    moves.append((r, c))
        return moves

    elif piece_type == 'k':
        moves = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r, c = row + dr, col + dc
                if is_inside_board(r, c):
                    target = chess_board[r][c]
                    if target == ' ' or target.isupper() != piece.isupper():
                        moves.append((r, c))

        # Castling
        if color == 'white' and row == 7 and col == 4 and castling_rights['white_king']:
            if castling_rights['white_kingside']:
                if chess_board[7][5] == ' ' and chess_board[7][6] == ' ':
                    moves.append((7, 6))
            if castling_rights['white_queenside']:
                if chess_board[7][1] == ' ' and chess_board[7][2] == ' ' and chess_board[7][3] == ' ':
                    moves.append((7, 2))
        if color == 'black' and row == 0 and col == 4 and castling_rights['black_king']:
            if castling_rights['black_kingside']:
                if chess_board[0][5] == ' ' and chess_board[0][6] == ' ':
                    moves.append((0, 6))
            if castling_rights['black_queenside']:
                if chess_board[0][1] == ' ' and chess_board[0][2] == ' ' and chess_board[0][3] == ' ':
                    moves.append((0, 2))
        return moves

    moves = []
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while is_inside_board(r, c):
            target = chess_board[r][c]
            if target == ' ':
                moves.append((r, c))
            else:
                if target.isupper() != piece.isupper():
                    moves.append((r, c))
                break
            r += dr
            c += dc
    return moves

def move_piece(from_row, from_col, to_row, to_col):
    global turn
    piece = chess_board[from_row][from_col]
    target = chess_board[to_row][to_col]

    # Handle castling rook move
    if piece.lower() == 'k' and abs(to_col - from_col) == 2:
        if to_col == 6:  # kingside
            chess_board[to_row][5] = chess_board[to_row][7]
            chess_board[to_row][7] = ' '
        elif to_col == 2:  # queenside
            chess_board[to_row][3] = chess_board[to_row][0]
            chess_board[to_row][0] = ' '

    # Clear castling rights if king or rook moves
    if piece == 'K':
        castling_rights['white_king'] = False
    elif piece == 'k':
        castling_rights['black_king'] = False
    elif piece == 'R' and from_row == 7 and from_col == 0:
        castling_rights['white_queenside'] = False
    elif piece == 'R' and from_row == 7 and from_col == 7:
        castling_rights['white_kingside'] = False
    elif piece == 'r' and from_row == 0 and from_col == 0:
        castling_rights['black_queenside'] = False
    elif piece == 'r' and from_row == 0 and from_col == 7:
        castling_rights['black_kingside'] = False

    chess_board[to_row][to_col] = piece
    chess_board[from_row][from_col] = ' '

    # Switch turn
    turn = 'black' if turn == 'white' else 'white'

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    draw_board()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = x // TILE_SIZE
            row = y // TILE_SIZE

            if selected_pos:
                if (row, col) in possible_moves:
                    move_piece(*selected_pos, row, col)
                selected_pos = None
                possible_moves = []
            else:
                if chess_board[row][col] != ' ':
                    selected_pos = (row, col)
                    possible_moves = get_moves_for_piece(row, col)
                else:
                    selected_pos = None
                    possible_moves = []

    clock.tick(1000)
    pygame.display.set_caption(str(clock.get_fps()))

pygame.quit()
sys.exit()

