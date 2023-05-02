import random, timeit


# 기본적인 퀵소트
def quick_sort(A, left, right):
    global Qc, Qs
    if left >= right: return
    pivot = A[left]
    i, j = left, right
    while i < j:
        while i < j and A[j] >= pivot:
            Qc += 1
            j -= 1
        if i < j:
            Qs += 1
            A[i] = A[j]
            i += 1
        while i < j and A[i] <= pivot:
            Qc += 1
            i += 1
        if i < j:
            Qs += 1
            A[j] = A[i]
            j -= 1
    A[i] = pivot
    quick_sort(A, left, i - 1)
    quick_sort(A, i + 1, right)


# 추가점수 1
# arr의 길이가 10과 40 사이일 때 insertion sort를 활용하여 정렬한다.
def hybrid_quick_sort(arr, low, high):
    global Q1c, Q1s

    if low < high:
        if 10 <= high - low + 1 <= 40:
            insertion_sort(arr, low, high)
        else:
            pivot_index = partition(arr, low, high)
            hybrid_quick_sort(arr, low, pivot_index - 1)
            hybrid_quick_sort(arr, pivot_index + 1, high)


# 이때, partition 함수는 기본적인 퀵소트의 방식을 활용한다.
def partition(arr, low, high):
    global Q1c, Q1s

    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            Q1c += 1
            i += 1
        while i <= j and arr[j] >= pivot:
            Q1c += 1
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            Q1s += 1
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    Q1s += 1
    return j


# insertion sort는 기본적인 insertion sort의 방식을 활용한다.
def insertion_sort(arr, low, high):
    global Q1c, Q1s

    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low:
            Q1c += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                Q1s += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
        Q1s += 1


# 추가점수 2
# 적당한 K개가 남을 떄까지만 분할한 후, 따로 insertion sort를 활용하여 정렬하지 않는다면, 전체 값이 완전히 정리되지는 않는다.
# 하지만 대부분 정렬이 된 상태가 된다. 따라서, 이를 활용하여 insertion sort를 활용하여 정렬한다.
# 사실상 추가점수 1과 같은 방식이다.
def hybrid_quick_sort_2(arr, low, high, K):
    global Q2c, Q2s

    if low < high:
        if high - low + 1 <= K:
            insertion_sort_2(arr, low, high)
        else:
            pivot_index = partition_2(arr, low, high)
            hybrid_quick_sort(arr, low, pivot_index - 1)
            hybrid_quick_sort(arr, pivot_index + 1, high)


def partition_2(arr, low, high):
    global Q2c, Q2s

    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            Q2c += 1
            i += 1
        while i <= j and arr[j] >= pivot:
            Q2c += 1
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            Q2s += 1
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    Q2s += 1
    return j


# insertion sort는 기본적인 insertion sort의 방식을 활용한다.
def insertion_sort_2(arr, low, high):
    global Q2c, Q2s

    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low:
            Q2c += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                Q2s += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
        Q2s += 1


# 기본적인 Merge Sort
def merge_sort(A, left, right):
    global Mc, Ms
    if left >= right: return
    mid = (left + right) // 2
    merge_sort(A, left, mid)
    merge_sort(A, mid + 1, right)
    B = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        Mc += 1
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    while i <= mid:
        B.append(A[i])
        i += 1
    while j <= right:
        B.append(A[j])
        j += 1
    for i in range(left, right + 1):
        Ms += 1
        A[i] = B[i - left]


