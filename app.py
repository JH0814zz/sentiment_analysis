from textblob import TextBlob
from googletrans import Translator

# 번역기 객체 생성
translator = Translator()

# 분석할 텍스트 입력
text_korean = input(">> 긍정 / 부정, 객관 / 주관을 분석할 문장을 입력해주세요: ")

# 한국어를 영어로 번역
translated = translator.translate(text_korean, src='ko', dest='en')

# 번역된 텍스트
text = translated.text

print(f"영어로 번역된 문장 : {text}")

# TextBlob 객체 생성
blob = TextBlob(text)

# 감정 분석
sentiment = blob.sentiment

# 감정 분석 결과를 한국어로 번역
def translate_sentiment(polarity, subjectivity):
    # Polarity를 백분율로 변환
    polarity_percentage = round(polarity * 100, 2)
    # Subjectivity를 백분율로 변환
    subjectivity_percentage = round(subjectivity * 100, 2)
    
    if polarity > 0:
        sentiment_p = "긍정적"
    elif polarity < 0:
        sentiment_p = "부정적"
    else:
        sentiment_p = "중립적"
    
    if subjectivity > 0.5:
        sentiment_s = "주관적"
    else:
        sentiment_s = "객관적"
    
    sentiment_str = f"감정: {sentiment_p}, 주관성: {sentiment_s}"
    
    return polarity_percentage, subjectivity_percentage, sentiment_str

# 백분율로 변환된 감정 분석 결과
polarity_percentage, subjectivity_percentage, sentiment_str = translate_sentiment(sentiment.polarity, sentiment.subjectivity)

# 결과 출력
print(f"긍정도: {polarity_percentage}% ({'긍정적' if sentiment.polarity > 0 else '부정적' if sentiment.polarity < 0 else '중립적'})")
print(f"주관도: {subjectivity_percentage}% ({'주관적' if sentiment.subjectivity > 0.5 else '객관적'})")

if sentiment.polarity > 0:
    comparison = "긍정적입니다."
elif sentiment.polarity < 0:
    comparison = "부정적입니다."
else:
    comparison = "중립적입니다."

print(f"해석: {comparison}")
