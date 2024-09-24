file= open('text.txt')
#Read all the contents of the file
#read n number of characters by passing parameter

# print(file.read(5))
#read one single line at a time readLine()
# print(file.readline())

#print line by line using readline method

line=file.readline()
while line!="":
    print(line)
    line=file.readline()

#about using readlines
for line in file.readlines():
    print(line)



file.close()
