#!/usr/bin/node

/**
 * Completed Tasks Counter
 * -----------------------
 *
 * Description: This script retrieves data from a specified URL and counts the number of completed tasks
 *              for each user.
 *
 * Author: sebsibe solomon
 *
 * Date: February 20, 2024
 *
 * Usage: node completed-tasks-counter.js [url]
 *
 * Exceptions:
 * - Error: Raised when an unexpected error occurs during the request or data processing.
 * - TypeError: Raised when the URL is not provided as a command line argument.
 *
 * Dependencies:
 * - request module: Used to send HTTP requests and retrieve the data.
 */

const request = require('request')

// Retrieve the URL from the command line argument
const url = process.argv[2]

// Send a GET request to the specified URL
request(url, function (err, _res, body) {
  if (err) {
    console.error(err)
  } else {
    // Initialize an object to store the completed task count for each user
    const completedTasksByUsers = {}

    // Parse the response body as JSON
    body = JSON.parse(body)

    // Iterate over the data
    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId
      const completed = body[i].completed

      // If the task is completed and the user is not already in the completedTasksByUsers object, initialize the count to 0
      if (completed && !completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0
      }

      // If the task is completed, increment the count for the respective user
      if (completed) ++completedTasksByUsers[userId]
    }

    console.log(completedTasksByUsers)
  }
})
