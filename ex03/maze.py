import tkinter as tk
import tkinter.messagebox as tkm

#練習5
def key_down(event):
    global key
    key = event.keysym

#練習6
def key_up(event):
    global key
    key = ""

#練習7
def main_proc():
    global cx, cy
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Right":
        cx += 20
    if key == "Left":
        cx -= 20
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    
    #練習1
    root = tk.Tk()
    root.title("迷えるこうかとん") 
    
    #練習2
    canv = tk.Canvas(root, height=900, width=1500, bg="black")
    canv.pack()
    
    #練習3
    tori = tk.PhotoImage(file="Ex03/fig/3.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori")
    
    #練習4
    key=""
    
    #練習5
    root.bind("<KeyPress>", key_down)
    #練習⑥
    root.bind("<KeyRelease>", key_up)

    #練習7
    main_proc()


    root.mainloop()