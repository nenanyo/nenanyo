var http = require('http');
var fs = require('fs')


var server = http.createServer();

var port = 3000;
server.listen(port, function() {
    console.log('start web server : %d', port);
});


// 클라이언트 연결 이벤트 처리
server.on('connection', function(socket){
    var addr = socket.address();
    console.log('client connect : %s, %d', addr.address, addr.port);
});

//클라이언트 요청 이벤트 처리
server.on('request', function(req, res){
    console.log('client request');
//    console.dir(req); 
    var filename = 'house.png';
    fs.readFile(filename, function(err, data) {
        res.writeHead(200, {"Content-Type": "image/png"});
        res.write(data);
        res.end();
    });
});

//서버 종료 이벤트 처리
server.on('close', function() {
    console.log('end server');
});