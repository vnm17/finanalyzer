from transactions_loader import *
import os
import re

def data_options():
    options = os.listdir("data")
    options.remove(".DS_Store")
    for idx, op in enumerate(options):
        print(idx, op)
    choice = int(input("What data would you like to load? "))
    path = "data/" + options[choice]
    return path

def is_date(date):
    date_regex = re.compile("[0-1]*[0-9]/[0-3]*[0-9]/20[1-2][0-9]")
    return not not date_regex.match(date)

def limit_range(data):
    start_date = input("Starting date (MM/DD/YYYY) ")
    if not is_date(start_date):
        start_date = input("uhoh! That doesn't look like it's the right format. Try again: ")
    if is_date(start_date):
        data = after(data, start_date)
        print("start date added")
    else:
        print("no start date added")
    end_date = input("Ending date (MM/DD/YYYY) ")
    if not is_date(end_date):
        end_date = input("uhoh! That doesn't look like it's the right format. Try again: ")
    if is_date(end_date):
        data = before(data, end_date)
        print("end date added")
    else:
        print("no end date added")
    return data

def separate_by_months(data):
    start = 0
    month = data.iloc[0]["date"].month
    all_data = []
    for index, row in data.iterrows():
        if month != row["date"].month:
            all_data.append(data.iloc[start:index])
            start = index
            month = row["date"].month
    all_data.append(data.iloc[start:])
    return all_data


def loop(data):
    # ask what data, dates, function
    choose_data_range = input("Would you like to limit the data range? y/n ") == "y"
    if choose_data_range:
        data = limit_range(data)
    # Todo: allow counts
    split_months = input("Would you like to split data by months? y/n") == "y"
    if split_months:
        data = separate_by_months(data)
    else:
        data = [data]
    return data

if __name__ == "__main__":
    # future: choose data to read
    transactions = read_data()
    print("we have your data! hooray!")
    transactions = loop(transactions)
