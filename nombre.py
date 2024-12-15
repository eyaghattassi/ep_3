from PyQt5.QtWidgets import *
from PyQt5.uic import *
from pickle import dump,load
from numpy import array
def ajout():
    f=open('pléniptent.txt','a')
    nombre=win.ch.text()
    if not(nombre.isdecimal() and int(nombre)>0):
        QMessageBox.critical(win,'erreur','Nombre incorrect')
    elif not(existe(nombre)):
        QMessageBox.critical(win,'erreur','nombre existe dans le fichier')
    else:
        f.write(nombre+'\n')
        QMessageBox.information(win,'valider','Nombre ajouter avec succés')
    f.close()

def taille():
    global n
    f=open('pléniptent.txt','r')
    fin=False
    n=0
    while not fin:
        ch=f.readline()
        ch=ch[:len(ch)-1]
        if ch=="":
            fin=True
        else:
            n=n+1
    f.close()
    win.taille.setText(str(n))

def existe(x):
    f=open('pléniptent.txt','r')
    fin=False
    while not fin:
        ch=f.readline()
        if ch=='' or int(ch)==int(x):
            fin=True
    f.close()
    return fin

def afficher():
    win.list.clear()
    f=open('pléniptent.txt','r')
    win.list.addItem(f.read())
    f.close()
    
def determiner():
    taille()
    f=open('pléniptent.txt','r')
    win.tab.setRowCount(n)
    for i in range(n):
        ch=f.readline()
        ch=ch[:len(ch)-1]
        win.tab.setItem(i,0,QTableWidgetItem(ch))
        fact=facteur_premier(int(ch))
        if fact.find('^1*')==-1:
            pléniptent='oui'
        else:
            pléniptent='non'
        win.tab.setItem(i,1,QTableWidgetItem(fact[0:len(fact)-1]))
        win.tab.setItem(i,2,QTableWidgetItem(pléniptent))
    f.close()

def facteur_premier(x):
    t=array([int]*100000)
    i=2
    n=0
    while x!=1:
        if x % i==0:
            t[n]=i
            n=n+1
            x=x//i
            
        else:
            i=i+1
    ch=""
    nb=1
    for i in range(n):
        if t[i]==t[i+1]:

            nb=nb+1
        else:
            ch=ch+str(t[i])+'^'+str(nb)+'*'
            nb=1
#     ch=ch+str(t[i])+'^'+str(nb)+'*'
    return ch 
        
            

    


app=QApplication([])
win=loadUi("interfaceplénipotent.ui")
win.show()
win.b1.clicked.connect(ajout)
win.b2.clicked.connect(afficher)
win.b3.clicked.connect(taille)
win.b4.clicked.connect(determiner)

app.exec_()