MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
change_to_user={}

def process(user_amount,user_choice):
   
    water_remaining=resources['water']-int(MENU[user_choice]["ingredients"]['water'])
    if user_choice=="espresso":
        milk_remaining=resources['milk']
    else:
        milk_remaining=resources['milk']-int(MENU[user_choice]["ingredients"]['milk'])
        report('milk',milk_remaining)
    coffee_remaining=resources['coffee']-int(MENU[user_choice]["ingredients"]['coffee'])
    change=user_amount-MENU[user_choice]["cost"]
    amount_in=MENU[user_choice]["cost"]
    
    try:
        resources['amount_in_the_box']+=amount_in
    except KeyError:
        resources['amount_in_the_box']=amount_in
    report('water',water_remaining)
    report('coffee',coffee_remaining)
    
    change_to_user['change']=change
    

def report(item,qunatity):
    resources[item]=qunatity
    
def amount_from_user(quarters,dimes,nickles,pennies):
    q=quarters*0.25
    d=dimes*0.15
    n=nickles*0.1
    p=pennies*0.01
    total=q+d+n+p
    return total

repeat=True
while repeat:
    item=input('What would you like? (espresso/latte/cappuccino')
    if item!='report':
        print('Please insert coins')
        quarters=int(input('How many quarters'))
        dimes=int(input('How many dimes'))
        nickles=int(input('How many nickles'))
        pennies=int(input('How many pennies'))
        total_amount=amount_from_user(quarters,dimes,nickles,pennies)
        if total_amount>MENU[item]["cost"]:
            process(total_amount,item)
            if(resources['milk']>0 and resources['water']>0 and resources['coffee']>0):
                print(f"Here is your change {change_to_user['change']}.")
                print(f'Here is your {item}, Enjoy!!')
            else:
                repeat=False
                print("Sorry that's not enough resources. Money refunded")
                for i in resources.keys():
                    print(f'{i.upper()}:{resources[i]} ')
        else:
            repeat=False
            print("Sorry that's not enough money. Money refunded")
      
    else:
        
        for i in resources.keys():
            print(f'{i.upper()}:{resources[i]}')
        
        repeat=False
        
# %%
#Angerla's Version 
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

