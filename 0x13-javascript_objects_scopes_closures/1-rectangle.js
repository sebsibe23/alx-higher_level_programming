#!/usr/bin/node

/**
 * Class representing a rectangle.
 */
class Rectangle {
  /**
   * Create a new rectangle instance.
   * @param {number} wth - The width of the rectangle.
   * @param {number} hig - The height of the rectangle.
   */
  constructor (wth, hig) {
    this.width = wth;
    this.height = hig;
  }
}

module.exports = Rectangle;
