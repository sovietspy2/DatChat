import tkinter as tk
import tkinter.scrolledtext as tkst
import os
import time

f2 = open("me/chat.txt", "a")

def evaluate(event):
    editArea.configure(state='normal')
    #entry.get()
    editArea.insert(tk.INSERT,'YOU: '+entry.get()+'\n')
    input_field.set("")
    send(entry.get())
    editArea.configure(state='disabled')


win = tk.Tk()
frame1 = tk.Frame(
    master = win,
    bg = '#808000'
)
frame1.pack(fill='both', expand='yes')
editArea = tkst.ScrolledText(
    master = frame1,
    wrap   = tk.WORD,
    width  = 20,
    height = 10
)

win.title("DAT CHAT")
# Don't use widget.place(), use pack or grid instead, since
# They behave better on scaling the window -- and you don't
# have to calculate it manually!
editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
# Adding some text, to see if scroll is working as we expect it
editArea.insert(tk.INSERT, "messages are gonna be here!\n")
input_field = tk.StringVar()
tk.Label(win, text="Your message:").pack()
entry = tk.Entry(win,textvariable=input_field)
entry.bind("<Return>", evaluate)
entry.pack()
res = tk.Label(win)
res.pack()
win.geometry("500x500") #You want the size of the app to be 500x500
def load():
    try:
            if (os.stat("partner/chat.txt").st_size!=0):
                editArea.configure(state='normal')
                f = open("chat.txt",'r+')
                for line in f:
                    print(line)
                    editArea.insert(tk.INSERT,'PARTNER: '+line)
                editArea.configure(state='disabled')   
                f.seek(0)
                f.truncate()
                f.close()
    except Exception:
        time.sleep(1)
        load()

def send(text):
    f2.write(text+'\n')
    f2.flush()


#win.mainloop()
while True:
    win.update()
    load()






