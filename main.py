# import mp3_to_wav
from tkinter import *
import text_sum as t
import wav_to_txt as w
# import yt_to_mp3
from tkinter import *


import tkinter as tk


def submit_form():
    src = name_entry.get()
    type = type_var.get()
    if type == ("file_name"):
        import file_to_final
    else:
        import url_to_final


root = tk.Tk()
root.title("Data Collection Form")
root.geometry("300x300")

name_label = tk.Label(root, text="Enter URL or file name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()


type_label = tk.Label(root, text="URL or File name:")
type_label.pack()

type_var = tk.StringVar()
type_var.set("URL")

file_radio = tk.Radiobutton(root, text="File name",
                            variable=type_var, value="file_name")
file_radio.pack()

url_radio = tk.Radiobutton(root, text="URL", variable=type_var, value="url")
url_radio.pack()

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

root.mainloop()
