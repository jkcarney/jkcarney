DELETE_LINE = 10 # Line 11

a_file = open("README.md", "r")
lines = a_file.readlines()
a_file.close()

del lines[DELETE_LINE]
new_file = open("README.md", "w+")

for line in lines:
    new_file.write(line)


new_file.close()