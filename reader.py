import csv
import pandas

# f = open('tester.csv')
# stuff = f.read()
# print(stuff)
data = pandas.read_csv("data/july_2017_discover.csv")
# model:
# Date,Amount,Transaction,Category,Notes

#ToDos:
# adding in new information
# pie chart
# graphss
balance = 0.0
for index,row in data.iterrows():
    addition = int(row["Amount"]*100)
    print(row["Date"],row["Amount"])
    balance += addition
    print("New balance:",balance/100)
