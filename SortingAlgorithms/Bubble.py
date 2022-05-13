def BubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
 
        for j in range(n-i-1):
    
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
    return arr
 

def get_data_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for item in lines:
            data_test_array=item.split()
        test_array=[int(x) for x in data_test_array]
        return test_array

