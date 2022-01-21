#code starts here


print("What kind of calculation you want to do?\n (a)add\n (s)sub\n (m)multiply\n (d)div\n")
value= input("select by a,s,m or d\n")
if (value=="a"):
    no_1=int(input("Enter 1st no.\n"))
    no_2=int(input("Enter 2nd no.\n"))
    add = no_1 + no_2
    print(add)

elif (value=="s"):
    no_1=int(input("Enter 1st no.\n"))
    no_2=int(input("Enter 2nd no.\n"))
    sub = no_1 - no_2
    print(sub)

elif (value=="m"):
    no_1=int(input("Enter 1st no.\n"))
    no_2=int(input("Enter 2nd no.\n"))
    multyply = no_1 * no_2
    print(multiply)

elif (value=="d"):
    no_1=int(input("Enter 1st no.\n"))
    no_2=int(input("Enter 2nd no.\n"))
    div = no_1 / no_2
    print("div")

else:
    print("wrong option\n")
    
