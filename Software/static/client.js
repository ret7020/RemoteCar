var img = document.getElementById("liveImg");
var wsProtocol = (location.protocol === "https:") ? "wss://" : "ws://";

var ws = new WebSocket(wsProtocol + location.host + "/image");
ws.binaryType = 'arraybuffer';
var data;
ws.onmessage = (evt) => {
	data = new Uint8Array(evt.data);
	//data = pako.ungzip(data);
	img.src = window.URL.createObjectURL(new Blob([data], { type: "image/jpeg" }));
}
