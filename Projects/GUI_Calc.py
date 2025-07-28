import tkinter as tk

def click(event):
    text = event.widget["text"]
    if text == "=":
        try:
            result = str(eval(str(entry_var.get())))
            entry_var.set(result)
        except:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

root = tk.Tk()
root.title("Python Calculator")
root.geometry("320x400")
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for row in buttons:
    frame = tk.Frame(btn_frame)
    frame.pack(expand=True, fill='both')
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 18", relief='ridge', bd=2)
        btn.pack(side='left', expand=True, fill='both')
        btn.bind("<Button-1>", click)

root.mainloop()
