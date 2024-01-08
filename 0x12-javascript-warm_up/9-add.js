#!/usr/bin/node

/*
 * This Node.js script defines a function named 'add' that takes two parameters
 * 'a' and 'b'. It calculates the sum of 'a' and 'b', and prints the result.
 * The script then calls the 'add' function with the first two command-line
 * arguments (excluding the default ones) converted to numbers.
 */

function add (a, b) {
  const c = a + b;
  console.log(c);
}

add(Number(process.argv[2]), Number(process.argv[3]));
