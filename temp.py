import tkinter as tk

win = tk.Tk()
""" tao 1 bien va luu cua so vao do """
win.geometry("500x400")  # kick thuoc cua so

# win.title('minhthanh dep con me no trai')

# ten = tk.Label(master=win, text="minh thanh dep trai")

# ten.pack(expand=True)

# frame_1= tk.Frame(win,width=500,height=100,relief='solid',borderwidth=1,background="blue")

# frame_1.pack()

win.config(background="blue")

win.grid_columnconfigure(index=0, weight=1)
win.grid_columnconfigure(index=1, weight=1)
win.grid_columnconfigure(index=2, weight=1)
"""chia thanh 3 cot"""

win.grid_rowconfigure(index=0, weight=1)
win.grid_rowconfigure(index=1, weight=2)
win.grid_rowconfigure(index=2, weight=1)

frame_1 = tk.Frame(win, width=500 / 3, height=400 / 4, borderwidth=3, relief="solid")

frame_1_tittle = tk.Label(master=frame_1, text="minh Thanh", font=("Arial", 12, "bold"))
frame_1_tittle.pack_propagate(False)
frame_1_tittle.pack()
frame_1.grid(row=0, column=2)

win.mainloop()
