def InsertionSort(arr):
    for i in range(1, len(arr)):
  
        key = arr[i]
  
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

    return arr
  
def get_data_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for item in lines:
            data_test_array=item.split()
        test_array=[int(x) for x in data_test_array]
        return test_array

       
# print(InsertionSort(get_data_file('data_test1.txt')))
# print(InsertionSort(get_data_file('data_test2.txt')))
# print(InsertionSort(get_data_file('data_test3.txt')))
# print(InsertionSort(get_data_file('data_test4.txt')))
print(InsertionSort(get_data_file('data_test5.txt')))