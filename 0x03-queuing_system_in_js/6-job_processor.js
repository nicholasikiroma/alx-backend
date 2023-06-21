import { createQueue } from 'kue';

function sendNotification(phoneNumber, message) {
  console.log(`Sending notication to ${phoneNumber}, with message: ${message}`);
}

const queue = createQueue();

queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
