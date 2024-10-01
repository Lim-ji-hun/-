import React, { useState } from 'react';
import './App.css';

function App() {
  const [variable, setVariable] = useState('');
  const [formData, setFormData] = useState({
    round: '',
    num1: '',
    num2: '',
    num3: '',
    num4: '',
    num5: '',
    num6: '',
    num7: ''
  });

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

  // 폼 데이터가 변경되면 상태를 업데이트하는 함수
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value
    }));
  };

  // 숫자들을 서버로 보내는 함수
  const sendNumbersToDB = async (e) => {
    e.preventDefault(); // 폼 제출 시 페이지 새로고침 방지

    // 모든 필드가 비어있지 않은지 확인
    for (const key in formData) {
      if (formData[key] === '') {
        window.alert(`모든 필드를 채워주세요: ${key}이(가) 비어있습니다.`);
        return;
      }
    }

    try {
      const response = await fetch('http://localhost:5000/send-numbers', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData), // 8개의 숫자와 회차 정보를 서버로 전송
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      window.alert('번호가 성공적으로 전송되었습니다!');
    } catch (error) {
      console.error('Error sending numbers:', error);
      window.alert('번호 전송 중 오류가 발생했습니다.');
    }
  };

  return (
    <div className="container">
      <h1>Jupyter 변수 가져오기</h1>
      <button onClick={fetchJupyterData}>변수 가져오기</button>
      <div className="variable">
        {variable && `받은 변수: ${variable}`}
      </div>

      <h2>복권 번호 입력</h2>
      <form onSubmit={sendNumbersToDB}>
        <input
          type="number"
          name="round"
          value={formData.round}
          onChange={handleInputChange}
          placeholder="복권 회차"
          required
        />
        <input
          type="number"
          name="num1"
          value={formData.num1}
          onChange={handleInputChange}
          placeholder="번호 1"
          required
        />
        <input
          type="number"
          name="num2"
          value={formData.num2}
          onChange={handleInputChange}
          placeholder="번호 2"
          required
        />
        <input
          type="number"
          name="num3"
          value={formData.num3}
          onChange={handleInputChange}
          placeholder="번호 3"
          required
        />
        <input
          type="number"
          name="num4"
          value={formData.num4}
          onChange={handleInputChange}
          placeholder="번호 4"
          required
        />
        <input
          type="number"
          name="num5"
          value={formData.num5}
          onChange={handleInputChange}
          placeholder="번호 5"
          required
        />
        <input
          type="number"
          name="num6"
          value={formData.num6}
          onChange={handleInputChange}
          placeholder="번호 6"
          required
        />
        <input
          type="number"
          name="num7"
          value={formData.num7}
          onChange={handleInputChange}
          placeholder="번호 7"
          required
        />
        <button type="submit">번호 보내기</button>
      </form>
    </div>
  );
}

export default App;
