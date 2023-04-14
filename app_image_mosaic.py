import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    # 画像を読み込んでモザイク変換
    newImage = PIL.Image.open(path).convert("L").resize((32, 32)).resize((300, 300), resample = 0)
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()

    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text = "ファイルを開く", command = openFile)
imageLabel = tk.Label(text = "ここに画像が表示される")
btn.pack()
imageLabel.pack()
tk.mainloop()