list=[1,2,2,1]
copy_list=list.copy()
copy_reverse= copy_list.reverse()

if list == copy_list:
    print("list is palindrome")
else:
    print("List is not palindrome")
