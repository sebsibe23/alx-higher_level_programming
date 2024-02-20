#!/usr/bin/node

/**
 * File Reader
 * ------------
 *
 * Description: This script reads a file and
 * outputs its contents to the console.
 *
 * Author: John Doe
 *
 * Date: February 20, 2024
 *
 * Usage: node file-reader.js [file_path]
 *
 * Exceptions:
 * - Error: Raised when an unexpected error
 *   occurs during file reading.
 * - TypeError: Raised when the file path is
 *   not provided as a command line argument.
 * - ENOENT: Raised when the file specified by
 *   the file path does not exist.
 */
const fs = require('fs')

fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err)
  } else {
    process.stdout.write(data)
  }
})
