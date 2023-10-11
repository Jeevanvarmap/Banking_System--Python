from validate import *
from adminVerify import *
from accountsClass import *
from dummyData import *

def start():
    flag=True
    print("---------- Welcome To Banking Management System ----------")
    print("\n")
    ask=int(input("Do you want to add dummy data before proceeding: 1.Yes ; 2.No : "))
    if ask==1:
        addDummyData()
        print("Dummy Data Added Successfully")
    else:
        print("Proceeding without adding Data")
    
    while(flag):
        print("\n")
        print("Who are you?")
        print("1. Bank Employee")
        print("2. Account Holder")
        print("3. Close The System")
        print("\n")
        choice=int(input("Enter Your Choice: "))
        print("\n")
        
        if choice==1:
            print("-----ADMIN Login-----")
            print("\n")
            username=input("Username: ")
            password=input("Password: ")
            if verifyAdminAccount(username,password):
                print("\n")
                print("Login Successful")
                while True:
                    print("\n")
                    print("What do you want to do?")
                    print("1. Open A Account")
                    print("2. Diaplay All The Accounts")
                    print("3. Close An Account")
                    print("4. Update Account Details")
                    print("5. Get Details of a specific Account")
                    print("6. Add Money in an Account")
                    print("7. Account Type Wise Division")
                    print("8. Go Back")
                    print("\n")
                    choice=int(input("Enter Your Choice: "))
                    print("\n")
                    if choice == 1:
                        print("Account Opening Form")
                        print("\n")
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
                        while True:
                            phone=input("Enter Phone Number: ")
                            if not verifyPhone(phone):
                                print("Invalid Phone Number! Please Enter It Again.")
                            else:
                                break
                        print("Enter the address:")
                        houseNo=input("House: ")
			while True:
                            	city=input("City: ")
                            	if city.lower() not in ('pune','chandigarh','hyderbad','bengaluru','chennai'):
                                	print("Invalid City! Please Enter It Again.")
                            	else:
                                	break
			while True:
				state=input("State: ")
                            	if state.lower() not in ('maharastra','karnataka','telangana','tamilnadu','haryana'):
                               		print("Invalid state! Please Enter It Again.")
                            	else:
                                	break
                        address=houseNo + " , " + city + " , " + state
                        account=Accounts(name,gender,aadhar,PAN,DOB,phone,address,generateAccountNo(city,state,accountType),generateIFSC(city,state),accountType,generatePassword(PAN,phone),balance=0)
                        accountsData.append(account)
                        print("\n")
                        print("Account Opened Successfully!!!")
                        account.display()
                        x=input()
                        
                    elif choice==2:
                        print("All the accounts in the Database:")
                        for i in accountsData:
                            i.display()
                        x=input()
                    
                    elif choice==3:
                        accountNo=input("Enter The Account No. To Close: ")
                        for i in accountsData:
                            if i.accountNo==accountNo:
                                accountsData.remove(i)
                        print("Account Closed Successfully!")
                        x=input()
                    
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
                                            i.dob=DOB
                                            print("Account Details Updated Successfully!")
                                            break
                        x=input()
                        
                    elif choice==5:
                        print("Search Account Based on:")
                        print("1. Name")
                        print("2. AccountNo")
                        while True:
                            choice=int(input("Enter your choice: "))
                            if choice==1:
                                name=input("Enter The Name of The Account Holder: ")
                                for i in accountsData:
                                    if i.name==name:
                                        i.display()
                                        break
                            elif choice==2:
                                accountNo=input("Enter The AccountNo of The Account Holder: ")
                                for i in accountsData:
                                    if i.accountNo==accountNo:
                                        i.display()
                                        break
                            else:
                                print("Invalid choice!")
                            break
                        x=input()        
                        
                    elif choice==6:
                        accountNo=input("Enter The Account No.: ")
                        amount=int(input("Enter The amount to be deposited: "))
			found=False
                        for i in accountsData:
                            if i.accountNo==accountNo:
				found=True
                                i.balance=i.balance+amount
                                print("Balance Updated Successfully!")
                                break
			if(Found==False):
				print("Invalid Details Enterted")
                        x=input()
                    
                    elif choice==7:
                        print("Account Type Wise Division")
                        Accounts.accountTypeWiseDivision()
                        x=input()
                    
                    elif choice==8:
                        print("Thank You!")
                        break
                        
                    else:
                        print("Invalid Choice")
                        x=input()
            
            else:
                print("Invalid Username/Password")
        
        elif choice==2:
            print("\n")
            print("-----Customer Account Login-----")
            print(" ** Password Hint: First 4 letters of PAN followed by last 4 number of the mobile number **")
            print("\n")
            username=input("Account No.: ")
            password=input("Password : ")
            print("\n")
            check=False
            for i in accountsData:
                if i.accountNo==username and i.password==password:
                    print("Login Successful")
                    check=True
                    while True:
                        print("\n")
                        print("What do you want to do?")
                        print("1. Update Account Details")
                        print("2. Withdaw")
                        print("3. Transfer")
                        print("4. Balance Enquiry")
                        print("5. Go Back")
                        print("\n")
                        choice=int(input("Enter Your Choice: "))
                        print("\n")
                        
                        if choice==1:
                            print("Choose what do you want to update.")
                            print("1. Name")
                            print("2. DOB")
                            choice=int(input("Enter your choice: "))
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
                                        i.dob=DOB
                                        print("Account Details Updated Successfully!")
                                        break
                                    
                        elif choice==2:
                            amount=int(input("Enter the amount you want to withdraw: "))
                            if i.balance>=amount:
                                i.balance=i.balance-amount
                                print("Windraw Successful")
                                print("Updated balance is "+str(i.balance))
                            else:
                                print("insufficient balance")
                        
                        elif choice==3:
                            accountNoT=input("Enter The Account No. you want to transfer: ")
                            amount=int(input("Enter the amount you want to Transfer: "))
                            if i.balance>=amount:
                                i.balance=i.balance-amount
                                for j in accountsData:
                                    if j.accountNo==accountNoT:
                                        j.balance=j.balance+amount
                                        print("Transfer Successful")
                                        print("Updated balance is "+str(i.balance))
                                        
                            else:
                                print("insufficient balance")
                        
                        elif choice==4:
                            print("Account Balance: "+str(i.balance))
                            
                        elif choice==5:
                            print("Thank You!")
                            break
                        else:
                            print("Invalid Choice")
                    break
            if(check==False):
                print("Invalid Username/Password")
            
            
        elif choice==3:
            flag=False
            print("Thank You!")
        else:
            print("Invalid Choice")
   
start()
