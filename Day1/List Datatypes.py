
values = [1,2,"rahul",4,5]
#list is data type that allows multiple values and can be kdifferent data types
print(values[0]) #1
print(values[3]) #4
print(values[-1]) #5
print(values[1:3]) # 2 rahul

#to inject new values to your list use insert command and append command
values.insert(3, "shetty")
print(values)

values.append("End")
print(values)
#To update the list with new value use  below command
values[2]="RAHUL"
del values[0]
print(values)
