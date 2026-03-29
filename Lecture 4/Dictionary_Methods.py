info={"Name":"Himanshu",
      "Age": 22,
      "Marks":99.9,
      "is_adult":True,
      "subjects":["java","C","C++"],
      "topics":("dictionary","Set"),
      "Subjects":{
             "maths":99,
             "Physics":99,
             "Chemistry":100
         }

      }
print(len(info))
print(info.keys())       #Gives list of keys in dictionary
print(list(info.keys()))

print(info.values())     #Gives list of the values in dictionary
print(list(info.values()))

print(info.items())      #gives list of the key value pair in dictionary

print(info.get("Subjects"))                       #it print none if not found

print(info.update({"City":"Delhi"}))
print(info)