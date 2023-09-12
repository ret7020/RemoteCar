var img = document.getElementById("liveImg");

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


var ws = new WebSocket(wsProtocol + location.host + "/image");
ws.binaryType = 'arraybuffer';

// ws.onopen = function() {
//     console.log("connection was established");
//     // start_time = performance.now();
//     requestImage();
// };

ws.onmessage = function(evt) {
    var arrayBuffer = evt.data;
    var blob  = new Blob([new Uint8Array(arrayBuffer)], {type: "image/jpeg"});
    img.src = window.URL.createObjectURL(blob);
};
