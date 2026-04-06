# waf to identify in which line the word learning first occurs if not then print -1

def check_word():
    with open("Practice.txt","r") as f:
        data=True
        count=1
        while data:
            data=f.readline()
            if "learning" in data:
                return f"Found in line {count}"
            count+=1
    return -1
print(check_word())