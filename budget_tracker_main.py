import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
from datetime import date
import json
import os
import time


# B A C K E N D

class transcaction():
    def __init__(self, type, name, amount, date_of_transaction, tags):
        self.type = str(type)
        self.name = str(name)
        self.amount = float(amount)
        self.date_of_transaction = str(date_of_transaction)
        self.tags = list(tags)

'''
transaction = {"type":"",
               "name":"",
               "amount":float(),
               "date_of_transaction":"",
               "tags":[]
               }
'''

with open('transaction_tags.json') as transaction_tag_json:
    data = json.load(transaction_tag_json)

transaction_tags = []

for tag in data:
    transaction_tags.append(tag)

def declare_transaction_tags():
    global transaction_tags_length,add_new_tag_index
    transaction_tags_length = len(transaction_tags)
    add_new_tag_index = transaction_tags_length - 1

declare_transaction_tags()











# F R O N T E N D



def main():
    app = Application()
    app.mainloop()



class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Budget Tracker")
        self.geometry("960x540")
        self.resizable(False, False)




        global total_budget, total_budget_string
        total_budget = float()
        total_budget_string = str(total_budget)

        class transcaction():
            def __init__(self, type, name, amount, date_of_transaction, tags):
                self.type = ""
                self.name = ""
                self.amount = float()
                self.date_of_transaction = ""
                self.tags = []

        #self.rowconfigure(0, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.columnconfigure(0, weight = 2)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)

        label_frame_1 = Label(self)
        label_frame_1.grid(row = 0, column = 0, sticky = "sw", padx = 30, pady = 5)

        separator = ttk.Separator(self, orient = "horizontal")
        separator.grid(row=1, column = 0, sticky = "ew", padx = 5,pady = 5, columnspan= 3)

        transaction_input = TransactionInput(self)
        transaction_input.grid(row = 2, column = 0, sticky = "nsew", padx = 5, pady = 5)

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




        # - - - - - - - - - - NAME - - - - - - - - - -
        self.transaction_name_frame = ttk.Frame(self)
        self.transaction_name_frame.grid(row = 1, column = 0, sticky = "ew", padx = 15, pady = 10)
        self.columnconfigure(0, weight=1)

        self.transaction_name_label = ttk.Label(self.transaction_name_frame, text = "Name: " )
        self.transaction_name_label.grid(row = 0, column = 0, sticky = "nw")

        self.transaction_name_entry = ttk.Entry(self.transaction_name_frame)
        self.transaction_name_entry.grid(row = 1, column = 0, columnspan=2, sticky = "ew")
        self.transaction_name_frame.columnconfigure(0, weight = 1)



        # - - - - - - - - - - TYPE - - - - - - - - - -
        self.transaction_type_frame = ttk.Frame(self)
        self.transaction_type_frame.grid(row = 1, column = 1, padx = 1, pady = 10)

        self.transaction_type_variable = tk.IntVar()

        self.transaction_type_radio_button_1 = ttk.Radiobutton(self.transaction_type_frame, text = "Income", variable = self.transaction_type_variable, value = 1).grid(row = 0, column = 0, padx = 5)
        self.transaction_type_radio_button_1 = ttk.Radiobutton(self.transaction_type_frame, text = "Expense", variable = self.transaction_type_variable, value = 2).grid(row = 1, column = 0, padx = 5)

        


        # - - - - - - - - - - AMOUNT - - - - - - - - - -
        self.transaction_amount_frame = ttk.Frame(self)
        self.transaction_amount_frame.grid(row = 2, column = 0, sticky = "ew", padx = 15, pady = 5, columnspan=2)

        self.transaction_amount_label = ttk.Label(self.transaction_amount_frame, text = "Amount: ")
        self.transaction_amount_label.grid(row = 0, column = 0, sticky = "nw")

        self.transaction_amount_entry = ttk.Entry(self.transaction_amount_frame)
        self.transaction_amount_entry.grid(row = 1, column = 0, sticky = "ew")
        self.transaction_amount_frame.columnconfigure(0,weight=1)




        # - - - - - - - - - - DATE - - - - - - - - - -
        self.transaction_date_frame = ttk.Frame(self)
        self.transaction_date_frame.grid(row = 3, column = 0, sticky= "ew", padx = 15, pady = 15, columnspan= 2)

        self.transaction_date_label = ttk.Label(self.transaction_date_frame, text = "Date: ")
        self.transaction_date_label.grid(row = 0, column = 0, sticky = "nw")

        self.transaction_date_dropdown = DateEntry(self.transaction_date_frame, date_pattern="yyyy-mm-dd")
        self.transaction_date_dropdown.grid(row = 0, column = 2, sticky = "ew")
        self.transaction_date_frame.columnconfigure(2, weight = 1)




        # - - - - - - - - - - TAGS - - - - - - - - - -
        self.transaction_tags_frame = ttk.Frame(self)
        self.transaction_tags_frame.grid(row = 4, column = 0, sticky = "nsew", padx = 15, pady = 5, columnspan=2)
        '''
        self.rowconfigure(4, weight=1)
        self.columnconfigure(0, weight=1)
        '''

        self.transaction_tags_label = ttk.Label(self.transaction_tags_frame, text = "Tags: ")
        self.transaction_tags_label.grid(row = 0, column = 0)

        self.transaction_tags_combobox = ttk.Combobox(self.transaction_tags_frame, values = transaction_tags)
        self.transaction_tags_combobox.grid(row = 0, column = 1, sticky = "ew", columnspan = 2)
        self.transaction_tags_frame.columnconfigure(1, weight = 1)
        self.transaction_tags_combobox.bind("<Key>", lambda a: "break")
        self.transaction_tags_combobox.bind("<<ComboboxSelected>>", self.add_new_tag)

        self.transaction_tags_add_button = ttk.Button(self.transaction_tags_frame, text = "Add tag", command = self.add_tag_to_list)
        self.transaction_tags_add_button.grid(row = 1, column = 2, sticky = "e", pady = 5)

        self.transaction_tags_delete_button = ttk.Button(self.transaction_tags_frame, text = "Delete tag", command = self.delete_tag)
        self.transaction_tags_delete_button.grid(row = 1, column = 1, sticky = "e", pady = 5)

        self.transaction_tags_list = tk.Listbox(self.transaction_tags_frame, cursor='hand2')
        self.transaction_tags_list.grid(row = 2, column = 0, sticky = "nsew", pady = 5, columnspan=3)
        




        # - - - - - - - - - - FINAL ADDITION OF TRANSACTION - - - - - - - - - - 
        self.transaction_final_button = ttk.Button(self, text = "Add Transaction", command = self.add_transaction)
        self.transaction_final_button.grid(row = 5, column = 1, sticky = "se")



    def add_transaction(self):
        
        if self.transaction_name_entry.get():
            input_name = str(self.transaction_name_entry.get())
        else:
            messagebox.showerror("showerror", "An input is required in the 'Name' field!")
        
        if self.transaction_type_variable.get() != 0:
            input_type = str(self.transaction_type_variable.get())
        else:
            messagebox.showerror("showerror", "Please select a transaction type!")
            return input_type
        
            
        while True:
            try:
                input_amount = float(self.transaction_amount_entry.get())
            except:
                messagebox.showerror("showerror", "Please enter a numerical value in the 'Amount' field!")
                break
            else: 
                break

        input_date = str(self.transaction_date_dropdown.get_date())

        input_tags = list(self.transaction_tags_list.get(0, 'end'))
        
        new_transaction_data = {"Name":input_name, "Amount":input_amount, "Date":input_date, "Tags":input_tags}

        key = str()
        if input_type == '1':
            key = 'Income'
        elif input_type == '2':
            key = 'Expense'
        else:
            return key
        


        print(key)

        with open('transactions.json', "r") as file:
            transactions_json = json.load(file)

        if isinstance(transactions_json[key], list):
            transactions_json[key].append(new_transaction_data)
        else:
            print("oof")

        with open('transactions.json', "w") as file:
            
            json.dump(transactions_json, file, indent=4)


        
            

        

    def add_tag_to_list(self):
        selected_tag = self.transaction_tags_combobox.get()
        current_tags = self.transaction_tags_list.get(0,'end')
        
        if selected_tag != transaction_tags[0] and selected_tag not in current_tags:
            self.transaction_tags_list.insert(tk.END, selected_tag)

    def delete_tag(self):
        tags_list_selected_index = self.transaction_tags_list.curselection()
        try:
            self.transaction_tags_list.delete(tags_list_selected_index)
        except:
            pass
            
    
    def add_new_tag(self, event=None):

        def add_to_global_tags_list():
            new_tag = new_tag_toplevel_entry.get()
            transaction_tags.append(new_tag)
            print(transaction_tags)

            self.transaction_tags_combobox['values'] = transaction_tags

            with open('transaction_tags.json', "r") as file:
                data = json.load(file)

            with open('transaction_tags.json', "w") as file:
                json.dump(transaction_tags, file, indent = 2)


            added_label = ttk.Label(new_tag_toplevel, text = "Added !")
            added_label.grid(row=1, sticky = "e")
            
            added_label.after(1000, added_label.destroy)
            
            
            

        if self.transaction_tags_combobox.get() == transaction_tags[0]:
            print("yeah they clicked it mate")

            new_tag_toplevel = tk.Toplevel(self.transaction_tags_frame)
            new_tag_toplevel.geometry("250x75")

            new_tag_toplevel_label = ttk.Label(new_tag_toplevel, text = "Name of Tag: ")
            new_tag_toplevel_label.grid(row = 0, column = 0, padx = 10, pady = 10)

            new_tag_toplevel_entry = ttk.Entry(new_tag_toplevel)
            new_tag_toplevel_entry.grid(row = 0, column = 1, padx = 10, pady = 10)

            new_tag_toplevel_button = ttk.Button(new_tag_toplevel, text = "Add", command=add_to_global_tags_list)
            new_tag_toplevel_button.grid(row = 1, column = 1, sticky = 'e', padx = 10)


            self.transaction_tags_combobox.current(1)
        
        








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

#root.mainloop()