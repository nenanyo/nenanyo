// app.js 또는 index.js
const express = require('express');
const { Sequelize } = require('sequelize');
const User = require('./models/User'); // User 모델 가져오기

const app = express();

// 데이터베이스 연결
const sequelize = new Sequelize('test', 'test_user', 'test', {
    host: 'localhost',
    dialect: 'mysql',
});

// 데이터베이스 연결 테스트
sequelize.authenticate()
    .then(() => {
        console.log('데이터베이스 연결 성공');
    })
    .catch(err => {
        console.error('데이터베이스 연결 실패:', err);
    });

// 서버 시작
app.listen(3000, () => {
    console.log('서버가 3000 포트에서 시작되었습니다.');
});
