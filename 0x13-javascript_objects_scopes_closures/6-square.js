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
   * @param {string} [c='X'] - The character
   * to use for printing the square.
   */
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
