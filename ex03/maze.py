import tkinter as tk
import tkinter.messagebox as tkm
#練習8
import maze_maker as mm

#練習5
def key_down(event):
    global key
    key = event.keysym

#練習6
def key_up(event):
    global key
    key = ""

#練習7、11,12
def main_proc():
    global cx, cy
    global mx, my
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Right":
        mx += 1
    if key == "Left":
        mx -= 1
    if maze_lst[my][mx] == 0:
        cx, cy = mx*100+50, my*100+50
    else:
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Right":
            mx -= 1
        if key == "Left":
            mx += 1
    canv.coords("tori", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    
    #練習1
    root = tk.Tk()
    root.title("迷えるこうかとん") 
    
    #練習2
    canv = tk.Canvas(root, height=900, width=1500, bg="black")
    canv.pack()
    
    #練習3、11
    tori = tk.PhotoImage(file="Ex03/fig/3.png")
    mx, my = 1, 1
    cx, cy = mx*100, my*100
    
    #練習4
    key=""
    
    #練習5
    root.bind("<KeyPress>", key_down)
    #練習⑥
    root.bind("<KeyRelease>", key_up)

    #練習9
    maze_lst = mm.make_maze(15, 9)
    
    #練習7
    main_proc()

    #練習3,10
    mm.show_maze(canv, maze_lst)
    canv.create_image(cx, cy, image=tori, tag="tori")

    root.mainloop()