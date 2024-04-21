import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from playsound import playsound ## PyQt5 라이브러리를 가져오겠습니다 


Traffic_Light=[] ## 데이터 처리 빨간불과 초록불 
situation_handling=[] ## 상황처리 빨간불 1 초록불 0 으로 처리


flie_name="red.mp3" ## mp3 파일을 flie_name으로 정의 하겠습니다
flie_name2="green.mp3" 


class MyApp(QWidget): 

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
            self.Lable_name=QLabel('신호등 판별하기' , self)
            self.Lable_name.adjustSize()
            self.Lable_name.setGeometry(QRect(234, 50, 121, 81))
             
            self.image=QLabel(self) 
            ## GUI 화면에 드라이브에서 가져온 이미지를 보기위해 선언
       
            self.guide=QLabel('신호등 이미지를 산입하여 신호등을 분류합니다' , self)
            self.guide.move(130,500)
            self.guide.adjustSize()
            
            self.Traffic_Light=QLabel('빨간불과 초록불',self)
            self.Traffic_Light.setGeometry(QRect(258,540, 200, 100))
            self.Traffic_Light.adjustSize()
            self.Traffic_Light.setHidden(True)
            
            ## 신호등의 사진을 인식하여 사용자에게 빨간불 초록불 이라고 알려줌
            
            self.Traffic_NOTLight=QLabel('구별 할수없습니다',self)
            self.Traffic_NOTLight.setGeometry(QRect(224,540, 200, 100))
            self.Traffic_NOTLight.adjustSize()
            self.Traffic_NOTLight.setHidden(True)
            
            ## 인식을 하지못한다면 구별할수없습니다라고 사용자에게 보여줌
            
            self.upload=QPushButton('파일 업로드',self)
            self.upload.move(170,430)
            self.upload.resize(240,40)
            self.upload.setEnabled(True)
            self.upload.clicked.connect(self.loadImage)
         
            ## 버튼을 클릭시 loadImage 함수가 발생한다 
            
            self.setWindowTitle('신호등 판별 알림 도우미')
            self.resize(600, 600)
            self.show() 
            
    def loadImage(self):
        
        fname = QFileDialog.getOpenFileName(self)
        pixmap = QPixmap(fname[0])
        self.image.setPixmap(QPixmap(pixmap))
        self.image.setGeometry(QRect(10, 110, 581, 301))
        self.image.setScaledContents(True)
        
        ## 버튼클릭시 QFileDialog 가 발생한다 
     
        if "빨간불" in fname[0]:
           ## 파일명에 빨간불이 있으면 다음과 같이 처리하겠습니다
            self.Traffic_Light.setText('빨간불')
            self.Traffic_Light.setHidden(False)
            self.Traffic_NOTLight.setHidden(True)
            playsound(flie_name,True)
            Traffic_Light.append("빨간불")
            print(*Traffic_Light)
            situation_handling.append(1)
            print(*situation_handling)
           
        
        elif "초록불" in fname[0]:
           ## 파일명에 초록불이 있으면 다음과 같이 처리하겠습니다
            self.Traffic_Light.setText('초록불')
            self.Traffic_Light.setHidden(False)
            self.Traffic_NOTLight.setHidden(True)
            playsound(flie_name2,True)
            Traffic_Light.append("초록불")
            print(*Traffic_Light)
            situation_handling.append(0)
            print(*situation_handling)
           
            
       
        elif "redLight" in fname[0]:
             self.Traffic_Light.setText('빨간불')
             self.Traffic_Light.setHidden(False)
             self.Traffic_NOTLight.setHidden(True)
             playsound(flie_name,True)
             Traffic_Light.append("빨간불")
             print(*Traffic_Light)
             situation_handling.append(1)
             print(*situation_handling)
        
        elif "greenLight" in fname[0]:
            self.Traffic_Light.setText('초록불')
            self.Traffic_Light.setHidden(False)
            self.Traffic_NOTLight.setHidden(True)
            playsound(flie_name2,True)
            Traffic_Light.append("초록불")
            print(*Traffic_Light)
            situation_handling.append(0)
            print(*situation_handling)
            
            
        else:
           self.Traffic_Light.setHidden(True)
           self.Traffic_NOTLight.setHidden(False)
           ## 이미지를 여러번 처리하기떄문에 글자를 보여주는것 
           ## True,False 구분을 잘해줘야한다
       
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())