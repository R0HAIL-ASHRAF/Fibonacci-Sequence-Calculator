#include <iostream> // Include the iostream library for input and output operations

using namespace std; // Use the standard namespace to avoid typing 'std::' before standard functions

// Function to compute the nth Fibonacci number using an iterative approach
int fibonacci_iterative(int n) {
    // If the input n is less than or equal to 0, return 0 as Fibonacci numbers are defined for positive integers
    if (n <= 0) return 0;

    // If the input n is 1, return 0 as the first Fibonacci number is 0
    if (n == 1) return 0;

    // If the input n is 2, return 1 as the second Fibonacci number is 1
    if (n == 2) return 1;

    // Initialize variables to store the previous two Fibonacci numbers
    int a = 0; // This will store F(0)
    int b = 1; // This will store F(1)
    int c; // This will be used to store the current Fibonacci number being calculated

    // Iterate from 3 up to n (inclusive) to calculate Fibonacci numbers iteratively
    for (int i = 3; i <= n; i++) {
        // Calculate the next Fibonacci number as the sum of the previous two
        c = a + b;

        // Update the values of a and b for the next iteration
        a = b; // Move b to a
        b = c; // Move the newly calculated c to b
    }

    // Return the last computed Fibonacci number, which is stored in b
    return b;
}

// Main function to test the Fibonacci function
int main() {
    // Declare a variable to store the position in the Fibonacci sequence
    int n;

    // Prompt the user to enter a position in the Fibonacci sequence
    cout << "Enter the position in the Fibonacci sequence: ";

    // Read the user's input
    cin >> n;

    // Call the Fibonacci function and store the result
    int result = fibonacci_iterative(n);

    // Print the result to the console
    cout << "The Fibonacci number at position " << n << " is " << result << endl;

    // Return 0 to indicate successful completion of the program
    return 0;
}
