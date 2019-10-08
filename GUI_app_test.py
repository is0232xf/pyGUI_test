# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:37:54 2019

@author: FujiiChang
"""

import tkinter

root = tkinter.Tk()

root.title("demo window")
root.geometry("400x400")

label = tkinter.Label(root, text = "This is a test.")
label.grid()
root.mainloop()
