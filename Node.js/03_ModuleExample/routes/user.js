/*
 * 사용자 정보 처리 모듈
 * 데이터베이스 관련 객체들을 req.app.get('database')로 참조
 *
 * @date 2016-11-10
 * @author Mike
 */

const bcrypt = require('bcrypt');

var login = async function(req, res) {
    console.log('user(user2.js) 모듈 안에 있는 login 호출됨.');

    // 요청 파라미터 확인
    var paramId = req.body.id || req.query.id;
    var paramPassword = req.body.password || req.query.password;

    console.log('요청 파라미터 : ' + paramId + ', ' + paramPassword);

    // 데이터베이스 객체 참조
    var database = req.app.get('database');

    // 데이터베이스 객체가 초기화된 경우
    if (database.db) {
        try {
            const docs = await authUser(database, paramId, paramPassword);  // 비동기 함수 호출

            // 조회된 레코드가 있으면 성공 응답 전송
            if (docs && docs.length > 0) {
                console.dir(docs);

                // 조회 결과에서 사용자 이름 확인
                var username = docs[0].name;

                res.writeHead('200', {'Content-Type': 'text/html;charset=utf8'});
                res.write('<h1>로그인 성공</h1>');
                res.write('<div><p>사용자 아이디 : ' + paramId + '</p></div>');
                res.write('<div><p>사용자 이름 : ' + username + '</p></div>');
                res.write("<br><br><a href='/public/login.html'>다시 로그인하기</a>");
                res.end();

            } else {  // 조회된 레코드가 없는 경우 실패 응답 전송
                res.writeHead('200', {'Content-Type': 'text/html;charset=utf8'});
                res.write('<h1>로그인 실패</h1>');
                res.write('<div><p>아이디와 패스워드를 다시 확인하십시오.</p></div>');
                res.write("<br><br><a href='/public/login.html'>다시 로그인하기</a>");
                res.end();
            }
        } catch (err) {
            console.error('사용자 로그인 중 에러 발생 : ' + err.stack);
            res.writeHead('200', {'Content-Type': 'text/html;charset=utf8'});
            res.write('<h2>사용자 로그인 중 에러 발생</h2>');
            res.write('<p>' + err.stack + '</p>');
            res.end();
        }
    } else {  // 데이터베이스 객체가 초기화되지 않은 경우 실패 응답 전송
        res.writeHead('200', {'Content-Type': 'text/html;charset=utf8'});
        res.write('<h2>데이터베이스 연결 실패</h2>');
        res.write('<div><p>데이터베이스에 연결하지 못했습니다.</p></div>');
        res.end();
    }
};


var adduser = async function(req, res) {
    console.log('user(user2.js) 모듈 안에 있는 adduser 호출됨.');

    var paramId = req.body.id || req.query.id;
    var paramPassword = req.body.password || req.query.password;
    var paramName = req.body.name || req.query.name;

    console.log('요청 파라미터 : ' + paramId + ', ' + paramPassword + ', ' + paramName);

    // 데이터베이스 객체 참조
    var database = req.app.get('database');

    // 데이터베이스 객체가 초기화된 경우
    if (database.db) {
        try {
            // 새로운 사용자 추가
            const user = new database.UserModel({ id: paramId, password: paramPassword, name: paramName });
            const addedUser = await user.save();  // 비동기 저장 처리

            if (addedUser) {
                console.dir(addedUser);
                res.writeHead('200', {'Content-Type': 'text/html;charset=utf8'});
                res.write('<h2>사용자 추가 성공</h2>');
                res.end();
            } else {
                res.writeHead('200', {'Content-Type': 'text/html;charset=utf8'});
                res.write('<h2>사용자 추가 실패</h2>');
                res.end();
            }
        } catch (err) {
            console.error('사용자 추가 중 에러 발생 : ' + err.stack);
            res.writeHead('200', {'Content-Type': 'text/html;charset=utf8'});
            res.write('<h2>사용자 추가 중 에러 발생</h2>');
            res.write('<p>' + err.stack + '</p>');
            res.end();
        }
    } else {
        res.writeHead('200', {'Content-Type': 'text/html;charset=utf8'});
        res.write('<h2>데이터베이스 연결 실패</h2>');
        res.end();
    }
};


var listuser = async function(req, res) {
    console.log('user(user2.js) 모듈 안에 있는 listuser 호출됨.');

    // 데이터베이스 객체 참조
    var database = req.app.get('database');

    // 데이터베이스 객체가 초기화된 경우
    if (database.db) {
        try {
            // 모든 사용자 검색 (비동기 처리)
            const results = await database.UserModel.find(); // findAll -> find로 수정

            if (results && results.length > 0) {
                console.dir(results);

                res.writeHead('200', {'Content-Type': 'text/html;charset=utf8'});
                res.write('<h2>사용자 리스트</h2>');
                res.write('<div><ul>');

                for (var i = 0; i < results.length; i++) {
                    var curId = results[i]._doc.id;
                    var curName = results[i]._doc.name;
                    res.write('    <li>#' + i + ' : ' + curId + ', ' + curName + '</li>');
                }

                res.write('</ul></div>');
                res.end();
            } else {
                res.writeHead('200', {'Content-Type': 'text/html;charset=utf8'});
                res.write('<h2>사용자 리스트 조회 실패</h2>');
                res.end();
            }
        } catch (err) {
            console.error('사용자 리스트 조회 중 에러 발생 : ' + err.stack);
            res.writeHead('200', {'Content-Type': 'text/html;charset=utf8'});
            res.write('<h2>사용자 리스트 조회 중 에러 발생</h2>');
            res.write('<p>' + err.stack + '</p>');
            res.end();
        }
    } else {
        res.writeHead('200', {'Content-Type': 'text/html;charset=utf8'});
        res.write('<h2>데이터베이스 연결 실패</h2>');
        res.end();
    }
};


//사용자를 인증하는 함수 : 아이디로 먼저 찾고 비밀번호를 그 다음에 비교하도록 함
var authUser = async function(database, id, password) {
    console.log('authUser 호출됨.');

    try {
        // 1. 아이디를 이용해 검색 (비동기 처리)
        const user = await database.UserModel.findById(id);

        if (user) {
            console.log('아이디와 일치하는 사용자 찾음.');

            // 2. 패스워드 확인: 사용자 객체에서 salt와 hashed_password를 가져옴
            var authenticated = await bcrypt.compare(password, user.salt, user.hashed_password);

            if (authenticated) {
                console.log('비밀번호 일치함');
                return user;  // 비밀번호가 일치하면 사용자 객체 반환
            } else {
                console.log('비밀번호 일치하지 않음');
                return null;  // 비밀번호가 일치하지 않으면 null 반환
            }
        } else {
            console.log('아이디와 일치하는 사용자를 찾지 못함.');
            return null;  // 사용자를 찾지 못했을 때 null 반환
        }
    } catch (err) {
        console.error('사용자 인증 중 에러 발생:', err);
        throw err;  // 에러 발생 시 throw
    }
};



//사용자를 등록하는 함수
var addUser = function(database, id, password, name, callback) {
	console.log('addUser 호출됨.');
	
	// UserModel 인스턴스 생성
	var user = new database.UserModel({"id":id, "password":password, "name":name});

	// save()로 저장
	user.save(function(err) {
		if (err) {
			callback(err, null);
			return;
		}
		
	    console.log("사용자 데이터 추가함.");
	    callback(null, user);
	     
	});
}


module.exports.login = login;
module.exports.adduser = adduser;
module.exports.listuser = listuser;

