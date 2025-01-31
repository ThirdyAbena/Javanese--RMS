import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk

# Create the main window
root = ttk.Window(themename = 'darkly')
root.geometry('1920x1080')
# Set window background to transparent (works only on Windows)


# Create a canvas widget
canvas = tk.Canvas(root, width=400, height=400,  bg='white', bd=0, highlightthickness=0)
canvas.pack()

# Open an image using PIL
image = Image.open("C:/Users/Windows 10/Documents/Python/1_Final Projects/PUP_re1.png")
resized_image = image.resize((200, 200))
photo = ImageTk.PhotoImage(image)

# Place the image on the canvas
canvas.create_image(200, 200, image=photo)

# Run the Tkinter event loop
root.mainloop()