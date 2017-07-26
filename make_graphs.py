import pandas
import matplotlib.pyplot as plt

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
