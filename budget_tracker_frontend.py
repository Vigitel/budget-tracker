import tkinter as tk
from tkinter import ttk

def main():
    app = Application()
    app.mainloop()

global total_budget
total_budget = float()
total_budget_string = "₱"+str(total_budget)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Budget Tracker")
        self.geometry("960x540")

        separator = ttk.Separator(self, orient = "horizontal")
        separator.grid(row=1, column = 0, sticky = "ew", padx = 5,pady = 5, columnspan= 2)
        
       
        #self.rowconfigure(0, weight = 1)
        self.rowconfigure(2, weight = 1)

        frame1 = InputForm(self)
        frame1.grid(row = 2, column = 1, sticky = "nsew", padx = 5, pady = 5)
        self.columnconfigure(0, weight = 1)


        frame3 = Label(self)
        frame3.grid(row = 0, column = 0, sticky = "sw", padx = 10, pady = 2.5)
       
class Label(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = ttk.Label(self, text = "Total money: " + total_budget_string, font = ("Arial", 20, "bold"))
        self.label.grid(row = 0, column = 0, sticky = "sw")

        pass

class TransactionInput(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)




class InputForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)

        self.entry = ttk.Entry(self)
        self.entry.grid(row = 0, column = 0, sticky = "ew")

        self.entry.bind("<Return>",self.add_to_list)

        self.entry_button_1 = ttk.Button(self, text = "Add", command=self.add_to_list)
        self.entry_button_1.grid(row = 0, column = 1)

        self.entry_button_2 = ttk.Button(self, text = "Clear", command=self.clear_list)
        self.entry_button_2.grid(row = 0, column = 2)

        self.text_list = tk.Listbox(self)
        self.text_list.grid(row=1,  column=0, columnspan=3, sticky="nsew")

        #columnspan is amount of columns it takes, "ew" in sticky means it sticks to east and west

    def add_to_list(self, event=None):
    
        text = self.entry.get()
        if text:
            self.text_list.insert(tk.END, text)  
            self.entry.delete(0, tk.END) 
    
    def clear_list(self):
        self.text_list.delete(0,tk.END)




if __name__ == "__main__":
    main()




'''
 




#weight determines how much percent of additional space the widget will take up 
#also dictates whether it changes in size when you resize the tab

frame_1 = ttk.Frame(root)






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
#root.mainloop()