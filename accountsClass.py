accountsData=[]

class Accounts:
    
    accTypeDiv={}
    
    def __init__(self,name,gender,aadhar,pan,dob,phone,address,accountNo,ifscCode,accountType,password,balance):
        self.name=name
        self.gender=gender
        self.aadhar=aadhar
        self.pan=pan
        self.dob=dob
        self.phone=phone
        self.address=address
        self.accountNo=accountNo
        self.ifscCode=ifscCode
        self.accountType=accountType
        self.password=password
        self.balance=balance
        if self.accountType in self.accTypeDiv.keys():
            self.accTypeDiv[self.accountType].append(self.accountNo)
        else:
            self.accTypeDiv[self.accountType]=[self.accountNo]

    def display(self):
        print("\n")
        print("Name: "+ self.name)
        print("-----Personal Details-----")
        print("Aadhar: "+str(self.aadhar))
        print("PAN: "+self.pan)
        print("DOB: "+self.dob)
        print("Phone Number: "+str(self.phone))
        if self.gender == 1:
            print("Gender: Male")
        elif self.gender == 2:
            print("Gender: Female")
        print("Address: "+self.address)
        print("-----Account Details-----")
        print("AccountNo: "+self.accountNo)
        print("IFSC Code: "+self.ifscCode)
        if self.accountType == 1:
            print("Account Type: Savings")
        elif self.accountType == 2:
            print("Account Type: Current")
        print("Balance: "+str(self.balance))
    
    @classmethod    
    def accountTypeWiseDivision(self):
        print("\n")
        print("Savings Accounts:")
        for k,v in self.accTypeDiv.items():
            if k==1:
                for l in v:
                    print(l,end=" ")
                print("")
        print("Current Accounts:")
        for k,v in self.accTypeDiv.items():
            if k==2:
                for l in v:
                    print(l,end=" ")
                print("")