from games import *

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""
    def __init__(self, board=[3,1]):

        moves = []
        for row in range(len(board)):
            for amount in range(1, board[row] + 1):
                moves.append((row, amount))

        self.initial = GameState(to_move='MAX', utility=0, board=board, moves=moves)

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves

    def result(self, state, move):
        """Return the state that results from making a move from a state."""
        newBoard = state.board.copy()
        newBoard[move[0]] -= move[1]

        new_moves = []
        for row in range(len(newBoard)):
            for amount in range(1, newBoard[row] + 1):
                new_moves.append((row, amount))

        next_player = ("MIN" if state.to_move == "MAX" else "MAX")
        
        return GameState(to_move=next_player, utility=self.utility(state, state.to_move), board=newBoard, moves=new_moves)

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        if state.to_move == player:
            return 1
        else:
            return -1

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        if len(state.moves) == 0:
            return True
        else:
            return False

    def display(self, state):
        board = state.board
        print(board)

if __name__ == "__main__":
    nim = GameOfNim([7, 5, 3, 1])
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")