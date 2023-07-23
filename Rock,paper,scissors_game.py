import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", "blue"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "Congratulations, you win!", "green"
    else:
        return "Computer wins! Better luck next time.", "red"

def on_button_click(user_choice):
    global user_score, computer_score

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    result, color = determine_winner(user_choice, computer_choice)
    result_text.config(text=result, fg=color)

    if color == "green":
        user_score += 1
    elif color == "red":
        computer_score += 1

    update_score()

def update_score():
    score_label.config(text=f"Your Score: {user_score}   Computer Score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score, computer_score = 0, 0
    update_score()
    result_text.config(text="", fg="black")

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x300")

user_score, computer_score = 0, 0

user_choice_label = tk.Label(root, text="Choose: Rock, Paper, or Scissors")
user_choice_label.pack(pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

rock_button = tk.Button(buttons_frame, text="Rock", command=lambda: on_button_click("rock"))
rock_button.pack(side=tk.LEFT, padx=5)

paper_button = tk.Button(buttons_frame, text="Paper", command=lambda: on_button_click("paper"))
paper_button.pack(side=tk.LEFT, padx=5)

scissors_button = tk.Button(buttons_frame, text="Scissors", command=lambda: on_button_click("scissors"))
scissors_button.pack(side=tk.LEFT, padx=5)

result_text = tk.Label(root, text="", font=("Arial", 16))
result_text.pack(pady=20)

score_label = tk.Label(root, text="Your Score: 0   Computer Score: 0", font=("Arial", 12))
score_label.pack()

reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.pack(pady=10)

root.mainloop()
