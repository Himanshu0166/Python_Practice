# File Input and output
# modes
# r=  open for reading  (default)
# w=  open for writing ,truncating the file
# a=  open for appending adds at the ends of the file
# x= creates a new file and open it for writing
# b=binary mode
# t=text mode (default)
# + = open file for updating (read and write) ex r+  w+,a+
# r+= open file to read and write here pointer is at starting
# w+= opens file to read and write ,it overwrite everything
# a+=open file to read and write ,here pnter is at end 

f=open("demo.txt",'r+')
f.write("hi")
data=f.read()
print(data)
f.close()

f=open("Sample.txt","w")
f.write("Hello")
f.close()


with open("demo.txt","r") as d,open("sample.txt","a") as s:
    s.write("\n")
    s.write(d.read())
    
