#!/usr/bin/node

const Rectangle = require('./4-rectangle');

/**
 * Class representing a square.
 * @extends Rectangle
 */
class Square extends Rectangle {
  /**
   * Create a new square instance with a given size.
   * @param {number} size - The size of the square's sides.
   */
  constructor(size) {
    super(size, size);
  }
}

module.exports = Square;
