import sys
from heapq import heapify, heappop


def rearrangement(arr, k):
    """
    arr를 heapify를 활용하여 heap 구조로 구현해준 후, k번째로 작은 수를 heapop를 활용해 출력한다.
    이때, k번째로 작은 수를 찾는데 O(logN)의 시간 복잡도가 요구된다. 이때, 전체 리스트를 순회해야 하므로, 시간복잡도는 O(NlogN)이 된다.
    """
    heapify(arr)

    result = 0

    for i in range(k):
        result = heappop(arr)

    return result


def summing_m(arr):
    """
    조건에 만족하는 리스트를 생성하기 위해 k를 (i//3) + 1로 치환한 후, rearrangement에서 k번째로 작은 값들을 리스트에 저장한다.
    마지막으로, 완성된 리스트의 합을 반환한다. 이때, rearrangement를 n번 순회하는데, 최종적인 시간 복잡도는 O(N^2logN)이 된다.
    """
    n = len(arr)
    m = []

    for i in range(n):
        k = (i // 3) + 1
        m.append(rearrangement(arr[:i + 1], k))  # 리스트의 메모리 주소는 0부터 시작하므로, i를 그대로 사용하면 안된다.

    return m


_lst = list(map(int, sys.stdin.readline().split()))
print(summing_m(_lst))
