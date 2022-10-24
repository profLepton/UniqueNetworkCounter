import math

def fact(n):
    return math.factorial(n)

def nCr(n, r):
    return fact(n) // (fact(r) * fact(n-r))

def graphs_count(n):
    graphs = 0
    for i in range(0, int(n*(n-1)/2)+1):
            graphs += nCr(int(n*(n-1)/2), i)
    return graphs 

for i in range(10):
    print(i, " > ", graphs_count(i))

