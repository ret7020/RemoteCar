var img = document.getElementById("liveImg");
var fpsText = document.getElementById("fps");

var target_fps = 600;

var request_start_time = performance.now();
var start_time = performance.now();
var time = 0;
var request_time = 0;
var time_smoothing = 0.99; // larger=more smoothing
var request_time_smoothing = 0.99; // larger=more smoothing
var target_time = 1000 / target_fps;
var last_frame_time = 0;
var current_time;

var wsProtocol = (location.protocol === "https:") ? "wss://" : "ws://";

var path = location.pathname;
if(path.endsWith("index.html"))
{
    path = path.substring(0, path.length - "index.html".length);
}
if(!path.endsWith("/")) {
    path = path + "/";
}
var ws = new WebSocket(wsProtocol + location.host + path + "websocket");
ws.binaryType = 'arraybuffer';

function requestImage() {
    request_start_time = performance.now();
    ws.send('more');
}

ws.onopen = function() {
    console.log("connection was established");
    // start_time = performance.now();
    requestImage();
};

ws.onmessage = function(evt) {
    var arrayBuffer = evt.data;
    var blob  = new Blob([new Uint8Array(arrayBuffer)], {type: "image/jpeg"});
    img.src = window.URL.createObjectURL(blob);
    current_time = performance.now();
    fpsText.textContent = Math.round(1000 / (current_time - last_frame_time));
    last_frame_time = current_time;

    requestImage();
};
