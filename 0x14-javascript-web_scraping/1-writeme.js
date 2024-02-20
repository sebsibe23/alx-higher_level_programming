#!/usr/bin/node

// Description: Node.js script to write data to a file specified by command-line arguments.
// Parameters:
//   - process.argv[2]: File name (command-line argument)
//   - process.argv[3]: Data to be written to the file (command-line argument)

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
