list=[2,1,3]
list.append(4)
print(list)
list.sort()    #list.sort(reverse=True) for assending 
print(list)
list.reverse() #reverse rhe list 
list.insert(0,8)  #list.insert(indec,value)
print(list)
list.remove(1)  #remove first occurence of given value    syntax list.remove(value)
list.pop(0)     #remove value from give index      list.pop(index)
print(list)
print(list.index(3))
print(sum(list))
print(max(list))
print(min(list))