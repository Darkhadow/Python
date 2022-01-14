##a = 0
##while a <= 10:
##    print('a:',a)
##    b = 0
##    while b <= 5:
##        print('  b:',b)
##        b += 1
##        break
##    a += 1

##box = ['aA','bB','cC']
##count = 0
##while count < len(box):
##    print("check1")
##    for i in box:
##        print("check2")
##        for x in i:
##            print("check3")
##            print(x)

##box1 = ['A','B','C']
##box2 = ('D','E','F')
##box3 = {'letter1': 'G',
##        'letter2': 'H',
##        'letter3': 'I'}
##box4 = "JKL"
##
##box5 = {'b1':box1,
##        'b2':box2,
##        'b3':box3,
##        'b4':box4}
##
##print(box5['b4'][0]+box5['b1'][0]+box5['b2'][0]+box5['b2'][1])

##name1 = 'abel'
##name2 = 'bell'
##name3 = 'cain'
##name4 = 'dante'
##a = [name1,name2,name3,name4]
##name = input("Enter name: ")
##if name in a:
##    print("Accepted")
##else:
##    print("Deny")

##name_list = [('abel',10),('bell',19),
##             ('cain',12),('dante',20)]
##
##count = 0
##while count < len(name_list):
##    if name_list[count][1] > 18:
##        print(name_list[count][0].title(),"is above 18 years old")
##    count += 1

SL = {
      'abel': {'permit level':2,'age':10,
             'VIP':False,'arrived':False},
      'bell': {'permit level':1,'age':19,
             'VIP':True,'arrived':False},
      'cain': {'permit level':3,'age':12,
             'VIP':False,'arrived':False},
      'dante':{'permit level':4,'age':20,
             'VIP':True,'arrived':False}
      }
name = input('''
----------------------------------------------------------


            -----TOP SECERT FACILITY-----


----------------------------------------------------------
Please Enter Name: ''')
print('-------------------------------')
if name == 
