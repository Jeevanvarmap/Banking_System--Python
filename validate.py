accountSeq=1000
cities={'pune':11,'chandigarh':12,'hyderbad':13,'bengaluru':14,'chennai':15}
states={'maharastra':21,'karnataka':22,'telangana':23,'tamilnadu':24,'haryana':25}


def verifyName(inputName):
    names=inputName.split()
    if len(names)!=3:
        return False
    for name in names:
        if name.isalpha and name.istitle()==False:
            return False
    return True

def verifyAccountType(accountType):
    if accountType not in (1,2):
        return False
    return True

def verifyGender(gender):
    if gender not in (1,2):
        return False
    return True

def verifyAadhar(aadhar):
    if not aadhar.isnumeric:
        return False
    if len(aadhar)!=12:
        return False
    return True

def verifyDOB(inputDOB):
    DOB=inputDOB.split('/')
    if len(DOB)!=3:
        return False
    if int(DOB[1])>12 or int(DOB[1])<0:
        return False
    elif int(DOB[1]) in (1,3,5,7,8,10,12):
        if int(DOB[0])>31 or int(DOB[0])<0:
            return False
    elif int(DOB[1]) in (2,4,6,9,11):
        if int(DOB[0])>30 or int(DOB[0])<0:
            return False
    return True
    
def verifyPhone(phone):
    if len(phone)!=10:
        return False
    if not phone.isnumeric:
        return False
    return True

def generateAccountNo(city,state,accountType):
    global accountSeq
    accountSeq=accountSeq+1
    accountNo=str(accountType)+str(cities[city.lower()])+str(states[state.lower()])+str(accountSeq)
    return accountNo
    
def generateIFSC(city,state):
    IFSC=str('AMDOCS')+str(cities[city.lower()])+str(states[state.lower()])
    return IFSC
    
def generatePassword(pan,phone):
    password=str(pan[0:4])+str(phone)[6:]
    return password
   
def verifyPAN(inputPAN):
    if len(inputPAN)!=10:
        return False
    if (inputPAN[0:5]).isalpha()==False:
        return False
    if (inputPAN[6:9]).isnumeric()==False:
        return False
    if (inputPAN[9]).isalpha()==False:
        return False
    return True