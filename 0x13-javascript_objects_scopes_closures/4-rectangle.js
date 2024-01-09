#!/usr/bin/node

/**
 * Class representing a rectangle.
 */
class Rectangle {
	/**
	 * Create a new rectangle instance with positive width and height.
	 * @param {number} w - The width of the rectangle.
	 * @param {number} h - The height of the rectangle.
	 */
	constructor (w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}

	/**
	 * Print a visual representation of the rectangle using 'X' characters.
	 */
	print () {
		for (let i = 0; i < this.height; i++) {
			let s = '';
			for (let j = 0; j < this.width; j++) {
				s += 'X';
			}
			console.log(s);
		}
	}

	/**
	 * Rotate the rectangle by swapping its width and height.
	 */
	rotate () {
		const aux = this.width;
		this.width = this.height;
		this.height = aux;
	}

	/**
	 * Double the width and height of the rectangle.
	 */
	double () {
		this.width *= 2;
		this.height *= 2;
	}
}

module.exports = Rectangle;
