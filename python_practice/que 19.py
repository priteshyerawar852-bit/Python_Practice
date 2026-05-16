while True:

    print("1. convert cm to ft: ")
    print("2. convert kl to miles: ")
    print("3. convert usd to inr: ")

    choice = int(input("enter your choice: "))

    if choice == 1:
        length = float(input("enter a length: "))
        ft = length*0.0328084
        print("ft is :",ft)
    elif choice == 2:
        kl = float(input("enter a kl : "))
        miles = kl*1.609344
        print("miles is : ",miles)
    elif choice == 3:
       usd = float(input("enter a usd: "))
       incr = usd*96
       print("incr is : ",incr)  
       break
    
    else:
        print("bhadd may jao !!! ")
