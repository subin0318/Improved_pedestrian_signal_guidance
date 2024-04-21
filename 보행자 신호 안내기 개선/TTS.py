from gtts import gTTS
from playsound import playsound

text="현제 신호등이 빨간불입니다 조금만 기달려주세요 감사합니다"


flie_name="red.mp3"


tts=gTTS(text=text,lang='ko')

tts.save(flie_name)


playsound(flie_name)