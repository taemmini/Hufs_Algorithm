arr = list(map(int, input().split()))


def finding_max_index(A):
    """
    오름차순으로 정렬된 리스트에서 조건에 따른 회전이 이루어졌다면, 회전이 이루어진 횟수는 전체 리스트 길이에서
    리스트 내 최고값을 가지는 메모리 위치를 뺀 값으로 나타낼 수 있을 것이다. 다음 함수는 리스트 내 최고값의
    메모리 인덱스를 찾아내는 함수이다. 이때, 이진 탐색을 이용하여 최고값의 메모리 인덱스를 찾아낸다.
    이때, 비교는 리스트를 절반씩 나누는 과정을 값이 도출될 때까지 반복한다.
    따라서, 총 비교 횟수는 log2(len(A))회 이루어지므로, 시간 복잡도는 O(log n)이다.
    :param A: 입력 받을 리스트
    :return: 최고값의 메모리 인덱스
    """
    left, right = 0, len(A) - 1

    while left < right:
        mid = (left + right) // 2

        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid

    return left

def rotation_count(A):
    """
    finding_max_index() 함수를 통해 최고값의 메모리 위치를 찾고, 이를 통해 회전 횟수를 구한다.
    이떄, 봉우리 메모리 위치가 0이라면 회전이 이루어지지 않았다는 것이므로, 0을 반환한다.
    여기서 비교는 find_max_index() 함수를 호출하여 값을 비교하는 행위밖에 하지 않는다.
    따라서, 총 비교는 log2(len(A)) + 1번 이루어지므로, 시간 복잡도는 O(log n)이다.
    :param A: 입력 받을 리스트
    :return: 회전한 횟수
    """
    if finding_max_index(A) == 0:
        return 0
    else:
        return len(A) - finding_max_index(A)


print(rotation_count(arr))