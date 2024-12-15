from PyQt5.QtWidgets import *
from PyQt5.uic import *
from pickle import dump,load
def ajout():
    x=win.x.text()
    epsilon=win.e.text()
    if x=="" or not(-1<=float(x)<=1):
        QMessageBox.critical(win,'erreur','x incorrect')
    elif epsilon=="" or not(0<=float(epsilon)<=0.1):
        QMessageBox.critical(win,'erreur','e incorrect')
    else:
        f=open('cal_sin.dat','ab')
        e=dict()
        e['x']=float(x)
        e['e']=float(epsilon)
        e['sin']=sin(e['x'],e['e'])
        dump(e,f)
        f.close()
        QMessageBox.information(win,'erreur','Enregistrement ajouter avec succés')
def afficher():
    f=open('cal_sin.dat','rb')
    fin=False
    i=-1
    win.tab.setRowCount(0)
    while not fin:
        try:
            i=i+1
            win.tab.insertRow(i)
            e=load(f)
            win.tab.setItem(i,0,QTableWidgetItem(str(e['x'])))
            win.tab.setItem(i,1,QTableWidgetItem(str(e['e'])))
            win.tab.setItem(i,2,QTableWidgetItem(str(e['sin'])))
        except Exception as es:
            print(es)
            fin=True
    f.close()
    
        


def sin(x,ep):
    sp=0
    s=x
    signe=-1
    i=3
    while not( abs(s-sp)<=ep):
        sp=s
        s=s+puissance(x,i)/fact(i)*signe
        signe=-signe
        i=i+2
    return s
def puissance(x,i):
    if i==0:
        return 1
    else:
        return x*puissance(x,i-1)

def fact(i):
    if i==1:
        return 1
    else:
        return i*fact(i-1)
    










app=QApplication([])
win=loadUi("interfacesinus.ui")
win.show()
win.b1.clicked.connect(ajout)
win.b2.clicked.connect(afficher)
app.exec_()