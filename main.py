#Create a simple chatbot for a retail store that can answer customers' frequently asked questions about store hours, location, available products, and prices.
#Create a chatbot for a restaurant that can take orders, provide information about the menu and specials, and make reservations.
#Create a financial institution chatbot to assist customers with checking account balances, transferring funds, and providing information about products and services.
import time
import random

repeat = True

error_ans = [
  "\nSorry, I didn't quite get that.",
  "\nI don't seem to understand.",
  "\nExcuse me, could you repeat that?",
  "\nSorry, I'm not sure."
]

pos_response = [
  "sure", "ok", "okay", "alright", "yes"
]

neg_response = [
  " no ", "no ", " no", "no"
]

def bank_bot():
  print("--Welcome to my bank!--")

  repeat = True
  
  acc_balance = []
  
  def deposit():
    print("**Depositing**")
    print("------------------")
    dep_amt = input("How much would you like to deposit? ")
  
    if ' dollar' in dep_amt:
      print(f'Depositing {dep_amt}...')
    elif 'dollar' not in dep_amt:
      print(f'Depositing {dep_amt} dollars...')
  
    dep_amt = int(dep_amt)
  
    acc_balance.append(dep_amt)
    new_bal = sum(acc_balance)
  
    print(f'Your balance is now {new_bal}!')
  
  def withdraw():
    new_bal = sum(acc_balance)
    wit_amt = input("How much would you like to withdraw? ")
    
    if ' dollar' in wit_amt:
      print(f'Withdrawing {wit_amt}...')
      
    elif 'dollar' not in wit_amt:
      print(f'Withdrawing {wit_amt} dollars...')
      
    for n in wit_amt:
      if n.isdigit():
        n = int(n)
        
    wit_amt = int(wit_amt)
  
    sum_bal = sum(acc_balance)
    if sum_bal < wit_amt:
      print("Error... \nYour account balance is low.")
    elif sum_bal > wit_amt:
      new_bal = new_bal - n
      acc_balance.clear()
      acc_balance.append(new_bal)
    print(f'Your balance is now {new_bal}.')
    
    
  while repeat:
    
    prompt = input("What can I help you with today? ")
  
    if 'balance' in prompt:
      print (acc_balance)
  
    elif 'deposit' in prompt:
      deposit()
      
    elif 'withdraw' in prompt:
      withdraw()
  
    elif 'service' in prompt:
      print("We ")
  
    elif 'nothing' in prompt:
      print("Goodbye!")
      start()
    else:
      print(random.choice(error_ans))
      time.sleep(1.5)
      





