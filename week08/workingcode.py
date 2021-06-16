
def fibonacci(n, remember = None):
    # If this is the first time calling the function, then
    # we need to create the dictionary.
    if remember is None:
        remember = dict()

    # Base Case
    if n <= 2:
        return 1

    # Check if we have solved this one before
    if n in remember:
        return remember[n]

    # Otherwise solve with recursion
    result = fibonacci(n-1, remember) + fibonacci(n-2, remember)

    # Remember result for potential later use
    remember[n] = result
    return result

print(fibonacci(1))    # 1
print(fibonacci(2))    # 1
print(fibonacci(3))    # 2
print(fibonacci(4))    # 3
print(fibonacci(10))   # 55
print(fibonacci(100))  # 354224848179261915075 (This one will
                       # not work if you don't have the 
                       # 'remember' dictionary implemented).
