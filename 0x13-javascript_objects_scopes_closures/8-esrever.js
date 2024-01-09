#!/usr/bin/node

/**
 * Reverses the elements in a given list.
 * @param {Array} list - The list to reverse.
 * @returns {Array} - The reversed list.
 */
exports.esrever = function (list) {
  let varlen = list.length - 1;
  let j = 0;
  while ((varlen - j) > 0) {
    const aux = list[varlen];
    list[varlen] = list[j];
    list[j] = aux;
    j++;
    varlen--;
  }
  return list;
};
