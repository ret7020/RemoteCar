var img = document.getElementById("liveImg");
var wsProtocol = (location.protocol === "https:") ? "wss://" : "ws://";

var ws = new WebSocket(wsProtocol + location.host + "/image");
ws.binaryType = 'arraybuffer';

ws.onmessage = (evt) => img.src = window.URL.createObjectURL(new Blob([new Uint8Array(evt.data)], { type: "image/jpeg" }));
