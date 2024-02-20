#!/usr/bin/node

/**
 * File Writer
 * ------------
 *
 * Description: This script writes content to a file specified by the user.
 *
 * Author: John Doe
 *
 * Date: February 20, 2024
 *
 * Usage: node file-writer.js [file_path] [content]
 *
 * Exceptions:
 * - Error: Raised when an unexpected error occurs during file writing.
 * - TypeError: Raised when the file path or content is not provided as command line arguments.
 * - EACCES: Raised when the user does not have permission to write to the specified file.
 */

const fs = require('fs')

try {
  if (process.argv.length < 4) {
    throw new TypeError('File path and content not provided. Usage: node file-writer.js [file_path] [content]')
  }

  const filePath = process.argv[2]
  const content = process.argv[3]

  fs.writeFile(filePath, content, 'utf8', function (err) {
    if (err) {
      if (err.code === 'EACCES') {
        throw new Error(`Permission denied. Cannot write to file "${filePath}".`)
      } else {
        throw err
      }
    } else {
      console.log(`Successfully wrote content to file: ${filePath}`)
    }
  })
} catch (error) {
  console.error(error)
}
