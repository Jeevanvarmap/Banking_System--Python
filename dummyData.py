from accountsClass import *
from validate import *

def addDummyData():
    name=["Jeevan Narayana Raju","Nani Reddy Bakka"]
    accountType=['1','2']
    gender=[1,1]
    DOB=["31/08/2001","25/09/2001"]
    PAN=["CKXPN9761N","ASDFG1234H"]
    aadhar=[522237006297,123456789012]
    phone=[9848849911,7093940445]
    houseNo=["Flat N0: 1408A, Majestique Towers","Flat N0: 304, SSV Vaibhav"]
    city=["Pune","Hyderbad"]
    state=["Maharastra","Telangana"]
    address=[houseNo[0] + " , " + city[0] + " , " + state[0],houseNo[1] + " , " + city[1] + " , " + state[1]]
    account0=Accounts(name[0],gender[0],aadhar[0],PAN[0],DOB[0],phone[0],address[0],generateAccountNo(city[0],state[0],accountType[0]),generateIFSC(city[0],state[0]),accountType[0],generatePassword(PAN[0],phone[0]),balance=0)
    account1=Accounts(name[1],gender[1],aadhar[1],PAN[1],DOB[1],phone[1],address[1],generateAccountNo(city[1],state[1],accountType[1]),generateIFSC(city[1],state[1]),accountType[1],generatePassword(PAN[1],phone[1]),balance=0)
    accountsData.append(account0)
    accountsData.append(account1)