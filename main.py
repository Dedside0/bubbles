import tkinter as tk
import random
from PIL import Image, ImageTk

W, H = 1600, 800
bubbles = {}
pil_img = Image.open("bbl.png")
score = 0
speed = 3

win = tk.Tk()
win.title("Лопни пузыри")
win.geometry(f"{W}x{H}")

canvas = tk.Canvas(win, width=W, height=H)
score_label = tk.Label(win, text="Лопнуто: 0", font=("Arial", 25))
score_label.pack(side="top", fill="x")
canvas.pack(side="top", fill="both", expand=True)
    
def pop(e, bubble_id):
    global score
    if bubble_id in bubbles:
        score += 1
        canvas.delete(bubble_id)
        del bubbles[bubble_id]
        score_label.config(text=f"Лопнуто: {score}")
        print(f"Счет: {score}")
    
def spawn_bubble():
    size = random.randint(40, 150) 
    resized_img = pil_img.resize((size, size))
    img = ImageTk.PhotoImage(resized_img)
    x, y = random.randint(0, W - size), H + size
    img_id = canvas.create_image(x, y, image=img)
    bubbles[img_id] = img
    
    canvas.tag_bind(img_id, "<Button-1>", lambda e, b_id=img_id: pop(e, b_id))
    win.after(300, spawn_bubble)

def fly():
    for b_id in list(bubbles.keys()):
        canvas.move(b_id, 0, -speed)
        x, y = canvas.coords(b_id)
        if y < -100:
            del bubbles[b_id]
            canvas.delete(b_id)
    win.after(16, fly)


spawn_bubble()
fly()
win.mainloop()

