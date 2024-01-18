class Varos:
    def __init__(self,sor:str) -> None:
        #Város;Ország;Lakosság
        adatok=sor.split(';')
        self.varos=adatok[0]
        self.orszag=adatok[1]
        self.lakossag=int(adatok[2])
    
    def szokozok_szama(self)->int:
        db=0
        for karakter in self.varos:
            if karakter==' ':
                db+=1
        return db