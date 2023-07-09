# Checking for values that exists in both arrays

def intersection(arr1, arr2) -> list:
    # Function printing the intersections between two lists
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    new_values = []
    for indices1 in range(arr1_len):
        for indices2 in range(arr2_len):
            if arr1[indices1] == arr2[indices2]:
                if arr1[indices1] in new_values:
                    continue
                else:
                    new_values.append(arr1[indices1])
    
    return new_values


data1 = [1,2,3,4,5]
data2 = [3,5,6,7,8]

test = intersection(data1, data2)

print(test)