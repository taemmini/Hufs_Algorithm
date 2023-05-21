def left_allign(W, words):
    """
    각 단어들을 순서대로 확인하면서, penalty를 최소화하면서 한 줄에 최대한 많은 단어를 넣는 방식으로 문제를 해결한다.
    이렇게 삽입했을 때의 공백을 최소화한 값의 세제곱이 곧 penalty가 된다.
    이때 penalty를 최소화하는 방법은 다음과 같다.

    1. 첫 번째 단어부터 i번째 단어까지 한 줄에 넣는 경우를 고려한다.
        1.1 이 경우, 첫 번째 단어부터 i번째 단어까지 한 줄에 넣는 penalty는 penalties[i]가 된다.
    2. 첫 번째 단어부터 i번째 단어까지 여러 줄에 넣는 경우를 고려한다.
        2.1. 첫 번째 단어부터 j번째 단어까지 한 줄에 넣고, j+1번째 단어부터 i번째 단어까지 한 줄에 넣는 경우를 고려한다.
        2.2. 이 경우, 첫 번째 단어부터 j번째 단어까지 한 줄에 넣는 penalty는 penalties[j-1]이고, j+1번째 단어부터 i번째 단어까지 한 줄에 넣는 penalty는 penalties[i]가 된다.
        2.3. 따라서, 첫 번째 단어부터 i번째 단어까지 여러 줄에 넣는 penalty는 penalties[j-1] + penalties[i]가 된다.
    3. 첫 번째 단어부터 i번째 단어까지 한 줄에 넣는 경우와 여러 줄에 넣는 경우 중 penalty가 더 작은 값을 선택한다.

    :param W: 페이지 폭
    :param words: 입력 받은 문장
    :return: 최소 패널티
    """
    n = len(words)

    # word_lengths[i] = words[i]의 길이를 저장한다.
    # 각 줄의 penalty를 계산할 때, 해당 줄에 들어갈 단어의 길이를 알아야 하기 때문이다.
    word_lengths = []
    for i in range(n):
        word_lengths.append(len(words[i]))

    # penalties[i] = 첫 번째 단어부터 i번째 단어까지의 최소 패널티를 저장한다.
    # i번째 단어까지의 최소 peanlty를 추적하기 위함이다.
    penalties = [0] * (n + 1)

    # lines[i] = 한 문장이 끝나는 단어의 위치를 저장한다.
    # 줄바꿈이 일어날 경우, 이것이 어디서 이루어졌는지 추적하기 위함이다.
    lines = [0] * (n + 1)

    for i in range(1, n + 1):

        # 첫 번째 단어부터 i번째 단어까지 한 줄에 넣는 경우를 고려한다.
        # 이 경우 penalty는 이전 단어까지의 penalty에다 현재 단어를 추가하였을 때의 penalty를 더한 값이다.
        penalties[i] = penalties[i-1] + (W - word_lengths[i-1])**3
        # 단어를 추가하면 lines의 값도 1 증가한다.
        lines[i] = lines[i-1] + 1

        # 첫 번째 단어부터 i번째 단어까지 여러 줄에 넣는 경우를 고려한다.
        # 이때, 현재의 결과를 저장하기 위해 현재 줄에 이미 배치된 단어들의 총 길이를 저장하는 width 변수를 사용한다.
        width = word_lengths[i-1]
        for j in range(i-1, 0, -1):
            # 이전 단어와 그 단어의 길이(공백을 포함한다)를 width에 더한다.
            width += 1 + word_lengths[j - 1]
            # 만약 width가 W보다 크다면 더 이상 단어를 추가할 수 없으므로 반복을 멈춘다.
            if width > W:
                break
            # 첫 번째 단어부터 j번째 단어까지 한 줄에 넣고, 그 다음 줄부터 현재 단어까지 넣는 경우의 penalty를 계산한다.
            # 이때 penalty는 이전 단어까지의 penalty에다 현재 단어를 새로운 줄에 넣었을 때의 penalty를 더한 값이다.
            # 만약 이 값이 현재 penalty보다 작다면 penalty와 마지막으로 사용된 단어의 위치를 갱신한다.
            if penalties[j-1] + (W - width)**3 < penalties[i]:
                penalties[i] = penalties[j-1] + (W - width)**3
                lines[i] = lines[j-1] + 1

    return penalties[n]


W = int(input())
words = input().split()
print(left_allign(W, words))

# 해당 왼쪽 정렬의 DP 점화식은 penalties[i] = min(penalties[j-1] + (W - width)**3 for all j in [1, i])이다.
# penalties[i]는 이전에 계산한 penalties[j-1] 값에서 j번째 단어부터 i번쨰 단어까지 한 줄에 넣는 경우의 penalty를 더한 값의 최솟값이어야 하기 때문이다.
# 이를 통해 연산이 입력된 각 단어를 두고 이전 단어와 함께 고려하여 이루어진다는 것을 알 수 있다.
# 따라서 해당 알고리즘의 시간 복잡도는 O(n^2)이 된다.
