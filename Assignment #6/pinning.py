def pinning(n, strips):
    """
    막대들을 최소 못의 개수로 박기 위해, 오른쪽 끝점에 따라 정렬한다.
    오른쪽 끝점이 작은 순서대로 정렬하면 최소성을 보장할 수 있기 때문이다.
    이전에 박혀있는 못의 위치보다 막대의 왼쪽 끝점이 더 크다면, 해당 막대의 오른쪽 끝점에 못을 박는다.

    여기서 수행시간은 막대를 정렬하는 작업과, 필요한 못의 최소 개수를 세는 작업 각각으로 이루어진다.
    이때, 정렬은 sort 함수를 사용하였기에 O(nlogn)의 시간 복잡도를 가진다.
    못의 최소 개수를 세는 작업은 O(n)의 시간 복잡도를 가진다.
    이 두 작업은 의족적으로 이루어지는 것이 아니므로, 두 작업의 시간 복잡도는 O(nlogn)이다.

    :param n: 막대의 개수
    :param strips: 막대의 길이
    :return: 최소 못의 개수
    """
    # 오른쪽 끝점에 따라 정렬
    strips.sort(key=lambda x: x[1])
    # 첫 번째 막대에 못을 박기
    last = strips[0][1]
    nails = 1
    # 나머지 막대들 확인
    for i in range(1, n):
        # 만약 현재 막대가 이전에 박은 못으로 커버되지 않으면
        if strips[i][0] > last:
            # 현재 막대에 새로운 못을 박기
            nails += 1
            last = strips[i][1]
    return nails

n = int(input().strip())
strips = []
for _ in range(n):
    a, b = map(int, input().strip().split())
    strips.append((a, b))

print(pinning(n, strips))
