// models/User.js
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = new Sequelize('test', 'test_user', 'test', {
    host: 'localhost',
    dialect: 'mysql',
});

const User = sequelize.define('User', {
    id: {
        type: DataTypes.STRING,
        primaryKey: true,
        allowNull: false,
    },
    password: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    name: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    age: {
        type: DataTypes.INTEGER,
        defaultValue: -1,
    },
   
}, {
    timestamps: true, // createdAt, updatedAt 필드를 자동으로 생성
});

// User 모델을 export
module.exports = User;
