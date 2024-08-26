<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>개선된 번역 및 감정 분석 앱</title>
</head>
<body>
  <div>
    <h1>개선된 번역 및 감정 분석 앱</h1>
    <div>
      <label for="textInput">분석 및 번역할 한국어 텍스트 입력:</label>
      <input type="text" id="textInput">
    </div>
    <button id="translateButton">분석 및 번역</button>
    <div id="translatedText"></div>
    <div id="sentimentAnalysis"></div>
    <div id="errorMessage"></div>
  </div>

  <!-- Load Sentiment.js from CDN -->
  <script src="https://cdn.jsdelivr.net/npm/sentiment@5.0.2/build/sentiment.min.js"></script>

  <script>
    document.addEventListener("DOMContentLoaded", function() {
      // Sentiment 객체를 전역에서 생성
      let sentiment;
      try {
        sentiment = new Sentiment();
      } catch (error) {
        console.error('Sentiment.js 라이브러리를 로드하는 데 실패했습니다.', error);
        document.getElementById('errorMessage').textContent = 'Sentiment.js 라이브러리를 로드하는 데 실패했습니다.';
        return;
      }

      async function translateText() {
        const textInput = document.getElementById('textInput').value;
        const errorMessageElement = document.getElementById('errorMessage');
        errorMessageElement.textContent = ''; // 이전 오류 메시지 초기화

        if (!textInput.trim()) {
          errorMessageElement.textContent = '텍스트를 입력해주세요.';
          return;
        }

        const url = 'https://google-translate1.p.rapidapi.com/language/translate/v2';
        const options = {
          method: 'POST',
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-RapidAPI-Key': '3805e733dcmsh0bb5fc49895ecd3p177bcejsn76dea8ebcbc9',
            'X-RapidAPI-Host': 'google-translate1.p.rapidapi.com'
          },
          body: `q=${encodeURIComponent(textInput)}&source=ko&target=en`
        };

        try {
          const response = await fetch(url, options);
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          const data = await response.json();
          if (data.data && data.data.translations && data.data.translations[0]) {
            const translatedText = data.data.translations[0].translatedText;
            const sentimentData = analyzeSentiment(translatedText); // 번역된 텍스트에 대해 감정 분석
            displayResults(translatedText, sentimentData);
          } else {
            throw new Error('번역 데이터를 받지 못했습니다.');
          }
        } catch (error) {
          console.error('번역 오류:', error);
          errorMessageElement.textContent = `오류 발생: ${error.message}. API 키를 확인하고 네트워크 연결을 확인해주세요.`;
          displayResults('번역 중 오류가 발생했습니다', { sentiment: '오류', score: 0, subjectivity: '알 수 없음' });
        }
      }

      function analyzeSentiment(text) {
        if (!sentiment) {
          console.error('Sentiment.js 객체가 정의되지 않았습니다.');
          return { sentiment: '오류', score: 0, subjectivity: '알 수 없음' };
        }

        const result = sentiment.analyze(text);

        // 감정 점수 계산 및 변환
        const polarityPercentage = ((result.score + 5) / 10 * 100).toFixed(2);
        const sentimentP = result.score > 0 ? "긍정적" : result.score < 0 ? "부정적" : "중립적";
        const subjectivity = Math.abs(result.score) > 2 ? "주관적" : "객관적";

        return {
          sentiment: sentimentP,
          score: polarityPercentage,
          subjectivity: subjectivity
        };
      }

      function displayResults(translatedText, sentimentData) {
        document.getElementById('translatedText').innerHTML = `<strong>번역된 텍스트:</strong> ${translatedText}`;
        document.getElementById('sentimentAnalysis').innerHTML = 
          `<strong>감정 분석 결과:</strong><br>
          감정: ${sentimentData.sentiment}<br>
          점수: ${sentimentData.score}%<br>
          주관성: ${sentimentData.subjectivity}`;
      }

      document.getElementById('translateButton').addEventListener('click', translateText);
    });
  </script>
</body>
</html>
