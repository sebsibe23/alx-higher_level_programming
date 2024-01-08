#!/usr/bin/node

// Conditional Statement
// Description: This block of code checks the length of the process.
// argv array and logs a corresponding message to the console.
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
