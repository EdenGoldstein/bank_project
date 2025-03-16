import random

class Bank:
    
    
    
    def __init__(self, bank_name: str):
        self.max_account_num = 10000
        self.account_number = 0
        self.name = ''
        self.account_balance = 0.0
        self.account_type = ''
        self.bank_name = bank_name
        self.accounts = {}
        
        
    
        
    def create_account(self, account_name, account_type):
        if len(self.accounts) == self.max_account_num:
            return
        
        random_account_number = random.randint(1, self.max_account_num)
        while random_account_number in self.accounts:
            random_account_number = random.randint(1, self.max_account_num)
        costumer_details = [account_name, 0, account_type]

        self.accounts[random_account_number] = costumer_details
        return  random_account_number
    
    def authenticate(self, user_name, account_number):
        account_number = int(account_number)
        for account in self.accounts:
            if account_number == account:
                if user_name == self.accounts[account][0]:
                    self.name = user_name
                    self.account_number = account_number
                    return True
        else:
            return False
    
    def withdraw(self, withdraw_amount):
        withdraw_amount = float(withdraw_amount)
        if withdraw_amount > self.account_balance:
            return
        self.account_balance = self.account_balance - withdraw_amount
        self.accounts[self.account_number][1] -= withdraw_amount
        return self.account_balance
    
    def deposit(self, deposit_ammount):
        deposit_ammount = float(deposit_ammount)
        self.accounts[self.account_number][1] += deposit_ammount
        self.account_balance = self.account_balance + deposit_ammount
        return self.account_balance
    
        
    def check_balance(self):
        
        balance = self.accounts[self.account_number][1]
        return balance
    
    
    
    def is_logged_in(self):
        if self.name != '':
            return True
        return False
  
    def get_logged_in_user_name(self):
        return self.name

    def logout(self):
        self.account_number = 0
        self.name = ''
        self.account_balance = 0.0
        self.account_type = ''
        
  
  
deutsche_bank = Bank('deutsche bank')          
        
print(f'Welcome to {deutsche_bank.bank_name}') 

while True:
    if deutsche_bank.is_logged_in():
        user_name = deutsche_bank.get_logged_in_user_name()             
        print(f'Welcome, {user_name}')
            
        print('Enter the number of the action you want to perform')
        selected_action = input('1.Withdraw\n2.Deposit\n3.Check balance\n4.Logout: ')
        selected_action = int(selected_action)
        if selected_action == 1:
            withdraw_amount = input('Enter the amount you want to withdraw: ')
            balance_after_withdraw = deutsche_bank.withdraw(withdraw_amount)
            print(f'Your account balance after withdraw is: {balance_after_withdraw}')
            
        elif selected_action == 2:
            deposit_amount = input('Enter the amount you want to deposit: ')
            balance_after_deposit = deutsche_bank.deposit(deposit_amount)
            print(f'Your account balance after deposit is: {balance_after_deposit}')
            
            
            
        elif selected_action == 3:
            balance = deutsche_bank.check_balance()
            print(f'Your account balance is: {balance}')
        else:
            deutsche_bank.logout()
        continue
        
    selected_action = input('Enter (R) if you want to register or (l) if you want to login: ')
    if selected_action == 'l':

        user_name = input('enter a user name: ')
        account_number = input('enter an account number: ')
        is_auth = deutsche_bank.authenticate(user_name, account_number)
        if is_auth:
            print('Logged in successfully!')
        else:
            print('Unknown user name or account number')


    if selected_action == 'R':
        new_user_name = input('enter a user name: ')
        new_account_type = input('enter your account type: ')
        account_number = deutsche_bank.create_account(new_user_name, new_account_type)
        print(f'Registration successful, your account number is: {account_number}')