from PyQt5 import QtCore,QtGui,QtWidgets
from pygame import mixer 

from index import GravityNinja
from db import db
dbase = db()
selectUser=()
'''
اگه بخواهیم یه اهنگ یا صدایی رو به بازی اضافه کنیم
 کد های زیر رو میزنیم و اسم هر اهنگی رو دلخواه میزاریم
 البته باید یه جور باشه که بتونیم استفاده کنیم
بعد ادرس اون اهنگ رو کپی پست میکنیم و اسم اون اهنگ با فرمت رو میزنیم

mixer.music.load("ادرس اون اهنگ")   
mixer.music.play(loops=0)
power by hossin 
'''
global volume_seda
global music_1
global music_2
global music_3
global music_4
global music_5
global Acc_EMH
volume_seda = mixer.music.set_volume
mixer.init()

mixer.pre_init(44100,16,2,4096)
mixer.init()

# ذخیره سرعت و صدای بازی 
speed = "3" # "2" "3"
music = 'Music\Music 5.mp3'

# متغییر گلوبال برای صفحات که بتوانیم انها رو ببندیم و باز کنیم
main,ui2 = "",""
setting ,ui3 = "",""
begining,ui4 = "",""

#اهنگ های بازی

music_1 = 'Music\Music 1.mp3'
music_2 = 'Music\Music 2.mp3'
music_3 = 'Music\Music 3.mp3'
music_4 = 'Music\Music 4.mp3'
music_5 = 'Music\Music 5.mp3'
music_fail_1 = 'Music\Music Fail 1.mp3'
music_fail_2 = 'Music\Music Fail 2.mp3'




#اولی صدای دکمه برای ورود به صفحات
#دومی برای بازگشت به منو
#سومی ثبت نام موفق!
#چهارمی صدای ارور برای ورود به منو
#پنجمی برای حالت تک نفره
#ششمی برای حالت دو نفره
#هفتمی برای تعیین میزان سختی

music_button =mixer.Sound (r'Sound\sfx_menu_c.wav')
music_bakeM = mixer.Sound (r'Sound\sfx_menu_back.wav')
music_Inter = mixer.Sound (r'Sound\sfx_Register.wav')
music_InterM = mixer.Sound (r'Sound\cannot.ogg')
single_player = mixer.Sound(r'Sound\sfx_single_player.ogg')
multi_player = mixer.Sound(r'Sound\sfx_multi_player.ogg')
Acc_EMH = mixer.Sound(r'Sound\Acc_E_M_H.ogg')



#صفحه اخر که مربوط به بخش چند نفره و تک نفره هست
class Begining(object):
    def setupUi(self, begining):
        Form = begining
        Form.setObjectName("Form")
        Form.resize(542, 544)
        Form.setMinimumSize(QtCore.QSize(542, 544))
        Form.setMaximumSize(QtCore.QSize(542, 544))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-20, -100, 571, 831))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/BackGround.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
