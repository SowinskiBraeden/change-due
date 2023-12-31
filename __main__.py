#!/usr/bin/env python3.11
from customtkinter import set_appearance_mode, set_default_color_theme
from customtkinter import CTk, CTkEntry, CTkButton, CTkLabel, CTkFrame, CTkSwitch, StringVar, CTkTextbox, END
from currencyButtons import initializeCurrencyButtons
from math import floor

class Window(CTk):
	def __init__(self):
		super().__init__()
		
		set_appearance_mode("dark")
		set_default_color_theme("dark-blue")

		self.width:  int = self.winfo_screenwidth()
		self.height: int = self.winfo_screenheight()
		
		self.title("Change Calculator")
		self.attributes("-fullscreen", True) # Initialize screen as fullscreen
		self.bind("<Escape>", self.quitApplication) # quit application

		# Left frame top half
		self.left_frame: CTkFrame = CTkFrame(
			master=self,
			width=(self.width / 2 - 20),
			height=(self.height / 2 - 40),
			fg_color="gray20"
		)
		self.left_frame.grid_propagate(False)
		self.left_frame.grid(row=0, column=0, pady=20, padx=10, sticky='NW')

		# Static label
		mainLabel: CTkLabel = CTkLabel(
			master=self.left_frame,
			text="Amount Due",
			font=("Arial", 18, 'bold')
		)
		mainLabel.grid(row=0, column=0, pady=12)

		# Calculator frame
		calcFrameWidth: int = (self.width / 2 - 20) / 2 - 15
		calculateFrame: CTkFrame = CTkFrame(
			master=self.left_frame,
			width=calcFrameWidth,
			height=(self.height / 2 - 110),
			fg_color="gray15"
		)
		calculateFrame.grid_propagate(False)
		calculateFrame.grid(pady=(0, 12), padx=(15, 0))

		self.amount = StringVar()
		self.amountBox: CTkEntry = CTkEntry(
			master=calculateFrame,
			width=(calcFrameWidth - 20),
			height=50,
			textvariable=self.amount,
			justify='right',
			font=("Arial", 24, 'bold'),
		)
		self.amountBox.configure(state="disabled")
		self.amountBox.grid(row=0, column=0, pady=12, padx=10)
		
		# Calculator buttons frame
		calculateButtonFrame: CTkFrame = CTkFrame(
			master=calculateFrame,
			width=(calcFrameWidth - 20),
			height=(self.height / 2 - 196),
			fg_color="gray15"
		)
		calculateButtonFrame.grid_propagate(False)
		calculateButtonFrame.grid(row=1, column=0, pady=(0, 12), padx=10)

		buttons: list[CTkButton] = [CTkButton(
			master=calculateButtonFrame,
			text=str(i),
			width=(calcFrameWidth - 20) / 3 - 8,
			height=(self.height / 2 - 196) / 4 - 12,
			font=("Arial", 24, 'bold'),
		) for i in range(0, 10)]

		buttons[0].grid(row=3, column=1, padx=(0, 12), pady=(12, 0))
		i = 1
		for r in range(3):
			for c in range(3):
				buttons[i].grid(row=r, column=c, padx=(0, 12), pady=(12, 0))
				i += 1

		# I have already tried multiple ways to define the command in either the 
		# buttons list comprehension or in the button layout loop, but the lambda
		# function always passes 'i' as the last number (9) so all buttons have the
		# value 9 passed to self.amountConcat
		# So this is the solution >:(
		buttons[0]._command = lambda: self.amountConcat('0')
		buttons[1]._command = lambda: self.amountConcat('1')
		buttons[2]._command = lambda: self.amountConcat('2')
		buttons[3]._command = lambda: self.amountConcat('3')
		buttons[4]._command = lambda: self.amountConcat('4')
		buttons[5]._command = lambda: self.amountConcat('5')
		buttons[6]._command = lambda: self.amountConcat('6')
		buttons[7]._command = lambda: self.amountConcat('7')
		buttons[8]._command = lambda: self.amountConcat('8')
		buttons[9]._command = lambda: self.amountConcat('9')

		decimalButton: CTkButton = CTkButton(
			master=calculateButtonFrame,
			text='.',
			command=lambda: self.amountConcat('.'),
			width=(calcFrameWidth - 20) / 3 - 8,
			height=(self.height / 2 - 196) / 4 - 12,
			font=("Arial", 24, 'bold'), 
		)
		decimalButton.grid(row=3, column=0, padx=(0, 12), pady=(12, 0))

		deleteButton: CTkButton = CTkButton(
			master=calculateButtonFrame,
			text='⌫',
			command=lambda: self.amountConcat('⌫'),
			width=(calcFrameWidth - 20) / 3 - 8,
			height=(self.height / 2 - 196) / 4 - 12,
			font=("Arial", 24, 'bold'), 
		)
		deleteButton.grid(row=3, column=2, padx=(0, 12), pady=(12, 0))

		# General action buttons frame, (next to calculator frame)
		actionFrame: CTkFrame = CTkFrame(
			master=self.left_frame,
			width=calcFrameWidth,
			height=(self.height / 2 - 110),
			fg_color="gray20"
		)
		actionFrame.grid_propagate(False)
		actionFrame.grid(row=1, column=1, pady=(0, 12), padx=(15, 0))

		calculateButton: CTkButton = CTkButton(
			master=actionFrame,
			text="Calculate",
			command=self.calculate,
			width=200, height=50
		)
		calculateButton.grid(row=1, column=2, pady=12, padx=10)

		clearButton: CTkButton = CTkButton(
			master=actionFrame,
			text="Reset",
			command=self.clear,
			width=200,
			height=50
		)
		clearButton.grid(row=1, column=3, pady=12, padx=10)
		
		self.warningLabel: CTkLabel = CTkLabel(
			master=actionFrame,
			text="Not enough cash provided.\nAdd to total paid below.",
			text_color="red",
			font=("Arial", 14, 'bold')
		)

		# Left frame bottom
		self.left_frame_bottom: CTkFrame = CTkFrame(
			master=self,
			width=(self.width / 2 - 20),
			height=(self.height / 2 - 40),
			fg_color="gray20"
		)
		self.left_frame_bottom.grid_propagate(False)
		self.left_frame_bottom.grid(row=0, column=0, pady=20, padx=10, sticky='SW')

		paidWithLabel: CTkLabel = CTkLabel(
			master=self.left_frame_bottom,
			text="Paid With",
			font=("Arial", 18, 'bold')
		)
		paidWithLabel.grid(row=0, column=0, pady=(16, 0), padx=10)

		# Options
		self.mode: bool = True # True == ADD, False == SUBTRACT
		self.modeLabel: CTkLabel = CTkLabel(
			master=self.left_frame_bottom,
			text=f"Mode: {'ADD' if self.mode else 'SUBTRACT'}",
			font=("Arial", 18, 'bold')
		)
		self.modeLabel.grid(row=0, column=4, pady=(16, 0), padx=(50, 10))
		
		self.modeSelect: CTkSwitch = CTkSwitch(
			master=self.left_frame_bottom,
			text="Mode",
			command=self.updateMode
		)
		self.modeSelect.grid(row=0, column=3, pady=(16, 0), padx=(50, 10))

		self.total: float = 0.0
		self.totalLabel: CTkLabel = CTkLabel(
			master=self.left_frame_bottom,
			text=f"Total: {self.total}",
			font=("Arial", 18, 'bold')
		)
		self.totalLabel.grid(row=0, column=2, pady=(16, 0), padx=10, sticky='NE')

		# input Buttons
		currencyButtons: list[CTkButton] = initializeCurrencyButtons(self.left_frame_bottom, self.sum)

		r, c = 1, 0
		for button in currencyButtons:
			button.grid(row=r, column=c, pady=12, padx=10)
			if c < 3: c += 1
			else: c = 0; r += 1

		clearTotalButtons: CTkButton = CTkButton(
			master=self.left_frame_bottom,
			text="Clear\nTotal",
			font=("Arial", 20, 'bold'), 
      fg_color="IndianRed3", 
      hover_color="IndianRed4",
			command=self.clearTotal,
			width=152, 
      height=70,
		)
		clearTotalButtons.grid(row=3, column=3, pady=12, padx=10)

		# Right frame for output
		self.right_frame: CTkFrame = CTkFrame(
			master=self,
			width=(self.width / 2 - 20),
			height=(self.height - 40),
			fg_color="gray20"
		)
		self.right_frame.grid_propagate(False)
		self.right_frame.grid(row=0, column=1, pady=20, padx=10)

		returnAmountLabel: CTkLabel = CTkLabel(
			master=self.right_frame,
			text="Return Amount:",
			font=("Arial", 32, 'bold')
		)
		returnAmountLabel.grid(row=0, column=0, pady=20, padx=30)

		self.returnAmountBox: CTkTextbox = CTkTextbox(
			master=self.right_frame,
			width=(self.width / 2 - 60),
			height=(self.height - 150),
			font=("Arial", 24, 'bold'),
			fg_color="gray15"
		)
		self.returnAmountBox.configure(state="disabled")
		self.returnAmountBox.grid(row=1, column=0, padx=(20, 0))

		self.mainloop()

	def updateMode(self) -> None:
		self.mode = not self.mode
		self.modeLabel.configure(text=f"Mode: {'ADD' if self.mode else 'SUBTRACT'}")

	def quitApplication(self, event=None) -> None: self.destroy()

	def calculate(self) -> None:
		self.returnAmountBox.configure(state="normal")
		self.returnAmountBox.delete('1.0', END)
		self.warningLabel.grid_forget()
		amountDue:    float = float(self.amount.get())
		returnAmount: float = round(self.total - amountDue, 2)
		print(self.total, amountDue, returnAmount)
		if returnAmount < 0:
			self.warningLabel.grid(row=2, column=2, pady=12, padx=10)
			return
		
		denominationsStrings: dict[float: str] = {
			100.0: '$100 BillX',
			50.0:  '$50 BillX',
			20.0:  '$20 BillX',
			10.0:  '$10 BillX',
			5.0:   '$5 BillX',
			2.0:   '$2 CoinX',
			1.0:   '$1 CoinX',
			0.25:  'QuarterX ($0.25)',
			0.10:  'DimeX ($0.10)',
			0.05:  'NickelX ($0.05)',
			0.01:  'PennX ($0.01)'
		}
		returnAmountString: str = ""
		for d in denominationsStrings:
			due = floor(returnAmount / d)
			returnAmount -= due * d
			denominationEnd = "s" if due > 1 else ""
			if d == 0.01: denominationEnd = "ies" if due > 1 else "y"
			if due > 0: returnAmountString += f"x{due} {denominationsStrings[d].replace('X', denominationEnd)}\n"
			if returnAmount == 0: break

		returnAmountString += f"Total Change: ${round(self.total - amountDue, 2)}"

		self.returnAmountBox.insert('1.0', returnAmountString)
		self.returnAmountBox.configure(state="disabled")

	def sum(self, value: float) -> None:
		self.warningLabel.grid_forget()
		if self.total == 0 and not self.mode: return
		self.total += value * (1 if self.mode else -1)
		if self.total < 0: self.total = 0
		self.totalLabel.configure(text=f"Total: {self.total:.2f}")

	def amountConcat(self, value: str) -> None:
		current: str = self.amount.get()
		if value == "⌫": current = current[:-1]
		elif len(current) == 0 and value == "0": return
		elif '.' in current and value == '.': return
		elif '.' in current and len(current.split('.')[1]) == 2: return
		else: current += value
		self.amount.set(current)

	def clear(self) -> None:
		self.amount.set("")
		self.total: float = 0.0
		self.totalLabel.configure(text=f"Total: {self.total:.2f}")
		self.returnAmountBox.configure(state="normal")
		self.returnAmountBox.delete('1.0', END)
		self.returnAmountBox.configure(state="disabled")
	
	def clearTotal(self) -> None:
		self.total: float = 0.0
		self.totalLabel.configure(text=f"Total: {self.total:.2f}")

if __name__ == '__main__':
	window = Window()
