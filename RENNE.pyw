import tkinter as tk
import os

main = tk.Tk()
main.configure(width = "500", height = "300", bg = "yellow")
main.title("RUN!")

def frame_exit():
	main.destroy()

def open_path():
                op_path = "start " + ent.get()
                if op_path == "start ":
                        l1["text"] = "You have to enter a valid executable!"
                elif op_path[6] == ">":
                        items = op_path.split('>')
                        items.remove(items[0])
                        cmd = items[0]
                        os.system(cmd)
                else:
                        os.system(op_path)

l1 = tk.Label(main, text = "Enter an executable!", width = "60", height = "2", bg = "black", fg = "white")
l1.pack()

l2 = tk.Label(main, text = "(If you don't want to start something but enter", width = "60", height = "1", bg = "black", fg = "white")
l2.pack()

l3 = tk.Label(main, text = " a command write '>' before the command)", width = "60", height = "1", bg = "black", fg = "white")
l3.pack()

ent = tk.Entry(main, width = "75")
ent.pack()

bttn = tk.Button(main, text = "Run", width = "60", height = "4", command = open_path, bg = "black", fg = "white")
bttn.pack()

exit_bttn = tk.Button(main, text = "Close Frame", width = "20", height = "2", command = frame_exit, bg = "black", fg = "white")
exit_bttn.pack()

main.mainloop()
