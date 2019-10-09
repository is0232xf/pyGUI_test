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
    is_reverse = order_comb.get()
    input_dir = folder_path.get()
    # select pdf file name(save as ...)
    path = filedialog.asksaveasfilename(
        filetypes=[("text", "*.txt")], defaultextension=".txt"
    )
    
    if not input_dir or not path:
        return
    # execute
    for file in os.listdir(input_dir):
        input_file.append(file)
    word_list = make_a_word_list.make_list(input_dir, input_file)
    result = search_on_weblio.search_on_weblio(word_list)
    
    output_file = open(path, "w")
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
main_win.geometry("500x120")

# main framel
main_frm = ttk.Frame(main_win)
main_frm.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)

folder_path = tkinter.StringVar()
# widget(folder path)
folder_label = ttk.Label(main_frm, text="Path")
folder_box = ttk.Entry(main_frm, textvariable=folder_path)
folder_btn = ttk.Button(main_frm, text="Ref", command=ask_folder)

# widget(allignment sequence)
order_label = ttk.Label(main_frm, text="Sequence")
order_comb = ttk.Combobox(main_frm, values=["Ascending", "Descending"], width=10)
order_comb.current(0)

# widget（execute button）
app_btn = ttk.Button(main_frm, text="OK", command=app)

# configuration of widget
folder_label.grid(column=0, row=0, pady=10)
folder_box.grid(column=1, row=0, sticky=tkinter.EW, padx=5)
folder_btn.grid(column=2, row=0)
order_label.grid(column=0, row=1)
order_comb.grid(column=1, row=1, sticky=tkinter.W, padx=5)
app_btn.grid(column=1, row=2)

# set up cinfiguration
main_win.columnconfigure(0, weight=1)
main_win.rowconfigure(0, weight=1)
main_frm.columnconfigure(1, weight=1)

main_win.mainloop()