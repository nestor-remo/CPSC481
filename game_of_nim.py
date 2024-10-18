from games import *
    
class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""
    
    def __init__(self, board=[3, 1]):

        moves = []
        for row in range(len(board)):
            for i in range(1, board[row] + 1):
                moves.append((row, i))

        self.initial = GameState(to_move='MAX', utility=0, board=board, moves=moves)

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves
    

    def result(self, state, move):
        """Return the state that results from making a move from a state."""
        if move not in state.moves:
            return state
        board = state.board.copy()
        board[move[0]] -= move[1]

        new_moves = [(i, j) for i in range(len(board)) 
                     for j in range(1, board[i] + 1)]

        next_player = 'MIN' if state.to_move == 'MAX' else 'MAX'
        
        return GameState(to_move=next_player, utility=self.utility(state, state.to_move), board=board, moves=new_moves)

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        if player == 'MAX' and len(state.moves) == 0:
            return 1
        elif player == 'MIN' and len(state.moves) == 0:
            return -1
        else:
            return 0

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        if len(state.moves) == 0:
            return True
        else:
            return False

    def display(self, state):
        board = state.board
        print("board: ", board)

if __name__ == "__main__":
    #nim = GameOfNim(board=[0, 5, 3, 1])  # Creating the game instance
    nim = GameOfNim(board=[7, 5, 3, 1])  # a much larger tree to search
    print(nim.initial.board)  # must be [0, 5, 3, 1]
    print(nim.initial.moves)  # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1, 3)))
    utility = nim.play_game(alpha_beta_player, query_player)  # computer moves first
    if utility < 0:
        print("MIN won the game")
    else:
        print("MAX won the game")
