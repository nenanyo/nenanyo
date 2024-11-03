var express = require('express')
    , http = require('http')

var app = express();

app.use(function(req, res, next) {
    console.log('first middleware');    
    res.redirect('http://google.co.kr');
    
});



http.createServer(app).listen(3000, function(){
    console.log('Express 서버가 3000 포트에서 시작');
});