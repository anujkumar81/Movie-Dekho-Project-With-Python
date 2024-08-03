print("Welcome to MOVIE DEKHO")
#city()
def city():
    print("Please select a city\n1.Bengaluru\n2.Kolkata\n3.Delhi\n4.Mumbai")
    c=int(input())
    if c==1:
        print("You have selected Bengaluru")
    elif c==2:
        print("You have selected Kolkata")
    elif c==3:
        print("You have selectd Delhi")
    elif c==4:
        print("You have selectd Mumbai")
    else:
        print("Please enter a valid option")
        city()
    t_movie()
     
def t_movie():
    print("Please select a movie you would like to see \n1.KANTARA \n2.KGF CHAPTER 2 \n3.VIKRANTH RONA \n4.back")
    t=int(input())
    if t==1:
        print("You have selected KANTARA")
    elif t==2:
        print("You have selected KGF-CHAPTER 2")
    elif t==3:
        print("You have selectd VIKRANTH RONA")
    elif t==4:
        city()
    else:
        print("Please enter a valid option")
        t_movie()
    theatre()
    return 

def theatre():
    print("Please select the Theatre. \n1.INOX \n2.PVR \n3.back")
    h=int(input())
    if h==1:
        print("You have selected INOX")
    elif h==2:
        print("You have selected PVR")
    elif h==3:
        t_movie()
    else:
        print("Please enter a valid option")
        theatre()
    print("If you select 3-5 seats you get a discount of 5%")
    print("If you select 6-10 seats you get a discount of 10%")
    print("If you select more than 10 seats you get a discount of 15%")
    y=int(input("Enter number of seats "))
    
    print("Selected number of seats=",y)
    if y>=3 and y<=5:
        print("You have availed a discount of 5%")
    elif y>=6 and y<=10:
        print("You have availed a discount of 10%")
    elif y>10:
        print("You have availed a discount of 15%")
    
    screen()
    return 
        
def screen():
    print("Available timings for screens")
    print("Screen 1=1.10:00-1:00\n\t 2.1:10-4:10\n\t 3.4:20-7:20\n\t 4.7:30-10:30")
    print("Screen 2=1.10:15-1:15\n\t 2.1:25-4:25\n\t 3.4:35-7:35\n\t 4.7:45-10:45")
    print("Screen 3=1.10:30-1:30\n\t 2.1:40-4:40\n\t 3.4:50-7:50\n\t 4.8:00-10:45")
    s=int(input("Please select screen "))
    if s==1:
        print("You have selected Screen 1")    
    elif s==2:
        print("You have selected Screen 2")
    elif s==3:
        print("You have selectd Screen 3")
    elif s==4:
        theatre()
    else:
        print("Please enter a valid option")
        screen()
    time(s)
    return
    
def time(s):
    
    
    slot1 = {
        "1": "      10.00-1.00",
        "2": "      1.10-4.10",
        "3": "      4.20-7.20",
        "4": "      7.30-10.30"
    }
    slot2 = {
        "1": "      10.15-1.15",
        "2": "      1.25-4.25",
        "3": "      4.35-7.35",
        "4": "      7.45-10.45"
    }
    slot3 = {
        "1": "      10.30-1.30",
        "2": "      1.40-4.40",
        "3": "      4.50-7.50",
        "4": "      28.00-10.45"
    }
    
   
    
    if s==1:
        print("please select timings ")
        print("Available timimgs")
        print("1. 10:00-1:00\n2. 1:10-4:10\n3. 4:20-7:20\n4. 7:30-10:30")
        time=input()
        print("Selected time is ",slot1[time])
    elif s==2:
        print("please select timings ")
        print("Available timimgs")
        print("1. 10:15-1:15\n2. 1:25-4:25\n3. 4:35-7:35\n4. 7:45-10:45")
        time=input()
        print("Selected time is ",slot2[time])
    elif s==3:
        print("please select timings ")
        print("Available timimgs")
        print("1. 10:30-1:30\n2. 1:40-4:40\n3. 4:50-7:50\n4. 8:00-10:45")
        time=input()
        print("Selected time is ",slot3[time])
    elif s==4:
        screen()
    else:
        print("please enter a valid option")
        time(s)
    donation()
    return

   

    
def donation():
    print("Do you wish to donate 5 Rs Women Empowerment funds\n1.Yes\n2.No")
    d=int(input())
    if d==1:
        print("Thank you for your kind donation")
        print("Enjoy your movie while having a nice day!!\n Thank you for using MOVIE DEKHO")
    elif d==2:
        print("Enjoy your movie while having a nice day!!\n Thank you for using MOVIE DEKHO")
    else:
        print("Please enter a valid option")
        donation()
    
    return
city()
     