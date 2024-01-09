#!/usr/bin/node

/**
 * Returns a function that converts a number to
 * a string representation in the specified base.
 * @param {number} base - The base to use for
 * the conversion.
 * @returns {function} - The conversion function.
 */
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
