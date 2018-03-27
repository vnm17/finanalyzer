from transactions_loader import *
import os
import re

months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

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

def maybe_limit_range(data):
    choose_data_range = input("Would you like to limit the data range? y/n ") == "y"
    if not choose_data_range:
        return data
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
    split_months = input("Would you like to split data by months? y/n ") == "y"
    if split_months:
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
    return [data]

def account_filter(data):
    print("Filter by account?")
    accounts = set()
    for index, row in data.iterrows():
        accounts.add(row["account_name"])
    accounts = list(accounts)
    for i, account in enumerate(accounts):
        print(i, account)
    try:
        choice = int(input("Choose account: "))
        account_name = accounts[choice]
        return data[data.account_name == account_name]
    except ValueError:
        return data

def description_filter(data):
    filter_by_description = input("Choose specific vendor? y/n ") == "y"
    if filter_by_description:
        description = input("Description: ")
        filtered_data = data[data.description == description]
        while len(filtered_data) == 0:
            try_again = input("There are no transactions with this description. Try again? y/n ") == "y"
            if try_again:
                description = input("Description: ")
                filtered_data = data[data.description == description]
            else:
                return data
        return filtered_data

############################################################################
## FUNCTIONS
def total(data, description):
    total = 0
    for index, row in data.iterrows():
        if row["description"] == description:
            if row["transaction_type"] == "debit":
                total += row["amount"]
            else:
                total -= row["amount"]
        total = total / 100
        return total


def choose_function(data):
    functions_names = ["total", "counts"]
    functions = { "total": total}
    print("Choose the desired function:")
    for index, function in enumerate(functions_names):
        print(index,function)
    choice = int(input("Choose function (number): "))
    return functions[functions_names[choice]](data[0], "Lyft")

def loop(data):
    data = maybe_limit_range(data)
    data = account_filter(data)
    data = separate_by_months(data)
    data = choose_function(data)
    return data

if __name__ == "__main__":
    # future: choose data to read
    transactions = read_data()
    print("we have your data! hooray!")
    transactions = account_filter(transactions)
