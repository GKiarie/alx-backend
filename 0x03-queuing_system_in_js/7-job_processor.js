#!/usr/bin/yarn dev
import { createQueue } from 'kue';
const queue = createQueue();

const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notifications and track progress
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
    done(new Error(errorMessage));
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
}

// Process jobs in the 'push_notification_code_2' queue with a concurrency of 2
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message, job, (error) => {
    if (error) {
      console.error(`Notification job ${job.id} failed: ${error.message}`);
      done(error);
    } else {
      console.log(`Notification job ${job.id} completed`);
      done();
    }
  });
});

// Handle errors in the queue
queue.on('error', (err) => {
  console.error('Queue error:', err);
});

console.log('Job processor is listening for new jobs...');
