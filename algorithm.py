def lomuto_partition(arr, left, right) -> int:
    pivot = arr[left]
    p = left
    for i in range(left + 1, right + 1):
        if arr[i] < pivot:
            p += 1
            arr[p], arr[i] = arr[i], arr[p]
    arr[left], arr[p] = arr[p], arr[left]
    return p


def quick_select_kth_largest(arr, k):
    if k > len(arr) or k <= 0:
        raise IndexError(f'Invalid Index, k = {k}')
    k = len(arr) - k
    left, right = 0, len(arr) - 1
    if left == right:
        return arr[left]
    while True:
        p = lomuto_partition(arr, left, right)
        if p > k:
            right = p - 1
        elif p < k:
            left = p + 1
        elif p == k:
            return arr[k]


# Sorted: [1, 2, 3, 4, 5]
A = [4, 2, 1, 5, 3]
K = 2
print(f"The {K} Largest Element in the array is: {quick_select_kth_largest(A, K)}\n")
