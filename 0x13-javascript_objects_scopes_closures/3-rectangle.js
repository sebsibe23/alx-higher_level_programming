#!/usr/bin/node

/**
 * Class representing a rectangle.
 */
class Rectangle {
  /**
   * Create a new rectangle instance with positive width and height.
   * @param {number} wth - The width of the rectangle.
   * @param {number} hig - The height of the rectangle.
   */
  constructor (wth, hig) {
    if (wth > 0 && hig > 0) {
      this.width = wth;
      this.height = hig;
    }
  }

  /**
   * Print a visual representation of the rectangle using 'X' characters.
   */
  print () {
    for (let x = 0; x < this.height; x++) {
      let s = '';
      for (let k = 0; k < this.width; k++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}

module.exports = Rectangle;
