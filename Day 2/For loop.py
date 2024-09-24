#how to iterate over list data type using for loop

obj = [2,3,5,7,9]
for i in obj:
    print(i)

# how to print the above code with multiple of 2 with simple change *
obj = [2,3,5,7,9]
for i in obj:
    print(i*2)

# Som of first natural numbers 1+2+3+4+5=15
#range(i,j)--->i to j-1
# summation=0
for j in range(1,6):
    summation = summation+j
print(summation)


for k in range(1,10,2):
    print(k)

for h in range(1,50,100-30):
    print(h)
