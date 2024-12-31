import tkinter as tk
import random
from PIL import Image, ImageTk
from select import select


def animate_images():
    global current
    canvas.itemconfig(image_on_canvas, image = image_sequence[current])
    current = (current + 1)%len(image_sequence)
    window.after(20, animate_images)

def stop_coin():
    canvas.delete("all")
    sides = [side1_entry.get(), side2_entry.get()]
    selection = random.randrange(0,2)
    if selection == 0:
        canvas.create_image(500, 450, image=image_sequence[0])
    elif selection == 1:
        canvas.create_image(500, 450, image=image_sequence[4])
    selection_label = tk.Label(text = sides[selection])
    selection_label.config(font=("Arial", 20), fg="red")
    selection_label.grid(column= 1, row=0)

window = tk.Tk()
window.title("Flipping coin")
window.minsize(width=800, height=800)

text_label = tk.Label(text = "Definitive decision making tool")
text_label.config(font=("Arial", 30, "bold") )
text_label.grid(column= 0, row = 0)

text_label1 = tk.Label(text = "One side")
text_label1.config(font=("Arial", 20))
text_label1.grid(column= 0, row = 1)

side1_entry = tk.Entry()
side1_entry.insert(0, "Head")
side1_entry.config(width=75, font=("Arial", 15),highlightthickness= 1)
side1_entry.grid(column= 0, row = 2)

text_label2 = tk.Label(text = "The other side")
text_label2.config(font=("Arial", 20))
text_label2.grid(column= 0, row = 4)

side2_entry = tk.Entry()
side2_entry.insert(0, "Tail")
side2_entry.config(width=75, font=("Arial", 15), highlightthickness= 1)
side2_entry.grid(column= 0, row = 5)

canvas = tk.Canvas()

turn_button = tk.Button(text ="Flip the coin", command=animate_images)
turn_button.config(font=("Arial",15))
turn_button.grid(column= 0, row = 6)

stop_button = tk.Button(text ="Stop the coin", command=stop_coin)
stop_button.config(font=("Arial",15))
stop_button.grid(column= 1, row = 6)

spacer = tk.Label(text ="  ")
spacer.grid(column= 0, row = 7)
spacer = tk.Label(text ="  ")
spacer.grid(column= 0, row = 8)

canvas = tk.Canvas(window, width=900,height=900)
image_sequence = []
frames = ["coin1.png", "coin2.png", "coin3.png", "coin4.png", "coin5.png" ]
for path in frames:
    img = Image.open(path).resize((500,450))
    photo = ImageTk.PhotoImage(img)
    image_sequence.append(photo)
current = 0
image_on_canvas = canvas.create_image(500,450, image = image_sequence[current])
canvas.grid(column= 1, row = 0, rowspan=6)

window.mainloop()