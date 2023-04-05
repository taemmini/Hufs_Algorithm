def max_sum(A, left, right):
    # left와 right가 같으면 리스트의 요소가 하나라는 것을 의미하므로, A[0]이 최대 구간의 합이 된다.
    if left == right:
        return A[0]

    # 리스트를 반으로 나누어 각각의 최대 구간 합을 구한다.
    mid = (left + right) // 2
    left_sum = max_sum(A, left, mid)
    right_sum = max_sum(A, mid + 1, right)
    cross_sum = max_cross_sum(A, left, mid, right)
    return max(left_sum, right_sum, cross_sum)


def max_cross_sum(A, left, mid, right):
    left_sum = 0
    right_sum = 0
    sum = 0
    for i in range(mid, left - 1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
    sum = 0
    for i in range(mid + 1, right + 1):
        sum += A[i]
        if sum > right_sum:
            right_sum = sum
    return left_sum + right_sum

# A[left], ..., A[right] 중 최대 구간 합 리턴

A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A) - 1)
print(sol)