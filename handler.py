from transactions_loader import *
import os

def data_options():
    options = os.listdir("data")
    options.remove(".DS_Store")
    for idx, op in enumerate(options):
        print(idx, op)
    choice = int(input("What data would you like to load? "))
    path = "data/" + options[choice]
    return path

def loop(transactions):
    print("we have the dataz!")
    choose_data_range = input("Would you like to limit the data range? y/n ") == "y"
    if choose_data_range:
        start_data = input("Starting date (MM/DD/YYYY) ")


if __name__ == "__main__":
    transactions = read_data()
    while True:
        loop(transactions)
