import sys
import csv
import pandas
import os
import _pickle as pickle
from make_graphs import *
from datetime import datetime
from math import floor

# new file
# created: 10/31/2019

# pickle documentation
# saving:
#   f = open(fname,"wb")
#   pickle.dump(obj, f)
# loading:
#   f = open(fname,"rb")
#   obj = pickle.load(f)


############################################################################


def read_data(fileName):
    data = pandas.read_csv(fileName)
    data.columns = ["date", "description", "original_description", "amount",
                    "transaction_type","category","account_name","labels","notes"]
    data.date = data.date.apply(lambda d: datetime.strptime(d, "%m/%d/%Y").date())
    data.amount = data.amount.apply(lambda a: floor(a * 100))
    # print(data.columns)

    return data.iloc[::-1]

def get_date(s):
    return datetime.strptime(s, "%m/%d/%Y")

def formatAmount(a):
    return a / 100

############################################################################
## TESTING



def printTransactions(data):
    groupings = {}
    groupingNames = []
    action = -1
    for _, row in data.iterrows():
        print(row.description, row.date, formatAmount(row.amount))
        if len(groupingNames) > 0:
            print('You have', len(groupingNames), 'groupings:')
            for i in range(len(groupingNames)):
                print(i, groupingNames[i])


if __name__ == "__main__":
    transactions = read_data(sys.argv[1])
    # total_car(transactions)
    printTransactions(transactions)
    # counts(transactions)
    # category_counts(transactions)
