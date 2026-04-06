#Difference Between read and readlines
with open("Sample.txt","r") as f:
    data=f.read()
    print(data)
    print(type(data))
# OUTPUT for this is
# Hello my name is himanshu
# How are you 
# I am fine
# What aabout you
# <class 'str'>
with open("Sample.txt","r") as f:
    data=f.readlines()
    print(data)
    print(type(data))
    print(f.tell())
    f.seek(10)
    print(f.tell())
# OUTPUT for this is
# ['Hello my name is himanshu\n', 'How are you \n', 'I am fine\n', 'What aabout you']
# <class 'list'>

with open("Sample.txt","r") as f:
    for line in f:
        print(line.split())
