#!/usr/bin/node

const list = require('./100-data.js').list;

console.log(list);

/**
 * Maps each element of the list to the product
 * of the element and its index.
 * @param {number} item - The current element.
 * @param {number} index - The index of the
 * current element.
 * @returns {number} - The product of the
 * element and its index.
 */
console.log(list.map((item, index) => item * index));
