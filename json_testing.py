import json
import os

# import required packages 
import json 
  
class transcaction():
    def __init__(self, type, name, amount, date_of_transaction, tags):
        self.type = str(type)
        self.name = str(name)
        self.amount = float(amount)
        self.date_of_transaction = str(date_of_transaction)
        self.tags = list(tags)

tags_1 = ["yup", "yass"]

# custom class 
class Student: 
    def __init__(self, roll_no, name, batch): 
        self.roll_no = roll_no 
        self.name = name 
        self.batch = batch 
  
  
class Car: 
    def __init__(self, brand, name, batch): 
        self.brand = brand 
        self.name = name 
        self.batch = batch 
  
  
# main function 
if __name__ == "__main__": 
    
    # create two new student objects 
    s1 = Student("85", "Swapnil", "IMT") 
    s2 = Student("124", "Akash", "IMT") 
  
    # create two new car objects 
    c1 = Car("Honda", "city", "2005") 
    c2 = Car("Honda", "Amaze", "2011") 

    transaction_1 = transcaction("Income", "Salary", 3000, "2024-11-01", ["yup", "yeah"])
  
    # convert to JSON format 
    jsonstr1 = json.dumps(s1.__dict__) 
    jsonstr2 = json.dumps(s2.__dict__) 
    jsonstr3 = json.dumps(c1.__dict__) 
    jsonstr4 = json.dumps(c2.__dict__) 

    json_transaction_1 = json.dumps(transaction_1.__dict__)
  
    # print created JSON objects 
    print(jsonstr1) 
    print(jsonstr2) 
    print(jsonstr3) 
    print(jsonstr4) 

    print(json_transaction_1)




with open('transactions.json') as transactions_json:
    data = json.load(transactions_json)

print(data)
'''
transaction = {"type":"",
               "name":"",
               "amount":float(),
               "date_of_transaction":"",
               "tags":[]
               }
'''




    
    
    


'''
type_input = input("Type: ")
name_input = input("Name: ")
while True:
    try:
        amount_input = float(input("Amount: "))
    except:
        print("Please input numbers only")
    else: 
        break
date_input = input("Date: ")
tags_input = ["bloop", "bleep"]

transaction.update({"type":type_input,
               "name":name_input,
               "amount":amount_input,
               "date_of_transaction":date_input,
               "tags":tags_input
               })

print(transaction)
'''

'''
transaction_tags = []

for tag in data:
    transaction_tags.append(tag)

print(transaction_tags)

user_input = str(input("Add a new tag: "))
transaction_tags.append(user_input)

os.remove('transaction_tags.json')
with open('transaction_tags.json', 'w') as f:
    json.dump(transaction_tags, f, indent = 2)
    
'''


