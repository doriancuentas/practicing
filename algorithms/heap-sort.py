#heap sort

heap_list_changes = []

def heap_sort(arr):
    global heap_list_changes
    heap_list_changes += [arr.copy()]
    build_help(arr)
    n = len(arr)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_list_changes += [arr.copy()]
        heapify(arr, 0, i)
    return arr

def build_help(arr):
    n = len(arr)
    for i in range(int((n)/2-1), -1, -1):
        heapify(arr, i, n)

def heapify(arr, i, n):
    global heap_list_changes
    largest = i
    left = 2*i +1
    right = 2*i +2

    if left<n and arr[left] > arr[largest]:
        largest = left
    if right<n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heap_list_changes += [arr.copy()]
        heapify(arr, largest, n)

a = [23, 95, 38, 44, 68, 84, 94, 9, 85]
print(a)
heap_sort(a)
print(a) 

for x in range(40):
    print("--")
    from random import randint
    arr = [randint(0,100) for i in range(40)]
    print(arr)
    sorted_arr = sorted(arr.copy())
    arr = heap_sort(arr)
    print(sorted_arr)
    print(arr)
    print("Is sorted" if sorted_arr == arr else "error")
