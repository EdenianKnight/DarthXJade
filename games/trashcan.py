import tkinter as tk
import random

# Game Constants
WIDTH, HEIGHT = 500, 500
TRASH_SIZE = 30
CAN_SIZE = 80
LEVELS = 6

# Initialize Window
root = tk.Tk()
root.title("TrashCan")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# Trash Can Setup
can = canvas.create_rectangle(WIDTH//2 - CAN_SIZE//2, HEIGHT - CAN_SIZE, WIDTH//2 + CAN_SIZE//2, HEIGHT, fill="green")

# Trash Setup
trashes = []
level = 1
speed = 5
trash_count = 1
score = 0

# Spawn Trash
def spawn_trash():
    for _ in range(trash_count):
        x_pos = random.randint(0, WIDTH - TRASH_SIZE)
        trash = canvas.create_oval(x_pos, 0, x_pos + TRASH_SIZE, TRASH_SIZE, fill="brown")
        trashes.append(trash)
    root.after(1500, spawn_trash)  # Spawn new trash every 1.5 seconds

# Move Trash
def move_trash():
    global score, level, speed, trash_count
    for trash in trashes[:]:
        canvas.move(trash, 0, speed)
        if canvas.coords(trash)[1] > HEIGHT:
            canvas.delete(trash)
            trashes.remove(trash)
        elif canvas.coords(trash)[1] + TRASH_SIZE >= canvas.coords(can)[1]:
            if canvas.coords(can)[0] <= canvas.coords(trash)[0] <= canvas.coords(can)[2]:
                score += 1
                canvas.delete(trash)
                trashes.remove(trash)
    
    # Level Up
    if score > 0 and score % 10 == 0 and level < LEVELS:
        level += 1
        speed += 1
        trash_count += 1
    root.after(50, move_trash)

# Move Trash Can
def move_left(event):
    if canvas.coords(can)[0] > 0:
        canvas.move(can, -20, 0)

def move_right(event):
    if canvas.coords(can)[2] < WIDTH:
        canvas.move(can, 20, 0)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# Start Game
spawn_trash()
move_trash()
root.mainloop()
