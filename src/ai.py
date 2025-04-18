# ai.py
from copy import deepcopy
from move import Move

piece_values = {
    'pawn': 1,
    'knight': 3,
    'bishop': 3,
    'rook': 5,
    'queen': 9,
    'king': 1000
}

def evaluate_board(board, color):
    score = 0
    for row in board.squares:
        for square in row:
            if square.has_piece():
                piece = square.piece
                value = piece_values.get(piece.name, 0)
                if piece.color == color:
                    score += value
                else:
                    score -= value
    return score

def get_best_ai_move(board, color):
    best_score = float('-inf')
    best_move = None
    best_piece = None

    for row_idx in range(8):
        for col_idx in range(8):
            square = board.squares[row_idx][col_idx]
            if square.has_piece() and square.piece.color == color:
                piece = square.piece
                board.calc_moves(piece, row_idx, col_idx, bool=False)

                for move in piece.moves:
                    # simulate move on a deep copy of board
                    temp_board = deepcopy(board)
                    temp_piece = temp_board.squares[row_idx][col_idx].piece
                    temp_board.move(temp_piece, move)

                    score = evaluate_board(temp_board, color)
                    if score > best_score:
                        best_score = score
                        best_move = move
                        best_piece = piece

    return best_piece, best_move
