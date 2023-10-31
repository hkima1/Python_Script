f = open("text.txt", "w")
with open("example.txt") as file:
  for item in file:
    f = open('file.txt', 'a')
    f.write(chr(int(item)))
  f.close()
file.close()