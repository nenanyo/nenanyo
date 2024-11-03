
/**
 * 데이터베이스 사용하기
 * 
 * MySQL에 연결하고 클라이언트에서 로그인할 때 데이터베이스 연결하도록 만들기
 * 
 * 웹브라우저에서 아래 주소의 페이지를 열고 웹페이지에서 요청
 *    http://localhost:3000/public/login.html
 *
 * @date 2016-11-10
 * @author Mike
 */

// Express 기본 모듈 불러오기
var express = require('express')
  , http = require('http')
  , path = require('path');

// MySQL2 모듈 불러오기
const mysql = require('mysql2');

// Express의 미들웨어 불러오기
var bodyParser = require('body-parser')
  , cookieParser = require('cookie-parser')
  , static = require('serve-static')
  , errorHandler = require('errorhandler');

// 에러 핸들러 모듈 사용
var expressErrorHandler = require('express-error-handler');

// Session 미들웨어 불러오기
var expressSession = require('express-session');

// Sequelize 모듈 사용
const { Sequelize, Datatypes, DataTypes } =require('sequelize');

// 익스프레스 객체 생성
var app = express();

// 기본 속성 설정
app.set('port', process.env.PORT || 3000);

// body-parser를 이용해 application/x-www-form-urlencoded 파싱
app.use(bodyParser.urlencoded({ extended: false }));

// body-parser를 이용해 application/json 파싱
app.use(bodyParser.json());

// public 폴더를 static으로 오픈
app.use('/public', static(path.join(__dirname, 'public')));

// cookie-parser 설정
app.use(cookieParser());

// 세션 설정
app.use(expressSession({
	secret: 'my key',
	resave: true,
	saveUninitialized: true
}));

//===== 데이터베이스 연결 =====//

// Sequelize 객체
const sequelize = new Sequelize('test','test_user','test',{
	host : 'localhost',
	dialect :'mysql'
});

//user 모델
const User = sequelize.define('User', {
	id: {
		type: DataTypes.STRING,
		primaryKey:true
	},
	name: {
		type: DataTypes.STRING,
		allowNull:false
	},
	password: {
		type: DataTypes.STRING,
		allowNull:false
	}
}, {
	tableName: 'user',
	timestamps: false
});



//데이터베이스에 연결
async function connectDB() {
	try{
		await sequelize.authenticate();
		console.log('데이터베이스에 연결');
		await sequelize.sync();
	} catch (error) {
		console.error('데이터베이스 연결 실패', error);
	}
}



//===== 라우팅 함수 등록 =====//

// 라우터 객체 참조
var router = express.Router();

// 로그인 라우팅 함수 - 데이터베이스의 정보와 비교
router.route('/process/login').post(async function(req, res) {
	console.log('/process/login 호출됨.');

    // 요청 파라미터 확인
    var paramId = req.body.id || req.query.id;
    var paramPassword = req.body.password || req.query.password;
	
    console.log('요청 파라미터 : ' + paramId + ', ' + paramPassword);

    try {
		const user = await User.findOne({ where:{ id: paramId, password: paramPassword} });
		if (user) {
			const username = user.name;
			console.dir(user);			
			res.writeHead('200', {'Content-Type': 'text/html;charset=utf8'});
			res.write('<h1>로그인 성공</h1>');
			res.write('<div><p>사용자 아이디 : ' + paramId + '</p></div>');
			res.write('<div><p>사용자 이름 : ' + username + '</p></div>');
			res.write("<br><br><a href='/public/login.html'>다시 로그인하기</a>");
			res.end();				
		} else {  
			res.writeHead('200', {'Content-Type': 'text/html;charset=utf8'});
			res.write('<h1>로그인 실패</h1>');
			res.write('<div><p>아이디와 패스워드를 다시 확인하십시오.</p></div>');
			res.write("<br><br><a href='/public/login.html'>다시 로그인하기</a>");
			res.end();
		}
	} catch (error) {
		console.log('로그인 처리 중 오류', error);
		res.writeHead('200', {'Content-Type': 'text/html;charset=utf8'});
		res.write('<h2>데이터베이스 연결 실패</h2>');
		res.write('<div><p>데이터베이스에 연결하지 못했습니다.</p></div>');
		res.end();
	}
});
 

//사용자 추가 라우팅
router.route('/process/adduser').post(async function(req,res) {
    console.log('/process/adduser 호출');

    var paramId = req.body.id || req.query.id;
    var paramPassword = req.body.password || req.query.password;
    var paramName = req.body.name || req.query.name; 

    console.log('요청 파라미터 :' + paramId + ',' + paramPassword + ',' +paramName);

    try{
		const user = await User.create({ id: paramId, password: paramPassword, name: paramName});
		console.dir(user);
          
		res.writeHead('200', {'Content-Type':'text/html;charset=utf8'});
		res.write('<h2>사용자 추가 성공</h2>');
		res.end();
	} catch (error) {  
		res.writeHead('200', {'Content-Type':'text/html;charset=utf8'});
		res.write('<h2>사용자 추가 실패</h2>');
		res.end();
    }
});


// 라우터 객체 등록
app.use('/', router);

// 사용자를 인증하는 함수
var authUser = function(connection, id, password, callback) {
	console.log('authUser 호출됨 : ' + id + ', ' + password);
	
    // MySQL 쿼리 실행
	const sql = 'SELECT * FROM user WHERE id = ? AND password = ?';
	connection.query(sql, [id, password], function(err, results) {
		if (err) { // 에러 발생 시 콜백 함수를 호출하면서 에러 객체 전달
			callback(err, null);
			return;
		}
		
	    if (results.length > 0) {  // 조회한 레코드가 있는 경우 콜백 함수를 호출하면서 조회 결과 전달
	    	console.log('아이디 [%s], 패스워드 [%s] 가 일치하는 사용자 찾음.', id, password);
	    	callback(null, results);
	    } else {  // 조회한 레코드가 없는 경우 콜백 함수를 호출하면서 null, null 전달
	    	console.log("일치하는 사용자를 찾지 못함.");
	    	callback(null, null);
	    }
	});
}

// 사용자 추가 함수
var addUser = function(connection, id, password, name, callback) {
    console.log('addUser 호출' + id + ',' + password + ',' + name);

    //Mysql 쿼리 실행
    var sql = 'INSERT INTO user (id,password,name) VALUES (?,?,?)';
    connection.query(sql, [id, password, name], function(err, result) {  
        if (err) { // 오류가 발생했을 때 콜백 함수를 호출하면서 오류 객체 전달
            callback(err,null);
            return;
        }        
       
        // 오류가 아닌경우, 콜백 함수를 호출하면서 결과 객체 전달
        if (result.affectedRows > 0) {
            console.log("사용자 레코드 추가" + result.affectedRows);        
        } else {
            console.log('추가된 레코드가 없음');
        }

        callback(null, result);
    });
}



// 404 에러 페이지 처리
var errorHandler = expressErrorHandler({
	static: {
		'404': './public/404.html'
	}
});

app.use(expressErrorHandler.httpError(404));
app.use(errorHandler);

// =============서버 시작==========//

// 프로세스 종료 시에 데이터베이스 연결 해제
process.on('SIGTERM', function() {
	console.log('프로세스가 종료됩니다.');
	app.close;
});

app.on('close', function() {
	console.log('Express 서버 객체 종료');
	sequelize.close();
});

// Express 서버 시작
http.createServer(app).listen(app.get('port'), function() {
	console.log('서버가 시작되었습니다. 포트 : ' + app.get('port'));

	// 데이터베이스 연결을 위한 함수 호출
	connectDB();
});