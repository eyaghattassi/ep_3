from PyQt5.QtWidgets import *
from PyQt5.uic import *
from pickle import dump,load
from numpy import array 
from math import*
def combo():
    f=open("Age.txt",'r')
    fin=False
    while not(fin):
        ch=f.readline()
        if ch=="":
            fin=True
        else:
            win.combo.addItem(ch[:len(ch)-1])
    f.close()


def ajout():
    pseu=win.pseu.text()
    age=win.combo.currentText()
    if not(2<=len(pseu)<=10) or not(distinct(pseu)):
        QMessageBox.critical(win,'erreur','pseudo non valide')
        win.pseu.clear()
        win.pseu.setFocus()
    else:
        fb=open('suiteRaison.dat','ab')
        e=dict()
        if win.rad1.isChecked():
            e['sexe']='M'
        elif win.rad2.isChecked():
            e['sexe']='F'
        e['age']=age
        e['pseudo']=pseu
        dump(e,fb)
        fb.close()
        QMessageBox.information(win,'valider','enregistrement jouter avec succés')

def distinct(ch):
    test=('A'<=ch[0]<='Z')
    while (len(ch)!=1 and  test ):
        a=ch[0]
        ch=ch[1:]
        if ('A'<=ch[0]<='Z' and ch.find(a)==-1):
            test=True
        else:
            test=False
    return test
        
def afficher1():
    fb=open('suiteRaison.dat','rb')
    fin=False
    i=-1
    win.tab.setRowCount(0)
    while not fin:
        try:
            e=dict()
            e=load(fb)
            i=i+1
          
            win.tab.insertRow(i)
            win.tab.setItem(i,0,QTableWidgetItem(e['pseudo']))
            win.tab.setItem(i,1,QTableWidgetItem(str(e['sexe'])))
            win.tab.setItem(i,2,QTableWidgetItem(str(e['age'])))
            
        except :
            fin=True
            fb.close()

    
    
def remplir():
    fb=open('suiteRaison.dat','rb')
    f2=open('raison.txt','w')
    fin=False
    while not fin:
        try:
            e=dict()
            e=load(fb)
            ch=e['pseudo']
            chtrier=trier(ch)
            r=raison(chtrier)
            if r!=-1:
                ch=ch+"#"+chtrier+"#"+str(r)
                f2.write(ch+'\n')
        except :
            fin=True
            
    QMessageBox.information(win,'valider','fichier rempli avec succés')
    f2.close()
    fb.close()

def afficher2():
    win.list.clear()
    f2=open('raison.txt','r')
    win.list.addItem(f2.read())
    f2.close()
    
def raison(ch):
    n=abs(ord(ch[0])-ord(ch[1]))
    i=1
    test=True
    while i<len(ch)-1:
        if abs(ord(ch[i])-ord(ch[i+1]))!=n:
            test=False
        i=i+1
    if test==False:
        return -1
    else:
        return n
            
            

    
def trier(ch):
    t=array([str()]*10)
    for i in range(len(ch)):
        t[i]=ch[i]
        
    n=len(ch)-1
    for i in range(1,n):
       x=t[i]
       j=i-1
       while j>=0 and t[j]>x:
           t[j+1]=t[j]
           j=j-1
       t[j+1]=x 
           
    ch2=""
    for i in range(len(ch)):
        ch2=ch2+t[i]

    return ch2

            



app=QApplication([])
win=loadUi("raison.ui")
win.show()
combo()
win.rad1.setChecked(True)
win.b1.clicked.connect(ajout)
win.b2.clicked.connect(afficher1)
win.b3.clicked.connect(remplir)
win.b4.clicked.connect(afficher2)

app.exec_()