import tkinter as tk
import tkinter.messagebox as tkm

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん") #練習1

    canv = tk.Canvas(root, height=900, width=1500, bg="black")
    canv.pack() #練習2

    tori = tk.PhotoImage(file="Ex03/fig/3.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori") #練習3

    key="" #練習4

    root.mainloop()