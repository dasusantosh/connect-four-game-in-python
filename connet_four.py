import tkinter as tk

ROWS, COLS = 6, 7
EMPTY = " "
RED = "R"
YELLOW = "Y"

def create_board():
    return [[EMPTY]*COLS for _ in range(ROWS)]

def valid_move(board, col):
    return board[0][col] == EMPTY

def make_move(board, col, color):
    for row in reversed(board):
        if row[col] == EMPTY:
            row[col] = color
            return

def game_won(board, color):
    for row in range(ROWS):
        for col in range(COLS-3):
            if board[row][col] == color and all(board[row][col+i] == color for i in range(4)):
                return True

    for col in range(COLS):
        for row in range(ROWS-3):
            if board[row][col] == color and all(board[row+i][col] == color for i in range(4)):
                return True

    for row in range(ROWS-3):
        for col in range(COLS-3):
            if board[row][col] == color and all(board[row+i][col+i] == color for i in range(4)):
                return True

    for row in range(3, ROWS):
        for col in range(COLS-3):
            if board[row][col] == color and all(board[row-i][col+i] == color for i in range(4)):
                return True

    return False

class ConnectFour(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Connect Four")
        self.geometry("700x600")
        self.board = create_board()
        self.configure(bg='sky blue')
        self.current_player = RED
        self.game_over = False
        self.heading_label = tk.Label(self, text="CONNECT FOUR GAME", font=("Goudy Old Style", 16,'bold'),bg='sky blue',fg='black')
        self.heading_label.grid(row=0, column=0, columnspan=COLS)
        self.buttons = [tk.Button(self, command=lambda col=col: self.make_move(col), width=10, height=2) for col in range(COLS)]
        for col, button in enumerate(self.buttons):
            button.grid(row=1, column=col)
        self.restart_button = tk.Button(self, text="NEW GAME", command=self.restart)
        self.restart_button.grid(row=ROWS+3, column=COLS//2)
        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=ROWS+4, column=0, columnspan=COLS)
        self.update()

    def make_move(self, col):
        if not self.game_over and valid_move(self.board, col):
            make_move(self.board, col, self.current_player)
            self.game_over = game_won(self.board, self.current_player)
            if self.game_over:
                winner = "Red" if self.current_player == RED else "Yellow"
                self.result_label.config(text=f"{winner} has won the match!", font=("Goudy Old Style", 14), fg='red')
            self.current_player = YELLOW if self.current_player == RED else RED
            self.update()

    def restart(self):
        self.board = create_board()
        self.current_player = RED
        self.game_over = False
        self.result_label.config(text="")
        self.update()

    def update(self):
        for row in range(ROWS):
            for col in range(COLS):
                color = "red" if self.board[row][col] == RED else "yellow" if self.board[row][col] == YELLOW else "white"
                label = tk.Label(self, text=self.board[row][col], bg=color, width=10, height=2, relief="groove")
                label.grid(row=row+2, column=col)

if __name__ == "__main__":
    ConnectFour().mainloop()