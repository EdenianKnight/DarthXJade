import tkinter as tk
import random

# Game Constants
WIDTH, HEIGHT = 500, 500
PLAYER_SIZE = 50
ENEMY_SIZE = 50
ENEMY_SPEED = 5

# Initialize Window
root = tk.Tk()
root.title("Battlement")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# Player Setup
player = canvas.create_rectangle(WIDTH//2 - PLAYER_SIZE//2, HEIGHT - PLAYER_SIZE - 10,
                                 WIDTH//2 + PLAYER_SIZE//2, HEIGHT - 10, fill="blue")

# Enemy Setup
enemies = []
score = 0
running = True
score_text = canvas.create_text(50, 20, text=f"Score: {score}", font=("Arial", 16), fill="black")

def spawn_enemy():
    if running:
        x_pos = random.randint(0, WIDTH - ENEMY_SIZE)
        enemy = canvas.create_rectangle(x_pos, 0, x_pos + ENEMY_SIZE, ENEMY_SIZE, fill="red")
        enemies.append(enemy)
        root.after(1000, spawn_enemy)  # Spawn every second

# Move Enemies
def move_enemies():
    global running, score
    if running:
        for enemy in enemies:
            canvas.move(enemy, 0, ENEMY_SPEED)
            if canvas.coords(enemy)[1] > HEIGHT:
                canvas.delete(enemy)
                enemies.remove(enemy)
                score += 1
                canvas.itemconfig(score_text, text=f"Score: {score}")
            elif check_collision(player, enemy):
                game_over()
        root.after(50, move_enemies)

# Check Collision
def check_collision(player, enemy):
    px1, py1, px2, py2 = canvas.coords(player)
    ex1, ey1, ex2, ey2 = canvas.coords(enemy)
    return px1 < ex2 and px2 > ex1 and py1 < ey2 and py2 > ey1

# Game Over
def game_over():
    global running
    running = False
    canvas.create_text(WIDTH//2, HEIGHT//2, text="Game Over", font=("Arial", 24), fill="red")

# Player Movement
def move_left(event):
    if running and canvas.coords(player)[0] > 0:
        canvas.move(player, -20, 0)

def move_right(event):
    if running and canvas.coords(player)[2] < WIDTH:
        canvas.move(player, 20, 0)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# Start Game
spawn_enemy()
move_enemies()
root.mainloop()
