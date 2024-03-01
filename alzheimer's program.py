'''program for the person who is suffering from the Alzheimer's disease, we can develop a software which will be wearable for them just like the watch '''
print("THIS PERSON IS SUFFERING FROM ALZHEIMER'S DISEASE")

#Using module for time


import time
localtime = time.asctime(time.localtime(time.time()))
print("Current time and date: ",localtime)
print ("Welcome Mahesh!")
while True:
    print("1.Personal Details\n2.Password\n3.Address and Contacts\n4.Important Notes\n5.Todays Tasks\n6.Calender")
    a=int(input("Enter the choise code: "))
    if (a==1):
        print("Mahesh Patil\nAge:40\nHeight:5'4\nBlood Group:O -ve\nMo.No.2563551***\nEmail Address:patilmahesh@gmail.com")
    elif(a==2):
        print("Email:kate@mahesh\nWhatsApp:12345\nInstagram:8970@mka\nFacebook:Maheshnana\nlinkdin:mahesh\nlaptop:9886")
    elif(a==3):
       print("Laxminagar, Near the S.B Patil road ,behind Pccoer, Ravet\nson:67755843**\nDaughter:52752825**\nwife:41738289**\nVinod:63836382**")
    elif(a==4):
        print("1.Collect 1000rs from Rupesh\n2.Renewal of life insurance (last date today)\n3.You have to collect medicines from Kanika")
    elif(a==5):
        print ("1.visit to the Ramesh farmhouse\n2.Yoga class in the evening\n3.bring some grocery items")
    elif(a==6):
        import calendar
        print (calendar.month(2023,2))
    else:
        print ("choose corect code!")
    print("1.Continue the program\n2.Terminate the program")
    ch=int(input("Enter your choice code: "))
    if(ch==2):
        break
while True:
        print("Do you want to check your physical activity ?\n1.yes\n2.no")
        ch2=int(input("Enter your choice number: "))
        if(ch2==2):
            break
        while True:
            print("1.Calories burn by Walking\n2.Total Calories Intake\n3.Medicines with timings\n[ENTER 4 TO EXIT]")
            dk=int(input("Choose the correct code of your Choice:"))
            if (dk==4):
                break

            #Using Modules
            if (dk==1):
                cal=int(input("Enter the distance in km:\n"))
                def calo(a):
                       var=a*170
                       print ("Burnt Calories are :",var)
                calo(cal)

            if(dk==2):
                print ("1.Bhaji")
                print ("2.Rice")
                print("3.chapati")
                pi=int(input("Enter the code: "))
                if (pi==1):
                    print("130 Calories")
                elif(pi==2):
                    print ("200 calories")
                elif(pi==3):
                    print ("20 calories")
                elif(pi==12):
                    print ("330 Calories")
                elif(pi==23):
                    print ("220 Calories")
                elif(pi==13):
                    print ("150 Calories")
                elif(pi==123 or pi==132 or pi==213 or pi==231 or pi==312 or pi==321):
                    print ("350 Calories")
                else:
                    print ("invalid entry!")
                   
                   
            #Using membership operator

            if (dk==3):
                t=int(input("Enter Current time(ONLY HOURS): "))
                t1=[6,7,8,9,10,11,12]
                t2=[13,14,15,16,17,18]
                t3=[19,20,21,22,23,24]
                t4=[1,2,3,4,5]
                if (t in t1):
                    print ("Take\nMedafit 40\nCloten667\nOxichrome 400 ")
                elif (t in t2):
                    print("Take\nClopivas\nSolvin D cold")
                elif(t in t3):
                    print ("Take\nMetrofit 40\nTrizel 45")
                else:
                    print ("There is no medicines now!")
print ("TAKE CARE MAHESH!")