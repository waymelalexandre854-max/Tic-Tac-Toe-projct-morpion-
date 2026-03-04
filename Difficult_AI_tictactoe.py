"""AI difficult tictactoe"""
"""This AI work with minmax function and study the best play to win."""


def difficult_AI(Grid):
    from random import choice        #choice from random give us a possibility from all possible one, resulting to a hazardous play
    from Recurring_function import verifgame, create_new_Grid        #verifgame verify if there is a win or not and create_new_Grid make a new form of the grid to avoid any issue

    def available_moves(g):        #give all the potential place where it's possible to play in the form of a list of tuple
        return [(r, c) for r in range(3) for c in range(3) if g[r][c] == 0]

    def minmax(grid, player, depth=0):        #This is the minmax function that minimize the maximum lost
        winner = verifgame(grid)
        if winner != 0:        #if there is a direct win or lose, return the score (+/- 1000 + the depth of the move)
            return (1000 - depth) if winner == 2 else (-1000 + depth)

        
        moves = available_moves(grid)        #generate all the possible move available
        if moves == []:        #end condition
            return 0
        
        if player == 2: 
            best = -1000000000000000000000000000000        #a way to have a really low value for the best value on player 2 (AI player)
            for r, c in moves:        #tree loop of recursive until a solution is found
                new_grid = create_new_Grid(grid)        #make a new grid that will be modify and input in the recursive
                new_grid[r][c] = player
                score = minmax(new_grid, 1, depth + 1)
                if score > best:        #when the final score return, it verify what is the best value possible (depending on the player)
                    best = score
            return best
        else:
            best = 1000000000000000000000000000000        #a way to have a really high value for the best value on player 1 (real player)
            for r, c in moves:        #tree loop of recursive until a solution is found
                new_grid = create_new_Grid(grid)        #make a new grid that will be modify and input in the recursive
                new_grid[r][c] = player
                score = minmax(new_grid, 2, depth + 1)
                if score < best:        #when the final score return, it verify what is the best value possible (depending on the player)
                    best = score
            return best

    best_value = -1000000000000000000000000000000        #the best score we have for the next move
    play_list = []        #list of all possible move

    for i in range(9):
        if i == 0 or i == 1 or i == 2:        #choose the row and the column to try minmax
            r = 0
            c = i
        elif i == 3 or i == 4 or i == 5:
            r = 1
            c = i-3
        elif i == 6 or i == 7 or i == 8
            r = 2
            c = i-6
        if Grid[r][c] != 0:
            continue
        trial = create_new_Grid(Grid)        #create and try to see if an action is good or not.
        trial[r][c] = 2
        score = minmax(trial, 1, 1)
        if score > best_value:        #take from all result which one have the best score
            best_value = score
            play_list = [i + 1]
        elif score == best_value:        #make the whole list of possible move
            play_list.append(i + 1)


    return choice(play_list)
