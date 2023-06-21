import { createQueue } from 'kue';

const jobData = {
  phoneNumber: '09012348593',
  message: 'Received',
};

const queue = createQueue({ name: 'push_notification_code' });

const job = queue.create('push_notification_code', jobData);

job
  .on('enqueue', () => {
    console.log('Notification job created:', job.id);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed attempt', () => {
    console.log('Notification job failed');
  })
  .on('failed', () => {
    console.log('Notification job failed');
  });
job.save()
