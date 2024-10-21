import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Budget Tracker")

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 4)
        self.rowconfigure(0, weight = 1)

app = Application()

class InputForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)



app.mainloop()


'''
def add_to_list(event=None):
    text = entry.get()
    if text:
       text_list.insert(tk.END, text)  
       entry.delete(0, tk.END)   




#weight determines how much percent of additional space the widget will take up 
#also dictates whether it changes in size when you resize the tab

frame_1 = ttk.Frame(root)
frame_1.grid(row = 0, column = 0, sticky = "nsew", padx = 5, pady = 5)

frame_1.columnconfigure(0, weight = 1)
frame_1.rowconfigure(1, weight = 1)

entry = ttk.Entry(frame_1)
entry.grid(row = 0, column = 0, sticky = "ew")

entry.bind("<Return>",add_to_list)

entry_button_1 = ttk.Button(frame_1, text = "Enter", command=add_to_list)
entry_button_1.grid(row = 0, column = 1)

text_list = tk.Listbox(frame_1)
text_list.grid(row=1,  column=0, columnspan=2, sticky="nsew")

#columnspan is amount of columns it takes, "ew" in sticky means it sticks to east and west




frame_2 = ttk.Frame(root)
frame_2.grid(row = 0, column = 1, sticky = "nsew", padx = 5, pady = 5)

frame_2.columnconfigure(0, weight = 1)
frame_2.rowconfigure(1, weight = 1)

entry = ttk.Entry(frame_2)
entry.grid(row = 0, column = 0, sticky = "ew")

entry.bind("<Return>",add_to_list)

entry_button_2 = ttk.Button(frame_2, text = "Enter", command=add_to_list)
entry_button_2.grid(row = 0, column = 1)

text_list = tk.Listbox(frame_2)
text_list.grid(row=1,  column=0, columnspan=2, sticky="nsew")
'''







'''
def test_command():
    print("Chat the button was pressed")

test_label = tk.Label(root,text = "Label 1" )
test_label.grid(row = 0, column = 0)

test_button = tk.Button(root, text = "Buttton 1", command = test_command)
test_button.grid(row = 0, column = 1)
'''
root.mainloop()