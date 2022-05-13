import sys

def SelectionSort(arr):
    for i in range(len(arr)):
        
        Min = i
        for j in range(i+1, len(arr)):
            if arr[Min] > arr[j]:
                Min = j
                      
        arr[i], arr[Min] = arr[Min], arr[i]
    return arr
  

def get_data_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for item in lines:
            data_test_array=item.split()
        test_array=[int(x) for x in data_test_array]
        return test_array


# print(SelectionSort(get_data_file('data_test1.txt')))
# print(SelectionSort(get_data_file('data_test2.txt')))
# print(SelectionSort(get_data_file('data_test3.txt')))
# print(SelectionSort(get_data_file('data_test4.txt')))
print(SelectionSort(get_data_file('data_test5.txt')))