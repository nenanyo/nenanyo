var express = require('express')
    , http = require('http')

var app = express();

app.use(function(req, res, next) {
    console.log('first middleware');    

    var userAgent = req.header('User-Agent');
    var paramName = req.query.name;
    
    res.writeHead('200', {'Content-Type':'text/html;charset=utf8'});
    res.write('<h1>Express 서버에서 응답한 결과</h1>');
    res.write('<div><p> '+userAgent+' </p></div>');
    res.write('<div><p> '+paramName +' </p></div>');
    res.end()
});



http.createServer(app).listen(3000, function(){
    console.log('Express 서버가 3000 포트에서 시작');
});