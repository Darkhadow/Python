import mymodule
##ask=input('''
##Plz type your birthyear if you want to
##find out your age: ''')
##print(mymodule.ageChecker(ask))

while True:
    a=int(input("dice?: "))
    b=int(input("side?: "))
    mymodule.mulitDice(a,b)
    c= input("exit (Y/N): ").upper()
    if c in "Y":
        exit()
    else:
        continue
