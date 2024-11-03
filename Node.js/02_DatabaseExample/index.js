const express = require('express');
const mysql2 = require('mysql2');
const app = express();
const port = 8080;

const cnn = mysql2.createConnection({
    host: 'localhost',
    user: 'test_user',
    password: 'test',
    database: 'test'
});

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    cnn.query('select * from user', (err, result) => {
        if (err) throw err;
    

        console.log(result);
        res.render('index', {rows: result});
    });
});


app.listen(port, () => {
    console.log('server open : ', port);
});
