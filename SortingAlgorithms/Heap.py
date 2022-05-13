def heapify(arr, n, i):
    largest = i  
    left = 2 * i + 1     
    right = 2 * i + 2     
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
 
 
def heapSort(arr):
    n = len(arr)
 
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)
    if arr==sorted(arr):
        return arr
 
 
def get_data_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for item in lines:
            data_test_array=item.split()
        test_array=[int(x) for x in data_test_array]
        return test_array
