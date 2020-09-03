"""
MQ MALA

carFinanceCalculator.py
"""

import math

class CarFinanceCalculator:
	"""
	Take in 3 parameters from following list [loan amount, number of payments, annual interest rate, payment amount] and return the 4th.
	"""
	
	def __init__(self, loanAmount=0.0, numberOfPayments=0, annualInterestRate=0.0, paymentAmount=0):
		self.loanAmount = loanAmount
		self.numberOfPayments = numberOfPayments
		self.annualInterestRate = annualInterestRate/100 # divide by 100 for demical%
		self.paymentAmount = paymentAmount
		self.interest = 100.0001
		
	def getLoanAmount(self):
		"""
		post: return loan amount
		"""
		return round(self.loanAmount)
		
	def getNumberOfPayments(self):
		"""
		post: return number of payments
		"""
		return round(self.numberOfPayments)
		
	def getAnnualInterestRate(self):
		"""
		post: return annual interest rate
		"""
		return round(self.annualInterestRate, 5)
		
	def getPaymentAmount(self):
		"""
		post: return payment amount
		"""
		return round(self.paymentAmount,2)
		
	def calculatePaymentAmount(self):
		"""
		pv = principal or loan amount
		r = annual interest rate
		p = payment amount
		n = number of periods 
		
		post: calculate paymnent amount
		"""
		self.paymentAmount = ((self.annualInterestRate * self.loanAmount)/(1-(1+self.annualInterestRate)**(-self.numberOfPayments)))
		
		return self.getPaymentAmount()
		
	def calculateLoanAmount(self):
		"""
		post: calculate loan amount
		"""
		self.loanAmount = (self.paymentAmount * (1-(1+self.annualInterestRate)**(-self.numberOfPayments))/self.annualInterestRate)
		
		return self.getLoanAmount()
		
	def calculateAnnualInterestRate(self):
		"""
		post: calculate Annual insterest rate
		"""
		PAYMENT = self.paymentAmount
		while self.interest >= 0:
			self.annualInterestRate = self.interest
			if PAYMENT == self.calculatePaymentAmount():
				return round((self.interest*100),1)
			else:
				self.interest -= 0.0001
		return -1.0
		
	def calculateNumberOfPayments(self):
		"""
		post: calculate number of payments
		"""
		x = math.log(self.paymentAmount/((-self.loanAmount*self.annualInterestRate)+ self.paymentAmount))
		y = math.log(self.annualInterestRate + 1)
		self.numberOfPayments = x/y
		
		return self.getNumberOfPayments()
			
