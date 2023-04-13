import tkinter as tk
import random

def dispLabel():
    kuji = ["大吉", "中吉", "末吉", "吉", "凶", "大吉"]
    lbl.configure(text=random.choice(kuji))

root = tk.Tk()
root.geometry("200x100")

lbl0 = tk.Label(text="クジの結果は...")
lbl = tk.Label(text="-")
btn = tk.Button(text="PUSH", command = dispLabel)

lbl0.pack()
lbl.pack()
btn.pack()
tk.mainloop()