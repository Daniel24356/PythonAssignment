#1. Digit Classifier
def digitClassifier(number):
    if(number == 0):
        print("Zero")
    elif(number%2 == 0 and number%3 == 0):
        print("Even and divisible by 3")   
    elif(number%2 == 0):
        print("Even")
    else:
        print("Odd")

digitClassifier(9) 

# 2. Reverse Engineering
def reverseEngineering(number):
    reversedNum = 0
    number = abs(number)
    while number > 0:
        reversedNum = reversedNum * 10 + number % 10
        number //= 10
    return reversedNum
print(reverseEngineering(1234))

# 3. List Compression
def listCompression(values):
    result = []
    for value in values:
        if value % 2 == 0:
            result.append(value * 2)
    return result

print(listCompression([2,3,4,5,6]))