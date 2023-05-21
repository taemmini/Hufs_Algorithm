def longest_palindrome_subsequence(word):
    """
    문자열 s의 부수열 중 가장 긴 회문의 길이를 출력한다.
    시작 문자와 끝 문자가 같을 경우의 회문의 길이는 이전 부분 문자열의 회문 길이에서 2를 더한 것과 같다.
    시작 문자와 끝 문자가 다를 경우의 회문의 길이는 현재 부분 문자열에서 마지막 문자(왼쪽 이웃 값), 혹은 첫 문자(오른쪽 이웃 값)을 제외한 부분 문자열의 회문 길이 중 큰 값과 같다.
    이 점을 활용하여 모든 가능한 문자열에 대해 DP테이블을 채우고, DP테이블의 마지막 요소를 출력한다. 이유는 DP테이블의 마지막 요소가 가장 긴 회문의 길이이기 때문이다.
    이럴 경우의 수행 시간은 입력 문자열의 길이 n * n의 테이블을 채워야 한다는 점에서 O(n^2)이다.
    ::param s: 문자열
    ::return: 가장 긴 회문의 길이
    """

    # DP테이블을 2차원 리스트로 초기화한다.
    n = len(word)
    table = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        table.append(row)

    # 길이가 1인 부분 문자열에 대해 회문의 길이는 항상 1이므로, DP테이블의 대각선 요소는 모두 1로 초기화한다.
    for i in range(n):
        table[i][i] = 1

    # 길이가 2 이상인 부분 문자열을 DP 테이블에 채운다.
    for subsequence in range(2, n + 1):
        for i in range(n - subsequence + 1):
            j = i + subsequence - 1
            if word[i] == word[j] and subsequence == 2:
                table[i][j] = 2
            elif word[i] == word[j]:
                table[i][j] = table[i + 1][j - 1] + 2
            else:
                table[i][j] = max(table[i][j - 1], table[i + 1][j])

    # DP 테이블의 마지막 요소가 문자열의 회문 중 가장 긴 회문의 길이므로, 이를 출력한다.
    return table[0][n - 1]


s = input()
print(longest_palindrome_subsequence(s))
