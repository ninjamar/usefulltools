class Math:
  def fib(n):
    list = []
    a, b = 0, 1
    while a < n:
      list.append(a)
      a, b = b, a+b
    return list