def restaurant_bot():
  print("--Welcome to my restaurant!--")

  repeat = True
  
  menu = [
    {'item_Id': 1, 'type': 'Hamburger', 'price': 10, 'description': 'A standard cheeseburger with a side of fries.'},
    {'item_Id': 2, 'type': 'Hotdog', 'price': 2.50, 'description': 'A grilled or steamed sausage served in the slit of a \npartially sliced bun.'},
    {'item_Id': 3, 'type': 'Chicken Nuggets', 'price': 10, 'description': 'Deep-fried and breaded pieces of chicken with a side of fries'},
    {'item_Id': 4, 'type': 'Fries', 'price': 2, 'description': 'A basket of deep-fried sliced potatoes.'},
    {'item_Id': 5, 'type': 'Drink', 'price': 1, 'description': 'A fountain drink of your choice.'}
  ]

  final_order = []
  total_cost = []
  
  def show_menu():
    print("\n **RESTAURANT MENU**")
    for item in menu:
      print("------------------------------------")
      for key, value in item.items():
        print(f'{key}: {value}')
    print("------------------------------------")

  def reservation():
    date = input("\nWhat day would you like to reserve for? ")
    time = input("What time would you like to reserve at? ")
    people = input("How many people are you reserving for? ")

    print(f'\nWe will prepare a table for {people} guests on {date} at {time}.')

  def order_product():
    repeat = True
    show_menu()
  
    print("\n **Placing an Order**")
    print("-----------------")
  
    #avail_quantity = 0  #available quantity in stock
    cost = 0  # cost of the purchase
    type = ''  # type of the product
    price = 0  #price of a unit
    while repeat:
      try:
        PID = int(input("Enter the item id: "))
      except:
        PID = 0
      try:
        quantity = int(input("Enter an amount: "))
      except:
        quantity = 0
  
      
      for i in range(len(menu)):
        item = (menu[i]['item_Id'])
        if item == PID:
          price = menu[i]["price"]
          type = menu[i]["type"]
          cost = quantity * price  # add taxes later

      new_product = Product(PID, type, cost, quantity) 
      final_order.append(new_product.features())
          
      loop = input('Do you want to order anything else? ')
      if loop in neg_response:
        repeat = False
        print(final_order)
        for i in range(len(final_order)):
          order = (final_order[i]['price'])
          total_cost.append(order)
        for x in range(len(total_cost)):
          total = sum(total_cost)
          
    print(f'Total price is {total}!')
    total_cost.clear()
    final_order.clear()

  class Product:
    def __init__(self,PID, type, price, total):
      self.PID = PID
      self.type = type
      self.price = price
      self.total = total
    def features(self):
      return {
        "item_Id":self.PID,
        "type":self.type,
        "price":self.price,
        "total":self.total
      }
  
  while repeat:
    prompt = input("\nWhat may I help you with today? \n\n")
    response = prompt.lower()
    
    if ('order') in response:
      order_product()
      
    elif ('reservation') in response:
      reservation()

    elif ('reserve') in response:
      reservation()
      
    elif ('menu') in response:
      show_menu()

    elif ('nothing') in response:
      print("\nGoodbye!")
      start()
      
    else:
      print(random.choice(error_ans))
      time.sleep(1.5)

#restaurant_bot()


def retail_bot():
  inventory = [
    {'prod_Id': 4327, 'type': 'Shoes', 'price': 100, 'total': 20},
    {'prod_Id': 3915, 'type': 'Tshirts', 'price': 43.5, 'total': 32},
    {'prod_Id': 2119, 'type': 'Pants', 'price': 34, 'total': 19},
    {'prod_Id': 1194, 'type': 'Jumpers', 'price': 250, 'total': 5},  
    {'prod_Id': 1300, 'type': 'Blouse', 'price': 24.76, 'total': 3},
    {'prod_Id': 1118, 'type': 'Dress', 'price': 50, 'total': 10}, 
    {'prod_Id': 1664, 'type': 'Suits', 'price': 250, 'total': 5}
  ]
  
  print("--Welcome to my retail store!--")
  
  repeat = True

  def show_inventory():
    print("\n **RETAIL STORE INVENTORY**")
    for product in inventory:
      print("------------------------------------")
      for key, value in product.items():
        print(f'{key}: {value}')
    print("------------------------------------")
    time.sleep(1.5)
  
  while repeat:
    prompt = input("\nWhat would you like to know about?\n\n")
    if ('hour') in prompt:
      print ("\nThe store is open everyday from 8 am to 10 pm excluding holidays")
      
    elif ('where') in prompt:
      print("\nThe store is located in Sesame Street 123")
      
    elif ('product') in prompt:
      show_inventory()
      
    elif ('price') in prompt:
      show_inventory()
      
    elif ('nothing') in prompt:
      print("\nGoodbye!")
      start()
      
    else:
      print(random.choice(error_ans))
      time.sleep(1.5)

#retail_bot()
def start():
  repeat = True
  while repeat:
    print("1: Retail Store Bot")
    print("2: Restaurant Bot")
    print("3: Bank Bot")
    print("4: Exit")
    bot = input("Which bot would you like to use? \n Respond 'nothing' to each bot to exit. ")
    
    if bot == '1':
      retail_bot()
    elif bot == '2':
      restaurant_bot()
    elif bot == '3':
      bank_bot()
    elif bot == '4':
      repeat = False
    else:
      print(random.choice(error_ans))
      time.sleep(1.5)
start()