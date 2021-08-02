# 1
def countdown(num):
    return [i for i in range(num, -1, -1)]

print(countdown(5))

# 2
def print_and_return(arr):
    print(arr[0])
    return arr[1]

print(print_and_return([1,2]))

# 3
def first_plus_length(arr):
    return arr[0] + len(arr)

print(first_plus_length([1,2,3,4,5]))

# 4
def values_greater_than_second(arr):
    new_arr = []
    if len(arr) < 2:
        return False
    else:
        for i in arr:
            if i > arr[1]:
                new_arr.append(i)
        print(len(new_arr))
        return new_arr

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# 5
def length_and_value(size, value):
    return [value for i in range(size)]

print(length_and_value(4,7))
print(length_and_value(6,2))