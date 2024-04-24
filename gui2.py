import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My GUI App")

# Add a label widget
label = tk.Label(root, text="Hello, World!")
label.pack()  # pack the label into the window

# Define a function for the button click
def click_event():
  print("Button clicked!")

# Add a button widget
button = tk.Button(root, text="Click Me", command=click_event)
button.pack()

# Run the main event loop
root.mainloop()
