#!/usr/bin/node
function add (a, b) {
  const tot = a + b;
  console.log(tot);
}

add(Number(process.argv[2]), Number(process.argv[3]));
