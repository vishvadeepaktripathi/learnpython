'''
Created on Dec 19, 2018

@author: Vishva Deepak Tripathi
'''

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
    #def __init__(self):
        #self.x=x
