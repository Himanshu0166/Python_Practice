string="Himanshu"
string2='Himanshu'
string3="""Himanshu"""
print(string)
print(string2)
print(string3)

str1="This is a string. We are working in python"
str2="This is a string. \nWe are working in python"
print(str1)
print(str2)


#Basic operation
str3=str1 + " " + str2
print(str3)
print(len(str3))

print(str3[5])
print(str3[5:60])
print(str3[5:60:2])

print(str3[5:])  #[5:len(str3)
print(str3[:20])  #[0:20]