var Users = [{name : '소녀시대', age : 20}, {name : '걸스데이', age : 22}, {name : '티아라', age : 23}];

console.log('배열요소 수 : %d', Users.length);
for (var i=0; i<Users.length; i++) {
    console.log('배열 요소 #' + i + ' : %s', Users[i].name);
}

Users.forEach(function(item,index) {
    console.log('배열 요소 #' + index + ' : %s', item.name);
});