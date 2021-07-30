import os


if not os.path.isfile('dairy.txt'):
    file = open("dairy.txt", "w+")
    file.write(input('what time it is :') + '\n')
    file.write(input('how are you :') + '\n')
    file.close()
else:
    file = open("dairy.txt", "a")
    file.write(input('what time it is :') + '\n')
    file.write(input('how are you :') + '\n')
    file.close()
with open('dairy.txt', 'r') as file:
    print(file.read())



