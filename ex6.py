def solution(A):
    N = len(A)
    for i in range(1, 2147483648):
        if i not in A:
            return i
