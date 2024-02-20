#!/usr/bin/node

/**
 * File Reader
 * -----------
 *
 * Description: This script reads the content of a file and prints it to the console.
 *
 * Author: sebsibe solomon
 *
 * Date: 02202024
 *
 * Usage: node file_reader.js [file_path]
 *
 * Exceptions:
 * - Error: Raised when an error occurs during the file reading process.
 * - TypeError: Raised when the file path is not provided as a command line argument.
 *
 * Dependencies:
 * - fs module: Used to read the content of the file.
 *
 * Parameters:
 * - file_path: A string representing the path to the file.
 */

const fs = require('fs');

const filePath = process.argv[2];

try {
  if (!filePath) {
    throw new TypeError('Error: File path is missing. Please provide a file path as a command line argument.');
  }

  fs.readFile(filePath, 'utf8', function (error, content) {
    if (error) {
      throw error;
    } else {
      console.log(content);
    }
  });
} catch (error) {
  console.error(error);
}
