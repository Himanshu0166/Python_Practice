#Search if word learning exists in file

with open("Practice.txt","r") as f:
    data=f.read()
    if "learning" in data:
        print("Found")
    else:
        print("Not Found")