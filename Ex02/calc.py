import tkinter as tk
import tkinter.messagebox as tkm

root=tk.Tk()
root.title("電卓")
root.geometry("300x600")

def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(num, f"{num}のボタンがクリックされました")
    entry.insert(tk.END, num)

def click_equal(event):
    equal = entry.get()
    res = eval(equal)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

r=1
c=0
numbers = list(range(9, -1, -1))
operators = ["+"]
for i, num in enumerate(numbers+operators, 1):
    btn = tk.Button(root, text=f"{num}", font=("Times New Roman", 30), width=4, height=2)
    btn.bind("<1>", button_click)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0

entry = tk.Entry(root, justify="right", width=10, font=("Times New Roman", 40))
entry.grid(row=0, column=0, columnspan=3)

btn = tk.Button(root, text=f"=", font=("Times New Roman", 30), width=4, height=2)
btn.bind("<1>", click_equal)
btn.grid(row=r, column=c)

root.mainloop()