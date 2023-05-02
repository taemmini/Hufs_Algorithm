import heapq


def find_m(A):
    min_heap = []
    max_heap = []
    m = []
    for i, value enumerate(A):
        if len(max_heap) <= i // 3 + 1:
            heapq.heappush(max_heap, -A[i])
        else:
            if A[i] < -max_heap[0]:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
                heapq.heappush(max_heap, -A[i])
            else:
                heapq.heappush(min_heap, A[i])
        m.append(-max_heap[0])
    return sum(m)


_list = list(map(int, input().split()))
print(find_m(_list))