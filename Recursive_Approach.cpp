#include <iostream> // Include the iostream library for input and output operations

using namespace std; // Use the standard namespace to avoid typing 'std::' before standard functions

// Recursive function to compute the nth Fibonacci number
int fibonacci_recursive(int n) {
    // Base case: If the input n is less than or equal to 0, return 0 as Fibonacci numbers are defined for positive integers
    if (n <= 0) return 0;

    // Base case: If the input n is 1, return 0 as the first Fibonacci number is 0
    if (n == 1) return 0;

    // Base case: If the input n is 2, return 1 as the second Fibonacci number is 1
    if (n == 2) return 1;

    // Recursive case: Compute the nth Fibonacci number as the sum of the (n-1)th and (n-2)th Fibonacci numbers
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2);
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
    int result = fibonacci_recursive(n);

    // Print the result to the console
    cout << "The Fibonacci number at position " << n << " is " << result << endl;

    // Return 0 to indicate successful completion of the program
    return 0;
}
