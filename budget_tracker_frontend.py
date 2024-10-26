import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import budget_tracker_backend as backend

def main():
    app = Application()
    app.mainloop()

global total_budget
total_budget = float()
total_budget_string = str(total_budget)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Budget Tracker")
        self.geometry("960x540")

        
        
       
        #self.rowconfigure(0, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.columnconfigure(0, weight = 2)
        self.columnconfigure(1, weight = 3)
        self.columnconfigure(2, weight = 3)

        label_frame_1 = Label(self)
        label_frame_1.grid(row = 0, column = 0, sticky = "sw", padx = 30, pady = 5)

        separator = ttk.Separator(self, orient = "horizontal")
        separator.grid(row=1, column = 0, sticky = "ew", padx = 5,pady = 5, columnspan= 3)

        transaction_input = TransactionInput(self)
        transaction_input.grid(row = 2, column = 0, sticky = "nsw", padx = 5, pady = 5)

        input_form_frame_1 = InputForm(self)
        input_form_frame_1.grid(row = 2, column = 1, sticky = "nsew", padx = 5, pady = 5)

        input_form_frame_2 = InputForm(self)
        input_form_frame_2.grid(row = 2, column = 2, sticky = "nsew", padx = 5, pady = 5)

        



       


        

        
       
class Label(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = ttk.Label(self, text = "₱"+total_budget_string, font = ("Arial", 30, "bold"))
        self.label.grid(row = 0, column = 0, sticky = "sw")

        pass

class TransactionInput(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.new_transaction_label = ttk.Label(self, text = "New Transaction", font = ("Arial", 16))
        self.new_transaction_label.grid(row = 0, column = 0, sticky = "nw")



        self.transaction_name_frame = ttk.Frame(self)
        self.transaction_name_frame.grid(row = 1, column = 0, padx = 1, pady = 10)

        self.transaction_entry_label = ttk.Label(self.transaction_name_frame, text = "Name: " )
        self.transaction_entry_label.grid(row = 0, column = 0, sticky = "nw")

        self.transaction_name_entry = ttk.Entry(self.transaction_name_frame)
        self.transaction_name_entry.grid(row = 1, column = 0, columnspan=2, sticky = "ew")
        self.columnconfigure(1, weight = 1)



        self.transaction_type_frame = ttk.Frame(self)
        self.transaction_type_frame.grid(row = 1, column = 1, padx = 1, pady = 10)

        transaction_type_variable = tk.IntVar()

        self.transaction_type_radio_button_1 = ttk.Radiobutton(self.transaction_type_frame, text = "Income", variable = transaction_type_variable, value = 1).grid(row = 0, column = 0, padx = 5)
        self.transaction_type_radio_button_1 = ttk.Radiobutton(self.transaction_type_frame, text = "Expense", variable = transaction_type_variable, value = 2).grid(row = 1, column = 0, padx = 5)

        

        self.transaction_amount_frame = ttk.Frame(self)
        self.transaction_amount_frame.grid(row = 2, column = 0, sticky = "ew", padx = 15, pady = 5, columnspan=2)

        self.transaction_amount_label = ttk.Label(self.transaction_amount_frame, text = "Amount: ")
        self.transaction_amount_label.grid(row = 0, column = 0, sticky = "nw")

        self.transaction_amount_entry = ttk.Entry(self.transaction_amount_frame)
        self.transaction_amount_entry.grid(row = 1, column = 0, sticky = "ew")
        self.transaction_amount_frame.columnconfigure(0,weight=1)



        self.transaction_date_frame = ttk.Frame(self)
        self.transaction_date_frame.grid(row = 3, column = 0, sticky= "ew", padx = 15, pady = 15, columnspan= 2)

        self.transaction_date_dropdown = DateEntry(self.transaction_date_frame, date_pattern="yyyy-mm-dd")
        self.transaction_date_dropdown.grid(row = 0, column = 0, sticky = "ew")




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