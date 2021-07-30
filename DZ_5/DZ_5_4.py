import os, pickle, io


if not os.path.isfile('dairy.txt'):
    data = [0,1]
    data[0] = input("today")
    data[1] = input('How are you')
    file = open("dairy.txt", "wb")
    pickle.dump(data, file)
    file.close()
else:
    file = open("dairy.txt", "rb")
    data[0] = input("today")
    data[1] = input('How are you')
    file = open("dairy.txt", "wb")
    pickle.dump(data, file)
    file.close()

print('spisok del', data[0], ",", data[1])
