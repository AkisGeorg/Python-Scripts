def selectionSort(number, size):
    for i in range(size):
        min = i

        for x in range(i + 1, size):
            if number[x] < number[min]:
                min = x

        number[i], number[min] = number[min], number[i]


numbers = [1, 9, 2, 10, 8, 13, 5]
size = len(numbers)
selectionSort(numbers, size)
print(f"Numbers: {numbers}")
