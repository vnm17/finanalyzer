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

def total(data):
    total = 0
    for index,row in data.iterrows():
        if row["date"] > get_date("09/01/2017"):
            # print(row["description"])
            if row["description"] == "Uber.com":
                if row["transaction_type"] == "debit":
                    total += row["amount"]
                else:
                    total -= row["amount"]
    total = total / 100
    print("Total spent on uber:",total)

def counts(data):
    categories = {}
    for index,row in data.iterrows():
        if row["date"] < get_date("09/01/2017"):
            continue
        if row["description"] not in categories:
            categories[row["description"]] = 0
        categories[row["description"]] += 1
    for c in categories:
        # if categories[c] > 1:
        print(c,categories[c])

def category_counts(data):
    categories = {}
    for index, row in data.iterrows():
        if row["date"] < get_date("09/01/2017"):
            continue
        if row["category"] not in categories:
            categories[row["category"]] = 0
        categories[row["category"]] += 1
    for c in categories:
        print(c, categories[c])

# separate credit from debit
def separate(data):
    purchases = data[data.transaction_type == "debit"]
    credits = data[data.transaction_type == "credit"]
    return purchases,credits

def account(data, account_name):
    transactions = data[data.account_name == account_name]
    print(len(transactions),"transactions")
    return transactions


if __name__ == "__main__":
    transactions = read_data()
    total(transactions)
    account(transactions, "Chase Preferred")
    # counts(transactions)
    # category_counts(transactions)
