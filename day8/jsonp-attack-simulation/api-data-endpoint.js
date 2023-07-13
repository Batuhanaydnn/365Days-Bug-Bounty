const express = require('express');
const app = express();

// Endpoint that returns sample data
app.get('/data', (req, res) => {
  const data = {
    message: 'Sample data',
    value: 42
  };

  res.json(data);
});

// Start the server
app.listen(8000, () => {
  console.log('Server is running on port 8000');
});
