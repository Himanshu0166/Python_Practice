with open("data.csv","r") as f:
    data=f.read()
    print(data)
    print(type(data))

# This reads csv file as string and doesnot follow or know any rule for csv format

import csv
with open("data.csv","r") as f:
    data=csv.reader(f)
    print(type(data))

    for i in data:
        print(i)

# this show output fitted for csv format

