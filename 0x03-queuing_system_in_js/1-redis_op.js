import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) =>
  console.log(`Redis client not connected to the server: ${err}`)
);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function displaySchoolValue(schoolName) {
  client.GET(schoolName, (_err, reply) => {
    console.log(reply);
  });
}

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, print);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
