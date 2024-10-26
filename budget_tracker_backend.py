from datetime import date

class transcaction():
    def __init__(self, type, name, amount, date_of_transaction, tags):
        self.type = ""
        self.name = ""
        self.amount = float()
        self.date_of_transaction = ""
        self.tags = []


transaction_types = []

month_and_days_list = {"January" : 31, 
            "February" : 29,
            "March" : 31, 
            "April" : 30,
            "May" : 31,
            "June" : 31,
            "July" : 30,
            "August" : 31,
            "September" : 30,
            "October" : 31,
            "November" : 30,
            "December" : 31}


            


