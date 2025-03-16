import tkinter as tk

# List to store coordinates
coordinates = []

def show_coordinates(event):
    # Append tuple of x and y coordinates to the list
    coords = (event.x, event.y)
    coordinates.append(coords)
    # Update the label to show all coordinates
    label.config(text="Click coordinates: " + ", ".join(f"({x}, {y})" for x, y in coordinates))
    # Write coordinates to a file
    with open("click_coordinates.txt", "a") as file:
        file.write(f"{coords[0]}, {coords[1]}\n")

def toggle_fullscreen(event=None):
    root.attributes('-fullscreen', False)  # Exit full screen

def on_closing():
    # Optionally write all coordinates at once when the application is closed
    with open("click_coordinates.txt", "w") as file:
        for x, y in coordinates:
            file.write(f"{x}, {y}\n")
    root.destroy()

root = tk.Tk()
root.title("Transparent Click Window")

# Set full-screen and make the background partially transparent
root.attributes('-fullscreen', True)
root.attributes('-alpha', 0.0)  # Adjust transparency level: 0.0 (fully transparent) to 1.0 (opaque)

root.bind("<Escape>", toggle_fullscreen)

label = tk.Label(root, text="Click anywhere in this window", fg="black")
label.pack(expand=True, fill='both')
label.bind("<Button-1>", show_coordinates)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
