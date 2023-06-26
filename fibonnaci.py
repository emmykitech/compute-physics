def fibonacci(n):
    series = [0,1] # Starting numbers
    while len(series) < n:
        series.append(series[-1]+ series[-2])
    return series

fibonacci_series = fibonacci(10)

print(fibonacci_series)