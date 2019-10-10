# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:21:36 2019

@author: FujiiChang
"""

import os
import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import make_a_word_list
import search_on_weblio

def ask_folder():
    # ref button action
    path = filedialog.askdirectory()
    folder_path.set(path)


def app():
    # OK button action
    input_file = []
    max_level = int(order_maxlevel.get())
    min_level = int(order_minlevel.get())
    check = bln.get()
    sort = True
    
    if check is False:
        sort = True
    
    if min_level > max_level:
        messagebox.showinfo("Error", "min level > max level")
        return
    
    input_dir = folder_path.get()
    # select pdf file name(save as ...)
    """
    path = filedialog.asksaveasfilename(
        filetypes=[("text", "*.txt")], defaultextension=".txt"
    )
    
    if not input_dir or not path:
        return
    """
    # execute
    for file in os.listdir(input_dir):
        input_file.append(file)
        
    path2 = filedialog.asksaveasfilename(
        filetypes=[("text", "*.txt")], title="Save as", defaultextension=".txt"
    )
    
    word_list = make_a_word_list.make_list(input_dir, input_file)
    result = search_on_weblio.search_on_weblio(word_list, int(min_level), int(max_level), sort)
    
    output_file = open(path2, "w")
    for word in result:
        line = str(word[0])+", " + str(word[1]) + ", " + str(word[2]) + "\n"
        b = line.encode('cp932', 'ignore')
        trans_txt = b.decode('cp932')
        output_file.write(trans_txt)
    output_file.close()
        
    # message box
    messagebox.showinfo("Finish", "Finish join")

# main window
main_win = tkinter.Tk()
main_win.title("En-to-Ja Word minner")
main_win.geometry("500x130")

# main framel
main_frm = ttk.Frame(main_win)
main_frm.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)

folder_path = tkinter.StringVar()
# widget(folder path)
folder_label = ttk.Label(main_frm, text="Path")
folder_box = ttk.Entry(main_frm, textvariable=folder_path)
folder_btn = ttk.Button(main_frm, text="Ref", command=ask_folder)

# widget(select level(max))
value = list(range(20))
order_maxlabel = ttk.Label(main_frm, text="max level")
order_maxlevel = ttk.Combobox(main_frm, values=value, width=10)
order_maxlevel.current(0)

# widget(select level(min))
order_minlabel = ttk.Label(main_frm, text="min level")
order_minlevel = ttk.Combobox(main_frm, values=value, width=10)
order_minlevel.current(0)

bln = tkinter.BooleanVar()
bln.set(True)
check_box = tkinter.Checkbutton(main_frm, variable=bln, text="Sort")

# widget（execute button）
app_btn = ttk.Button(main_frm, text="OK", command=app)

# configuration of widget
folder_label.grid(column=0, row=0, pady=10)
folder_box.grid(column=1, row=0, sticky=tkinter.EW, padx=5)
folder_btn.grid(column=2, row=0)
order_minlabel.grid(column=0, row=1)
order_minlevel.grid(column=1, row=1, sticky=tkinter.W, padx=5)
order_maxlabel.grid(column=0, row=2)
order_maxlevel.grid(column=1, row=2, sticky=tkinter.W, padx=5)
check_box.grid(column=0, row=3)
app_btn.grid(column=1, row=3)

# set up cinfiguration
main_win.columnconfigure(0, weight=1)
main_win.rowconfigure(0, weight=1)
main_frm.columnconfigure(1, weight=1)

main_win.mainloop()