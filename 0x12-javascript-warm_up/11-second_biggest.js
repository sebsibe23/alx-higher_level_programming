#!/usr/bin/node
let args = process.argv.slice(2).map(Number);
if (args.length <= 1) {
    console.log(0);
} else {
    args.sort((a, b) => b - a);
    let unique = [...new Set(args)];
    console.log(unique[1]);
}
