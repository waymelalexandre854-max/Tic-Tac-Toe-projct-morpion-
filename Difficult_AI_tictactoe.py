"""AI difficult tictactoe"""
"""This AI should know his potential victory at every moment by looking three time of his action and two time the player action"""


def difficult_AI(Grid):
    from random import choice
    from Recurring_function import verifgame

    def copy_grid(g):
        return [row[:] for row in g]

    def available_moves(g):
        return [(r, c) for r in range(3) for c in range(3) if g[r][c] == 0]

    def minimax(grid, player, depth=0):
        winner = verifgame(grid)
        if winner != 0:
            return (1000 - depth) if winner == 2 else (-1000 + depth)

        moves = available_moves(grid)
        if not moves:
            return 0

        if player == 2:
            best = -float("inf")
            for r, c in moves:
                ng = copy_grid(grid)
                ng[r][c] = player
                score = minimax(ng, 1, depth + 1)
                if score > best:
                    best = score
            return best
        else:
            best = float("inf")
            for r, c in moves:
                ng = copy_grid(grid)
                ng[r][c] = player
                score = minimax(ng, 2, depth + 1)
                if score < best:
                    best = score
            return best

    best_score = -float("inf")
    candidates = []

    for i in range(9):
        r, c = divmod(i, 3)
        if Grid[r][c] != 0:
            continue
        trial = copy_grid(Grid)
        trial[r][c] = 2
        score = minimax(trial, 1, 1)
        if score > best_score:
            best_score = score
            candidates = [i + 1]
        elif score == best_score:
            candidates.append(i + 1)

    return choice(candidates) if candidates else None