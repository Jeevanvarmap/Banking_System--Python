class Accounts:
    def __init__(self,name,gender,aadhar,pan,dob,address,accountNo,accountType,balance):
        self.name=name
        self.gender=gender
        self.aadhar=aadhar
        self.pan=pan
        self.dob=dob
        self.address=address
        self.accountNo=accountNo
        self.accountType=accountType
        self.balance=balance

    def display(self):
        print("\n")
        print("Name: "+ self.name)
        print("-----Personal Details-----")
        print("Aadhar: "+self.aadhar)
        print("PAN: "+self.pan)
        print("DOB: "+self.dob)
        print("Address: "+self.address)
        print("-----Account Details-----")
        print("AccountNo: "+self.accountNo)
        print("Account Type: "+str(self.accountType))
        print("Balance: "+str(self.balance))
        
        

from validate import *
from adminVerify import *

accountsData=[]

def start():
    flag=True
    while(flag):
        print("\n")
        print("Welcome To Banking Management System")
        print("Who are you?")
        print("1. Bank Employee")
        print("2. Account Holder")
        print("3. Close The System")
        choice=int(input("Enter Your Choice: "))
        print("\n")
        
        if choice==1:
            
            print("-----Login-----")
            username=input("Username: ")
            password=input("Password: ")
            if verifyAccount(username,password):
                print("Login Successful")
                while True:
                    print("\n")
                    print("What do you want to do?")
                    print("1. Open A Account")
                    print("2. Diaplay All The Accounts")
                    print("3. Close An Account")
                    print("4. Update Account Details")
                    print("5. Exit")
                    choice=int(input("Enter Your Choice: "))
                    print("\n")
                    if choice == 1:
                        print("Account Opening Form")
                        while True:
                            accountType=int(input("Select Account Type: 1.Savings ; 2.Current : "))
                            if not verifyAccountType(accountType):
                                print("Invalid AccountType! Please Enter It Again.")
                            else:
                                break
                        while True:
                            name=input("Enter Name: ")
                            if not verifyName(name):
                                print("Invalid Name! Please Enter It Again.")
                            else:
                                break
                        while True:
                            gender=int(input("Select gender: 1.Male ; 2.Female : "))
                            if not verifyGender(gender):
                                print("Invalid! Please Enter It Again.")
                            else:
                                break
                        while True:
                            DOB=input("Enter DOB: ")
                            if not verifyDOB(DOB):
                                print("Invalid DOB! Please Enter It Again.")
                            else:
                                break
                        while True:
                            PAN=input("Enter PAN: ")
                            if not verifyPAN(PAN):
                                print("Invalid PAN! Please Enter It Again.")
                            else:
                                break
                        while True:
                            aadhar=input("Enter Aadhar: ")
                            if not verifyAadhar(aadhar):
                                print("Invalid Aadhar! Please Enter It Again.")
                            else:
                                break
                        print("Enter the address:")
                        houseNo=input("House: ")
                        city=input("City: ")
                        state=input("State: ")
                        address=houseNo + " , " + city + " , " + state
                        account=Accounts(name,gender,aadhar,PAN,DOB,address,generateAccountNo(city,state,accountType),accountType,balance=0)
                        accountsData.append(account)
                        print("\n")
                        print("Account Opened Successfully!!!")
                        account.display()
                        
                    elif choice==2:
                        print("All the accounts in the Database:")
                        for i in accountsData:
                            i.display()
                    
                    elif choice==3:
                        accountNo=input("Enter The Account No. To Close: ")
                        for i in accountsData:
                            if i.accountNo==accountNo:
                                accountsData.remove(i)
                        print("Account Closed Successfully!")
                    
                    elif choice==4:
                        accountNo=input("Enter The Account No. of the account you want to update: ")
                        print("Choose what do you want to update.")
                        print("1. Name")
                        print("2. DOB")
                        choice=int(input("Enter your choice: "))
                        for i in accountsData:
                            if i.accountNo==accountNo:
                                if choice==1:
                                    while True:
                                        name=input("Enter Name: ")
                                        if not verifyName(name):
                                            print("Invalid Name! Please Enter It Again.")
                                        else:
                                            i.name=name
                                            print("Account Details Updated Successfully!")
                                            break
                                elif choice==2:
                                    while True:
                                        DOB=input("Enter DOB: ")
                                        if not verifyDOB(DOB):
                                            print("Invalid DOB! Please Enter It Again.")
                                        else:
                                            i.DOB=DOB
                                            print("Account Details Updated Successfully!")
                                            break
                        
                    elif choice==5:
                        break
                        print("Thank You!")
                        
                    else:
                        print("Invalid Choice")
            
            else:
                print("Invalid Username/Password")
        
        elif choice==2:
            print("Hello Customer!")
            
        elif choice==3:
            flag=False
            print("Thank You!")
        else:
            print("Invalid Choice")
   
start()