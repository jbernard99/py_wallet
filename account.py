from ledger import Ledger

class Account():

	def __init__(self, name, value, initial_value):
		self.name = name
		self.value = value
		self.initial_value = initial_value
		self.ledger = Ledger(name)

	def add_value(self, value):
		self.value = self.value + value

	def remove_value(self, value):
		self.value = self.value - value