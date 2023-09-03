#!/usr/bin/yarn dev
import { createQueue } from 'kue';
const queue = createQueue();

// Create an object containing the job data
const jobData = {
  phoneNumber: '123-456-7890',
  message: 'Hello, this is a notification message.',
};

// Create a queue named 'push_notification_code' and add a job
const job = queue.create('push_notification_code', jobData);

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.error(`Error creating notification job: ${err}`);
  }
  process.exit(0); // Exit the script
});
