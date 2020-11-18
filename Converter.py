from openexchangerate import OpenExchangeRates
import json
from tkinter import *
from tkinter import messagebox
import time

latest = None
names = None

def show():
    import subprocess as sp
    programName = "notepad.exe"
    fileName = "Codes.txt"
    sp.Popen([programName, fileName])

def helper():
    messagebox.showinfo("Help Text", "Welcome To The Currency Converter. Please Enter The 3 Letter Currency Codes Or The Full Name Of Currencies And Enter The Amount. To View Currency Codes, Click On The View Codes Button.")

def getrates():
    global latest, names
    final_text = ""
    client = OpenExchangeRates(api_key="api_key")
    latest = str(client.latest())
    names = str(client.currencies())
    latest = latest.split(", frozendict=mappingproxy(", 1)
    names = names.split(", frozendict=mappingproxy(", 1)
    latest = str(latest[0])
    names = str(names[0])
    latest = latest.split("=", 1)
    names = names.split("=", 1)
    latest = str(latest[1])
    names = str(names[1])
    latest = latest.replace("'", '"')
    names = names.replace("'", '"')
    names = names.replace('Tongan Pa"anga', "Tongan Pa'anga")
    latest = json.loads(latest)
    names = json.loads(names)
    latest = dict(latest)
    names = dict(names)

getrates()

EUR = latest["EUR"]
USD = latest["USD"]
AED = latest["AED"]
AFN = latest["AFN"]
ALL = latest["ALL"]
AMD = latest["AMD"]
ANG = latest["ANG"]
AOA = latest["AOA"]
ARS = latest["ARS"]
AUD = latest["AUD"]
AZN = latest["AZN"]
BAM = latest["BAM"]
BBD = latest["BBD"]
BDT = latest["BDT"]
BGN = latest["BGN"]
BHD = latest["BHD"]
BMD = latest["BMD"]
BND = latest["BND"]
BOB = latest["BOB"]
BRL = latest["BRL"]
BSD = latest["BSD"]
BTN = latest["BTN"]
BWP = latest["BWP"]
BYN = latest["BYN"]
BZD = latest["BZD"]
CAD = latest["CAD"]
CDF = latest["CDF"]
CHF = latest["CHF"]
CLF = latest["CLF"]
CLP = latest["CLP"]
CNH = latest["CNH"]
CNY = latest["CNY"]
COP = latest["COP"]
CRC = latest["CRC"]
CUC = latest["CUC"]
CUP = latest["CUP"]
CVE = latest["CVE"]
CZK = latest["CZK"]
DJF = latest["DJF"]
DKK = latest["DKK"]
DOP = latest["DOP"]
DZD = latest["DZD"]
EGP = latest["EGP"]
ERN = latest["ERN"]
ETB = latest["ETB"]
FJD = latest["FJD"]
FKP = latest["FKP"]
GBP = latest["GBP"]
GEL = latest["GEL"]
GGP = latest["GGP"]
GHS = latest["GHS"]
GIP = latest["GIP"]
GMD = latest["GMD"]
GNF = latest["GNF"]
GTQ = latest["GTQ"]
GYD = latest["GYD"]
HKD = latest["HKD"]
HNL = latest["HNL"]
HRK = latest["HRK"]
HTG = latest["HTG"]
HUF = latest["HUF"]
IDR = latest["IDR"]
ILS = latest["ILS"]
IMP = latest["IMP"]
INR = latest["INR"]
IQD = latest["IQD"]
IRR = latest["IRR"]
ISK = latest["ISK"]
JEP = latest["JEP"]
JMD = latest["JMD"]
JOD = latest["JOD"]
JPY = latest["JPY"]
KES = latest["KES"]
KGS = latest["KGS"]
KHR = latest["KHR"]
KMF = latest["KMF"]
KPW = latest["KPW"]
KRW = latest["KRW"]
KWD = latest["KWD"]
KYD = latest["KYD"]
KZT = latest["KZT"]
LAK = latest["LAK"]
LBP = latest["LBP"]
LKR = latest["LKR"]
LRD = latest["LRD"]
LSL = latest["LSL"]
LYD = latest["LYD"]
MAD = latest["MAD"]
MDL = latest["MDL"]
MGA = latest["MGA"]
MKD = latest["MKD"]
MMK = latest["MMK"]
MNT = latest["MNT"]
MOP = latest["MOP"]
MRO = latest["MRO"]
MRU = latest["MRU"]
MUR = latest["MUR"]
MVR = latest["MVR"]
MWK = latest["MWK"]
MXN = latest["MXN"]
MYR = latest["MYR"]
MZN = latest["MZN"]
NAD = latest["NAD"]
NGN = latest["NGN"]
NIO = latest["NIO"]
NOK = latest["NOK"]
NPR = latest["NPR"]
NZD = latest["NZD"]
OMR = latest["OMR"]
PAB = latest["PAB"]
PEN = latest["PEN"]
PGK = latest["PGK"]
PHP = latest["PHP"]
PKR = latest["PKR"]
PLN = latest["PLN"]
PYG = latest["PYG"]
QAR = latest["QAR"]
RON = latest["RON"]
RSD = latest["RSD"]
RUB = latest["RUB"]
RWF = latest["RWF"]
SAR = latest["SAR"]
SBD = latest["SBD"]
SCR = latest["SCR"]
SDG = latest["SDG"]
SEK = latest["SEK"]
SGD = latest["SGD"]
SHP = latest["SHP"]
SLL = latest["SLL"]
SOS = latest["SOS"]
SRD = latest["SRD"]
SSP = latest["SSP"]
STD = latest["STD"]
STN = latest["STN"]
SVC = latest["SVC"]
SYP = latest["SYP"]
SZL = latest["SZL"]
THB = latest["THB"]
TJS = latest["TJS"]
TMT = latest["TMT"]
TND = latest["TND"]
TOP = latest["TOP"]
TRY = latest["TRY"]
TTD = latest["TTD"]
TWD = latest["TWD"]
TZS = latest["TZS"]
UAH = latest["UAH"]
UGX = latest["UGX"]
UYU = latest["UYU"]
UZS = latest["UZS"]
VEF = latest["VEF"]
VES = latest["VES"]
VND = latest["VND"]
VUV = latest["VUV"]
WST = latest["WST"]
XAF = latest["XAF"]
XCD = latest["XCD"]
XOF = latest["XOF"]
XPF = latest["XPF"]
YER = latest["YER"]
ZAR = latest["ZAR"]
ZMW = latest["ZMW"]
ZWL = latest["ZWL"]

