#!/usr/bin/node

const fs = require('fs')

const filePath = process.argv[2]
const content = process.argv[3]

try {
  if (!filePath) {
    throw new TypeError('Error: File path is missing. Please provide a file path as a command line argument.')
  }

  if (!content) {
    throw new TypeError('Error: Content is missing. Please provide content to write as a command line argument.')
  }

  fs.writeFile(filePath, content, (error) => {
    if (error) {
      throw error
    } else {
      console.log('Content has been written to the file successfully.')
    }
  })
} catch (error) {
  console.error(error)
}
