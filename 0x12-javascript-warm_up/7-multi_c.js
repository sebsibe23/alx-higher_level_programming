#!/usr/bin/node

// Conditional Statement
// Description: This block of code checks if process.
// argv[2] is undefined or if it is not a number.
// If either condition is true, it logs
// 'Missing number of occurrences' to the console.
// Otherwise, it initializes a variable x with
// the numeric value of process.argv[2].
// Then, it declares a variable i and sets it to 0.
// It enters a while loop that executes as long as i is less than x.
// Inside the loop, it logs the string 'C is fun'
// to the console and increments the value of i by 1.
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const x = Number(process.argv[2]);
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
