# It occurs when function call itself

#common recursion func
def greet():
    print("Hello")
    greet()

greet()

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(3))


# The Fibonacci sequence is a series where the next
# number is found by adding up the two numbers before it.

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
print(fibonacci(6))  # Output: 8


# calculate x^n using recursion

def power(x, n):
    if n == 0:  # Base case
        return 1
    return x * power(x, n - 1)  # Recursive case

# Example usage
print(power(2, 3))  # Output: 8
