'''
while True:
    try:
        amount_input = float(input("Amount: "))
    except:
        print("Please input numbers only")
    else: 
        break
'''

import tkinter as tk
  
root = tk.Tk()
label = tk.Label(root)
  
listbox = tk.Listbox(root)
listbox1 = tk.Listbox(root)
  
label.pack(side="bottom", fill="x")
  
listbox.pack(side="top", fill="both", expand=True)
listbox1.pack(side="bottom", fill="both", expand=True)
  
listbox.insert("end", "one", "two", "three", "four", "five")
listbox1.insert("end", "one", "two", "three", "four", "five")
  
def callback(event):
    if not event.widget.curselection():
        return
    print("1")
  
def callback1(event1):
    if not event1.widget.curselection():
        return
    print("2")
 
listbox.bind("<<ListboxSelect>>", callback)
listbox1.bind("<<ListboxSelect>>", callback1)
 
root.mainloop()