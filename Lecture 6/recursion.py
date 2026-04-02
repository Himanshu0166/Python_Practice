#when a function call itself repeatedly
def factorial(a):
    if a==0 or a==1:
        return 1
    else:
        return a*factorial(a-1)
print(factorial(5))

def summ(n):
    if n==0:
        return 0
    return n + summ(n-1)

print(summ(5))


def list_elemt(list,ind=0):
    if ind==len(list):
        return
    print(list[ind])
    list_elemt(list,ind+1)
num=[1,2,3,4,5,6]
list_elemt(num)