import tkinter as tk
import tkinter.messagebox as tkm

root=tk.Tk()
root.title("電卓")
root.geometry("400x700")

#ボタンの動作設定
def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(num, f"{num}のボタンがクリックされました")
    entry.insert(tk.END, num)

#=ボタンの動作設定
def click_equal(event):
    equal = entry.get()
    res = eval(equal)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

#ACボタンの動作設定
def click_clear(event):
    entry.delete(0, tk.END)

r=1
c=0

#ACボタンの追加 
btn = tk.Button(root, text=f"AC", font=("Times New Roman", 30), width=13, height=2)
btn.bind("<1>", click_clear)
btn.grid(row=r, column=c, columnspan=3)

#.ボタンの追加
btn = tk.Button(root, text=".", font=("Times New Roman", 30), width=4, height=2)
btn.bind("<1>", button_click)
btn.grid(row=5, column=2)

#数字ボタンの追加
numbers = list(range(9, -1, -1))
operators = ["/", "*", "-", "+"]
for i, num in enumerate(numbers, 1):
    btn.bind("<1>", button_click)
    if num == 0:
        
        btn = tk.Button(root, text=f"{num}", font=("Times New Roman", 30), width=9, height=2)
        btn.grid(row=r+1, column=c, columnspan=2)
    else:    
        btn = tk.Button(root, text=f"{num}", font=("Times New Roman", 30), width=4, height=2)
        btn.grid(row=r+1, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0

#符号ボタンの追加
r=1
c=0
for i, num in enumerate(operators, 1):
    btn = tk.Button(root, text=f"{num}", font=("Times New Roman", 30), width=4, height=2)
    btn.bind("<1>", button_click)
    btn.grid(row=r, column=c+3)
    c += 1
    if i%1 == 0:
        r += 1
        c=0

#=ボタンの追加
btn = tk.Button(root, text=f"=", font=("Times New Roman", 30), width=4, height=2)
btn.bind("<1>", click_equal)
btn.grid(row=r, column=c+3)

#表示画面の設定
entry = tk.Entry(root, justify="right", width=13, font=("Times New Roman", 40))
entry.grid(row=0, column=0, columnspan=4)

root.mainloop()