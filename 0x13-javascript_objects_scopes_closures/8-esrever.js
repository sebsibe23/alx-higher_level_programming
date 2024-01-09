#!/usr/bin/node

/**
 * Reverses the elements in a given list.
 * @param {Array} list - The list to reverse.
 * @returns {Array} - The reversed list.
 */
exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  while ((len - i) > 0) {
    const aux = list[len];
    list[len] = list[i];
    list[i] = aux;
    i++;
    len--;
  }
  return list;
};
