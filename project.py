import tkinter as tk
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title("move wasd")
root.geometry("600x400")

canvas = tk.Canvas(root, width=600, height=400, bg="lightblue")
canvas.pack()

image_file = "/Users/djrangas/Documents/Github/demo.png"

if not os.path.exists(image_file):
    print("File not found:", image_file)
    root.destroy()

img = Image.open(image_file)
img = img.resize((50, 50))
player_image = ImageTk.PhotoImage(img)

player = canvas.create_image(300, 200, image=player_image)

def move_up(event):
    canvas.move(player, 0, -10)

def move_down(event):
    canvas.move(player, 0, 10)

def move_left(event):
    canvas.move(player, -10, 0)

def move_right(event):
    canvas.move(player, 10, 0)

root.bind("w", move_up)
root.bind("s", move_down)
root.bind("a", move_left)
root.bind("d", move_right)

root.mainloop()
