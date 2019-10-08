# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:21:36 2019

@author: FujiiChang
"""

import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import merge_pdf

def ask_folder():
    # ref button action
    path = filedialog.askdirectory()
    folder_path.set(path)


def app():
    # OK button action
    is_reverse = order_comb.get() == "descending"
    input_dir = folder_path.get()
    # select pdf file name(save as ...)
    output_file = filedialog.asksaveasfilename(
        filetypes=[("PDF files", "*.pdf")], defaultextension=".pdf"
    )
    if not input_dir or not output_file:
        return
    # execute
    merge_pdf.merge_pdf_files(input_dir, output_file, is_reverse)
    # message box
    messagebox.showinfo("Finish")

folder_path = tkinter.StringVar()
# main window
main_win = tkinter.Tk()
main_win.title("En-to-Ja Word minner")
main_win.geometry("500x120")

# main frame
main_frm = ttk.Frame(main_win)
main_frm.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)

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