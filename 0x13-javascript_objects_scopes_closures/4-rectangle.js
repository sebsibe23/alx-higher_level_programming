#!/usr/bin/node

/**
 * This is a Rectangle class in Node.js.
 * It has a constructor and three methods:
 * print, rotate, and double.
 *
 * Constructor (wt, hg): Initializes a new Rectangle
 * object if both width (wt) and
 * height (hg) are positive numbers.
 *
 * print(): Prints a visual representation of
 * the Rectangle object using 'X'
 * characters. The number of 'X' characters in
 * a row corresponds to the width,
 * and the number of rows corresponds to the height.
 *
 * rotate(): Swaps the width and the height
 * of the Rectangle object.
 *
 * double(): Doubles the width and the height
 * of the Rectangle object.
 *
 * The Rectangle class is exported as a module.
 */

class Rectangle {
  constructor (wt, hg) {
    if ((wt > 0) && (hg > 0)) {
      this.width = wt;
      this.height = hg;
    }
  }

  print () {
    for (let t = 0; t < this.height; t++) {
      let s = '';
      for (let u = 0; u < this.width; u++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
