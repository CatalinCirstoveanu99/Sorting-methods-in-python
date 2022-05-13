def countingSort(inputArray):
    Max= max(inputArray)
    countArrayLength = Max+1
    countArray = [0] * countArrayLength
    for item in inputArray: 
        countArray[item] += 1
    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1] 
    sortedArray = [0] * len(inputArray)
    i = len(inputArray) - 1

    while i >= 0:
        current_element = inputArray[i]
        countArray[current_element] -= 1
        newPosition = countArray[current_element]
        sortedArray[newPosition] = current_element
        i -= 1
    return sortedArray

def get_data_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for item in lines:
            data_test_array=item.split()
        test_array=[int(x) for x in data_test_array]
        return test_array


print(countingSort(get_data_file('data_test5.txt')))

 