import tkinter as tk
from datetime import datetime


def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)


# Create window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x200")
root.resizable(False, False)

# Heading
title_label = tk.Label(
    root,
    text="Digital Clock",
    font=("Arial", 24)
)
title_label.pack(pady=20)

# Time display
time_label = tk.Label(
    root,
    text="00:00:00",
    font=("Arial", 50)
)
time_label.pack()

# Start updating the clock
update_time()

# Run the application
root.mainloop()

