#fruit list
shop=['apple','durian','grapes','dragonfruit','coconut','lime','lemon','kiwi','orange','pear','plum','cherry']
def ALLFruits(): #Option A
  print("\nList of ALLfruits in my shop")
  for fruit in shop:
    print("-",fruit.capitalize())
  print(f"\nTotal number of fruits: {len(shop)}")
  input("\nPress Enter to continue...")
  return

def FirstLetter(): #Option B
  letter=input('\nWhat letter would you like to find?:').lower()
  check=[]
  for fruit in shop:
    if letter in fruit[0]:
      check.append(fruit)
  if len(check) > 0:
    print(f'\nResult found: {len(check)}')
    for fruit in check:
      print(f'-{fruit.capitalize()}')
  else:
    print(f'\nSorry,the shop does not have any fruits starting with "{letter}"')
  input('\nPress enter to continue...')
  return

def Order(): #Option C
  basket=[]
  print('''
  ~Instructions~
  To place an order, write the fruit you want and press enter.
  ONLY write 1 fruit at a time.
  Once finish, write "done" to complete your order.
  ''')
  while True:
    choice=input('Fruit: ').lower()
    if choice == "done":
      break
    elif choice in shop:
      basket.append(choice.capitalize())
      shop.remove(choice)
      print('Has been added to your basket...')
    else:
      Invalid()
    print(f'\nYou ordered a total of {len(basket)} fruit/s')
    for fruit in basket:
      print('-',fruit)
    input('\nPress enter to continue...')
    print('!Thank You!')
  return

def Ordered(): #Option f
  add=input('\nType a fruit that you what to add/donate to the shop: ')
  shop.append(add)
  print(shop)
  #Homework: try to add more then one fruit too the shop. 
  return

def Invalid(): #Invalid msg
  input('\nYou have entered an invalid option, \nPress enter to try again...')
  return
#program title
print("!Welcome to Dhira's Fruit Shop!")
#menu options
menu=('''
-MENU-
a) View all fruits
b) View fruits by first letter
c) Place order
d) Exit
f) Add fruits
Choice: ''')
while True: #Main loop
  choice=input(menu).lower()
  if choice == 'a':
    ALLFruits() #Option A
  elif choice == 'b':
    FirstLetter() #Option B
  elif choice == 'c':
    Order() #Option C
  elif choice == 'd':
    break #Option D
  elif choice == 'f':
    Ordered() #Option f
  else: Invalid()

print('\n!Thank you for visiting my fruit shop!') #goodbye msg
