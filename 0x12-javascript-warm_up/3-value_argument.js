#!/usr/bin/node

// Conditional Statement
// Description: This block of code checks if process.
// argv[2] is undefined and logs a corresponding message to the console. 
// If process.argv[2] is defined, it logs the value of process.argv[2].
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
