'''
Created on Dec 19, 2018

@author: Vishva Deepak Tripathi
'''
from _ast import Num
import time
import datetime
from datetime import date
from _datetime import datetime_CAPI

class TableClass():
    def userTable(self):
        for i in range(10):
            print(i)
            
    def nameInput(self):
        person=input('Enter your name')
        print('Hello ' + person)
    
    def countTable(self):
        for i in range(11):
            x = i*10
            print(x)
            
    def even_odd(self, n):
        if n % 2 ==0:
            print('Even')
            return
        print('Odd')
    
    def addition(self):
        Num1 = input('Enter First Number :  ')
        Num2 = input('Enter Second Number : ')
        Num3 = float(Num1) + float(Num2)
        print('Number after addition : ' + str(Num3))
        
    def substract(self):
        Num1 = float(input('Enter First Number : '))
        Num2 = float(input('Enter Second Number : '))
        #First need to convert input value then store into variable 
        #otherwise will it prompt some wrong substraction value 
        #Due to storage error if you will do the 100-50 = -50 
        # adn this will becuase of conversation issue
        if Num1 >= Num2:
            #Num3 = float(Num1) - float(Num2)
            Num3 = Num1 - Num2
            print('After substraction : ' +  str(Num3))
        elif Num2 >= Num1:
            #Num3 = float(Num2) - float(Num1)
            Num3 = Num2 - Num1
            print('After substraction : ' +  str(Num3))
        
    def squarecalcualtion(self):
        Num1 = float(input('Enter the number that you want to square : '))
        print(Num1**2)
    
    @staticmethod
    def CompareDate(self):
        date_1 = date.today()
        end_date = date_1 + datetime.timedelta(days=10)
        end_date.strftime("%x")
        print(self)
        dt_new=time.strptime(self, "%x")
        print(str(dt_new))
        #datetime.strptime(dt,"%x").date()
        dt_new=time.strptime(self,"%x")
        #dt_new=datetime.date(2020,7,19)
        print(end_date)
        if dt_new!=end_date:
            print("Date is not equal")
        
    #def __init__(self):
        #self.x=x
