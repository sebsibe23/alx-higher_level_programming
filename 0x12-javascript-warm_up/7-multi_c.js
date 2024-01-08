#!/usr/bin/node
let args = process.argv.slice(2);
let num = Number(args[0]);
if (isNaN(num) || num < 1) {
    console.log("Missing number of occurrences");
} else {
    for (let i = 0; i < num; i++) {
        console.log("C is fun");
    }
}
