def partial_pivot(A, B, k):
    if A[k][k] == 0:
        for i in range(k + 1, 4):
            if abs(A[i][k]) > abs(A[k][k]) and abs(A[k][k]) == 0:
                A[k], A[i] = A[i], A[k]
                B[k], B[i] = B[i], B[k]
    return A, B

def LU_decomposition(A, B):  # LU Decomposition
    for j in range(len(A)):
        partial_pivot(A, B, j)
    n = len(A)
    for i in range(0, n):
        for j in range(0, n):
            if i == j or i < j:
                diff = 0
                for k in range(0, i):
                    diff += A[i][k]*A[k][j]
                A[i][j] = A[i][j] - diff
            if i > j:
                delta = 0
                for k in range(0, j):
                    delta += A[i][k]*A[k][j]
                A[i][j] = (1/(A[j][j]))*(A[i][j] - delta)

    return A


def matrix_multiply(M, A):
    B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for x in range(len(M)):
        for y in range(len(A[0])):
            for z in range(len(M[0])):
                B[x][y] += M[x][z] * A[z][y]
    return B


def fwrdsub(A , B):
    global Y
    Y = []
    for k in range(len(A)):
        Y.append(float(0))
    for i in range(0,len(A)):
        val = 0
        for j in range(0,i):
            val+=A[i][j]*Y[j]
        Y[i] += B[i] - val
    return Y

def bkwdsub(A , B):
    global X
    X = []
    for k in range(len(A)):
        X.append(float(0))
    for i in reversed(range(len(A))):
        val = 0
        for j in reversed(range(0,len(A))):
            if j>i:
                val += A[i][j]*X[j]
        X[i] += round((1/A[i][i])*(B[i] - val), 2)
    return X
