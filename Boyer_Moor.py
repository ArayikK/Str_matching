def boyer_moor(T, P):
    n, m = len(T), len(P)

    L = {} 
    for i in range(m):
        if i == m - 1:
            if P[i] in L:
                break
            else:
                L[P[i]] = m
                break
            
        L[P[i]] = m - i - 1

    i = 0 
    while i <= n - m:
        for j in range(m - 1, -2, -1):
            if j == -1:
                return f"Found at index {i}"
            if T[i + j] != P[j]:
                break
                
        
        i = i + L[T[i + j]] if T[i + j]  in L else i + m
    return "FAIL"


print(boyer_moor("trusthardtoothbrushes", "aer"))
    