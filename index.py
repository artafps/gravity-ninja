import pygame

def GravityNinja(speed ,NinjaColor, music):
    
    #init pygame
    pygame.init()
    clock = pygame.time.Clock() # fps
    # تنظیم سختی بازی
    weidth= [300,280,250,0,220,200,180,150,120,100]
    mapy=10
    Leng = 9
    if speed =="2":
        weidth= [300,250,0,200,150,100]
        distance = 200
        mapy=10
        Leng = 5
    if speed =="3":
        weidth= [300,280,250,0,220,200,180,150,120,100]
        distance = 130
        mapy=10
        Leng = 9
    # تنظیم سایز صفحه
    w,h = 600,600
    sur = pygame.display.set_mode((w,h))
    # تعیین رنگ نینجا
    if(NinjaColor == "YELLOW"):
        imgurl = ["./img/P2.png","./img/P3.png"]
    else:
        imgurl = ["./img/2.png","./img/3.png"]
    number = True
    # ارایه ستون
    mapsarr = [{"x":0,"w":0,"y":0,"h":600},{"x":400,"y":0,"w":200,"h":600},]

    # اهنگ های پرش و برخورد و پس زمینه  
    music_effort = pygame.mixer.Sound (r'Sound\sfx_effort_1.wav')
    music_hurt = pygame.mixer.Sound (r'Sound\sfx_hurt_1.wav')
    music_song = pygame.mixer.Sound (music)
    
    music_song.play(loops=10)
    
    # متن گیم اور  
    font = pygame.font.SysFont("comicsansms", 72) # set font
    text = font.render("Game Over", True, (255, 0, 0))
    #دویدن نینجا
    cic = 3
    boleancic = False

    #متغییر ها برای افزودن ستون 
    p=180
    s=400
    z1,z2=0,0
    z=0
    bolean = True
    #موقیت اولیه نینجا
    x,y = 350,460
    xz = 200
    #چپ وراست بودن نینجا
    Area=True
    #زمانی که دکمه ها برای رفتن به چپ یا راست کلیک شد 
    btnclicked=False
    # متغییر برای استپ
    btnclickedPuse=False
    # برای افزودن ستون بصورت دانه ای
    blbox = True
    #تعداد جان نینجا
    Heart = 3
    # سرعت نینجا در محور x
    vx = 0
    # ارایه سکه
    coinarry = []

    
    
    while True :
           
        sur.fill((0,200,255))
        if( Heart != 0):#تشخیص مرگ نینجا 
            
            #backgroun img
            # پشت زمینه عکس خورشید
            sun= pygame.image.load("./img/sun.png")
            sun = pygame.transform.scale(sun,(400,400))  
            sur.blit(sun,(150,50))
            # عکس شهر پشت زمینه
            maps= pygame.image.load("./img/map.png")
            maps = pygame.transform.scale(maps,(620,620))  
            sur.blit(maps,(-10,-10))
            # افزودن ستون ها  
            if p == 180:
                p=200
            else:
                p=180
            if s == 200:
                s=180
            else:
                s=200
            if bolean:
                z+=1
            if not bolean:
                z-=1
            if(z==Leng):
                bolean = False
            if(z==0):
                bolean = True
            z1,z2 = z1-p,z2-s
            if weidth[z] == 0 :
                if not blbox:
                    mapsarr.append({"x":weidth[z]+distance+250,"w": 600-weidth[z]-distance,"y":z2+200,"h":s+10})
                    blbox = not blbox
                if blbox :
                    mapsarr.append({"x":0,"w":weidth[z],"y":z1,"h":p+10})
                    blbox = not blbox
        
            else:
                if not blbox:
                    mapsarr.append({"x":weidth[z]+distance,"w": 600-weidth[z]-distance,"y":z2+200,"h":s+10})
                    blbox = not blbox
                if blbox :
                    mapsarr.append({"x":0,"w":weidth[z],"y":z1,"h":p+10})
                    blbox = not blbox
                #coinarry.append({"nx":weidth[z]+130,"ny":z2+50})
            # پایان افزودن ستون ها
                    

            # vx change values
            x+=vx
            
            #event
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # if event is quit
                    
                    Heart=0   
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: # if event is keydown and key is escape
                    if(btnclickedPuse):# برسی استپ 
                        music_song.play() #پخش موزیک پس زمینه بازی
                    else:
                        music_song.stop()#قطع موزیک پس زمینه بازی
                    btnclickedPuse=not btnclickedPuse   
                if event.type == pygame.KEYDOWN:
                    if event.key==1073741903 and not Area:
                        music_effort.play() # پخش صدا پرش
                        vx = +10 #تنظیم سرعت vx برای جابه جایی نینجا
                        Area=True # برای ستون های راست یعنی نینجا از چپ به راست امده است
                        btnclicked=True # این برای ان است که وقتی دکمه پرش را زدیم در جاهای دیگر متوجه ان شویم و تغییرات لازم را انجام دهیم
                        #تغییر عکس نینجا زمان پرش
                        if(NinjaColor == "YELLOW"):
                            imgurl = ["./img/P2.png","./img/P3.png"]
                        else:
                            imgurl = ["./img/2.png","./img/3.png"]
                            
                            
                    if event.key==1073741904 and Area:
                        music_effort.play()# پخش صدا پرش
                        vx = -10 #تنظیم سرعت vx برای جابه جایی نینجا
                        Area=False # برای ستون های راست یعنی نینجا از چپ به راست امده است
                        btnclicked=True # این برای ان است که وقتی دکمه پرش را زدیم در جاهای دیگر متوجه ان شویم و تغییرات لازم را انجام دهیم
                        #تغییر عکس نینجا زمان پرش
                        if(NinjaColor == "YELLOW"):
                            imgurl = ["./img/P2R.png","./img/P3R.png"]
                        else:
                            imgurl = ["./img/2R.png","./img/3R.png"]
              
            # برسی محور x نینجا با ستون های برای اینکه داخل دیوار نرود و روی دیوار راه برود واگر با دیوار برخورد کرد یک قلب از ان بگیرد          
            if Area :
                for i in range(1,len(mapsarr),2):
                    if(i<len(mapsarr)-3):
                        if 510 - mapsarr[i+2]["h"] < mapsarr[i+2]["y"]<520:
                            if x == mapsarr[i+2]["x"]-50 :
                                #زمانی که ایکس نینجا با x ستون برابر شد x نینجا ثابت میماند
                                xz = mapsarr[i+2]["x"]
                                vx = 0
                        if mapsarr[i]["y"]==510:
                            if(xz<mapsarr[i+2]["x"] ):
                                #زمانی که سطح بعدی پایین تر است 
                                xz = mapsarr[i]["x"]  
                                vx = +10
                                break
                            if(xz==mapsarr[i+2]["x"] ):
                                #زمانی که دوسطح باهم برابر اند
                                xz = mapsarr[i]["x"]  
                                break
                            if(btnclicked):
                                # زمان جابه جا شدن
                                xz = mapsarr[i]["x"]  
                                btnclicked = False
                                break
                            if(xz>mapsarr[i+2]["x"]):
                                # زمان برخورد با دیوار و کم کردن قلب
                                Heart = Heart -1
                                xz = mapsarr[i]["x"]  
                                music_hurt.play()
                                break
                            
            else:
                for i in range(0,len(mapsarr),2):
                    if(i<len(mapsarr)-2):
                        if 500 - mapsarr[i+2]["h"] <mapsarr[i+2]["y"]<520 :
                            if x == mapsarr[i+2]["w"]  :
                                xz = mapsarr[i+2]["w"]
                                vx = 0
                        if mapsarr[i]["y"]==510:
                            if(xz>mapsarr[i+2]["w"]):
                                #زمانی که سطح بعدی پایین تر است 
                                xz = mapsarr[i]["w"]
                                vx = -10
                                break
                            if(xz==mapsarr[i+2]["w"]):
                                #زمانی که دوسطح باهم برابر اند
                                xz = mapsarr[i]["w"]
                                break
                            if(btnclicked):
                                # زمان جابه جا شدن
                                xz = mapsarr[i]["w"]
                                btnclicked =False
                                break
                            if(xz<mapsarr[i+2]["w"]):
                                # زمان برخورد با دیوار و کم کردن قلب
                                Heart = Heart - 1
                                xz = mapsarr[i]["w"]
                                music_hurt.play()
                                break
            # و سکه نمایش ستون ها و نینجا
            
            for i in range(len(mapsarr)):
                pygame.draw.rect(sur, (29,20,30), pygame.Rect(mapsarr[i]["x"],mapsarr[i]["y"] ,mapsarr[i]["w"] ,mapsarr[i]["h"] ))
                pygame.draw.rect(sur, (255,0,0), pygame.Rect(mapsarr[i]["x"],mapsarr[i]["y"] ,mapsarr[i]["w"] ,mapsarr[i]["h"] ),5)
                if not btnclickedPuse :#افزایش 
                    mapsarr[i]["y"]+=mapy
                else: # استپ کردن بازی
                    font = pygame.font.SysFont("comicsansms", 72) # set font
                    Esc = font.render("Esc", True, (255, 255, 255))
                    sur.blit(Esc,(125,h/2))
            
            # for i in range(len(coinarry)):
            #     coin= pygame.image.load("./img/coin3.png")
            #     coin = pygame.transform.scale(coin,(25,25)) 
            #     sur.blit(coin,(coinarry[i]["nx"]-80,coinarry[i]["ny"]+50))
            #     if not btnclickedPuse :
            #         coinarry[i]["ny"]+=mapy
            # حالت دویدن نینجا
            if cic==0:
                if not number :
                    ninja = pygame.image.load(imgurl[0])
                    number = True
                boleancic = True
            if cic==3:
                if number :
                    ninja = pygame.image.load(imgurl[1])
                    number = False
                boleancic = False
            
            if boleancic:
                cic+=1
            if not boleancic:
                cic-=1
            
            ninja = pygame.transform.scale(ninja,(50,50))   
            # نمایش نینجا
            sur.blit(ninja,(x,y))
            # نمایش قلب 
            Heartimg = pygame.image.load("./img/heart.png")
            Heartimg = pygame.transform.scale(Heartimg,(50,50))
            if(Heart==3):
                sur.blit(Heartimg,(5,5))
                sur.blit(Heartimg,(60,5))
                sur.blit(Heartimg,(115,5))
            if(Heart==2):
                sur.blit(Heartimg,(5,5))
                sur.blit(Heartimg,(60,5))
            if(Heart==1):
                sur.blit(Heartimg,(5,5))
            # خط مرگ
            if x==0:
                Heart = 0
            if x==550:
                Heart = 0



            # حذف ستون ها
            for i in range(len(mapsarr)-1):
                if mapsarr[i]["y"]>=600:
                    mapsarr.pop(i)

            # # remove coin
            # for i in range(len(coinarry)-1):
            #     if coinarry[i]["ny"]>=600:
            #         coinarry.pop(i)
            
                    
                    
        else:
            # پایان بازی
            music_song.stop()
            sur.blit(text,(125,h/2-50)) 
            pygame.quit() # بستن بازی
            return True 
            
        pygame.display.flip()
        clock.tick(60) # set time fps
   
    

