from random import randint

def pick_pivot(arr, min, max):
    return randint(min, max)

def qsort(arr, min, max):
    pivot = pick_pivot(arr, min, max)
    piv_value = arr[pivot]
    arr[pivot], arr[max] = arr[max], arr[pivot]

    store = min
    for i in range(min, max):
        if arr[i] <= piv_value:
            arr[i], arr[store] = arr[store], arr[i]
            store += 1
    arr[store], arr[max] = arr[max], arr[store]
    return store

def quicksort(arr, min, max):
    if min < max:
        pi = qsort(arr, min, max)
        quicksort(arr, min, pi-1)
        quicksort(arr, pi+1, max)
    return arr

l =  [35, 77, 77, 35, 86, 92, 6, 2, 56, 93 , 5]
s_l = [2, 5, 6, 35, 35, 56, 77, 77, 86, 92, 93]

qs_l = quicksort(s_l, 0, len(s_l)-1)

print(f"Sorted array is equal {s_l == qs_l}")
print(s_l)
print(qs_l)

for i in range(1000):
    l = [randint(0,10000) for d in range(1000)]
    qsl = quicksort(l.copy(), 0, len(l)-1)
    sl = sorted(l)
    if  qsl != sl:
        print("Error, qsl != sl")
        print(l)
        print(qsl)
        print(sl)

