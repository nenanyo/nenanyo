var fs = require('fs');

//비동기식
fs.writeFile('./output.txt', 'HELLO', function(err) {
    if(err){
        console.log(err);
    }
    console.log('파일에 데이트 쓰기 완료');
});



