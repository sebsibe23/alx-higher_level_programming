#!/usr/bin/node

/**
 * Web Page Downloader
 * -------------------
 *
 * Description: This script downloads the contents of a web page specified by the URL and
 *              saves it to a file specified by the file path.
 *
 * Author: sebsibe solomon
 *
 * Date: February 20, 2024
 *
 * Usage: node web-page-downloader.js [url] [file_path]
 *
 * Exceptions:
 * - Error: Raised when an unexpected error occurs during the request or file writing process.
 * - TypeError: Raised when the URL or file path is not provided as command line arguments.
 *
 * Dependencies:
 * - request module: Used to send HTTP requests and retrieve the web page contents.
 * - fs module: Used to write the web page contents to a file.
 */

const request = require('request')
const fs = require('fs')

// Retrieve the URL and file path from command line arguments
const url = process.argv[2]
const filePath = process.argv[3]

// Send a GET request to the specified URL
request(url, function (error, response, body) {
  if (error) {
    console.error(error)
  } else {
    // Write the response body (web page contents) to the specified file path
    fs.writeFile(filePath, body, 'utf8', function (err) {
      if (err) {
        console.error(err)
      } else {
        console.log(`Web page downloaded and saved to: ${filePath}`)
      }
    })
  }
})
