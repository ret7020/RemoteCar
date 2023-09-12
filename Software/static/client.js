var img = document.getElementById("liveImg");

var target_fps = 600;

var request_start_time = performance.now();
var start_time = performance.now();
var time = 0;
var request_time = 0;
var time_smoothing = 0.99; // larger=more smoothing
var request_time_smoothing = 0.99; // larger=more smoothing
var target_time = 1000 / target_fps;
var fpss = [];

var last_frame_time = 0;
var current_time;

var wsProtocol = (location.protocol === "https:") ? "wss://" : "ws://";


var ws = new WebSocket(wsProtocol + location.host + "/image");
ws.binaryType = 'arraybuffer';


ws.onmessage = function(evt) {
    current_time = performance.now();
    fpss.push(Math.round(1000 / (current_time - last_frame_time)))
    last_frame_time = current_time;  
    console.log((fpss.slice(2, ).reduce((partialSum, a) => partialSum + a, 0)) / fpss.slice(2,).length, Math.max(...fpss.slice(2, )));
    img.src = window.URL.createObjectURL(new Blob([new Uint8Array(evt.data)], {type: "image/jpeg"}));
    
};
