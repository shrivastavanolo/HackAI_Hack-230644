
# Import the required packages
import tkinter as tk

# Create a root window
def warn_mssg(text):
    root = tk.Tk()
    root.geometry("300x100")
    root.resizable(False, False)
    root.title=("EXTREME TEMPERATURE WARNING")
    label=tk.Label(root,text=text)
    label.pack(ipadx=10,ipady=50)
    # Start the main loop
    root.mainloop()