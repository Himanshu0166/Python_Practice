# Pass is a null statement
# It is used to do nothing
# If we want to execute the loop later we use pass in loop otherwise it throw an error
# Example
#This throw error
# for i in range(10):
#
# i=0
# while i<5:
#     print(i)
#     i += 1

for i in range(10):
    pass               #this does not throw error
i = 0
while i < 5:
    print(i)
    i += 1
