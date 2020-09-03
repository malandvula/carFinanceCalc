"""
carFinanceCalculatorTest.py
"""
import unittest

from carFinanceCalculator import CarFinanceCalculator

class TestCarFinanceCalculator(unittest.TestCase):
	
	def test_getLoanAmount(self):
		constructor = CarFinanceCalculator(32500.0, 48, 4.5)
		self.assertEqual(constructor.getLoanAmount(), 32500.0, 'Should be 32500.0')
		
	def test_calculatePaymentAmount(self):
		constructor = CarFinanceCalculator(32500.0, 8, 4.5)
		
		self.assertEqual(constructor.calculatePaymentAmount(), 4927.31, 'Should be 4927.31')
	
	def test_calculateLoanAmount(self):
		constructor = CarFinanceCalculator(0, 8, 4.5, 4927.31)
		
		self.assertEqual(constructor.calculateLoanAmount(), 32500.00, 'Should be 32500.00')
		
	def test_calculateNumberOfPayments(self):
		constructor = CarFinanceCalculator(32500.0, 0, 4.5, 4927.31)
		
		self.assertEqual(constructor.calculateNumberOfPayments(), 8, 'Should be 8')
		
	def test_calculateAnnualInterestRate(self):
		constructor = CarFinanceCalculator(32500.0, 8, 0, 4927.31)
		
		self.assertEqual(constructor.calculateAnnualInterestRate(), 4.5, 'Should be 4.5')

if __name__ == '__main__':
	unittest.main()