#دکمه بخش تک نفره
        self.SinglePLayer = QtWidgets.QPushButton(Form)
        self.SinglePLayer.setGeometry(QtCore.QRect(380, 280, 131, 141))
        self.SinglePLayer.setStyleSheet("")
        self.SinglePLayer.setText("")
        self.SinglePLayer.setIconSize(QtCore.QSize(40, 40))
        self.SinglePLayer.setCheckable(False)
        self.SinglePLayer.setFlat(True)
        self.SinglePLayer.setObjectName("SinglePLayer")
        self.SinglePLayer.clicked.connect(self.SINGLE_PLAYER)
        #دکمه بخش دو نفره
        self.MultiPlayer = QtWidgets.QPushButton(Form)
        self.MultiPlayer.setGeometry(QtCore.QRect(30, 280, 131, 141))
        self.MultiPlayer.setStyleSheet("")
        self.MultiPlayer.setText("")
        self.MultiPlayer.setIconSize(QtCore.QSize(40, 40))
        self.MultiPlayer.setCheckable(False)
        self.MultiPlayer.setFlat(True)
        self.MultiPlayer.setObjectName("MultiPlayer")
        self.MultiPlayer.clicked.connect(self.MULTI_PLAYER)
        
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(0, 10, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 280, 131, 141))
        self.label_2.setStyleSheet("border-radius:30%;\n"
"border:10px solid black;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/MULTI.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(380, 280, 131, 141))
        self.label_3.setStyleSheet("border-radius:30%;\n"
"border:10px solid black;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img/SINGLE.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.Returntomain_2 = QtWidgets.QPushButton(Form)
        self.Returntomain_2.setGeometry(QtCore.QRect(10, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(20)
        self.Returntomain_2.setFont(font)
        self.Returntomain_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.Returntomain_2.setFlat(True)
#دکمه بازگشت به منوی اصلی
        self.Returntomain_2.setObjectName("Returntomain_2")
        self.Returntomain_2.clicked.connect(self.SToMainMenu)
        self.label.raise_()
        self.label_8.raise_()
        self.label_3.raise_()
        self.SinglePLayer.raise_()
        self.Returntomain_2.raise_()
        self.label_2.raise_()
        self.MultiPlayer.raise_()
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "Gravity Ninja"))
        self.Returntomain_2.setText(_translate("Form", "بازگشت به منو"))
        

     # تابع بازگشت به منوی اصلی
    def SToMainMenu(self):
        global main ,ui2,begining
        music_bakeM.play()
        main= QtWidgets.QWidget()
        ui2 = MainPage()
        ui2.setupUi(main)
        begining.hide()
        main.show()
        
    def SINGLE_PLAYER(self):
        global music_button,music_bakeM,music_Inter,music_InterM,multi_player,Acc_EMH,main,dbase,selectUser,music,speed
        single_player = mixer.Sound(r'Sound\sfx_single_player.ogg')
        single_player.play()
        dbase.setnumplay(selectUser[0])
        selectUser =  dbase.searchByID(selectUser[0])[1]
        if  GravityNinja(speed,"YELLOW",music):
            mixer.init()
            mixer.pre_init(44100,16,2,4096)
            mixer.init()
            music_button =mixer.Sound (r'Sound\sfx_menu_c.wav')
            music_bakeM = mixer.Sound (r'Sound\sfx_menu_back.wav')
            music_Inter = mixer.Sound (r'Sound\sfx_Register.wav')
            music_InterM = mixer.Sound (r'Sound\cannot.ogg')
            single_player = mixer.Sound(r'Sound\sfx_single_player.ogg')
            multi_player = mixer.Sound(r'Sound\sfx_multi_player.ogg')
            Acc_EMH = mixer.Sound(r'Sound\Acc_E_M_H.ogg')
        pass
    
    
    def MULTI_PLAYER(self):
        multi_player.play()
        
        pass
     

#صفحه تنظیمات
class settingForm(object):
    def setupUi(self, setting):
        Form = setting
        Form.setObjectName("Form")
        Form.resize(542, 544)
        Form.setMinimumSize(QtCore.QSize(542, 544))
        Form.setMaximumSize(QtCore.QSize(542, 544))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-30, -100, 571, 831))
        self.label.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/BackGround.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(350, 270, 150, 21))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(380, 310, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10%;")
        
#انتخاب اهنگ
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.activated.connect(self.MusicPlayer)
        
        
#تنظیم میزان صدای اهنگ پس زمینه
        self.mizanSeda = QtWidgets.QSlider(Form)
        self.mizanSeda.setGeometry(QtCore.QRect(500, 210, 31, 141))
        self.mizanSeda.setProperty("value", 99)
        self.mizanSeda.setOrientation(QtCore.Qt.Vertical)
        self.mizanSeda.setObjectName("mizanSeda")
        self.label_3 = QtWidgets.QLabel(Form)
        self.mizanSeda.valueChanged.connect(self.MizanS)
        self.mizanSeda.setMinimum(10)
        self.mizanSeda.setMaximum(100)
        self.mizanSeda.setValue(100)
        self.mizanSeda.setTickInterval(10)
        
        self.label_3.setGeometry(QtCore.QRect(20, 260, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(18)
        
        
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.Sakhty = QtWidgets.QComboBox(Form)
        self.Sakhty.setGeometry(QtCore.QRect(30, 310, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(16)
        self.Sakhty.setFont(font)
        self.Sakhty.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10%;")
#تنظیم میزان سختی بازی
        self.Sakhty.setObjectName("Sakhty")
        self.Sakhty.addItem("")
        self.Sakhty.addItem("")
        self.Sakhty.activated.connect(self.E_M_H)
        
        self.Returntomain_2 = QtWidgets.QPushButton(Form)
        self.Returntomain_2.setGeometry(QtCore.QRect(10, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(20)
        
 #دکمه بازگشت به منوی اصلی
        self.Returntomain_2.setFont(font)
        self.Returntomain_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.Returntomain_2.setFlat(True)
        self.Returntomain_2.setObjectName("Returntomain_2")
        self.Returntomain_2.clicked.connect(self.SToMainMenu)

#دکمه قطع و وصل کردن موسیقی پس زمینه بازی
        self.Play = QtWidgets.QPushButton(Form)
        self.Play.setGeometry(QtCore.QRect(390, 210, 41, 41))
        self.Play.setStyleSheet("")
        self.Play.setText("")
        self.Play.setFlat(True)
        self.Play.setObjectName("Play")
        self.Play.clicked.connect(self.Play_Music)
        self.Stop = QtWidgets.QPushButton(Form)
        self.Stop.setGeometry(QtCore.QRect(440, 210, 41, 41))
        self.Stop.setStyleSheet("")
        self.Stop.setText("")
        self.Stop.setFlat(True)
        self.Stop.setObjectName("Stop")
        self.Stop.clicked.connect(self.Stop_music)
        
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(390, 210, 41, 41))
        self.label_4.setStyleSheet("border-radius:30%;\n"
"border:5px solid black;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img/Pause_Music.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(440, 210, 41, 41))
        self.label_6.setStyleSheet("border-radius:30%;\n"
"border:5px solid black;")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("img/Unpause_Music.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label.raise_()
        self.label_2.raise_()
        self.comboBox.raise_()
        self.mizanSeda.raise_()
        self.label_3.raise_()
        self.Sakhty.raise_()
        self.Returntomain_2.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        self.Stop.raise_()
        self.Play.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "انتخاب اهنگ"))
        self.comboBox.setItemText(0, _translate("Form", "اهنگ1"))
        self.comboBox.setItemText(1, _translate("Form", "اهنگ2"))
        self.comboBox.setItemText(2, _translate("Form", "اهنگ3"))
        self.comboBox.setItemText(3, _translate("Form", "اهنگ4"))
        self.comboBox.setItemText(4, _translate("Form", "اهنگ5"))
        self.label_3.setText(_translate("Form", "میزان سختی"))
        self.Sakhty.setItemText(0, _translate("Form", "متوسط"))
        self.Sakhty.setItemText(1, _translate("Form", "سخت"))
        self.Returntomain_2.setText(_translate("Form", "بازگشت به منو"))
        
        
        
        
    def SToMainMenu(self):
        global main ,ui2,setting
        music_bakeM.play()
        main= QtWidgets.QWidget()
        ui2 = MainPage()
        ui2.setupUi(main)
        setting.hide()                             
        main.show()
     
#تابع قطع و وصل کردن موسیقی
    def Play_Music(self):
        mixer.music.unpause()
            
    def Stop_music(self):
        mixer.music.pause()
      
#تابع میزان صدا
    def MizanS(self,value):
        volume_seda(value/100)
        
#تابع انتخاب موسیقی
    def MusicPlayer (self):
        global music
        M=self.comboBox.currentText()

        M1="اهنگ1"
        M2="اهنگ2"
        M3="اهنگ3"
        M4="اهنگ4"
        M5="اهنگ5"
        
        if (str(M) ==  M1 ):
            mixer.music.stop()
            mixer.music.load(music_1)
            music = music_1
            mixer.music.play(loops=10)
            
        elif (str(M) == M2 ):
            mixer.music.stop()
            mixer.music.load(music_2)
            music = music_2
            mixer.music.play(loops=10)
            
        elif (str(M) == M3 ):
            mixer.music.stop()
            mixer.music.load(music_3)
            music = music_3
            mixer.music.play(loops=10)
            
        elif (str(M) == M4):
           mixer.music.stop()
           mixer.music.load(music_4)
           music = music_4
           mixer.music.play(loops=10)
            
        elif (str(M)== M5 ):
           mixer.music.stop()
           mixer.music.load(music_5)
           music = music_5
           mixer.music.play(loops=10)
           
        
    def E_M_H(self):
        global speed
        stat = self.Sakhty.currentText()
        medium = "متوسط"
        hard = "سخت"
        
        
        if (str(stat) == medium):
            Acc_EMH.play()
            speed="3"
            pass
        elif (str(stat) == hard):
            Acc_EMH.play()
            speed="2"
            pass
            
#صفحه اصلی بازی
class MainPage(object):
    def setupUi(self, main):
        Form = main
        Form.setObjectName("Form")
        Form.resize(542, 544)
        Form.setMinimumSize(QtCore.QSize(542, 544))
        Form.setMaximumSize(QtCore.QSize(542, 544))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-20, -120, 571, 831))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/BackGround.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.wellcometogame = QtWidgets.QLabel(Form)
        self.wellcometogame.setGeometry(QtCore.QRect(0, 50, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(14)
        self.wellcometogame.setAlignment(QtCore.Qt.AlignCenter)
        self.wellcometogame.setFont(font)
        self.wellcometogame.setStyleSheet("color: rgb(255, 255, 255);")
        self.wellcometogame.setObjectName("wellcometogame")

        
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(0, 10, 541, 330))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(0, 10, 541, 400))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
       
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(0, 10, 541, 470))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(0, 10, 541, 540))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")


        self.begingame = QtWidgets.QPushButton(Form)
        self.begingame.setGeometry(QtCore.QRect(280, 400, 161, 131))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(18)
        
        self.begingame.setFont(font)
        self.begingame.setStyleSheet("color: rgb(255, 255, 255);")
        self.begingame.setFlat(True)
#دکمه رفتن به صفحه انتخاب بخش تک یا چند نفره بازی
        self.begingame.setObjectName("begingame")
        self.begingame.clicked.connect(self.SToBegining)
        self.setting = QtWidgets.QPushButton(Form)
        self.setting.setGeometry(QtCore.QRect(120, 400, 161, 131))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(18)
        self.setting.setFont(font)
        self.setting.setStyleSheet("color: rgb(255, 255, 255);")
        self.setting.setFlat(True)
#دکمه رفتن به تنظیمات بازی
        self.setting.setObjectName("setting")
        self.setting.clicked.connect(self.STosetting)
        self.khoshamadgoy = QtWidgets.QLabel(Form)
        self.khoshamadgoy.setAlignment(QtCore.Qt.AlignCenter)
        self.khoshamadgoy.setGeometry(QtCore.QRect(10, 80, 521, 111))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(20)
#خوش امد گوی بازی که با اسم به بازیکنان عصر بخیر  می گوید
        global A
        A=self.khoshamadgoy.setText
        self.khoshamadgoy.setFont(font)
        self.khoshamadgoy.setStyleSheet("color: rgb(255, 255, 255);")
        self.khoshamadgoy.setObjectName("khoshamadgoy")
        
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(0, 10, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        global selectUser
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.wellcometogame.setText(_translate("Form", "به بازی Grvity Ninja خوش امدید"))
        self.begingame.setText(_translate("Form", "شروع بازی"))
        self.setting.setText(_translate("Form", "تنظیمات"))
        self.label_8.setText(_translate("Form", "Gravity Ninja"))
        self.label_9.setText("نام بازیکن = " + selectUser[1])
        self.label_10.setText("تعداد سکه ها = " + selectUser[2])
        self.label_11.setText("تعداد بازی ها = " + selectUser[3])
        self.label_12.setText("ایدی بازیکن = " + selectUser[0])

#تابع رفتن به بخش تنیظمات بازی
    def STosetting (self):
        global setting ,ui3
        music_button.play()
        setting= QtWidgets.QWidget()
        ui3 = settingForm()
        ui3.setupUi(setting)
        main.hide()
        setting.show()

#تابع رفتن به صفحه انتخاب بخش تک یا چند نفره بازی
    def SToBegining(self):
       global begining,ui4,main
       music_button.play()
       begining= QtWidgets.QWidget()
       ui4 = Begining()
       ui4.setupUi(begining)
       main.hide()
       begining.show()
        
       

#صفحه نام نویسی کاربران
class RegisterForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(542, 544)
        Form.setMinimumSize(QtCore.QSize(542, 544))
        Form.setMaximumSize(QtCore.QSize(542, 544))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-20, -100, 571, 831))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/BackGround.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, -10, 541, 161))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 220, 461, 144))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Nninja1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Nninja1.setStyleSheet("border-radius:10%;\n"
"border:2px solid red;height:40px;")
#کادر وارد کردن اسم کاربر اول
        self.Nninja1.setText("")
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(20)
        self.Nninja1.setFont(font)
        self.Nninja1.setObjectName("Nninja1")
        self.gridLayout.addWidget(self.Nninja1, 0, 0, 1, 1)
        self.ninja1 = QtWidgets.QLabel(self.gridLayoutWidget)

        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(18)
        self.ninja1.setFont(font)
        self.ninja1.setStyleSheet("color: rgb(255, 255, 255);")
