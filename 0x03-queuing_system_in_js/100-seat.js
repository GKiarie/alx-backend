const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');

const app = express();
const port = 1245;

// Create a Redis client and promisify relevant functions
const redisClient = redis.createClient();
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

// Create a Kue queue
const queue = kue.createQueue();

// Initialize the number of available seats to 50
let numberOfAvailableSeats = 50;

// Initialize reservationEnabled to true
let reservationEnabled = true;

// Function to reserve seats
const reserveSeat = async (number) => {
  await setAsync('available_seats', number);
};

// Function to get current available seats
const getCurrentAvailableSeats = async () => {
  const seats = await getAsync('available_seats');
  return parseInt(seats) || 0;
};

// Middleware to parse JSON requests
app.use(express.json());

// Route to get the number of available seats
app.get('/available_seats', (req, res) => {
  res.json({ numberOfAvailableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
  } else {
    const currentAvailableSeats = await getCurrentAvailableSeats();
    if (currentAvailableSeats === 0) {
      reservationEnabled = false;
      res.json({ status: 'Reservation are blocked' });
    } else {
      queue
        .create('reserve_seat', {})
        .save((err) => {
          if (err) {
            res.json({ status: 'Reservation failed' });
          } else {
            res.json({ status: 'Reservation in process' });
          }
        });
    }
  }
});

// Route to process the queue and reserve a seat
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  // Process the queue reserve_seat
  queue.process('reserve_seat', async (job, done) => {
    const currentAvailableSeats = await getCurrentAvailableSeats();

    if (currentAvailableSeats > 0) {
      await reserveSeat(currentAvailableSeats - 1);
      if (currentAvailableSeats - 1 === 0) {
        reservationEnabled = false;
      }
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
