def Prime(n):    
    if n>1:
        for i in range(2,n):
            if( n % i) == 0:
                print ("false")
                break
            else:
                print ("true")
                break
    else:
        print ("false")

Prime(n = int(input("Please enter a number: ")))

