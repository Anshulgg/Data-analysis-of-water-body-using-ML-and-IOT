# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 07:36:06 2018

@author: SACHIN
"""
import numpy as np
from sklearn import preprocessing, cross_validation, neighbors, svm
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import style


data = pd.read_excel("data.xlsx")
data.replace('?',-99999, inplace=True)

year=[2018,2018,2018]
month=[4,4,4]
day=[5,6,7]
l_id=[1,1,1]


final=[]
no_alerts=[0,0,0]
predict_temp=[]
predict_flow=[]
predict_ph=[]
predict_tds=[]
predict_do=[]
predict_depth=[]
predict_turb=[]



sug_turb=[]
sug_temp=[]
sug_flow=[]
sug_ph=[]
sug_tds=[]
sug_do=[]
sug_depth=[]
sug_turb=[]
sug_solero=[]

a=np.array(data['temp'])
b=np.array(data['flow'])
c=np.array(data['ph'])
d=np.array(data['tds'])
e=np.array(data['do'])
f=np.array(data['dept'])
g=np.array(data['turb'])
h=np.array(data.drop(['temp','flow','ph','tds','do','dept','turb'],1))

def temp(x,y):
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=0.2)
    clf=svm.SVC()
    clf.fit(x_train,y_train)
    accuracy= clf.score(x_test,y_test)
    new_data=np.array([[2018,4,1,1],[2018,4,2,1],[2018,4,3,1]])
    new_data=new_data.reshape(3,-1)
    print("\nTemprature of water")
    predict_temp=clf.predict(new_data)
    print(predict_temp)
    print("Accuracy ",100-accuracy)
    for i in range(0,len(predict_temp)):
        if (predict_temp[i]<20):
            sug_temp.append("Water is not good for domestic use: COOL")
            no_alerts[i]+=1
        elif ((predict_temp[i]>20) and (predict_temp[i]<40)):
            sug_temp.append("Water is good for domestic use")
        else:
            sug_temp.append("Water is not good for domestic use : HOT")
            no_alerts[i]+=1
    print(sug_temp)
    
def flow(x,y):
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=0.2)
    clf=svm.SVC()
    clf.fit(x_train,y_train)
    accuracy= clf.score(x_test,y_test)    
    print("\nFlow of water")
    new_data=np.array([[2018,4,1,1],[2018,4,2,1],[2018,4,3,1]])
    new_data=new_data.reshape(3,-1)
    predict_flow=clf.predict(new_data)
    print(predict_flow)
    print("Accuracy ",100-accuracy)
    for i in range(0,len(predict_flow)):
        if (predict_flow[i]<3000):
            sug_temp.append("Drought may occur")
            no_alerts[i]+=1
        elif ((predict_flow[i]>3000) and (predict_flow[i]<6000)):
            sug_flow.append("Water flow is good")
        else:
            sug_flow.append("Flood may occur")
            no_alerts[i]+=1
    print(sug_flow)
    
def ph(x,y):
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=0.2)
    clf=svm.SVC()
    clf.fit(x_train,y_train)
    accuracy= clf.score(x_test,y_test)
    print("\npH of water")
    new_data=np.array([[2018,4,1,1],[2018,4,2,1],[2018,4,3,1]])
    new_data=new_data.reshape(3,-1)
    predict_ph=clf.predict(new_data)
    print(predict_ph)
    print("Accuracy ",100-accuracy)
    for i in range(0,len(predict_ph)):
        if (predict_ph[i]<6):
            sug_temp.append("Water is not good for domestic : acidic")
            no_alerts[i]+=1
        elif ((predict_ph[i]>6) and (predict_ph[i]<8.5)):
            sug_ph.append("Water is good for domestic use")
        else:
            sug_ph.append("Water is not good for domestic use : basic")
            no_alerts[i]+=1
    print(sug_ph)
    
def tds(x,y):
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=0.2)
    clf=svm.SVC()
    clf.fit(x_train,y_train)
    accuracy= clf.score(x_test,y_test)
    print("\nTDS of water")
    new_data=np.array([[2018,4,1,1],[2018,4,2,1],[2018,4,3,1]])
    new_data=new_data.reshape(3,-1)
    predict_tds=clf.predict(new_data)
    print(predict_tds)
    print("Accuracy ",100-accuracy)
    for i in range(0,len(predict_tds)):
        if (predict_tds[i]<50):
            sug_tds.append("Water is not good for domestic : distild")
            no_alerts[i]+=1
        elif ((predict_tds[i]>50) and (predict_tds[i]<200)):
            sug_tds.append("Water is good for domestic use")
        else:
            sug_tds.append("Water is not good for domestic use : dirty")
            no_alerts[i]+=1
    print(sug_tds)
    
def do(x,y):
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=0.2)
    clf=svm.SVC()
    clf.fit(x_train,y_train)
    accuracy= clf.score(x_test,y_test)
    print("\nDissolved Oxygen of water")
    new_data=np.array([[2018,4,1,1],[2018,4,2,1],[2018,4,3,1]])
    new_data=new_data.reshape(3,-1)
    predict_do=clf.predict(new_data)
    print(predict_do)
    print("Accuracy ",100-accuracy)
    for i in range(0,len(predict_do)):
        if ((predict_do[i]>0.5) and (predict_do[i]<1.0)):
            sug_do.append("Water is good for domestic use")
        else:
            sug_do.append("Water is not good for domestic use : Not fresh")
            no_alerts[i]+=1
    print(sug_do)
    
def depth(x,y):
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=0.2)
    clf=svm.SVC()
    clf.fit(x_train,y_train)
    accuracy= clf.score(x_test,y_test)
    print("\nDepth of water")
    new_data=np.array([[2018,4,1,1],[2018,4,2,1],[2018,4,3,1]])
    new_data=new_data.reshape(3,-1)
    predict_depth=clf.predict(new_data)
    print(predict_depth)
    print("Accuracy ",100-accuracy)
    for i in range(0,len(predict_depth)):
        if (predict_depth[i]<200):
            sug_depth.append("Low depth")
        elif ((predict_depth[i]>200) and (predict_depth[i]<250)):
            sug_depth.append("Depth is good")
        else:
            sug_depth.append("High depth")
    print(sug_depth)
    for i in range(0,len(predict_depth)):
        if (predict_depth[i]<200):
            sug_solero.append("No soil erosion depth")
        elif ((predict_depth[i]>200) and (predict_depth[i]<250)):
            sug_solero.append("low soil erosion")
            no_alerts[i]+=1
        else:
            sug_solero.append("High soil erosion")
            no_alerts[i]+=1
    print(sug_solero)
    
    
def turb(x,y):
    x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size=0.2)
    clf=svm.SVC()
    clf.fit(x_train,y_train)
    accuracy= clf.score(x_test,y_test)
    print("\nTurbidity of water")
    new_data=np.array([[2018,4,1,1],[2018,4,2,1],[2018,4,3,1]])
    new_data=new_data.reshape(3,-1)
    predict_turb=clf.predict(new_data)
    print(predict_turb)
    print("Accuracy ",100-accuracy)
    for i in range(0,len(predict_turb)):
        if ((predict_turb[i]>0) and (predict_turb[i]<5)):
            sug_turb.append("Water is good for domestic use")
        else:
            sug_turb.append("Water is not good for domestic use : Poor turbidity")
            no_alerts[i]+=1
    print(sug_turb)
    
temp(h,a)
flow(h,b)
ph(h,c)
tds(h,d)
do(h,e)
depth(h,f)
turb(h,g)
print("\nTOtal NO of alerts")
print(no_alerts)

    