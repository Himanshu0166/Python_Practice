# Write a function to replace java with python in file created in question1

def replace_function_java_with_python():
    with open("Practice.txt","r") as f:
        data=f.read()
    print(data)
    new_data=data.replace("Java","Python")
    print(new_data)
    with open("Practice.txt","w") as f:
        f.write(new_data)
replace_function_java_with_python()