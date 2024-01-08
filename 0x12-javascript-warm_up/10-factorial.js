#!/usr/bin/node

/*
 * This Node.js script defines a recursive function named 'factorial' that takes
 * a single parameter 'n'. If 'n' is less than 0, it returns -1. If 'n' is 0 or
 * not a number, it returns 1. Otherwise, it returns the product of 'n' and the
 * factorial of 'n-1'. The script then calls the 'factorial' function with the
 * first command-line argument (excluding the default ones) converted to a number
 * and prints the result.
 */

function factorial (n) {
  if (n < 0) {
    return (-1);
  }
  if (n === 0 || isNaN(n)) {
    return (1);
  }
  return (n * factorial(n - 1));
}

console.log(factorial(Number(process.argv[2])));
