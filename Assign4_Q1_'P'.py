"""
Assignment: 4
Question: 1
"""
# A matrix
with open("Matrix1.txt") as mat:
    A = []
    for line in mat:
        A.append(list(float(x) for x in line.split()))
# B matrix
with open("B.txt") as val:
    B = []
    run = val.readline().split()
    for line in run:
        B.append(int(line))


def LU_decomposition(A):  # LU Decomposition
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


def forward_sub(A , B):  # Forward substitution
    global G
    # LU_decomposition(A)
    Y = []
    for k in range(len(A)):
        Y.append(float(0))  # A null matrix
    for i in range(0,len(A)):
        value = 0
        for j in range(0,i):
            value += A[i][j]*Y[j]
        Y[i] += B[i] - value  # Replacing the values
    G = Y
    return Y


G = forward_sub(A, B)


def backward_sub(A, B):  # Backward substitution
    X = []
    for k in range(len(A)):
        X.append(float(0))  # A null matrix
    for i in reversed(range(len(A))):
        value = 0
        for j in reversed(range(0,len(A))):
            if j > i:
                value += A[i][j]*X[j]
        X[i] += (1/A[i][i])*(B[i] - value)  # Replacing the values
    return X


print("The Memory efficient LU decomposed matrix A is", LU_decomposition(A))
print("The Y matrix is:", forward_sub(A, B))
print("The X matrix is:", backward_sub(A, G))


"""
Output : Q1
LU decomposed A matrix:[[1.0, 0.0, 1.0, 2.0], [0.0, 1.0, -2.0, 0.0], [1.0, 2.0, 2.0, -2.0], [2.0, 1.0, 1.5, -3.0]]
Y matrix:[6.0, -3.0, -2.0, -6.0]
X matrix:[1.0, -1.0, 1.0, 2.0]
"""






