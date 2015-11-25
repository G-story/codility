def solution(A):
    ret = 0
    min_avg = float(A[0] + A[1]) / 2
    for i in xrange(len(A) - 1):
        sum = A[i]
        for j in xrange(i + 1, len(A)):
            sum += A[j]
            avg = float(sum) / (j - i + 1)
            if avg < min_avg:
                min_avg = avg
                ret = i
    return ret


print(solution([4, 2, 2, 5, 1, 5, 8]))
