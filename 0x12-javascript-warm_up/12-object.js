#!/usr/bin/node

/*
 * This Node.js script creates an object named 'myObject' with properties 'type'
 * and 'value'. Initially, 'type' is set to 'object' and 'value' is set to 12.
 * The script then prints the 'myObject'. Afterwards, it changes the 'value'
 * property of 'myObject' to 89 and prints the 'myObject' again.
 */

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.value = 89;
console.log(myObject);
