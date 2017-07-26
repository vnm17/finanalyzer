import csv
import pandas
import os
import _pickle as pickle
from make_graphs import *
from datetime import datetime



# pickle documentation
# saving:
#   f = open(fname,"wb")
#   pickle.dump(obj, f)
# loading:
#   f = open(fname,"rb")
#   obj = pickle.load(f)

def read_data():
    data = pandas.read_csv("data/transactions.csv")
    data.columns = ["date", "description", "description", "amount",
                    "transaction_type","category","account_name","labels","notes"]
    data.date = data.date.apply(lambda d: datetime.strptime(d, "%m/%d/%Y")) # 7/26/2017
    # print(data.columns)
    return data

def loop(data):
    categories = {}
    for index,row in data.iterrows():
        if row["category"] not in categories:
            categories[row["category"]] = 0
        categories[row["category"]] += 1
    print(categories)

# separate credit from debit
def separate(data):
    purchases = data[data.transaction_type == "debit"]
    credits = data[data.transaction_type == "credit"]
    return purchases,credits



if __name__ == "__main__":
    transactions = read_data()
    print("Have data!")
    purchases,credits = separate(transactions)
    spending(purchases)
    # pie_chart(purchases,"category")
