try:
    with open('C:\\Users\\colin\\Downloads\\test.txt') as file:
      print(file.read())
except FileNotFoundError:
   print("That file was not found :(")