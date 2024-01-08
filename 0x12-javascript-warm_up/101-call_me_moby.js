#!/usr/bin/node

/**
 * Function Name: callMeMoby
 *
 * Parameters:
 * - x: The number of times 'theFunction' should be executed.
 * - theFunction: The function to be executed 'x' times.
 *
 * Description:
 * This function, 'callMeMoby', executes a given function, 'theFunction',
 * a specified number of times, 'x'. It does this by using a for loop to
 * call 'theFunction' 'x' times.
 */
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};

