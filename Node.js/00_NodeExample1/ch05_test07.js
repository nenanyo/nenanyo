var https = require('https');

var options = {
    host : 'www.google.com',
    port : 443,
    path : '/',
    method: 'GET'
};

var req = https.get(options, function(res) {
    //응답처리
    var resData = '';
    res.on('data', function(chunk) {
        resData += chunk;
    });
    
    res.on('end', function() {
        console.log(resData);
    });
});
    
req.on('error', function(err) {
    console.log('오류발생', err.message);
});

req.end();