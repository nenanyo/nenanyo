var express = require('express')
    , http = require('http')
    , path = require('path');

var bodyParser = require('body-parser')
    ,static = require('serve-static');

var expressErrorHandler = require('express-error-handler');

var cookieParser = require('cookie-parser');

var app = express();

app.set('port', process.env.PORT || 3000);

app.use(bodyParser.urlencoded({ extended: false }));

app.use(bodyParser.json());

app.use('/public', static(path.join(__dirname, 'public')));

app.use(cookieParser());

// 라우터 객체 참조
var router = express.Router();

// 라우팅 함수 등록
router.route('/process/showCookie').get(function(req, res) {
	console.log('/process/showCookie 호출.');
    
    res.send(req.cookies);
});

router.route('/process/setUserCookie').get(function(req, res) {
    console.log('/process/setUserCookie 호출.');
    res.cookie('user', {
               id: 'mike',
               name: 'kim',
               authorized: true
               })
    res.redirect('/process/showCookie');

});


// 라우터 객체를 app 객체에 등록
app.use('/', router);




// 등록되지 않은 패스에 대해 페이지 오류 응답
var errorHandler = expressErrorHandler({
    static: {
        '404': './public/404.html'
    }
});

app.use( expressErrorHandler.httpError(404) );
app.use( errorHandler );


// Express 서버 시작
http.createServer(app).listen(app.get('port'), function(){
  console.log('Express server listening on port ' + app.get('port'));
});