def christmas_tree(size):
  '''create christmas tree with "*" '''
  for i in range(size-1,-1,-1):
    s = ' '*i + '*'*((2*(size-i))-1)
    print(s)

def rhombus(size):
  '''create rhombus with "#" '''
  for i in range((size//2)+1):
    s = ' '*(size//2-i)   + '#'*(2*i+1)
    print(s)

  for i in range(size//2):
      s = ' '*(i+1) + '#'*(2*((size//2-1)-i)+1)
      print(s)

def trophy(size):
  for i in range(size):
    s =  ' '*i  + '='*(9+2*(size-3)-2*i)
    print(s)
    s = ' '*i + '=' + '#'*(len(s)-2-i)   +'='
    print(s)
  print(' '*(size+1) +'=')

  for i in range(size//2):
      s= ' '*(size-i) + '='*(3+2*i)
      s_ = ' '*(size-i) + '=' +'#'*(len(s)-(size-i)-2) +'='
      print(s_)
      if size%2!=0:
          if len(s) - (size-i) == size:
              break
      if size%2==0:
          if len(s) - (size-i) == size+1:
              break
      print(s)

def mjoinir(size):
    '''create the thor mjoinir hammer'''
    print(' '+'o'*(4+3*size))
    for i in range(1+2*size):
        print('o'*(6+3*size))
    print(' '+'o'*(4+3*size))
    for i in range(2+size):
        print(' '*(3+size) +'o'*size)
    for i in range(size):
        print(' '*(2+size)+'o'*(2+size))
    print(' '*(3+size) +'o'*size)

def square_sun(size):
  '''create square sun'''
  for i in range(size-1):
        s= ' '*i + '*' + ' '*(size-2+(2*((size-1)-i))) + '*'
        print(s)
  s = ' '*(size-1)+'*'*size
  print(s)

  for i in range(size-2):
        s=' '*(size-1) + '*' + ' '*(size-2) + '*'
        print(s)

  s = ' '*(size-1)+'*'*size
  print(s)

  for i in range(size-1):
        s= ' '*((size-1)-i-1) + '*' + ' '*(size+(2*i)) + '*'
        print(s)