root = Tk()
root.title("Currency Converter")
root.geometry("600x600")

logo_image = PhotoImage(file="Logo.png")
root.iconphoto(False, logo_image)
background_image = PhotoImage(file="Background.png")
background_label = Label(root, image=background_image)
background_label.place(relheight=1, relwidth=1)
root.iconbitmap("Icon.ico")

def convert():
    input1=entry1.get()
    input2=entry2.get()
    input1 = str(input1)
    input2 = str(input2)
    isfull1 = True
    isfull2 = True
    short1 = None
    short2 = None
    if len(input1) == 3:
        input1 = input1.upper()
        isfull1 = False
        num1 = globals()[input1]
        short1 = input1
    if len(input2) == 3:
        input2 = input2.upper()
        isfull2 = False
        num2 = globals()[input2]
        short2 = input2
    if isfull1:
        if input1.count(" ") > 0:
            input1 = input1.split(" ")
            for item in input1:
                item.capitalize()
            input1 = " ".join(input1)
            for key, value in names.items():
                if value == input1:
                    num1 = globals()[key]
                    short1 = key
        else:
            input1 = input1.capitalize()
            for key, value in names.items():
                if value == input1:
                    num1 = globals()[key]
                    short1 = key
    if isfull2:
        if input2.count(" ") > 0:
            input2 = input2.split(" ")
            for item in input2:
                item.capitalize()
            input2 = " ".join(input2)
            for key, value in names.items():
                if value == input2:
                    num2 = globals()[key]
                    short2 = key
                    
        else:
            input2 = input2.capitalize()
            for key, value in names.items():
                if value == input2:
                    num2 = globals()[key]
                    short2 = key
    amount = int(entry3.get())
    am = num2 / num1
    final = amoount * am
    final_text = str(str(amount)+" "+names[short1]+" Are \n"+str(final)+" "+names[short2]+" ")
    label2 = Label(frame, text=str(final_text),font=("Times New Roman", 15), fg="Black", bg="white")
    label2.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.2)

frame = Frame(root,bg="white")
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

label = Label(frame, text="Currency Converter", font=("Times New Roman", 20), fg="Black", bg="White")
label.place(relwidth=0.5, relheight=0.08, relx=0.26, rely=0.055)

info = Button(frame, relief=RIDGE, text="i", font=("Times New Roman", 20), fg="Black", bg="White", command=helper)
info.place(relwidth=0.1, relheight=0.08, relx=0.85, rely=0.05)

froml = Label(frame, text="From:",font=("Times New Roman",20),fg="Black",bg="White")
froml.place(relx=0.1,rely=0.2,relwidth=0.2,relheight=0.1)

entry1 = Entry(frame,relief=GROOVE,bg="White",bd=7,font=("Times New Roman",20),fg="Black")
entry1.place(relx=0.3,rely=0.2,relwidth=0.6,relheight=0.1)

from2 = Label(frame,text="To:",font=("Times New Roman",20),fg="Black",bg="White")
from2.place(relx=0.1,rely=0.375,relwidth=0.2,relheight=0.1)

entry2 = Entry(frame,relief=GROOVE,bg="White",bd=7,font=("Times New Roman",20),fg="Black")
entry2.place(relx=0.3,rely=0.375,relwidth=0.6,relheight=0.1)

from3 = Label(frame,text="Amount:",font=("Times New Roman",20),fg="Black",bg="White")
from3.place(relx=0.08,rely=0.55,relwidth=0.2,relheight=0.1)

entry3 = Entry(frame,relief=GROOVE,bg="White",bd=7,font=("Times New Roman",20),fg="Black")
entry3.place(relx=0.3,rely=0.55,relwidth=0.6,relheight=0.1)

button = Button(frame,relief=RIDGE,text="Convert",bd=7,bg="White",fg="Black",command=convert, font=("Times New Roman", 15))
button.place(relx=0.1,rely=0.7,relwidth=0.35,relheight=0.1)

button2 = Button(frame,relief=RIDGE,text="View Codes",bd=7,bg="White",fg="Black",command=show, font=("Times New Roman", 15))
button2.place(relx=0.55,rely=0.7,relwidth=0.35,relheight=0.1)

root.mainloop()
