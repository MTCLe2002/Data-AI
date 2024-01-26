import tkinter as tk
from tkinter import messagebox 

win = tk.Tk()

win.geometry('500x400')

win.config(background="blue")

win.title("Giao Dien Guide")

def callBack():
    message = messagebox.showwarning(title='cảnh báo', message = "vui lòng nhập lại")
    
def yesorno():
    answer = messagebox.askyesno(tittle="lựa chọn",message="bạn có muốn thoát ?")
    
button_yesorno = tk.Button(master=win,text="error", command=yesorno)