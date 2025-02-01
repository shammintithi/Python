word = "Python"

with open("find.txt", "r") as file:
    data = file.read()

    if(data.find(word) != -1):
        print("Word found")

    else: 
        print("Word not found") 