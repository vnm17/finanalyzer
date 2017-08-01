import csv
import pandas
import os
import _pickle as pickle
from make_graphs import *
from datetime import datetime
from math import floor



# pickle documentation
# saving:
#   f = open(fname,"wb")
#   pickle.dump(obj, f)
# loading:
#   f = open(fname,"rb")
#   obj = pickle.load(f)

def read_data():
    data = pandas.read_csv("data/transactions.csv")
    data.columns = ["date", "description", "original_description", "amount",
                    "transaction_type","category","account_name","labels","notes"]
    data.date = data.date.apply(lambda d: datetime.strptime(d, "%m/%d/%Y")) # 7/26/2017
    data.amount = data.amount.apply(lambda a: floor(a * 100))
    # print(data.columns)
    return data

def get_date(s):
    return datetime.strptime(s, "%m/%d/%Y")

def loop(data):
    total = 0
    for index,row in data.iterrows():
        if row["date"] > get_date("06/09/2017"):
            # print(row["description"])
            if row["description"] == "Uber.com":
                if row["transaction_type"] == "debit":
                    total += row["amount"]
                else:
                    total -= row["amount"]
    total = total / 100
    print("Total spent on uber:",total)


# separate credit from debit
def separate(data):
    purchases = data[data.transaction_type == "debit"]
    credits = data[data.transaction_type == "credit"]
    return purchases,credits



if __name__ == "__main__":
    transactions = read_data()
    loop(transactions)
