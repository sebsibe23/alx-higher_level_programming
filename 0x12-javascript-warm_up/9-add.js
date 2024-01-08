#!/usr/bin/node

// Function: add
// Description: This function takes two parameters,
// a and b, and calculates their sum.
// It assigns the sum to a variable called tot
// and logs it to the console.
function add(a, b) {
  const tot = a + b;
  console.log(tot);
}

// Function Call: add
// Description: This line calls the add function,
// passing the numeric values of process.argv[2]
// and process.argv[3] as arguments.
add(Number(process.argv[2]), Number(process.argv[3]));
