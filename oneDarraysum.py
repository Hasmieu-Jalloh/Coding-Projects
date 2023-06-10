def sum(array):
    array_len = len(array)
    counter = 0
    summed_values = []

    for i in range(array_len):
        counter += array[i]
        summed_values.append(counter)
        i -= 1
    return summed_values

testing_array = [1,2,3,4,5,6,7,8,9]

test = sum(testing_array)

print(test)