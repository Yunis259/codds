import tkinter  as tk 
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(title="Open File",filetypes=[("Text","*.txt"),("ALL","*.*")])
    if file_path:
        global text_path
        text_path = file_path
        with open(file_path,'r')as f:
            textvar.set(str(f.read()))

def save_file():
    if text_path:
        with open(text_path,'w')as f:
            f.write(textvar.get())

window = tk.Tk()

textvar= tk.StringVar()

btn = tk.Button("Open file",command=open_file)
btn.pack()
eny= tk.Entry(textvar.get(),textvariable=textvar)
eny.pack()
btnsave= tk.Button(text="Save File",command=save_file)
btnsave.pack()
window.mainloop()