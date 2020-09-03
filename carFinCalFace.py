"""
MQ MALA

carFinCalFace.py
"""

from graphics import *
from carFinanceCalculator import *

def window(title, width, height):
	"""
	pre: takes title, width, height
	post: returns a window
	"""
	win = GraphWin(title, width, height)
	win.setCoords(0.0,0.0,float(width), float(height))
	
	return win
	
def entry(x,y, text):
	"""
	post: Create entry and get text
	"""
	textbox = Entry(Point(x,y), 10)
	textbox.setText(text)
	
	return textbox
	
def messages(x,y, text):
	"""
	post: return message
	"""
	message = Text(Point(x, y), text)
	return message
	
def calculate(la=0.0, nop=0, air=0.0, p=0.0):
	"""
	pre: takes loan amount, number of payments, annual interest rate, payments
	post: reurns value with no input
	"""
	calculate = CarFinanceCalculator(la, nop, air, p)
	if la == 0.0:
		return calculate.calculateLoanAmount()
	elif nop == 0:
		return calculate.calculateNumberOfPayments()
	elif air == 0.0:
		return calculate.calculateAnnualInterestRate()
	elif p == 0.0:
		return calculate.calculatePaymentAmount()
	else:
		print("Check that you entered 3 pieces of information.")

	
def main():
	# Create window
	title, width, height = "Car finance calculator", 320, 240 
	win = window(title, width, height)
	
	# Message
	x, y, text = width/2, height - 220, "Fill in 3 input box and click on screen."
	prompt = messages(x,y, text).draw(win)	
	
	# draw input boxes
	label = ["Payment Amount?: ", "Annual Interest Rate?: ", "Number of payments?: ", "Loan amount?: "]
	texts = ["0", "4.5", "48", "$32500.00"]
	boxInputs = []
	messagesInputs = []
	add = 40
	start = 60
	for i in range(len(texts)):
		y = start 
		messagesInWin = messages(x-60, y, label[i]).draw(win)
		box = entry(x+80,y,texts[i])
		box.draw(win)
		start += add
		boxInputs.append(box)
		messagesInputs.append(messagesInWin)
	
	# get input and return result
	win.getMouse()
	cal = calculate(float(boxInputs[3].getText()), int(boxInputs[2].getText()), float(boxInputs[1].getText()), float(boxInputs[0].getText()))
	
	# answer
	missing = "There is an error"
	for i in range(len(boxInputs)):
		if float(boxInputs[i].getText()) == 0.0:
			if float(boxInputs[i].getText()) == 0:
				missing = "Payment amount is "
			elif float(boxInputs[i].getText()) == 1:
				missing = "Annual interest rate is "
			elif float(boxInputs[i].getText()) == 2:
				missing = "Number of payments is "
			elif float(boxInputs[i].getText()) == 3:
				missing = "Loan amount is " 
				
	answer = "{0} {1}".format(missing, cal)
	
	# clearing window
	indexNum = 0
	while len(boxInputs) > 0 and indexNum < 4:
		y = start
		boxInputs[indexNum].undraw()
		messagesInputs[indexNum].undraw()
		indexNum+=1
		 
	messages(width/2, height/2, answer).draw(win)
	
	# close window
	prompt.setText("Click to close")
	win.getMouse()
	win.close()	

if __name__ == '__main__':
	main()
