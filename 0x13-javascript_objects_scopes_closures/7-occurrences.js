#!/usr/bin/node

/**
 * Counts the number of occurrences of
 * a given element in a list.
 * @param {Array} list - The list to search in.
 * @param {*} searchElement - The element
 * to search for.
 * @returns {number} - The number of occurrences
 * of the search element in the list.
 */
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
