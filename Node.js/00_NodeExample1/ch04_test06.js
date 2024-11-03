var fs = require('fs');

//비동기식
fs.readFile('./package.json', 'utf8', function(err, data) {
    console.log(data);
});


console.log('프로젝트 폴더 안의 파일을 읽도록 요청했음');
