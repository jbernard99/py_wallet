import datetime
import tracemalloc
from transaction import Transaction

class Ledger():

	def __init__(self, name):
		self.name = name
		self.transactions = []

	def __str__(self):
		str = (f"			  Ledger : {self.name}\n"
				"			________________________\n")

		for transaction in self.transactions:
			str = str + str(transaction) + "\n"

		str = str + "	_________________________________________________\n\n"
		return (str)

	def add_transaction(self, date, value, desc):
		if value < 0:
			is_neg = True
			value = value * -1
		else:
			is_neg = False
		self.transactions.append(Transaction(date, value, is_neg, desc))

		