from random import randint


def merge_sort(arr, min, max):
    if max-min == 0:
        return [arr[max]]
    if max-min == 1:
        if arr[max] < arr[min]:
            return [arr[max], arr[min]]
        else:
            return [arr[min], arr[max]]

    mid = (min+max)//2
    lres = merge_sort(arr, min, mid)
    rres = merge_sort(arr, mid+1, max)

    res = []
    li, ri = 0, 0

    while len(res) < (max-min)+1:
        if li >= len(lres):
            res += rres[ri:]
            break
        if ri >= len(rres):
            res += lres[li:]
            break
        if lres[li] < rres[ri]:
            res += [lres[li]]
            li += 1
        else:
            res += [rres[ri]]
            ri += 1
    return res

"""
MergeSort implementation in Python
"""
def sort (A):
    """merge sort A in place."""
    copy = list (A)
    mergesort_array (copy, A, 0, len(A))


def mergesort_array (A, result, start, end):
    """Mergesort array in memory with given range."""
    if end - start < 2:
        return
    if end - start == 2:
        if result[start] > result[start+1]:
            result[start],result[start+1] = result[start+1],result[start]
        return

    mid = (end + start) // 2
    mergesort_array (result, A, start, mid)
    mergesort_array (result, A, mid, end)
    
    # merge A left- and right- side
    i = start
    j = mid
    idx = start
    while idx < end:
        if j >= end or (i < mid and A[i] < A[j]):
            result[idx] = A[i]
            i += 1
        else:
            result[idx] = A[j]
            j += 1
            
        idx += 1


def merge_sort_large_sort(arr):
    carray = arr.copy()
    return merge_sort_large_msort(arr, carray, 0, len(arr)-1)

def merge_sort_large_msort(arr, carray, min, max):
    if min == max:
        return
    mid = (min+max)//2
    merge_sort_large_msort(arr, carray, min, mid)
    merge_sort_large_msort(arr, carray, mid+1, max)
    return merge_sort_large_merge(arr, carray, min, max)

def merge_sort_large_merge(arr, carray, min, max):
    mid = (min+max)//2
    i = min
    j = mid+1
    idx = min
    while idx<=max:
        if j>max or (i<=mid and arr[i]<arr[j]):
            carray[idx] = arr[i]
            i+=1
        else:
            carray[idx] = arr[j]
            j+=1
        idx+=1
    arr[min:max+1] = carray[min:max+1]
    return arr

A = [9, 5, 3, 6, 1, 2, 8, 7, 4, 0]
ms1=merge_sort(A, 0, 9)
# ms2=sort(A.copy())
ms3=merge_sort_large_sort(A.copy())

print(f"{A}\n{ms1}\n{ms3}\n")

for x in range(5000):
    ul = [randint(0, 1000000) for x in range(1000)]
    sl = sorted(ul)
    ml = merge_sort(ul.copy(), 0, len(ul)-1)
    ml2 = merge_sort_large_sort(ul.copy())
    if sl != ml or sl !=ml2:
        print(f"error lists: \n")
        print(f"{ul}\n{sl}\n{ml}\n{ml2}\n")