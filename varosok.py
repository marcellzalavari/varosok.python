from Varos import Varos

varosok:list[Varos]=[]

def beolvas(fajlnev:str):
    fajl=open(fajlnev,'r',encoding='UTF8')
    fajl.readline()
    for sor in fajl:
        varosok.append(Varos(sor.strip()))
    fajl.close()

def orszag_lakossaga(orszag:str)->int:
    osszeg=0
    for v in varosok:
        if v.orszag==orszag:
            osszeg+=v.lakossag
    return osszeg*1000  # mert itt nem 1000 főben kell, hanem simán főben

def legnagyobb_varos()->Varos:
    legnagyobb=varosok[0]
    for v in varosok[1:]:
        if v.lakossag>legnagyobb.lakossag:
            legnagyobb=v
    return legnagyobb

def legnagyobb_varos_orszagban(orszag:str)->Varos|bool:
    for varos in varosok:
        if varos.orszag==orszag:
            legnagyobb=varos
            for v in varosok[1:]:
                if v.lakossag>legnagyobb.lakossag and v.orszag==orszag:
                    legnagyobb=v
            return legnagyobb
        
def legnagyobb_varos_orszagban2(orszag:str)->Varos|bool:
    # ha nem biztos, hogy az ország benne van a listában
    for varos in varosok:
        if varos.orszag==orszag:
            legnagyobb=varos
            for v in varosok[1:]:
                if v.lakossag>legnagyobb.lakossag and v.orszag==orszag:
                    legnagyobb=v
            return legnagyobb
    return False
        

def orszag_keres(orszag:str)->bool:
    for v in varosok:
        if v.orszag==orszag:
            return True
    return False

def szokozos_varosok(szokozok_szama:int)->int:  # pl. 1
    darab=0
    for v in varosok:
        if v.szokozok_szama()==szokozok_szama:
            darab+=1
    return darab

def orszag_statisztika()->dict[str,int]:
    stat:dict[str,int]={}
    for v in varosok:
        if v.orszag in stat.keys():
            stat[v.orszag]+=1
        else:
            stat[v.orszag]=1
    return stat

def orszag_mentes(fajlnev:str,orszag:str):
    fajl=open(fajlnev,'w',encoding='UTF8')
    for v in varosok:
        if v.orszag==orszag:
            fajl.write(f'{v.varos};{v.lakossag}\n')
    fajl.close()