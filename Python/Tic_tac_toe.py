import tkinter as tk
from tkinter import Label, Button, messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # Modern color scheme
        self.bg_color = "#1a1a2e"
        self.primary_color = "#0f3460"
        self.accent_color = "#e94560"
        self.button_empty = "#16213e"
        self.button_x = "#00d4ff"
        self.button_o = "#ff6b6b"
        self.text_color = "#ffffff"
        
        self.root.config(bg=self.bg_color)

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        # Title
        self.title_label = Label(
            self.root, 
            text="TIC TAC TOE", 
            font=("Segoe UI", 32, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        )
        self.title_label.pack(pady=20)

        # Status label
        self.status_label = Label(
            self.root, 
            text=f"Player {self.current_player}'s turn", 
            font=("Segoe UI", 16),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.status_label.pack(pady=10)

        # Game grid frame
        self.grid_frame = tk.Frame(self.root, bg=self.bg_color)
        self.grid_frame.pack(pady=20)

        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(
                    self.grid_frame, 
                    text="", 
                    font=("Segoe UI", 28, "bold"), 
                    width=6, 
                    height=2,
                    bg=self.button_empty,
                    fg=self.text_color,
                    activebackground=self.primary_color,
                    activeforeground=self.text_color,
                    bd=0,
                    relief=tk.FLAT,
                    cursor="hand2",
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                self.buttons[row][col].grid(row=row, column=col, padx=8, pady=8)
                self.bind_hover(self.buttons[row][col])

        # Reset button
        self.reset_button = tk.Button(
            self.root, 
            text="Reset Game", 
            font=("Segoe UI", 12, "bold"),
            bg=self.accent_color,
            fg=self.text_color,
            activebackground="#ff4757",
            activeforeground=self.text_color,
            bd=0,
            relief=tk.FLAT,
            cursor="hand2",
            padx=30,
            pady=10,
            command=self.reset_game
        )
        self.reset_button.pack(pady=20)

    def bind_hover(self, button):
        button.bind("<Enter>", lambda e: self.on_enter(button))
        button.bind("<Leave>", lambda e: self.on_leave(button))

    def on_enter(self, button):
        if button.cget("text") == "":
            button.config(bg=self.primary_color)

    def on_leave(self, button):
        text = button.cget("text")
        if text == "":
            button.config(bg=self.button_empty)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            color = self.button_x if self.current_player == "X" else self.button_o
            self.buttons[row][col].config(text=self.current_player, fg=color, bg=self.button_empty)
            
            if self.check_winner():
                messagebox.showinfo("🎉 Tic Tac Toe", f"🏆 Player {self.current_player} wins! 🏆")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("🎮 Tic Tac Toe", "🤝 It's a draw! 🤝")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return True
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        
        return False

    def check_draw(self):
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))

    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", bg=self.button_empty, fg=self.text_color)
        self.status_label.config(text=f"Player {self.current_player}'s turn")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()