def insertion_sort(arr):
    it = 0
    for i in range(len(arr)):
        value = arr[i]
        while i>0 and value < arr[i-1]:
            arr[i] = arr[i-1]
            i -= 1
            # print (arr)
            it += 1
        arr[i] = value
        it += 1
    return it, arr

def insertion_sort_short(a):
    it = 0
    for i in range(len(a)):
        while i-1>=0 and a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
            i-=1
            it += 1
        it += 1
    return it, a

from random import randint

for i in range(400):
    arr = [randint(0,20) for j in range(300)]
    sort_a = sorted(arr.copy())
    is1_it, is1_arr = insertion_sort(arr.copy())
    is2_it, is2_arr = insertion_sort_short(arr.copy())
    if is1_it != is2_it or is1_arr != is2_arr or is1_arr != sort_a or is2_arr != sort_a:
        print("Error : ")
        print(f"Long sort iterations  : {is1_it}")
        print(f"Short sort iterations : {is1_it}")
        print(arr)
        print(sort_a)
        print(is1_arr)
        print(is2_arr)

print("Finished")