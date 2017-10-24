import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit_me():
    tk.messagebox.showinfo(title='OK', message='OK')   # return 'ok'
    # tk.messagebox.showwarning(title='warning', message='warning')   # return 'ok'
    # tk.messagebox.showerror(title='Hi', message='No!! never')   # return 'ok'
    # print(tk.messagebox.askquestion(title='Askquestion', message='Y/N'))   # return 'yes' , 'no'
    # print(tk.messagebox.askyesno(title='askyesno', message='askyesno'))   # return True, False
    # print(tk.messagebox.asktrycancel(title='asktrycancel', message='asktrycancel'))   # return True, False
    # print(tk.messagebox.askokcancel(title='askokcancel', message='askokcancel'))   # return True, False
    # print(tk.messagebox.askyesnocancel(title="askyesnocancel", message="askyesnocancel"))     # return, True, False, None

tk.Button(window, text='hit me', command=hit_me).pack()
window.mainloop()