from tkinter import *
from tkinter import messagebox
import os, re, os.path
import shutil


top = Tk()
top.title("Cleaner App")
top.minsize(280,100)


def removeFolder():
	path = "C:/Users/dell/AppData/Local/Temp"
	try:
		shutil.rmtree(path,ignore_errors=True, onerror=None)
		messagebox.showinfo("Task Completed","Temporary folder successfully removed")
	except:
		messagebox.showwarning("Warning","Error Occur")

def cleanFiles():
	path = "C:/Users/dell/AppData/Local/Temp"
	try:
		for root, dirs, files in os.walk(path):
			for file in files:
				os.remove(os.path.join(root, file))
		messagebox.showinfo("Task Completed","Temporary files successfully removed")
	except:
		messagebox.showwarning("Warning","Error Occur")


L = Label(top, text = "Clean Folder", width = 25, height = 3).grid(row = "1", column = "0")
B = Button(top,text = "clean", command = removeFolder).grid(row = "1", column = "3")

L = Label(top, text = "Clean Files", width = 25, height = 3).grid(row = "3", column = "0")
B = Button(top,text = "clean", command = cleanFiles).grid(row = "3", column = "3")


top.mainloop()