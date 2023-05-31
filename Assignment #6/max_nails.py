def max_bars(n, bars):
    """
    막대가 가장 많이 겹치는 구간을 구하는 것과 같은 문제이다.
    막대의 왼쪽과 오른쪽 끝점을 모두 모아 각각 오름차순으로 정리한 뒤,
    정렬 순서에 따라 하나씩 순회하며 왼쪽 끝 점일 때 1씩 증가시키고, 오른쪽 끝 점일 때 1씩 감소시킨다.

    이 경우, 정렬에 Tim Sort를 사용하면서 O(nlogn)의 시간 복잡도를 가진다.
    정렬된 리스트를 순회하면서 막대의 수를 증가시키거나 감소시키는 작업은 O(n)의 시간 복잡도를 가진다.
    이 두 작업은 의존적으로 이루어지는 것이 아니므로, 두 작업의 시간 복잡도는 O(nlogn)이다.

    :param n: 입력되는 막대의 개수
    :param bars: 막대의 왼쪽 끝점과 오른쪽 끝점
    :return: 하나의 못으로 꽂을 수 있는 막대의 최대 개수, 즉 막대가 가장 많이 겹치는 지점의 막대 개수
    """
    assert len(bars) == n # 입력된 값과 막대의 개수가 일치하는지 확인한다.

    # 왼쪽 끝 점과 오른쪽 끝 점을 감소시키기 위해 각각 1과 -1로 표시한다.
    points = []
    for a, b in bars:
        points.append((a, 1))  # 왼쪽 끝점에 해당하면, 1을 append한다.
        points.append((b, -1))  # 오른쪽 끝점에 해당하면, -1을 append한다.

    # x 좌표에 따라 오름차순 정렬하고, 같은 x 좌표에서는 '-1' 표시가 '1' 표시보다 먼저 오도록 정렬
    points.sort(key=lambda x: (x[0], -x[1]))

    max_bars_count = 0
    current_bars_count = 0

    for _, delta in points:
        current_bars_count += delta  # 각각의 point 요소의 증감값을 갱신한다.
        if delta == 1: # delta가 1이라면, 수직선이 새로운 막대의 왼쪽 끝점에 도달했다는 것을 의미한다.
            max_bars_count = max(max_bars_count, current_bars_count)  # 따라서, 현재 막대의 개수와 최대 막대의 개수를 비교한다.

    return max_bars_count


n = int(input())
bars = [list(map(int, input().split())) for _ in range(n)]

print(max_bars(n, bars))
