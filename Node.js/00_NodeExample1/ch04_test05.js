var fs = require('fs');

//동기식
var data = fs.readFileSync('./package.json', 'utf8');
console.log(data);
