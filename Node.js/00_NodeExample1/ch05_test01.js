var http = require('http');

var server = http.createServer();

var port = 3000;
//server.listen(port, function() {
//    console.log('start server : %d', port);
//});

var host = '172.30.1.42';
var port = 3000;
server.listen(port, host, '50000', function() {
    console.log('start server : %s, %d', host, port);
});