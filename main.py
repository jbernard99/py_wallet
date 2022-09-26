from wallet import Wallet
from py_menu.menu import Menu

menu = Menu()
wlt = Wallet()

menu.set_header("--------------------  Julio's wallet -------------------------")
menu.set_footer("--------------------------------------------------------------")

main_menu = [
			"[ + ] Deposit",
			"[ - ] Withdraw", 
			"Balance by Account",
			"Transactions by Account",
			"Wallet Balance", 
			"Create new account",
			"Quit the program"
			]

def get_acc():
	acc = menu.print_menu("What account?", "int", choice_list=wlt.get_accounts())
	return (wlt.get_accounts()[acc - 1])

def get_t():
	date = menu.print_menu("When was this transaction done?\n(Date format : DDMMYYY)\n", "str")
	desc = menu.print_menu("Describe this transaction : \n", "str")
	value = menu.print_menu("How much was this transaction?\n	", "float")
	return (date, value, desc)

def add_deposit_transaction():
	acc = get_acc()
	date, value, desc = get_t()
	wlt.add_transaction(wlt.get_accounts()[acc - 1], date, value, 1, desc)

def add_withdraw_transaction():
	acc = get_acc()
	date, value, desc = get_t()
	wlt.add_transaction(wlt.get_accounts()[acc - 1], date, value, 0, desc)

def check_account_balance():
	acc = get_acc()
	acc.update_account()
	menu.print_transition(f"Account {acc.name} : \n 	 Initial Value : {acc.initial_value}\n  	Current Value : {acc.value}")

def check_account_transactions():
	acc = get_acc()
	txt = f"Transactions of {acc.name} : \n\n"
	for t in acc.ledger.transactions:
		txt = txt + "	->  " + str(t) + "\n"
	menu.print_transition(txt)

def check_wallet_balance():
	acc_value = wlt.get_wallet_balance()
	txt = "Wallet total balance : \n\n"
	for acc in wlt.accounts:
		txt = txt + f"	{acc.name} : {acc.value}\n"
	txt = txt + f"\nTotal balance: {acc_value}\n"
	menu.print_transition(txt)

def create_account():
	name = menu.print_menu("What is the name of this account?", "str")
	initial_value = menu.print_menu(("What is the initial value of the account?\n"
					"(The value before any transaction you want to add in the program)"),
					"float")
	wlt.create_account(name.lower(), initial_value)
	menu.print_transition(f"Account {name} added with success!")

def quit_wallet():
	quit()

while True:
	choice = menu.print_menu("What do you want to do?", "int", choice_list=main_menu)
	if (choice == 1):
		add_deposit_transaction()
	elif (choice == 2):
		add_withdraw_transaction()
	elif (choice == 3):
		check_account_balance()
	elif (choice == 4):
		check_account_transactions()
	elif (choice == 5):
		check_wallet_balance()
	elif (choice == 6):
		create_account()
	elif (choice == 7):
		quit_wallet()
