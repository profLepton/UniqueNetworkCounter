def graph_count(n):
    return int(pow(2, n*(n-1)/2))

for i in range(10):
    print(f"{i} > {graph_count(i)}")