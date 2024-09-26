import React, { useState } from 'react';
import './App.css';

function App() {
  const [numbers, setNumbers] = useState([]);
  const [variable, setVariable] = useState('');

  // Flask API에서 데이터를 받아오는 함수
  const fetchJupyterData = async () => {
    try {
      const response = await fetch('http://localhost:5000/get-variable');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setVariable(data.aaa); // 서버에서 받아온 변수 설정
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };
  

  const generateLotteryNumbers = () => {
    const numCount = 6; // 생성할 번호 개수
    const maxNum = 45;  // 최대 번호
    const uniqueNumbers = new Set();

    while (uniqueNumbers.size < numCount) {
      const randomNum = Math.floor(Math.random() * maxNum) + 1;
      uniqueNumbers.add(randomNum);
    }

    setNumbers(Array.from(uniqueNumbers).sort((a, b) => a - b));
  };

  return (
    <div className="container">

      <h1>복권 번호 생성기</h1>
      <button onClick={generateLotteryNumbers}>번호 생성</button>
      <h1>Jupyter 변수 가져오기</h1>
      <button onClick={fetchJupyterData}>변수 가져오기</button>
      <div className="numbers">
        {numbers.length > 0 && numbers.join(', ')}
      </div>
      <div className="variable">
        {variable && `받은 변수: ${variable}`}
      </div>

    </div>
  );
}

export default App;
