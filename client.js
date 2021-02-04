const io = require("socket.io-client")
const ioClient = io.connect("http://localhost:3000")

let count = 0
ioClient.on("exchange-rate", (resp) => {
    console.info('client received : ', count++)
    console.info(resp)
});