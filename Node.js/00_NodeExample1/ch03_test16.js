function add(a, b, callback) {
    var result = a + b;          //1
    callback(result);            //2
    
    var history = function() {   //3
      return a +' + ' + b + ' = ' + result;  
    };
    return history;             //4
}

var add_history = add(10, 10, function(result) {
    console.log('파라미터로 전달된 콜백 함수 호출');       //5
    console.log('더하기 (10,10) : %d', result);        //6  
});

console.log('결과 값으로 받은 함수 실행 결과', add_history());  //7
