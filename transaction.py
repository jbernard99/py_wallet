import datetime

class Transaction():

	def __init__(self, is_neg, value, date, description):
		self.sign = -1 if is_neg == True else 1
		self.value = value * self.sign
		self.date = date
		self.description = description

	def __str__(self):
		return (f"{self.date} | {self.value} | {self.description}\n")