#کادر وارد کردن اسم کاربر دوم
        self.ninja1.setObjectName("ninja1")
        self.gridLayout.addWidget(self.ninja1, 0, 1, 1, 1)
        self.ninja2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(18)
        self.ninja2.setFont(font)
        self.ninja2.setStyleSheet("color: rgb(255, 255, 255);")
        self.ninja2.setObjectName("ninja2")
        self.gridLayout.addWidget(self.ninja2, 2, 1, 1, 1)
        self.Nninja1_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Nninja1_2.setStyleSheet("border-radius:10%;\n"
"border:2px solid red;height:40px;")
        self.Nninja1_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(20)
        self.Nninja1_2.setFont(font)
        self.Nninja1_2.setObjectName("Nninja1_2")
        self.gridLayout.addWidget(self.Nninja1_2, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 480, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(0, 10, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
#دکمه ورود به صفحه اصلی بازی
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 450, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Login)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 370, 461, 71))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "اسمت رو وارد کن نینجا"))
        self.ninja1.setText(_translate("Form", "نام نینجا اول :"))
        self.ninja2.setText(_translate("Form", "نام نینجا دوم :"))
        self.label_5.setText(_translate("Form", "نکته : نام نینجای دوم اجباری نیست اما برای نینجای اولی اجباریست"))
        self.label_8.setText(_translate("Form", "Gravity Ninja"))
        self.pushButton.setText(_translate("Form", "ورود"))
