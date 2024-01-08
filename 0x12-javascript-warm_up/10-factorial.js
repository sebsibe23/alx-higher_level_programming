#!/usr/bin/node

// Function: factorial
// Description: This function calculates the factorial of a given number.
// It checks if the number is less than 0 and returns -1 in such cases.
// It also handles the case when the number is 0 or NaN and returns 1.
// For other positive numbers, it recursively calculatesi
// the factorial by multiplying the number with the factorial of (n-1).
function factorial(n) {
  if (n < 0) {
    return (-1);
  }
  if (n === 0 || isNaN(n)) {
    return (1);
  }
  return (n * factorial(n - 1));
}

// Output: Factorial
// Description: This line logs the factorial of the numeric
// value of process.argv[2] to the console.
console.log(factorial(Number(process.argv[2])));
