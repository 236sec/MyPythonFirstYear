def zero_by_matrix(A):
  '''create zero matrix by using matrix'''
  zero_ma = []
  for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
      row.append(0)
    zero_ma.append(row)
  return zero_ma

def zero_by_row(row,y):
  '''create zero matrix by using row and column'''
  zero_ma = []
  for i in range(row):
    row_ = []
    for j in range(y):
      row_.append(0)
    zero_ma.append(row_)
  return zero_ma

def get_row(A):
  '''return row and column'''
  row = len(A)
  y = len(A[0])
  return row,y

def plus_matrix(A,B):
  '''plus operation between two matrix'''
  C = zero_by_matrix(A)
  for i in range(len(A)):
    for j in range(len(A[i])):
      C[i][j] = A[i][j] + B[i][j]
  return C

def minus_matrix(A,B):
  '''minus operation between two matrix'''
  C = zero_by_matrix(A)
  for i in range(len(A)):
    for j in range(len(A[i])):
      C[i][j] = A[i][j] - B[i][j]
  return C

def print_matrix(A):
  '''print beautiful matrix easy to read'''
  for i in range(len(A)):
    for j in range(len(A[i])):
      print(f'{A[i][j]:^6}', end = ' ')
    print()

def transpose_matrix(A):
  '''return transpose of matrix'''
  row , y = get_row(A)
  C = zero_by_row(y,row)
  for i in range(len(A)):
    for j in range(len(A[0])):
      C[j][i]=A[i][j]
  return C


def mul_matrix(A,B):
  '''multiple between two matrix'''
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
  '''multiple  matrix with const'''
  ze = zero_by_matrix(A)
  for i in range(len(A)):
    for j in range(len(A[i])):
      ze[i][j] = A[i][j]*c
  return ze

def power_matrix(A,c):
  '''return multiple A matrix c times'''
  tmp = A
  for i in range(c-1):
    A = mul_matrix(A,tmp)
  return A

def find_det_2x2(A):
  '''return det of 2x2 matrix'''
  return (A[0][0]*A[1][1]) - (A[0][1]*A[1][0])

def find_det_3x3(A):
  '''return det of 3x3 matrix'''
  pl = A[0][0]*A[1][1]*A[2][2] + A[0][1]*A[1][2]*A[2][0] + A[0][2]*A[1][0]*A[2][1]
  do = A[2][0]*A[1][1]*A[0][2] + A[2][1]*A[1][2]*A[0][0] + A[2][2]*A[1][0]*A[0][1]
  return pl - do

def get_matrix(row,column):
  '''get values from input and return it in matrix'''
  re = []
  for ro in range(row):
    row_list = [int(i) for i in input(f'Row {ro+1} : ').split()]
    '''check that is correct collumn'''
    if len(row_list)!=column:
      print('Error')
      break
    re.append(row_list)
  return re

