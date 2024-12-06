'use strict';

const fs = require('fs');
const path = require('path');
const Sequelize = require('sequelize');
const process = require('process');
const basename = path.basename(__filename);
const env = process.env.NODE_ENV || 'development';  // 노드 실행 환경 가져오기, 설정된 값이 없으면 development
const config = require(__dirname + '/../config/config.json')[env]; // 실행 환경에 맞는 db 접속 정보 가져오기
const db = {};

let sequelize;
if (config.use_env_variable) {
  sequelize = new Sequelize(process.env[config.use_env_variable], config);
} else {
  sequelize = new Sequelize(config.database, config.username, config.password, config);
}

fs
  .readdirSync(__dirname)
  .filter(file => {
    return (
      file.indexOf('.') !== 0 &&
      file !== basename &&
      file.slice(-3) === '.js' &&
      file.indexOf('.test.js') === -1
    );    // index.js 파일 제외한 models 폴더에 있는 js 파일을 가져옴
  })
  .forEach(file => {
    const model = require(path.join(__dirname, file))(sequelize, Sequelize.DataTypes);
    db[model.name] = model;
  });    // db객체에 모델 정보 저장

Object.keys(db).forEach(modelName => {
  if (db[modelName].associate) {
    // 테이블 매핑을 위해 생성한 model 파일의 associate() 함수로 전체 모델 정보를 전달해서 모델간의 연관 관계 설정
    // 연관관계라는 것을 RDBMS에서 테이블 간의 외래키를 설정하는 것과 같은 테이블의 연관 관계를 sequelize 모델에서 하는 것
    db[modelName].associate(db);
  }
});

db.sequelize = sequelize;
db.Sequelize = Sequelize;

module.exports = db;
