import tkinter as tk
import text_sum as t
import wav_to_txt as w
root = tk.Tk()
root.title("Final Text")
root.geometry("400x400")
text = w.get_txt("testwav.wav")
final_sum = t.summ(text)
text_label = tk.Label(root, text=final_sum)
text_label.pack()

root.mainloop()
