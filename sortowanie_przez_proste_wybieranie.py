numbers = [ 5, 2, 9, 1, 5, 6, 3 , 8 ]

# i jest indeksem początku nieposortowanej części listy
# na początku cała listra jest nieposortowana
for i in range(len(numbers)):
    min_idx = i
    
    for j in range(i+1, len(numbers)):
        if numbers[j] < numbers[min_idx]:
            min_idx = j
    # po każdym przebiegu pętli 'j' najmniewszy element z części nieposortowanej 
    # zamienia się miejscami z jej pierwszym elementem 
    # i staje się ostatnim elementem posortowanej części listy - zwiększa się wartość i
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

print(numbers)

