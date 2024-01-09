#!/usr/bin/node

// Import the 'fs' module for file system operations
const fs = require('fs');

// Read the contents of the first file specified as the third command-line argument
const fArg = fs.readFileSync(process.argv[2]).toString();

// Read the contents of the second file specified as the fourth command-line argument
const sArg = fs.readFileSync(process.argv[3]).toString();

// Concatenate the contents of the two files
const concatenatedContent = fArg + sArg;

// Write the concatenated content to the file specified as the fifth command-line argument
fs.writeFileSync(process.argv[4], concatenatedContent);
