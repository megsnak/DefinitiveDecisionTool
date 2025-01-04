import tkinter as tk
import random
from PIL import Image, ImageTk


def animate_images():
    global current, is_animating
    if is_animating:
        canvas.itemconfig(image_on_canvas, image = image_sequence[current])
        current = (current + 1)%len(image_sequence)
        window.after(20, animate_images)

def stop_coin():
    global is_animating
    is_animating = False
    sides = [side1_entry.get(), side2_entry.get()]
    selection = random.randrange(0,2)
    # if selection == 0:
    #     canvas.create_image(500, 450, image=image_sequence[0])
    # elif selection == 1:
    #     canvas.create_image(500, 450, image=image_sequence[4])
    selected_image = image_sequence[0] if selection == 0 else image_sequence[4]
    canvas.itemconfig(image_on_canvas, image=selected_image) # Update image on canvas
    selection_label.config(text= sides[selection], font=("Arial", 20), fg="red")
    return selection_label

def start_coin():
    global is_animating
    selection_label.config(text=" ")
    if not is_animating:
        is_animating= True
        animate_images()
    if not side1_entry.get():
        side1_entry.insert(0, "Head")
    if not side2_entry.get():
        side2_entry.insert(0,"Tail")

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

turn_button = tk.Button(text ="Flip the coin", command=start_coin)
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
is_animating = False # Animation Flag
image_on_canvas = canvas.create_image(500,450, image = image_sequence[current])
canvas.grid(column= 1, row = 0, rowspan=6)

selection_label = tk.Label(text=" ", font=("Arial", 20))
selection_label.grid(column=1, row=0)

window.mainloop()