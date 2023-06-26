def fibonacci(n):
    series = [0,1] # Starting numbers
    while len(series) < n:
        series.append(series[-1]+ series[-2])
    return series

# Generate the Fibonacci sequence with 10 terms
fibonacci_sequence = fibonacci(40)

print(fibonacci_sequence)