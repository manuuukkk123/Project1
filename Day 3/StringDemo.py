str = "RahulShetty.com"
str1 = "Consulting firm"
str3 = "RahulShetty"

print(str[1])  #a
print(str[0:5])  #If you want substring in python
print(str + "    "+ str1)  #Concatenation
print(str3 in str) #substring check

var=str.split(".")
print(var)
print(var[0])

str4 = " great "
print(str4.strip())
print (str4.lstrip())
print(str4.rstrip())