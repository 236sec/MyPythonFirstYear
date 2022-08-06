def zero_by_matrix(A):
  zero_ma = []
  for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
      row.append(0)
    zero_ma.append(row)
  return zero_ma

def zero_by_row(row,y):
  zero_ma = []
  for i in range(row):
    row_ = []
    for j in range(y):
      row_.append(0)
    zero_ma.append(row_)
  return zero_ma

def get_row(A):
  row = len(A)
  y = len(A[0])
  return row,y

def plus_matrix(A,B):
  C = zero_by_matrix(A)
  for i in range(len(A)):
    for j in range(len(A[i])):
      C[i][j] = A[i][j] + B[i][j]
  return C

def minus_matrix(A,B):
  C = zero_by_matrix(A)
  for i in range(len(A)):
    for j in range(len(A[i])):
      C[i][j] = A[i][j] - B[i][j]
  return C

def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      print(f'{A[i][j]:^6}', end = ' ')
    print()

def transpose_matrix(A):
  row , y = get_row(A)
  C = zero_by_row(y,row)
  for i in range(len(A)):
    for j in range(len(A[0])):
      C[j][i]=A[i][j]
  return C


def mul_matrix(A,B):
  C = transpose_matrix(B)
  D = zero_by_matrix(A)
  for k in range(len(A)):
    for t in range(len(B)):
      summ = 0
      for l in range(len(A[0])):
        summ += A[k][l]*C[t][l]
      D[k][t] = summ
  return D

def mul_const(A,c):
  ze = zero_by_matrix(A)
  for i in range(len(A)):
    for j in range(len(A[i])):
      ze[i][j] = A[i][j]*c
  return ze

A = [[1,4],[2,5],[3,6]]
B = [[1,2],[3,4]]
print_matrix(mul_matrix(A,B))

