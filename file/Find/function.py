def find_Python():
    word = "Python"

    with open("find.txt", "r") as file:
        data = file.read()

        if(data.find(word) != -1):
            print("Word found")

        else: 
            print("Word not found") 
find_Python()

def find_line():

    word = "Python"
    data = True
    line_no = 1

    with open("find.txt", "r") as file:
        while data:
            data = file.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1

find_line()

