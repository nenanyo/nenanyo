const express = require('express')
const app = express()
const port = 3000


//HTTP 중 GET 이용해서 'host:port'로 요청을 보내면 실행되는 라우트
app.get('/',(req, res) => {
    res.send('hello world')
})

//app.listen()함수 사용해서 서버 실행
//클라이언트는 'host:port'로 노드 서버에 요청을 보낼 수 있다.
app.listen(port, () => {
    console.log(`서버 실행 http://localhost:${port}`)
});


app.get('/customer', function(req, res)  {
    res.send('get 응답');                                

});

app.post('/customer', function(req, res) {
    res.send('post 응답');
});

app.all('/customer', function(req, res) {
    res.send('HTTP 요청 상관없이');
});