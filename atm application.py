import os
from datetime import datetime
a={100:0,200:0,500:0,2000:0}
user=[{"user":"sangavi","password":"3335","balance":30000,"bank":"SBI"},{"user":"nandini","password":"1995","balance":10000,"bank":"NSK"}]
transaction=[]
def load():
    os.system('cls')
    for i in a:
        n=int(input("enter the num:"+str(i)+"notes:"))
        a[i]+=n
    print("Amount loaded successfully")

def show():
    os.system('cls')
    ad=0
    for i in a:
        print(i,":",a[i]) 
        ad+=(i*a[i])
    print("Amount in the atm",ad)
      
def admin():
    adminname="admin1"
    adminpin=2001
    name=input("Enter the admin name:")
    pin=int(input("Enter your 4 digit pin:"))
    if pin==adminpin and name==adminname:
        print("Welcome admin")
        print("Logged in succesfully")
        while(True):
            c=int(input("1.Load\n2.Show\n3.Exit\n Enter the choice:"))
            if(c==1):
                load()
            elif(c==2):
                show()    
            elif(c==3):
                os.system('cls')
                break

def ministatement():
    if len(transaction)>=3:
        print("Date","\t\tTime","\t User","\t     Total balance","\t  Amount Withdrawn/Desposited","\t Current balance")
        for i in transaction:
            print(i["Datetime"],"\t",i["User"],"\t",i["Total balance"],"\t\t\t",i["Withdrawn/Deposit"],"\t\t\t",i["Balance"])
    else:
        print("Not more than 3 Transaction done")


def deposit(i):
    v={}
    va=datetime.now()
    b=va.strftime("%d/%m/%Y   %H:%M:%S")
    v["Datetime"]=b
    v["User"]=i["user"]
    v["Total balance"]=i["balance"]
    v["Withdrawn/Deposit"]=0
    v["Balance"]=i["balance"]
    d=int(input("Enter the amount to deposit:"))
    v["Withdrawn/Deposit"]+=d
    y=i["balance"]
    y+=d
    i["balance"]=y
    v["Balance"]=i["balance"]
    print("*******Amount deposited*********")
    print("current balance",i["balance"])
    transaction.append(v)
         
def withdraw(i):
        v={}
        va=datetime.now()
        b=va.strftime("%d/%m/%Y   %H:%M:%S")
        v["Datetime"]=b
        v["User"]=i["user"]
        v["Total balance"]=i["balance"]
        v["Withdrawn/Deposit"]=0
        v["Balance"]=i["balance"]
        wa=int(input("Enter the withdraw amount:"))
        r=i["balance"]
        o=list(a.keys())
        p=list(a.values())
        if all(p)==0:
            print("check the amount entered")

        elif wa<r and wa%100==0:
            l=0
            for j in a:                
                f= int(input("enter the num:"+str(j)+"notes:"))
                l+=(f*j)
                
                if l>wa:
                    print("check amount entered")
                    break
                elif l==wa:
                    if f<=a[j]:
                        a[j]-=f
                    else:
                        print("denomination not available")
                        break
            else:
        
                v["Withdrawn/Deposit"]+=wa
                r=r-wa
                i["balance"]=r
                v["Balance"]=i["balance"]
                print("After withdrawal avaiable balance",i["balance"]) 

        else:
            print("daily limit exceeded")
        input("press enter to continue")
        transaction.append(v) 

def checkbalance(i):
    os.system('cls')
    print("Current balance:",i["balance"])     
    input("press enter to continue")

def changepin(i):
    os.system('cls')
    t=i["password"]
    t=input("enter the new pin:")
    i["password"]=t    
    print("Successfully changed",i["password"])
    input("press enter to continue")
        
def customer():
    os.system('cls')
    user1=input("enter the user name:")
    pin1=input("enter the pin num:")
    print("********Customer panel*******")
    for i in user:
        if i["user"]==user1 and i["password"]==pin1:
            print("successfully logged in ")
            print(" Welcome customer to bank ATM")
            while(True):
                c=int(input("_______select_______\n1.Deposit\n2.Withdraw\n3.Check balance\n4.Changepin\n5.Ministatement\n6.Exit\n Enter the choice:"))
                if(c==1):
                    deposit(i)
                    
                elif(c==2):
                    withdraw(i)
                elif(c==3):
                    checkbalance(i)
                elif(c==4):
                    changepin(i)
                elif(c==5):
                    ministatement()
                elif(c==6):
                    os.system('cls')
                    break
            
        
while(True):
    print("*******welcome to bank ATM*********")
    x=int(input("1.Admin\n2.Customer\n3Exit\n Enter your choice:"))
    if(x==1):
        admin()
    elif(x==2):
        customer()
    elif(x==3):
        os.system('cls')
        break


