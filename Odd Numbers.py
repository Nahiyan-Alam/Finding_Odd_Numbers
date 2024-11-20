def filter_odd_numbers(numbers_list):
    odd_numbers = [number for number in numbers_list if number % 2 != 0]
    return odd_numbers

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
new_odd_numbers_list = filter_odd_numbers(input_list)

print("Input list:", input_list)
print("New list with odd numbers:", new_odd_numbers_list)
