def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == x:
            return (iterations, arr[mid])
        elif arr[mid] < x:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    return (iterations, upper_bound)


sorted_array = [0.1, 1.5, 3.2, 4.8, 5.9, 7.3, 8.6]
value_to_find = 4.5

result = binary_search(sorted_array, value_to_find)
print(result)
