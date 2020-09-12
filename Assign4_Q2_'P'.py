from Lib import *

# A matrix
with open("Matrix2.txt") as mat:
    A = []
    for line in mat:
        A.append(list(float(x) for x in line.split()))

# Identity matrix
with open("I.txt") as iden:
    B = []
    for line in iden:
        B.append(list(float(x) for x in line.split()))


def partial_pivot(A, B, k):  # Partial pivoting
    if A[k][k] == 0:
        for i in range(k + 1, 4):
            if abs(A[i][k]) > abs(A[k][k]) and abs(A[k][k]) == 0:
                A[k], A[i] = A[i], A[k]
                B[k], B[i] = B[i], B[k]
    return A, B


def LU_decomposition(A, B):  # LU Decomposition
    global D, H
    for j in range(len(A)):
        partial_pivot(A, B, j)
    n = len(A)
    for i in range(0, n):
        for j in range(0, n):
            if i == j or i < j:
                diff = 0
                for k in range(0, i):
                    diff += A[i][k] * A[k][j]
                A[i][j] = A[i][j] - diff
            if i > j:
                delta = 0
                for k in range(0, j):
                    delta += A[i][k] * A[k][j]
                A[i][j] = (1 / (A[j][j])) * (A[i][j] - delta)
    D = A
    H = B
    return A


def determinant(D):  # Finding the determinant
    det = 1
    for i in range(len(A)):
        det *= A[i][i]

    if det == 0:
        print("The inverse of the matrix does not exist.")
    else:
        print("Inverse of the matrix exists.")
    return det


def Forward(D, H):  # Performing forward substitution
    global M
    M = []
    for i in range(len(D)):
        M.append(fwrdsub(D, H[i]))
    return M


def Backward(D, M):  # Performing backward substitution
    global N, S
    N = []
    for i in range(len(D)):
        N.append(bkwdsub(D, M[i]))
    S = N
    return N


K = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


# Transpose of the X matrix will give us inverse of A


def transpose(S, K):
    for i in range(len(S)):
        # iterate through columns
        for j in range(len(S[0])):
            K[j][i] = S[i][j]
    return K


print("The LU decomposed A:", LU_decomposition(A, B))
print("The determinant of the matrix is:", determinant(D))
print("The forward substituted Y matrix is:", Forward(D, H))
print("The backward substituted X matrix is:", Backward(D, M))
print("\nThe inverse of the A matrix is: ", transpose(S, K))

"""
# *** OUTPUT: ***
The LU decomposed A: [[3.0, 7.0, 1.0, 0.0], [0.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, 2.0], [0.0, 2.0, 8.0, -12.0]]
Inverse of the matrix exists.
The determinant of the matrix is: -36.0
The forward substituted Y matrix is: [[0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, -8.0], [0.0, 1.0, 0.0, -2.0], [1.0, 0.0, 0.0, 0.0]]
The backward substituted X matrix is: [[-0.24, 0.08, 0.16, -0.08], [1.68, -0.67, -0.34, 0.67], [-1.82, 0.83, -0.34, 0.17], [0.33, 0.0, 0.0, 0.0]]

The inverse of the A matrix is:  [[-0.24, 1.68, -1.82, 0.33], [0.08, -0.67, 0.83, 0.0], [0.16, -0.34, -0.34, 0.0], [-0.08, 0.67, 0.17, 0.0]]
"""
