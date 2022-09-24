from wallet import Wallet
from py_menu.menu import Menu

menu = Menu()
wlt = Wallet()

menu.set_header("--------------------  Julio's wallet -------------------------")
menu.set_footer("--------------------------------------------------------------")

main_menu = [
			"Add deposit transaction",
			"Add withdraw transaction", 
			"Check an account balance", 
			"Check total balance", 
			"Create new account",
			"Quit the program"
			]

def add_deposit_transaction():
	pass

def add_withdraw_transaction():
	pass

def check_account_balance(name):
	pass

def check_wallet_balance():
	pass

def create_account():
	name = menu.print_menu("What is the name of this account?", "str")
	value = menu.print_menu("What is the value of this account?", "float")
	initial_value = menu.print_menu(("What is the initial value of the account?\n"
					"(The value before any transaction you want to add in the program)"),
					"float")
	wlt.create_account(name.lower(), value, initial_value)
	menu.print_transition(f"Account {name} added with success!")

def quit_wallet():
	pass

while True:
	choice = menu.print_menu("What do you want to do?", "int", choice_list=main_menu)
	if (choice == 5):
		create_account()
