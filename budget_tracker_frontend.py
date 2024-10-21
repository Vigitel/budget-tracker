import tkinter as tk

root = tk.Tk()
root.title("Budget Tracker")

def add_to_list(event=None):
    text = entry.get()
    if text:
       text_list.insert(tk.END, text)  
       entry.delete(0, tk.END)   

frame = tk.Frame(root)
frame.grid(row = 0, column = 0)

entry = tk.Entry(frame)
entry.grid(row = 0, column = 0)

entry.bind("<Return>",add_to_list)

entry_button = tk.Button(frame, text = "Enter", command=add_to_list)
entry_button.grid(row = 0, column = 1)

text_list = tk.Listbox(frame)
text_list.grid(row=1,  column=0, columnspan=2, sticky="ew")

#columnspan is amount of columns it takes, "ew" in sticky means it sticks to east and west


'''
def test_command():
    print("Chat the button was pressed")

test_label = tk.Label(root,text = "Label 1" )
test_label.grid(row = 0, column = 0)

test_button = tk.Button(root, text = "Buttton 1", command = test_command)
test_button.grid(row = 0, column = 1)
'''
root.mainloop()