#تابع لاگین بازی که اسم یک یا دو کاربر را میگیرد
    def Login (self):
        
        global N1,N2,dbase,selectUser
        
        N1=[]
        N2=[]
        N1=self.Nninja1.text()
        N2=self.Nninja1_2.text()
        LenN1=len(N1)
        LenN2=len(N2)
        datares = dbase.searchByname(N1)
        if ( datares[0]) :
            selectUser = datares[1]
        else :
            res = dbase.createUser(N1)
            if(res[0]):
                selectUser = res[1]
        if (LenN1==0) and (LenN2==0):
            music_InterM.play()
            self.label_3.setText("زور نزن باید یه اسم وارد کنی \U0001F609")
        elif (LenN1==0) and (LenN2>=1):
            music_InterM.play()
            self.label_3.setText("خو همین اسم رو تو کادر اول بزن^_^")
        elif (LenN1>=1) and (LenN2==0):
            music_Inter.play()
            self.label_3.setText("{} اسمت با موفقیت ذخیره شد \U0001f603".format(N1))
            self.SToMainMenu()
            A("{} عصرت بخیر باشه \U0001f603".format(N1))
        elif (LenN1>=1) and (LenN2>=1):
            music_Inter.play()
            self.label_3.setText("{} و {} اسمتون با موفقیت ذخیر شد \U0001f600".format(N1,N2))
            self.SToMainMenu()

            A("{} و {} عصرتون بخیر باشه \U0001f600".format(N1,N2))
        
            
#تابع رفتن به منوی بازی
    def SToMainMenu(self):
        global main,ui2
        main= QtWidgets.QWidget()
        ui2 = MainPage()
        ui2.setupUi(main)
        Form.hide()
        main.show()
        
    def Off(self):
        import sys
        mixer.music.stop()
        sys.exit(app.exec_())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = RegisterForm()
    ui.setupUi(Form)
    Form.show()
    mixer.music.stop()
    sys.exit(app.exec_())





