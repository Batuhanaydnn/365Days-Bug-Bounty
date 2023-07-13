const express = require('express');
const axios = require('axios');
const app = express();

// Endpoint that returns a JSONP response
app.get('/api', async (req, res) => {
  const callback = req.query.callback;

  try {
    // Make a request to the local API service
    const response = await axios.get('http://localhost:8000/data');

    // Extract the data from the response
    const data = response.data;

    // Wrap the data in the callback function
    const jsonpData = `${callback}(${JSON.stringify(data)})`;

    // Set the appropriate content type
    res.setHeader('Content-Type', 'application/javascript');

    // Send the JSONP response
    res.send(jsonpData);
  } catch (error) {
    // Handle any errors that occur during the request
    console.error(error);
    res.status(500).send('Internal Server Error');
  }
});

// Start the server
app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
