import pandas
import matplotlib.pyplot as plt
from datetime import datetime

# data.columns = ["date", "description", "description", "amount",
                # "transaction_type","category","account_name","labels","notes"]

def counter(data,category):
    counts = {}
    for index,row in data.iterrows():
        if row[category] not in counts:
            counts[row[category]] = 0
        counts[row[category]] += 1
    return counts

def pie_chart(data,category):
    counts = counter(data,category)
    labels = []
    sizes = []
    for c in counts:
        labels.append(c)
        sizes.append(counts[c])
    # Plot
    # patches, texts = plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    patches,texts = plt.pie(sizes, startangle=140)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.show()

def spending(data):
    days = {}
    for index,row in data.iterrows():
        start = datetime.strptime("06/20/2017", "%m/%d/%Y")
        if row.date > start:
            if row.date not in days:
                days[row.date] = 0.0
            days[row.date] += row.amount
    points = []
    for d in days:
        points.append([d,days[d]])
    points.sort()
    x = []
    y = []
    for p in points:
        x.append(p[0])
        y.append(p[1])

    plt.plot(x, y)
    plt.show()
