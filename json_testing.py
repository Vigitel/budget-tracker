import json
import os

with open('transactions.json') as transactions_json:
    data = json.load(transactions_json)

print(data)

transaction = {"type":"",
               "name":"",
               "amount":float(),
               "date_of_transaction":"",
               "tags":[]
               }


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


