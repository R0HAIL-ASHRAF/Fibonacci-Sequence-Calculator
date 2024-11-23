import matplotlib.pyplot as plt
import numpy as np
import time

# Recursive Fibonacci function
# This function computes the n-th Fibonacci number using a simple recursive approach
# Time complexity: O(2^n) because it makes two recursive calls for each value of n
def recursive_fibonacci(n):
    if n <= 1:  # Base case: if n is 0 or 1, return n
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

# Memoization Fibonacci function
# This function computes the n-th Fibonacci number using a top-down dynamic programming approach with memoization
# Time complexity: O(n) because it stores the results of each Fibonacci number to avoid redundant calculations
memo = {}  # Dictionary to store previously computed Fibonacci numbers
def memo_fibonacci(n):
    if n in memo:  # If n is already computed, return the stored result
        return memo[n]
    if n <= 1:  # Base case: if n is 0 or 1, return n
        return n
    memo[n] = memo_fibonacci(n - 1) + memo_fibonacci(n - 2)  # Store the result in the dictionary
    return memo[n]

# Bottom-Up Fibonacci function
# This function computes the n-th Fibonacci number using a bottom-up dynamic programming approach
# Time complexity: O(n) because it builds the Fibonacci numbers iteratively
def bottom_up_fibonacci(n):
    if n <= 1:  # Base case: if n is 0 or 1, return n
        return n
    fib = [0, 1]  # Initialize the first two Fibonacci numbers
    for i in range(2, n + 1):  # Loop from 2 to n
        fib.append(fib[i - 1] + fib[i - 2])  # Compute the next Fibonacci number and append it to the list
    return fib[n]  # Return the n-th Fibonacci number

# Iterative Fibonacci function
# This function computes the n-th Fibonacci number using a simple iterative approach
# Time complexity: O(n) because it iteratively computes the Fibonacci numbers
def iterative_fibonacci(n):
    if n <= 1:  # Base case: if n is 0 or 1, return n
        return n
    a, b = 0, 1  # Initialize the first two Fibonacci numbers
    for _ in range(2, n + 1):  # Loop from 2 to n
        a, b = b, a + b  # Update the Fibonacci numbers
    return b  # Return the n-th Fibonacci number

# Function to measure the execution time of a Fibonacci function
# This function runs the given Fibonacci function for each value of n in n_values and records the time taken
def measure_time(fib_function, n_values):
    times = []  # List to store the execution times
    for n in n_values:  # Loop through each value of n
        start_time = time.time()  # Record the start time
        fib_function(n)  # Call the Fibonacci function
        times.append(time.time() - start_time)  # Record the elapsed time
    return times  # Return the list of execution times

n_values = np.arange(10, 31, 2)  # Generate an array of Fibonacci numbers to compute (10, 12, ..., 30)

# Measure execution times for each Fibonacci function
recursive_times = measure_time(recursive_fibonacci, n_values)
memo_times = measure_time(memo_fibonacci, n_values)
bottom_up_times = measure_time(bottom_up_fibonacci, n_values)
iterative_times = measure_time(iterative_fibonacci, n_values)

# Plotting the results
plt.figure(figsize=(10, 6))  # Create a new figure with a specific size
plt.plot(n_values, recursive_times, label="Recursive (O(2^n))")  # Plot the recursive times
plt.plot(n_values, memo_times, label="Memoization (O(n))")  # Plot the memoization times
plt.plot(n_values, bottom_up_times, label="Bottom-Up (O(n))")  # Plot the bottom-up times
plt.plot(n_values, iterative_times, label="Iterative (O(n))")  # Plot the iterative times
plt.xlabel('n (Fibonacci number)')  # Label the x-axis
plt.ylabel('Time (seconds)')  # Label the y-axis
plt.title('Time Complexity of Fibonacci Calculations')  # Set the title of the plot
plt.legend()  # Show the legend
plt.grid(True)  # Enable the grid
plt.show()  # Display the plot
