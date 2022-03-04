import tkinter as tk
import random


def color(ndex):
    button_label_list[ndex][1].config(bg="#%06x" % random.randint(0, 16777215))


def dump():
    global count, button_label_list
    button_label_list.append([tk.Button(frame, text="color", ),
                              tk.Label(frame, text="Color")])
    button_label_list[-1][0].grid(row=count, column=0, sticky='nsew')

    frame.rowconfigure(count,weight=1)
    count += 1


root = tk.Tk()

count = 0
button_label_list = []
root.title("Hello")
root.rowconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

frame = tk.Frame(root)
frame.rowconfigure(1, weight=1)
frame.grid(row=0, column=2, sticky='nsew', rowspan=2)

tk.Button(root, text="butt ON", command=dump).grid(row=count+1, column=0, sticky='nsew')
tk.Button(root, text="Quit!", command=root.quit).grid(row=0, column=count+1)


root.mainloop()