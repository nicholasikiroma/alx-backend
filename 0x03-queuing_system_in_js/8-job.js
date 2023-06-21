export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  jobs.forEach((job) => {
    const task = queue.create('push_notification_code_3', job);

    task
      .on('enqueue', () => {
        console.log('Notification job created:', task.id);
      })
      .on('complete', () => {
        console.log('Notification job', task.id, 'completed');
      })
      .on('failed', (err) => {
        console.log('Notification job', task.id, 'failed:', err.message || err.toString());
      })
      .on('progress', (progress, _data) => {
        console.log('Notification job', task.id, `${progress}% complete`);
      });
    task.save();
  });
}
