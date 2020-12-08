A = [1,2,3,3,4,5,6,7,7]
target = 3


def find(A, target):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            if A[mid - 1] != target:
                return mid
            high = mid - 1


x = find(A, target)
print("Data ditemukan pada index ke-" + str(x+1))