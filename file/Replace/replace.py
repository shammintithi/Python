with open("replace.txt", "r") as file:
    data = file.read()

    new_data = data.replace("Python", "Java")
    print(new_data)