import tkinter as tk

def say_hello():
    label.config(text="Hello, Tkinter!")

root = tk.Tk()
root.title("Simple GUI")

label = tk.Label(root, text="Click the button")
label.pack()

button = tk.Button(root, text="Say Hello", command=say_hello)
button.pack()

root.mainloop()
