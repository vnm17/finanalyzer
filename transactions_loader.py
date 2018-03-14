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

#############################################################################
## FILTER BY DATE

def before(data, end):
    # assumed that date is of form "%m/%d/%Y"
    end_date = get_date(end)
    return data[data.date <= end_date]

def after(data, start):
    # assumed that date is of form "%m/%d/%Y"
    start_date = get_date(start)
    return data[data.date >= start_date]

############################################################################
## FILTER BY ACCOUNTS

def pull_account(data, account_names):
    return data[data.account_name in account_names]

############################################################################

def read_data():
    data = pandas.read_csv("data/transactions.csv")
    data.columns = ["date", "description", "original_description", "amount",
                    "transaction_type","category","account_name","labels","notes"]
    data.date = data.date.apply(lambda d: datetime.strptime(d, "%m/%d/%Y"))
    data.amount = data.amount.apply(lambda a: floor(a * 100))
    # print(data.columns)
    return data

def get_date(s):
    return datetime.strptime(s, "%m/%d/%Y")

############################################################################
## TESTING

def total(data):
    uber_total = 0
    lyft_total = 0
    for index,row in data.iterrows():
        if row["date"] > get_date("09/01/2017"):
            # print(row["description"])
            if row["description"] == "Uber.com":
                if row["transaction_type"] == "debit":
                    uber_total += row["amount"]
                else:
                    uber_total -= row["amount"]
            elif row["description"] == "Lyft":
                if row["transaction_type"] == "debit":
                    lyft_total += row["amount"]
                else:
                    lyft_total -= row["amount"]
    uber_total = uber_total / 100
    print("Total spent on uber:",uber_total)
    lyft_total = lyft_total / 100
    print("Total spent on lyft:",lyft_total)

def counts(data):
    categories = {}
    for index,row in data.iterrows():
        # if row["date"] < get_date("09/01/2017"):
            # continue
        if row["account_name"] not in categories:
            categories[row["account_name"]] = 0
        categories[row["account_name"]] += 1
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
    counts(transactions)
    # counts(transactions)
    # category_counts(transactions)
