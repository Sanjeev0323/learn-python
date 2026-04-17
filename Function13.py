def find_max(numbers):
    if  not  numbers:
        raise ValueError("list is empty")
    maximum=numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum=num
    return maximum
print(find_max([1,2,3,4,5]))