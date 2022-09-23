from wallet import Wallet
from menu import Menu

menu = Menu()
wlt = Wallet()

menu.set_header("--------------------  Julio's wallet -------------------------")
menu.set_footer("--------------------------------------------------------------")

main_menu = [
			"Deposit", "Withdraw", 
			"Check an account balance", 
			"Check total balance", 
			"Create new account",
			"Quit the program"
			]

def create_account():
	name = menu.print_menu("What is the name of this account?", "str")
	value = menu.print_menu("What is the value of this account?", "float")
	initial_value = menu.print_menu(("What is the initial value of the account?\n"
					"(The value before any transaction you want to add in the program)"),
					"float")
	wlt.create_account(name.lower(), value, initial_value)
	menu.print_transition("Account added with success!")

while True:
	choice = menu.print_menu("What do you want to do?", "int", choice_list=main_menu)
	if (choice == 5):
		create_account()
