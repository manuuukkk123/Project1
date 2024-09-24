#Ex 1
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except:
    print("reached without failure")


#Ex 2
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)

finally:
    print("Cleaning up records")
