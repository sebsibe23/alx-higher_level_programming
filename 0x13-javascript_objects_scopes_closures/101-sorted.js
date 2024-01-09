#!/usr/bin/node

// Import the 'dict' object from the '101-data' module
const dict = require('./101-data').dict;

// Convert the 'dict' object into an array of [key, value] pairs
const totalist = Object.entries(dict);

// Extract the values from the 'dict' object
const vals = Object.values(dict);

// Get the unique values from the 'vals' array
const valsUniq = [...new Set(vals)];

// Create a new empty dictionary
const newDict = {};

// Loop through each unique value
for (const j in valsUniq) {
  const list = [];

  // Loop through each [key, value] pair in the 'totalist' array
  for (const k in totalist) {
    // If the value of the pair matches the current unique value
    if (totalist[k][1] === valsUniq[j]) {
      // Add the key to the beginning of the 'list' array
      list.unshift(totalist[k][0]);
    }
  }

  // Assign the 'list' as the value for the current unique value in the 'newDict' dictionary
  newDict[valsUniq[j]] = list;
}

// Print the 'newDict' dictionary
console.log(newDict);
