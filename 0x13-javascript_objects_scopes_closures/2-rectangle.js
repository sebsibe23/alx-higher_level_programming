#!/usr/bin/node

/**
 * Class representing a rectangle.
 */
class Rectangle {
  /**
   * Create a new rectangle instance with positive width and height.
   * @param {number} wt - The width of the rectangle.
   * @param {number} hg - The height of the rectangle.
   */
  constructor (wt, hg) {
    if (wt > 0 && hg > 0) {
      this.width = wt;
      this.height = hg;
    }
  }
}

module.exports = Rectangle;
