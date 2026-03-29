myset= set()
myset.add(1)          #ADDS VALUE
myset.add(123)
myset.add(11)
myset.add(8)
myset.add(7)
myset.add("Himanshu")
myset.add((1,2,3))

myset.remove(11)     #REMOVE VALUE
print(myset.pop())   #POP RANDOM VALUE
print(myset)
print(myset.clear()) #CLEAR ALL SET
print(myset)


#union and intersection 

set1={1,2,3,4}
set2={3,4,5,6}
print(set1.union(set2))
print(set1.intersection(set2))
