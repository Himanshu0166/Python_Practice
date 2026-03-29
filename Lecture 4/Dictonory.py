# Key Value Pair
# unordered , mutable,don't allow duplicate key
info={"Name":"Himanshu",
      "Age": 22,
      "Marks":99.9,
      "is_adult":True,
      "subjects":["java","C","C++"],
      "topics":("dictionary","Set"),
      11: 34    
      }
print(info)
print(info["Age"])
info["Name"]="Himanshu Joshi"
info["Gender"]="MAle"
print(info)

null_dictionary={}
print(null_dictionary)

# Nested Dictionary
student={"Name":"Himanshu",
         "Subjects":{
             "maths":99,
             "Physics":99,
             "Chemistry":100
         }
}
print(student)
print(student["Subjects"])
print(student["Subjects"]["maths"])