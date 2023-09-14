#text = "Yooooooo\nThis is some text \nHave a good one!\n"
text = "Have a nice day! See ya\n"

with open('test.txt','a') as file:
    file.write(text)