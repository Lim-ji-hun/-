const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');
const cors = require('cors'); // CORS 패키지 추가

const app = express();
const port = 5000;

// MySQL 데이터베이스 연결 설정
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '0252',
    database: 'lotto'
});

db.connect(err => {
    if (err) {
        console.error('DB 연결 오류:', err);
        return;
    }
    console.log('DB에 연결되었습니다.');
});

// Middleware 설정
app.use(cors()); // CORS 미들웨어 사용
app.use(bodyParser.json());

// POST 요청 처리
app.post('/send-numbers', (req, res) => {
    const { round, num1, num2, num3, num4, num5, num6, num7, num8 } = req.body;

    const sql = 'INSERT INTO lottery (round, num1, num2, num3, num4, num5, num6, num7) VALUES (?, ?, ?, ?, ?, ?, ?, ?)';
    db.query(sql, [round, num1, num2, num3, num4, num5, num6, num7, num8], (error, results) => {
        if (error) {
            console.error('DB 오류:', error);
            return res.status(500).json({ error: 'DB에 데이터를 저장하는데 오류가 발생했습니다.' });
        }
        res.status(200).json({ message: '데이터가 성공적으로 저장되었습니다.' });
    });
});

// 서버 실행
app.listen(port, () => {
    console.log(`서버가 http://localhost:${port}에서 실행 중입니다.`);
});
