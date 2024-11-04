const express = require('express')
const fs = require('fs')
const morgan = require('morgan')
const path = require('path')

const app = express()

// create a write stream (in append mode)/HTTP 요청로그 파일로 생성&기록
const accessLogStream = fs.createWriteStream(path.join(__dirname, 'access.log'), { flags: 'a' })

// setup the logger
app.use(morgan('combined', { stream: accessLogStream }))

app.get('/', function (req, res) {
  res.send('hello, world!')
})

app.listen(8080);