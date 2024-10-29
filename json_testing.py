import json
import os

with open('transaction_tags.json') as transaction_tag_json:
    data = json.load(transaction_tag_json)

transaction_tags = []

for tag in data:
    transaction_tags.append(tag)

print(transaction_tags)

user_input = str(input("Add a new tag: "))
transaction_tags.append(user_input)

os.remove('transaction_tags.json')
with open('transaction_tags.json', 'w') as f:
    json.dump(transaction_tags, f, indent = 2)
    



