#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};

function incr() {
  this.value++;
}

console.log(myObject);
myObject.incr = incr;
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
