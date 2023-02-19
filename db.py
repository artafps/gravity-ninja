import sqlite3
# ایمپورت کردن sql
from random import randrange




class db:
    def __init__(self):
        self.__con = sqlite3.connect("sql.db")
        self.__cur = self.__con.cursor()
    def createdb(self):
        self.__cur.execute("CREATE TABLE movie(id text, username text,  coin text, numplay text)")
    def getAlldata(self):
        res = self.__cur.execute("SELECT * FROM movie")
        return res.fetchall()
    def searchByname(self,username):
        res = self.getAlldata()
        for i in res:
            if(i[1]==username):
                self.__con.commit()
                return [True,i]
        self.__con.commit()
        return [False]
    def searchByID(self,id):
        res = self.getAlldata()
        for i in res:
            if(i[0]==id):
                self.__con.commit()
                return [True,i]
        self.__con.commit()
        return [False]
    def loginUser(self,username):
        res = self.getAlldata()
        for i in res:
            if(i[1]==username):
                self.__con.commit()
                return True     
        self.__con.commit()      
        return False 
    def createUser(self,username):
        if(self.searchByname(username)[0]):
            self.__con.commit()
            return [False]
        boolean = True 
        Id=""
        while boolean: 
            Id = self.createId() 
            if(not self.searchByID(Id)[0]):
                boolean = False
        infoUser=(Id, username, '0', '0')
        string1="""INSERT INTO movie VALUES """
        datastr = string1+str(infoUser)
        self.__cur.execute(datastr)
        self.__con.commit()
        return [True,infoUser]
    
    
    def setCoin(self,Id,num):
        coin = int(self.__cur.execute("SELECT coin FROM movie WHERE id=" + f"'{Id}'").fetchall()[0][0]) + int(num)
        if(coin):
            self.__cur.execute("UPDATE movie SET coin = "+ f"'{coin}'" +" WHERE id = "+f"'{Id}'")
            self.__con.commit()
            return True
        else:
            return False
    def setnumplay(self,Id):
        if Id :
            dataget =self.__cur.execute("SELECT numplay FROM movie WHERE id=" + f"'{Id}'").fetchall()
            if(dataget):
                num = int(dataget[0][0]) + 1
            else :
                return False
            if(num):
                self.__cur.execute("UPDATE movie SET numplay = "+ f"'{num}'" +" WHERE id = "+f"'{Id}'")
                self.__con.commit()
                return True
            else:
                return False
        else:
            return False
    
    def createId(self):
            boolean = True 
            Id=0
            while boolean:
                Id = randrange(1000000)
                if(100000<Id<1000000):
                    boolean = False
            return 'ID'+str(Id)




