import time
from datetime import datetime
print("This is the ATM Simulator")
print("\n")
time.sleep(2)


def sign_up():
    print("We will start by Signing you up.\n")
    time.sleep(2)
    pin_file = open("pin.txt", "w")
    print("Enter the pin you would like to set (4 digit number): ")
    pin = input("")
    pin_file.write(pin)
    pin_file.close()
    
    time.sleep(2)
    print("\nYour pin is set!")
    global log_in_status
    log_in_status = 1

def logIn():
    print("Welcome back! We will log in\n")
    time.sleep(2)
    p = open("pin.txt", "r")
    log_in_check_pin = p.read()
    # print(log_in_check_pin)
    log_in_pin = input("Enter your pin: ")
    if log_in_pin==log_in_check_pin:
        time.sleep(1)
        print("\nLogged in!")
        global log_in_status
        log_in_status = 1
    else:
        time.sleep(1)
        print("\nWrong pin")
        log_in_status = 0

with open("pin.txt", "r") as check_pin:
    pin_presence = check_pin.read()
    # print(pin_presence)
    if pin_presence != "":
        logIn()
    else:
        sign_up()

# sign_up()


def check_balance():
    c = open("balance.txt", "r")
    check_balance_func = c.read()
    print(f"Your balance is ${check_balance_func}")
    print("\n")
    c.close()
    time.sleep(4)
    functions()

def withdraw():
    c = open("balance.txt", "r")
    check_balance_func = c.read()
    c.close()
    withdraw_amt = input("How much would you like to withdraw: ")
    if int(withdraw_amt)>int(check_balance_func):
        print(f"Unable to complete withdrawl. You are asking for ${int(withdraw_amt)-int(check_balance_func)} over your balance")
        print("\n")
    else:
        new_balance = int(check_balance_func) - int(withdraw_amt)
        d = open("balance.txt", "w")
        d.write(str(new_balance))
        d.close()
        print("Withdrawal complete!")
        e = open("balance.txt", "r")
        check_balance_remain = e.read()
        e.close()
        print(f"Your remaining balance is ${check_balance_remain}")
        print("\n")
        i = open("transactions.txt", "a")
        now = datetime.now()
        formatted_time = now.strftime("%d-%m-%Y %H:%M:%S")
        i.write(f"{formatted_time}  :  You withdrew ${withdraw_amt} \n")
        i.write("\n")
        i.close()
    time.sleep(5)
    functions()


def deposit():
    deposit_amt = input("How much would you like to deposit: ")
    
    f = open("balance.txt", "r")
    current_balance = int(f.read())
    f.close()

    new_toadd_balance = int(deposit_amt)+current_balance
    g = open("balance.txt", "w")
    g.write(str(new_toadd_balance))
    g.close()
    print("Deposit complete!")
    time.sleep(1)
    print(f"Your balance is now ${new_toadd_balance}")
    print("\n")
    h = open("transactions.txt", "a")
    now = datetime.now()
    formatted_time = now.strftime("%d-%m-%Y %H:%M:%S")
    h.write(f"{formatted_time}  :  You deposited ${deposit_amt} \n")
    h.write("\n")
    h.close()
    time.sleep(5)
    functions()

def view_trans():
    print("\n")
    k = open("transactions.txt", "r")
    transactionHistory = k.read()
    time.sleep(2)
    print(transactionHistory)
    k.close()
    time.sleep(5)
    print("\n")
    functions()

def reset_pin():
    x = open("pin.txt", "r")
    current_pin = x.read()
    x.close()

    current_pin_test = input("Enter current pin: ")

    if current_pin_test != current_pin:
        print("Incorrect pin")
        time.sleep(1)
        print("Try again")
        print("\n")
        reset_pin()
    else:
        w = open("pin.txt", "w")
        new_set_pin = input("Enter new pin: ")
        w.write(str(new_set_pin))
        print("New pin set!")
        w.close()
        time.sleep(2)
        print("\n")
        functions()

if (log_in_status==1):
    time.sleep(1)
    print("At the moment, you have no money in your account")
    time.sleep(1)
    print("How much would you like to deposit: ")
    initial_deposit = int(input(""))
    with open("balance.txt", "w")as balance:
        balance.write(str(initial_deposit))
        balance.close()
    
    with open("transactions.txt", "a") as trans:
        now = datetime.now()
        # now = datetime.now()
        formatted = now.strftime("%d-%m-%Y %H:%M:%S")
        trans.write(f"{formatted}  :  You deposited ${initial_deposit} \n")
        trans.write("\n")
    time.sleep(1)
    print("Thank you!")
    print("\n")
    time.sleep(1)
    trans.close()
    
    def functions():
        print("These are you available functions(the number is what you have to type to access the function):")
        print("1 :  CHECK BALANCE")
        print("2 :  WITHDRAW")
        print("3 :  DEPOSIT")
        print("4 :  VIEW TRANSACTIONS")
        print("5 :  RESET PIN")
        print("6 :  EXIT")

        which_function = input("Which function: ")

        if which_function=="1":
            check_balance()
        if which_function=="2":
            withdraw()
        if which_function=="3":
            deposit()
        if which_function=="4":
            view_trans()
        if which_function=="5":
            reset_pin()
    time.sleep(2)
    functions()
