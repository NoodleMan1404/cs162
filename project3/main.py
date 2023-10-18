import tkinter as tk

class Oven:
    def __init__(self, door, preheat, timer):
        self.door = door
        self.preheat = preheat
        self.timer = timer

    def main(self):
        window = tk.Tk()
        text = tk.Label(
            text='Oven Model: 3000z',
            foreground='white',
            background='black',
            width=30,
            height=30
        )
        text.pack()
        window.mainloop()

test_oven = Oven('Closed', '0', 0)

test_oven.main()