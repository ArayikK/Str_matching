def naive_match(T, P):

    n, m = len(T), len(P)
    if n < m:
        return False

    for t in range(n - m):
        for p in range(m):
            if T[t + p] != P[p]:
                break
        else:
            return True
    return False
        

print(naive_match("acaabc", "aac"))