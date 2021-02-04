import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):  # The MainWindow class will hold all the visual elements. QWidget is just an empty container.
	operators_list = ["+", "-", "/", "*"]

	def __init__(self):
		"""
		All the elements of the GUI are coded inside this init function.
		Some elements like the window title don't need a location
		However, other elements like a button or a label do need locations!
		"""
		super().__init__()  # Inherits its parent class' dunder init method
		self.setWindowTitle("Calculator")  # This changes the title of the main window
		self.setLayout(qtw.QVBoxLayout())  # Creates a QVBox layout, suitable for a calculator. There are also other layouts.
		# btn1 = qtw.QPushButton("Test")  # Creates a button which can be pressed with the text Test.
		# self.layout().addWidget(btn1)  # This button was added to the layout of the main window.
		self.keypad()

		self.show()  # Displays all the elements of the object created from the MainWindow class

		self.temp_nums = []
		self.fin_nums = []


	def keypad(self):
		container = qtw.QWidget()  # Creates an empty container to house all of the GUI elements
		container.setLayout(qtw.QGridLayout())  # Sets the layout of the container to a grid layout

		# Buttons
		self.result_field = qtw.QLineEdit()  # This displays the text or the output, the self is added to attach the result field to the object itself and make it accessible from outside of the method
		btn_result = qtw.QPushButton("Enter", clicked = self.func_result)
		btn_clear = qtw.QPushButton("Clear", clicked = self.clear_calc)
		btn_9 = qtw.QPushButton("9", clicked = lambda:self.num_press("9"))
		btn_8 = qtw.QPushButton("8", clicked = lambda:self.num_press("8"))
		btn_7 = qtw.QPushButton("7", clicked = lambda:self.num_press("7"))
		btn_6 = qtw.QPushButton("6", clicked = lambda:self.num_press("6"))
		btn_5 = qtw.QPushButton("5", clicked = lambda:self.num_press("5"))
		btn_4 = qtw.QPushButton("4", clicked = lambda:self.num_press("4"))
		btn_3 = qtw.QPushButton("3", clicked = lambda:self.num_press("3"))
		btn_2 = qtw.QPushButton("2", clicked = lambda:self.num_press("2"))
		btn_1 = qtw.QPushButton("1", clicked = lambda:self.num_press("1"))
		btn_0 = qtw.QPushButton("0", clicked = lambda:self.num_press("0"))
		btn_dec = qtw.QPushButton(".", clicked = lambda:self.num_press("."))
		btn_plus = qtw.QPushButton("+", clicked = lambda:self.func_press("+"))
		btn_minus = qtw.QPushButton("-", clicked = lambda:self.func_press("-"))
		btn_mult = qtw.QPushButton("*", clicked = lambda:self.func_press("*"))
		btn_divd = qtw.QPushButton("/", clicked = lambda:self.func_press("/"))
		btn_pow = qtw.QPushButton("^", clicked = lambda:self.func_press("**"))


		# Adding the created buttons to the layout
		container.layout().addWidget(self.result_field, 0, 0, 1, 4)  # Adds the specific widget, by its variable name, to the layout. The 2nd and 3rd elements are its positions, x and y (top left is 0, 0). The last two elements are its size in rows and columns
		container.layout().addWidget(btn_result, 1, 0, 1, 2)
		container.layout().addWidget(btn_clear, 1, 2, 1, 2)
		container.layout().addWidget(btn_9, 2, 0)
		container.layout().addWidget(btn_8, 2, 1)
		container.layout().addWidget(btn_7, 2, 2)
		container.layout().addWidget(btn_plus, 2, 3)
		container.layout().addWidget(btn_6, 3, 0)
		container.layout().addWidget(btn_5, 3, 1)
		container.layout().addWidget(btn_4, 3, 2)
		container.layout().addWidget(btn_minus, 3, 3)
		container.layout().addWidget(btn_3, 4, 0)
		container.layout().addWidget(btn_2, 4, 1)
		container.layout().addWidget(btn_1, 4, 2)
		container.layout().addWidget(btn_mult, 4, 3)
		container.layout().addWidget(btn_0, 5, 0)
		container.layout().addWidget(btn_dec, 5, 1)
		container.layout().addWidget(btn_pow, 5, 2)
		container.layout().addWidget(btn_divd, 5, 3)

		self.layout().addWidget(container)  # This actually puts the widgets (elements) on the main window
		
	def num_press(self, key_number):
		"""
		Function which stores the numbers pressed into the calculator
		:param key_number: The number pressed
		"""
		if "=" in self.result_field.text():  # Automatically clears the calculator screen with new input after final output
			self.clear_calc()
		self.temp_nums.append(key_number)  # Stores each input number into a list which is then joined into a string
		temp_string = ''.join(self.temp_nums)
		if self.fin_nums:  # Checks if the secondary input is already empty
			self.result_field.setText(''.join(self.fin_nums) + temp_string)
		else:
			self.result_field.setText(temp_string)

	def func_press(self, operator):
		"""
		Function which stores the operator pressed into the calculator and initiates secondary input
		:param operator: The operator pressed
		"""
		temp_string = ''.join(self.temp_nums)
		self.fin_nums.append(temp_string)
		self.fin_nums.append(operator)
		self.temp_nums = []
		self.result_field.setText(''.join(self.fin_nums))

	def func_result(self):
		"""
		Function which calculates and displays the result
		"""
		fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
		if not fin_string:  # Prevents a crash where the user tries to calculate with no input
			self.result_field.setText("ERROR: No input!")
		elif fin_string[-1] in MainWindow.operators_list:  # Prevents a crash where the user tries to calculate with no secondary input
			self.result_field.setText("ERROR: No secondary input!")
		else:	
			result_string = eval(fin_string)  # This calculates the string as if it's code
			fin_string += "="
			fin_string += str(result_string)
			self.result_field.setText(fin_string)

	def clear_calc(self):
		"""
		Function which clears all the inputs of the calculator
		"""
		self.result_field.clear()
		self.temp_nums = []
		self.fin_nums = []


app = qtw.QApplication([])  # Creates the QApplication instance which keeps track of all of the things in the 'background'

mw = MainWindow()  # Creates an instance of the window class
app.setStyle(qtw.QStyleFactory.create("Fusion"))  # Changes the styling of the widgets and the layout
app.exec_()  # This tells python to run the application