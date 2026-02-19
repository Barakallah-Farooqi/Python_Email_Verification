j, k, d = 0, 0, 0

email = input("Do you want to enter your Email (y/n)? ")

while True:
    if email.lower() == "y":
        dalo = input("Alright.. Enter your Email: ")

        if len(dalo) >= 6:
            if dalo[0].isalpha():
                if ("@" in dalo) and (dalo.count("@") == 1):
                    if dalo[-4] == "." or dalo[-3] == ".":

                        for i in dalo:
                            if i.isspace():
                                j = 1
                            elif i.isalpha():
                                if i == i.upper():
                                    k = 1
                            elif i.isdigit():
                                continue
                            elif i == "_" or i == "@" or i == ".":
                                continue
                            else:
                                d = 1

                        if j == 0 and k == 0 and d == 0:
                            print("Your email has been saved")
                            break
                        else:
                            print("Invalid Email Pattern Try again....")

                    else:
                        print("Invalid Email Pattern Try again....")
                else:
                    print("Invalid Email Pattern Try again....")
            else:
                print("Invalid Email Pattern Try again....")
        else:
            print("Email too short")

    else:
        break
              
        
              
              
           
           
            
            
           
     
     
    