var express = require('express')
    , http = require('http')

var app = express();

app.use(function(req, res, next) {
    console.log('first middleware');
    
    res.writeHead(200, {'Content-Type':'text/html;charset=utf8'});
    res.end('<h1>Express 서버에서 응답한 결과</h1>');
});

http.createServer(app).listen(3000, function(){
    console.log('Express 서버가 3000 포트에서 시작');
});