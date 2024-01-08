#!/usr/bin/node

// Conditional Statement
// Description: This block of code checks if process.argv[2]
// is not a number or if it is undefined.
// If either condition is true, it logs 'Not a number'
// to the console.
// Otherwise, it logs 'My number:' followed by the
// parsed integer value of process.argv[2].
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(process.argv[2]));
}
