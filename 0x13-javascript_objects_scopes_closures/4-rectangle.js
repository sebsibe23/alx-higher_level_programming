#!/usr/bin/node

/**
 * This is a Rectangle class in Node.js.
 * It has a constructor and three methods:
 * print, rotate, and double.
 *
 * Constructor (w, h): Initializes a new Rectangle
 * object if both width (w) and
 * height (h) are positive numbers.
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
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
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
