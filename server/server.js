const WebSocket = require('ws');

var binanceSocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@trade");

binanceSocket.onmessage = (event) => {
	console.log(event.data)
}
