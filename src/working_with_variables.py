'''
Created on Dec 26, 2018

@author: Vishva 
'''

# Define Variable and find the type of the variable 
Name = 'Jhon ' #string variable 
Age =  23 #int variable 
Salary =10000.00 #float variable 
Address = 'Sector 21, Haryana, Gurugram' #String Variable 

#### Print the name iin simple formate with print function 
print(Name);
print(Age);
print(Salary);
print(Address);
#### End of the print function with the print()
print('###################################################################')
# check the type and print the type on the console 
## use str() this will convert the object into string that will help to print the function 
print('Name is ' + str(type(Name)) + ' type');
print('Age is ' + str(type(Age)) +' type ') ;
print('Salary is '+ str(type(Salary)) +' type ');
print('Address is '+ str(type(Address))+' type ');

