#!/usr/bin/node

/**
 * Object Name: myObject
 *
 * Properties:
 * - type: The type of the object. In this case, it's 'object'.
 * - value: The value of the object. Initially, it's set to 12.
 *
 * Methods:
 * - incr: This method increments the 'value' property of 'myObject' by 1.
 *
 * Description:
 * This script creates an object, 'myObject', with properties 'type' and 'value'.
 * It then logs the object to the console. After that, it adds a method, 'incr',
 * to 'myObject' that increments the 'value' property by 1. The 'incr' method is
 * then called three times, with the object being logged to the console after
 * each call, showing the incrementing 'value'.
 */
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function () {
  this.value++;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
