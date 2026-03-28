tup=(2,4,6,2,5)
print(tup.index(2))   #return index of first occurence of the value     tup.index(value)
print(tup.count(2))   #return the number of occurence of the value    tup.count(value)
print(sum(tup))       #return sum of values in tuple
print(sorted(tup))    #sort the tuple
print(f"maximum value in tuple is {max(tup)}") #return maximum value of tuple 
print(f"minimum value in tuple is {min(tup)}") #return minimum value of tuple
print(tup*2)       #print tuple 2 times
print(2 in tup)   #check that value present in tuple or not
print("Tuple Unpacking")
t1=(1,2,3)
a,b,c=t1
print(f"tuple is {t1}")
print(a)
print(b)
print(c)