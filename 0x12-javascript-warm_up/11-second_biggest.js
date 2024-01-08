#!/usr/bin/node

/*
 * This is a Node.js script that takes command-line arguments, excluding the
 * first two default arguments. If the number of arguments is less than or
 * equal to 3, it prints '0'. Otherwise, it converts the arguments into an
 * array of numbers, sorts them in descending order, and prints the second
 * largest number.
 */

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = process.argv.slice(2).map(Number);
  const second = arr.sort(function (a, b) { return b - a; })[1];
  console.log(second);
}
