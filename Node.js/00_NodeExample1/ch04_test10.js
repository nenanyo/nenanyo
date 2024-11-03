//버퍼 객체를 크기만 지정하여 만든 후 문자열 쓰기
var output = 'hello 1!';
var buffer1 = new Buffer(10);
var len = buffer1.write(output,'utf8');
console.log('1st buffer : %s', buffer1.toString());

//버퍼 객체를 문자열을 이용해 만들기
var buffer2 = new Buffer('hello 2!', 'utf8');
console.log('2nd buffer : %s', buffer2.toString());

//타입 확인
console.log('type : %s', Buffer.isBuffer(buffer1));

//버퍼 객체에  들어있는 문자열 데이터를 문자열 변수로
var byteLen = Buffer.byteLength(output);
var str1 = buffer1.toString('utf8',0,byteLen);
var str2 = buffer2.toString('utf8');


//첫번째 버퍼 객체의 문자열을 두 번째 버퍼 객체로 복사
buffer1.copy(buffer2,0,0,len);
console.log('after copy : %s', buffer2.toString('utf8'));

//두개의 버퍼 붙이기
var buffer3 = Buffer.concat([buffer1,buffer2]);
console.log('after concat : %s', buffer3.toString('utf8'));
