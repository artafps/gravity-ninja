import pygame
import requests

def GravityNinja(speed ,NinjaColor, selectgame):
    
    


    #init pygame
    pygame.init()
    clock = pygame.time.Clock() # fps
    
    # تنظیم سرعت بازی
    mapy=speed
    # تنظیم سایز صفحه
    w,h = 600,600
    sur = pygame.display.set_mode((w,h))

    if(NinjaColor == "YELLOW"):
        imgurl = ["./img/P2.png","./img/P3.png"]
    else:
        imgurl = ["./img/2.png","./img/3.png"]
    number = True
    mapsarr = [{"x":0,"w":200,"y":0,"h":600},{"x":400,"y":0,"w":200,"h":600},]

    # music 
    music_effort = pygame.mixer.Sound (r'Sound\sfx_effort_1.wav')
    music_hurt = pygame.mixer.Sound (r'Sound\sfx_hurt_1.wav')
    music_song = pygame.mixer.Sound (r'Music\Music 4.mp3')
    music_song.play()
    
    # text game over 
    font = pygame.font.SysFont("comicsansms", 72) # set font
    text = font.render("Game Over", True, (255, 0, 0))
    #change ninja picture
    cic = 3
    boleancic = False

    #add soton 
    p=180
    s=200
    z1,z2=0,0
    weidth= [300,250,0,200,150,100]#[300,280,250,0,220,200,180,150,120,100]
    z=0
    bolean = True

    x,y = 350,460
    xz = 200
    wx = 200
    wn = 1
    Area=True
    ileft,iright=0,0
    btnclicked=False
    btnclickedPuse=False
    Heart = 3
    vx = 0
    
    while True :
        sur.fill((0,200,255))
        if( Heart != 0):
            #backgroun img
            sun= pygame.image.load("./img/sun.png")
            sun = pygame.transform.scale(sun,(400,400))  
            sur.blit(sun,(150,50))
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
            if(z==5):
                bolean = False
            if(z==0):
                bolean = True
            z1,z2 = z1-p,z2-s
            if weidth[z] == 0 :
                mapsarr.append({"x":0,"w":weidth[z],"y":z1,"h":p+10})
                mapsarr.append({"x":weidth[z]+130+250,"w": 600-weidth[z]-130,"y":z2,"h":s+10})
            else:
                mapsarr.append({"x":0,"w":weidth[z],"y":z1,"h":p+10})
                mapsarr.append({"x":weidth[z]+130,"w": 600-weidth[z]-130,"y":z2,"h":s+10})
            
                    

            # vx change values
            x+=vx
            
            #event
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # if event is quit
                    
                    Heart=0   
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: # if event is keydown and key is escape
                    if(btnclickedPuse):
                        music_song.play()
                    else:
                        music_song.stop()
                    btnclickedPuse=not btnclickedPuse   
                if event.type == pygame.KEYDOWN:
                    if event.key==1073741903 and not Area:
                        if vx == 0 :
                            music_effort.play()
                            vx = +10
                            Area=True
                            btnclicked=True
                            if(NinjaColor == "YELLOW"):
                                imgurl = ["./img/P2.png","./img/P3.png"]
                            else:
                                imgurl = ["./img/2.png","./img/3.png"]
                            
                            
                    if event.key==1073741904 and Area:
                        if vx == 0 :
                            music_effort.play()
                            vx = -10
                            Area=False 
                            btnclicked=True
                            if(NinjaColor == "YELLOW"):
                                imgurl = ["./img/P2R.png","./img/P3R.png"]
                            else:
                                imgurl = ["./img/2R.png","./img/3R.png"]
                            
            if Area :
                for i in range(1,len(mapsarr),2):
                    if(i<len(mapsarr)-3):
                        if 510 - mapsarr[i+2]["h"] <mapsarr[i+2]["y"]<520:
                            if x == mapsarr[i+2]["x"]-50 :
                                xz = mapsarr[i+2]["x"]
                                print("A-1")
                                vx = 0
                        if mapsarr[i]["y"]==520:
                            print("B")
                            print(xz,mapsarr[i+2]["x"],mapsarr[i]["x"])
                            if(xz<mapsarr[i+2]["x"] ):
                                print("B-1")
                                xz = mapsarr[i]["x"]  
                                vx = +10
                                break
                            if(xz==mapsarr[i+2]["x"] ):
                                xz = mapsarr[i]["x"]  
                                break
                            if(btnclicked):
                                xz = mapsarr[i]["x"]  
                                btnclicked = False
                                break
                            if(xz>mapsarr[i+2]["x"]):
                                xz = mapsarr[i]["x"]  
                                music_hurt.play()
                                Heart = Heart -1 
                                break
                            
            else:
                for i in range(0,len(mapsarr),2):
                    if(i<len(mapsarr)-2):
                        if 500 - mapsarr[i+2]["h"] <mapsarr[i+2]["y"]<520:
                            if x == mapsarr[i+2]["w"]  :
                                xz = mapsarr[i+2]["w"]
                                print("C-1")
                                vx = 0
                        if mapsarr[i]["y"]==520:
                            print("D")
                            if(xz>mapsarr[i+2]["w"]):
                                print("D-1")
                                xz = mapsarr[i]["w"]
                                vx = -10
                                break
                            if(xz==mapsarr[i+2]["w"]):
                                xz = mapsarr[i]["w"]
                                break
                            if(btnclicked):
                                xz = mapsarr[i]["w"]
                                btnclicked =False
                                break
                            if(xz<mapsarr[i+2]["w"]):
                                xz = mapsarr[i]["w"]
                                music_hurt.play()
                                Heart = Heart - 1
                                break
            # نمایش ستون ها و نینجا
            for i in mapsarr:
                pygame.draw.rect(sur, (29,20,30), pygame.Rect(i["x"],i["y"] ,i["w"] ,i["h"] ))
                pygame.draw.rect(sur, (255,0,0), pygame.Rect(i["x"],i["y"] ,i["w"] ,i["h"] ),5)
                if not btnclickedPuse :
                    i["y"]+=mapy
                else:
                    font = pygame.font.SysFont("comicsansms", 72) # set font
                    Esc = font.render("Esc", True, (255, 255, 255))
                    sur.blit(Esc,(125,h/2)) 
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
            # game ninja
            sur.blit(ninja,(x,y))
            # Heart
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
            # end game
            if x==0:
                Heart = 0
            # remove soton
            for i in range(len(mapsarr)-1):
                if mapsarr[i]["y"]>=800:
                    mapsarr.pop(i)
        else:
            music_song.stop()
            sur.blit(text,(125,h/2-50)) 
            selectgame.show()
            break
        pygame.display.flip()
        clock.tick(120) # set time fps
    pygame.quit()