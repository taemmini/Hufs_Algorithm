def max_sum(_list, left, right):

    """
    최대 구간의 합을 구하는 함수이다. 이때, 최대 구간의 합이 왼쪽에만 있거나, 오른쪽에만 있거나, 양쪽에 걸쳐 있을 수 있다.
    따라서, 이 세 가지 경우를 모두 고려하여 최대 구간의 합을 구해야 한다. 이때, 최대 구간의 합이 왼쪽에만 있거나, 오른쪽에만 있을 경우는
    재귀적으로 구할 수 있으므로, 이를 이용하여 최대 구간의 합을 구한다. 최대 구간의 합이 양쪽에 걸쳐 있을 경우는 max_cross_sum()을 통해 구한다.
    """

    # left와 right가 같으면 리스트의 요소가 하나라는 것을 의미하므로, A[0]이 최대 구간의 합이 된다.
    if left == right:
        return _list[left]

    mid = (left + right) // 2
    left_sum = max_sum(_list, left, mid)
    right_sum = max_sum(_list, mid + 1, right)
    cross_sum = max_sum_crossed(_list, left, mid, right)
    return max(left_sum, right_sum, cross_sum)


def max_sum_crossed(_list, left, mid, right):
    """
    구간의 최대합이 L과 R에 걸쳐있을 경우의 최대합을 구하는 함수이다.
    이때, L의 경우는 L의 가장 끝부터 하나씩 왼쪽으로 가면서 최대합을 구한다.
    R의 경우는 R의 가장 앞부터 하나씩 오른쪽으로 가면서 최대합을 구한다.
    """

    # 왼쪽 합, 오른쪽 합, 각각에 사용할 임시합 초기화
    # 이때 왼쪽 합과 오른쪽 합 중 하나의 모든 요소가 음수일 수 있으므로, '-inf'로 초기화한다.
    left_sum = float('-inf')
    right_sum = float('-inf')
    temp_sum = 0

    for i in range(mid, left - 1, -1):
        temp_sum += _list[i]
        if temp_sum > left_sum:
            left_sum = temp_sum

    temp_sum = 0
    for i in range(mid + 1, right + 1):
        temp_sum += _list[i]
        if temp_sum > right_sum:
            right_sum = temp_sum

    return left_sum + right_sum

# 이때 T(n) 점화식은 T(n) = 2T(n/2) + O(n)이다.
# 여기서, 2T(n/2)는 왼쪽 절반과 오른쪽 절반의 최대 구간 합을 각각 계산하는데 사용되는 비용이다.
# O(n)은 최대 구간의 합이 양쪽에 걸쳐 있을 경우를 계산하는데 사용되는 비용이다.
# 따라서, 이 알고리즘의 시간 복잡도는 O(nlogn)이다.

arr = [int(x) for x in input().split()]
sol = max_sum(arr, 0, len(arr) - 1)
print(sol)
