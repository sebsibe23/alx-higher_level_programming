#!/usr/bin/node

const SquareP = require('./5-square');

/**
 * Class representing a square.
 * @extends SquareP
 */
class Square extends SquareP {
  /**
   * Print a visual representation of the
   * square using the specified character.
   * If no character is provided, 'X' is used.
   * @param {string} [f='X'] - The character
   * to use for printing the square.
   */
  charPrint (f) {
    if (f === undefined) {
      f = 'X';
    }
    for (let h = 0; h < this.height; h++) {
      let n = '';
      for (let k = 0; k < this.width; k++) {
        n += f;
      }
      console.log(n);
    }
  }
}

module.exports = Square;
