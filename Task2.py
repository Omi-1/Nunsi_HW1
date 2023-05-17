numbers=[]

#created an indefinite loop
while True:
    num = int(input("Enter an interger (and 0 to stop):"))
    if num == 0:
        break  
    numbers.append(num)
sumation = sum(numbers)

print("Sum of numbers;", sumation)
