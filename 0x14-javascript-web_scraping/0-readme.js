#!/usr/bin/node

/**
 * File Reader Script
 *
 * Description:
 * This script reads the content of a file specified as a command-line argument
 * and logs it to the console. It utilizes the 'fs' module from Node.js to
 * perform the file reading operation asynchronously. If an error occurs during
 * the file reading process, the error message is logged. Otherwise, the file
 * content is printed to the console.
 */

const fs = require('fs')

fs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content)
})
