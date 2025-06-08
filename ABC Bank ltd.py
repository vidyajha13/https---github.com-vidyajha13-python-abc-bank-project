store={}
custid=100
trans=1

def  customerid():
    global custid
    ci= f"CUST{custid}"
    custid += 1
    return ci
def transactionid():
    global trans
    tid = f"TXN{trans:03}"
    trans += 1
    return tid

    

def createaccount():
    try:
        age=int(input("User age : "))
        if age < 18:
            print (f"You are not eligible to create bank account \nCreate account after {18-age} year\nThankyou..... ")
            return
        else:
            print ("     DONE, your age is verify")
    except Exception as e:
        print(f"Do not write in word like(eighteen): {e}")
        return

    name=input("User name : ")
    password=(input("Create password : "))
    ci=customerid()
    store[ci] = {'name': name,'password': password, 'balance': 0, 'transactions': []}
    
    print(f" account created successfully! your COUSTOMER ID  is {ci} ")


def login():
    ci = input("Enter your customer ID: ").strip()
    if ci == "":
        return None
    if ci in store:
        print("okay, customer ID is valid")
        for i in range(3):
            try:
                p = input("Enter your password: ")
                if len(p) < 8:
                    print("Password must be at least 8 characters long.")
                    continue
                if store[ci]['password'] == p:
                    print("Login successful!")
                    return ci
                else:
                    print("Wrong password.")
            except Exception as e:
                if p==len(8):
                    print("Password must be at least 8 characters long.")
                else:
                    print(f"An error occurred: {e}")
        print("Too many failed attempts.")
    else:
        print("Invalid customer ID. Please try again.")
    return None
        

def deposit(ci):
    try:
        amt = float(input("Enter amount to deposit: "))
        if amt <= 0:
            print("try again with valid amount")
            return
        store[ci]['balance'] += amt
        tid = transactionid()
        store[ci]['transactions'].append(tid)
        print(f"Deposit successful! Transaction ID: {tid}")
    except Exception as e:
        if amt <= 0:
            print("try again with valid amount")
        else:
            print(f"An error occurred: {e}")
            print("words are not allowed, please enter a valid amount")



def withdraw(ci):
    try:
        amt = float(input("Enter amount to withdraw: "))
        extra=amt * 0.01
        total= amt + extra
        if store[ci]['balance'] >= total:
            store[ci]['balance'] -= total
            tid = transactionid()
            store[ci]['transactions'].append(tid)
            print(f"Withdrawal successful! Transaction ID: {tid} \n extra charge is {extra } \ntotal amount is {total } \n your balance is {store[ci]['balance']}")
        else:
            print("overdraft not allow")
    except Exception as e:
        print ("words are not allowed, please enter a valid amount")

def view(ci): 
        print("-----------------------------------Transaction History---------------------------------")
        print(f"Customer ID: {ci}")
        for transaction_id in store[ci]['transactions']:
            print(f"Transaction ID: {transaction_id} ")
        print(f"Name: {store[ci]['name']}")
        print(f"Balance: Rs.{store[ci]['balance']}")
        print(f"password: {'*' * len(str(store[ci]['password']))}" )
        if  store[ci]['balance']>1000:
            print("Your account is in good standing.")
        else:
            print("Your account balance is low. ")

def close(ci):
    try:
        a = input("Are you sure you want to close your account? (yes/no): ").lower()
        if a == 'yes':
            del store[ci]
            print("Account close successfully.")
        else:
            print("cancelled.")
    except Exception as e:
        if a != 'yes' or a != 'no':
            print("Please enter 'yes' or 'no'.")
def main():
    
    while True:
        print("......................Welcome to ABC Bank.............................")
        print("1. Create Account")
        print("2. Login")
        print("3. exit ")
        choice = input("Enter your choice: ")
        if choice == '1':
            createaccount()
        elif choice == '2':
            ci = login()
            if ci:
                while True:
                    print ("select your action")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. View Transactions")
                    print("4. Close Account")
                    print("5. Logout")
                    action = input("Enter your choice: ")
                    if action == '1':
                        deposit(ci)
                    elif action == '2':
                        withdraw(ci)
                    elif action == '3':
                        view(ci)
                    elif action == '4':
                        close(ci)
                        break
                    elif action == '5':
                        print("Logged out successfully.")
                        break
                    else:
                        print("please enter a valid choice.")
        elif choice == '3':
            print("Thank you for using ABC Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()

           