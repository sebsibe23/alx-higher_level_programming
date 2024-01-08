#!/usr/bin/node
let args = process.argv.slice(2);
let size = Number(args[0]);
if (isNaN(size) || size < 1) {
    console.log("Missing size");
} else {
    for (let i = 0; i < size; i++) {
        console.log("X".repeat(size));
    }
}
