#!/usr/bin/node

let strnarg = 0;

/**
 * Logs the given item along with a sequential number.
 * @param {*} item - The item to log.
 */
exports.logMe = function (item) {
  console.log(strnarg + ': ' + item);
  strnarg++;
};
