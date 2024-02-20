#!/usr/bin/node

/**
 * Star Wars Film Title Fetcher
 * ----------------------------
 *
 * Description: This script fetches and displays the title of a Star Wars film
 *              based on the film ID provided by the user.
 *
 * Author: sebsibe solomon
 *
 * Date: February 20, 2024
 *
 * Usage: node star-wars-fetcher.js [film_id]
 *
 * Exceptions:
 * - Error: Raised when an unexpected error occurs during the API request or response parsing.
 * - TypeError: Raised when the film ID is not provided as a command line argument.
 */
const request = require('request');
request.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
