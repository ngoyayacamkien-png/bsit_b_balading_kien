
#Sum the Array
def sum_array(arr):
    if len(arr) == 0:
        return 0

    return arr[0] + sum_array(arr[1:])

def find_largest(arr):
    if len(arr) == 1:
        return arr[0]

    largest = find_largest(arr[1:])
    return arr[0] if arr[0] > largest else largest

print(sum_array([]))
print(sum_array([5]))
print(sum_array([1, 2, 3, 4]))
print(sum_array([-1, 5, -3, 2]))

#find the largest number

def find_largest(arr):
    if len(arr) == 0:
        raise ValueError("Array must not be empty")

    if len(arr) == 1:
        return arr[0]

    largest_rest = find_largest(arr[1:])

    if arr[0] > largest_rest:
        return arr[0]
    else:
        return largest_rest

print(find_largest([5]))
print(find_largest([10, 5, 3, 2]))
print(find_largest([1, 4, 8, 12]))
print(find_largest([-5, -2, -10, -1]))

#Count a Chosen Number

def count_number(arr, target):
    if len(arr) == 0:
        return 0

    if arr[0] == target:
        return 1 + count_number(arr[1:], target)
    else:
        return count_number(arr[1:], target)

print(count_number([], 5))
print(count_number([1, 5, 5, 3, 5], 5))
print(count_number([1, 2, 3, 4], 5))
print(count_number([7, 7, 7, 7], 7))


