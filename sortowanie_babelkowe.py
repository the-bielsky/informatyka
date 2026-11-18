 
numbers = [ 5, 2, 9, 1, 5, 6, 3 , 8 ]

min= numbers[1]
for i in range(len(numbers)):
    if numbers[i] < min:
        min = numbers[i]
        
print(numbers)