//require() 메소드는 exports 객체 반화
var user1 = require('./user1');

function showUser () {
    return user1.getUser().name + ',' + user1.group.name;

}

console.log('사용자 정보 : %s', showUser());