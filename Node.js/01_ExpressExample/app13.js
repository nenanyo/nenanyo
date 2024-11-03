// express 기본 모듈
var express = require('express')
    , http = require('http')
    , path = require('path');

//express 미들웨어
var bodyParser = require('body-parser')
    ,static = require('serve-static')
    ,cookieParser = require('cookie-parser')
    ,errorHandler = require('errorhandler');

var expressErrorHandler = require('express-error-handler');
var expressSession = require('express-session');

//파일 업로드용 미들웨어
var multer = require('multer');
var fs = require('fs');

//클라이언트에서 ajax로 요청했을 때 CORS(다중 서버 접속) 지원
var cors = require('cors');

var app = express();

app.set('port', process.env.PORT || 3000);

app.use(bodyParser.urlencoded({ extended: false }));

app.use(bodyParser.json());

app.use('/public', static(path.join(__dirname, 'public')));
app.use('/uploads', static(path.join(__dirname, 'uploads')));


app.use(cookieParser());

app.use(expressSession({
    secret: 'my key',
    resave: true,
    saveUninitialized:true
}));

//CORS 다중서버접속 지원
app.use(cors());

//미들웨어 사용 (순서!!! body-parser -> multer -> router)
//파일제한 10개, 1G
var storage = multer.diskStorage({
    destination: function(req, file, callback) {
        callback(null, 'uploads')
    },
    filename: function(req, file, callback) {
        callback(null, file.originalname + Date.now())
    }
});

var upload = multer({
    storage: storage,
    limits: {
    files:10,
    fileSize: 1024 * 1024 *1024
}
});

// 라우터 객체 참조
var router = express.Router();


router.route('/process/photo').post(upload.array('photo',1), function(req,res) {
    console.log('process/photo 호출');
    
    try{
        var files = req.files;
        
        console.dir('#============ 업로드된 첫번째 파일 정보 ==============#')
        console.dir(req.files[0]);
        console.dir('#==========================#')
    



    //현재의 파일 정보를 저장할 변수 선언
    var originalname = '',
        filename = '',
        mimetype ='',
        size =0;

        //배열에 들어가 있는 경우, 1개의 파일이라도 배열에 넣었음
        if (Array.isArray(files)) {
            console.log("배열에 들어있는 파일 갯수 :%d", files.length);

            for (var index = 0; index < files.length; index++){
                originalname = files[index].originalname;
                filename = files[index].filename;
                mimetype = files[index].mimetype;
                size = files[index].size;            
            }
            // 배열에 들어가 있지 않은 경우
        } else {
            console.log("배열에 들어있는 파일 갯수 : 1 ");

            originalname = files[index].originalname;
            filename = files[index].filename;
            mimetype = files[index].mimetype;
            size = files[index].size;  

        }

        console.log('현재 파일 정보 :' + originalname + ',' + filename + ',' + mimetype + ',' + size );

        //클라이언트에 응답전송
        res.writeHead('200',{'Content-Type':'text/html;charset=utf8'});
        res.write('<h3>파일 업로드 성공</h3>');
        res.write('</hr>');
        res.write('<p>원본 파일 이름 : '+ originalname +' -> 저장 파일명 : ' + filename + '</p>');
        res.write('<p> mimetype : '+mimetype+'</p>');
        res.write('<p> size : '+size+'</p>');
        res.end();
    } catch(err){
        console.dir(err.stack);
    }
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