# 추가점수 3
# 3등분하여 재귀적으로 정렬한 후 merge한다.
# 이때, 3등분한 부분들을 재귀적으로 정렬하기 위해 3등분한 부분들을 각각의 배열로 만들어 정렬한다.
# 이후, 3등분한 부분들을 merge한다.
def three_way_merge_sort(A, left, right):
    global M1c, M1s
    if left >= right: return
    mid1 = left + (right - left) // 3
    mid2 = left + (right - left) // 3 * 2
    three_way_merge_sort(A, left, mid1)
    three_way_merge_sort(A, mid1 + 1, mid2)
    three_way_merge_sort(A, mid2 + 1, right)
    B = []
    i, j, k = left, mid1 + 1, mid2 + 1
    while i <= mid1 and j <= mid2 and k <= right:
        M1c += 2
        if A[i] <= A[j]:
            if A[i] <= A[k]:
                B.append(A[i])
                i += 1
            else:
                B.append(A[k])
                k += 1
        else:
            if A[j] <= A[k]:
                B.append(A[j])
                j += 1
            else:
                B.append(A[k])
                k += 1
    while i <= mid1 and j <= mid2:
        M1c += 1
        if A[i] <= A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    while i <= mid1 and k <= right:
        M1c += 1
        if A[i] <= A[k]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[k])
            k += 1
    while j <= mid2 and k <= right:
        M1c += 1
        if A[j] <= A[k]:
            B.append(A[j])
            j += 1
        else:
            B.append(A[k])
            k += 1
    while i <= mid1:
        B.append(A[i])
        i += 1
    while j <= mid2:
        B.append(A[j])
        j += 1
    while k <= right:
        B.append(A[k])
        k += 1
    for i in range(left, right + 1):
        M1s += 1
        A[i] = B[i - left]


# 기본적인 Heap Sort
# Heapify 모듈이나 Class를 사용하지 않고 구현하였다.
def heap_sort(A):
    global Hc, Hs
    n = len(A)
    for i in range(n):
        j = i
        while j > 0:
            Hc += 1
            if A[j] <= A[(j - 1) // 2]: break
            Hs += 1
            A[j], A[(j - 1) // 2] = A[(j - 1) // 2], A[j]
            j = (j - 1) // 2
    for i in range(n - 1, 0, -1):
        Hs += 1
        A[0], A[i] = A[i], A[0]
        j = 0
        while j * 2 + 1 < i:
            Hc += 1
            k = j * 2 + 1
            if k + 1 < i and A[k] < A[k + 1]: k += 1
            if A[j] >= A[k]: break
            Hs += 1
            A[j], A[k] = A[k], A[j]
            j = k


# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음


def check_sorted(A):
    for i in range(n - 1):
        if A[i] > A[i + 1]: return False
    return True


#
# Qc, Qs는 quick sort에서 비교, 교환(또는 이동) 횟수 저장
# Q1c, Q1s는 hybrid quick sort에서 비교, 교환(또는 이동) 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# M1c, M1s는 three-way merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Q1c, Q1s, Q2c, Q2s, Mc, Ms, M1c, M1s, Hc, Hs = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
K = random.randint(10, 40)
for i in range(n):
    A.append(random.randint(-1000, 1000))
B = A[:]
C = A[:]
D = A[:]
E = A[:]
F = A[:]
G = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))

print("Hybrid quick sort 1:")
print("time =", timeit.timeit("hybrid_quick_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Q1c, Q1s))

print("Hybrid quick sort 2: ")
print("time =", timeit.timeit("hybrid_quick_sort_2(C, 0, n-1, K)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Q2c, Q2s))

print("Merge sort:")
print("time =", timeit.timeit("merge_sort(D, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("3-way merge sort:")
print("time =", timeit.timeit("three_way_merge_sort(E, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(M1c, M1s))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(F)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

# Tim sort의 경우, 파이썬 내장 함수이므로 직접 구현할 필요가 없다.
# 따라서, 비교 횟수와 교환(또는 이동) 횟수를 직접 count할 수 없기에, 비교 횟수와 교환(또는 이동) 횟수를 count하는 코드를 작성하지 않았다.
print("Tim sort:")
print("time =", timeit.timeit("G.sort()", globals=globals(), number=1))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert (check_sorted(A))
assert (check_sorted(B))
assert (check_sorted(C))
assert (check_sorted(D))
assert (check_sorted(E))
assert (check_sorted(F))
assert (check_sorted(G))
