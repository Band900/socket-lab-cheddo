const {
       spawn
} = require('child_process');
const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);
const server = io.listen(3000);

let sequenceNumberByClient = new Map();

server.on("connection", (socket) => {
       console.info(`Client connected [id=${socket.id}]`);
       sequenceNumberByClient.set(socket, 1);

       socket.on("disconnect", () => {
              sequenceNumberByClient.delete(socket);
              console.info(`Client gone [id=${socket.id}]`);
       });
});

let count = 0
setInterval(() => {
       console.info("server send data : ", count)
       for (const [client, sequenceNumber] of sequenceNumberByClient.entries()) {
              var largeDataSet = [];
              const python = spawn('python3', ['script3.py']);
              python.stdout.on('data', function (data) {
                     largeDataSet.push(data);
              });

              python.on('close', (code) => {
                     client.emit("exchange-rate", JSON.parse(largeDataSet.join("")))
                     count++
              });

              sequenceNumberByClient.set(client, sequenceNumber + 1);
       }
}, 10000)