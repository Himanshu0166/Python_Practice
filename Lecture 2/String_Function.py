a="himanshu joshi"
print(a.endswith("shu"))
print(a.startswith("him"))
print(a.capitalize())      # capitalize only first letter of string
print(a.title())      # capitalize  first letter of each words in string

print(a.lower())
print(a.count('h'))
print(a.upper())
print(len(a))
print('him' in a)
print('hip' in a)
print(a.find('nshu'))
print(a.find('z'))          #does not raise eroor print -1
print(a.rfind('h'))         #from reverse
print(a.index('h'))
print(a.replace("joshi","Sharma")) #replace joshi with sharma
# print(a.index('r'))     raise error substring not found
print("   hello world   ".strip())     #remove leading and trailing white spaces
print("   hello world   ".rstrip())     #remove only trailing white spaces
print("   hello world   ".lstrip())     #remove only leading  white spaces
print("heLLo".swapcase())               #swap upeer and lower case
print("Hello World".split())            #splits string into list
print("a,b,c,d,e".split(","))            #splits string into list by ,
print("h#e#l#l#0".split("#"))            #splits string into list by #
print("a,b,c,d,e".rsplit(",",2))         #splits string into list from right 
print("".join(["Himanshu"," Joshi"]))
print("Hello world".center(21,'*'))
print(a.count("h"))

