var http = require('http');

var server = http.createServer(function(req, res){
    console.log('client connect');
    
    res.writeHead(200, {"Content-Type": "text/html; charset=utf-8"});
    res.write("<!DOCTYPE html>");
    res.write("<html>");
    res.write(" <head>");
    res.write("     <title>응답 페이지</title>");
    res.write(" </head>");
    res.write(" <body>");
    res.write("     <h1>response page</h1>");
    res.write(" </body>");
    res.write("</html>");
    res.end();    
});
    

var port = 3000;
server.listen(port, function() {
    console.log('start web server : %d', port);
});


// 클라이언트 연결 이벤트 처리
server.on('connection', function(socket){
    var addr = socket.address();
    console.log('client connect : %s, %d', addr.address, addr.port);
    
    
});

////클라이언트 요청 이벤트 처리
//server.on('request', function(req, res){
//    console.log('client request');
////    console.dir(req); 
//    
//    res.writeHead(200, {"Content-Type": "text/html; charset=utf-8"});
//    res.write("<!DOCTYPE html>");
//    res.write("<html>");
//    res.write(" <head>");
//    res.write("     <title>응답 페이지</title>");
//    res.write(" </head>");
//    res.write(" <body>");
//    res.write("     <h1>response page</h1>");
//    res.write(" </body>");
//    res.write("</html>");
//    res.end();    
//});

//서버 종료 이벤트 처리
server.on('close', function() {
    console.log('end server');
});