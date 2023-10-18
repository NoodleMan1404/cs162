import tkinter as tk


root = tk.Tk()
root.title("Oven-Galor3000z")


def preheat_oven():
    status_label.config(text="Oven is preheating...")


def set_timer():
    timer_value = timer_entry.get()
    status_label.config(text=f"Timer set to {timer_value} minutes")


door_label = tk.Label(root, text="Door: Closed")
preheat_button = tk.Button(root, text="Preheat Oven", command=preheat_oven)
timer_label = tk.Label(root, text="Timer (minutes):")
timer_entry = tk.Entry(root)
set_timer_button = tk.Button(root, text="Set Timer", command=set_timer)
status_label = tk.Label(root, text="Status: Idle")


door_label.pack()
preheat_button.pack()
timer_label.pack()
timer_entry.pack()
set_timer_button.pack()
status_label.pack()


root.mainloop()