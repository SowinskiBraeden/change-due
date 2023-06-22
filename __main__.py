#!/usr/bin/env python3.11
from customtkinter import set_appearance_mode, set_default_color_theme
from customtkinter import CTk, CTkEntry, CTkButton, CTkLabel, CTkFrame, CTkSwitch
from currencyButtons import initializeCurrencyButtons

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

		self.amountDue: float = 0.0

		self.left_frame: CTkFrame = CTkFrame(master=self, width=(self.width / 2 - 20), height=(self.height / 2 - 40), fg_color="gray20")
		self.left_frame.grid_propagate(False)
		self.left_frame.grid(row=0, column=0, pady=20, padx=10, sticky='NW')

		# Static label
		mainLabel: CTkLabel = CTkLabel(master=self.left_frame, text="Change Due Calculator", font=("Arial", 18, 'bold'))
		mainLabel.grid(row=0, column=0, pady=12, padx=10)

		charValidation = self.register(self.only_numbers)
		self.entry: CTkEntry = CTkEntry(
			master=self.left_frame,
			width=200,
			height=40,
			validate="key",
			validatecommand=(charValidation, '%d', '%s', '%S'),
			placeholder_text="Amount Charged..."
		)
		self.entry.grid(row=1, column=0, pady=12, padx=10)
		self.entry.insert(0, 'Amount Charged...')

		# Warning Label
		self.invalidLabel: CTkLabel = CTkLabel(master=self.left_frame, text="Not a Number!", text_color="red", font=("Arial", 20, 'bold'))
		
		calculateButton: CTkButton = CTkButton(master=self.left_frame, text="Calculate", command=self.calculate, width=200, height=50)
		calculateButton.grid(row=2, column=0, pady=12, padx=10)

		self.left_frame_bottom: CTkFrame = CTkFrame(master=self, width=(self.width / 2 - 20), height=(self.height / 2 - 40), fg_color="gray20")
		self.left_frame_bottom.grid_propagate(False)
		self.left_frame_bottom.grid(row=0, column=0, pady=20, padx=10, sticky='SW')

		paidWithLabel: CTkLabel = CTkLabel(master=self.left_frame_bottom, text="Paid With", font=("Arial", 18, 'bold'))
		paidWithLabel.grid(row=0, column=0, pady=(16, 0), padx=10)

		self.mode: bool = True # True == ADD, False == SUBTRACT
		self.modeLabel: CTkLabel = CTkLabel(master=self.left_frame_bottom, text=f"Mode: {'ADD' if self.mode else 'SUBTRACT'}", font=("Arial", 18, 'bold'))
		self.modeLabel.grid(row=0, column=4, pady=(16, 0), padx=(50, 10), sticky='NE')
		
		self.modeSelect: CTkSwitch = CTkSwitch(master=self.left_frame_bottom, text="Mode", command=self.updateMode)
		self.modeSelect.grid(row=0, column=3, pady=(16, 0), padx=(50, 10), sticky='NE')

		self.total: float = 0.0
		self.totalLabel: CTkLabel = CTkLabel(master=self.left_frame_bottom, text=f"Total: {self.total}", font=("Arial", 18, 'bold'))
		self.totalLabel.grid(row=0, column=2, pady=(16, 0), padx=10, sticky='NE')

		currencyButtons: list[CTkButton] = initializeCurrencyButtons(self.left_frame_bottom, self.sum)

		r, c = 1, 0
		for button in currencyButtons:
			button.grid(row=r, column=c, pady=12, padx=10)
			if c < 3: c += 1
			else: c = 0; r += 1

		self.right_frame: CTkFrame = CTkFrame(master=self, width=(self.width / 2 - 20), height=(self.height - 40), fg_color="gray20")
		self.right_frame.grid_propagate(False)
		self.right_frame.grid(row=0, column=1, pady=20, padx=10)

		self.mainloop()

	def updateMode(self) -> None:
		self.mode = not self.mode
		self.modeLabel.configure(text=f"Mode: {'ADD' if self.mode else 'SUBTRACT'}")

	def quitApplication(self, event=None) -> None: self.destroy()

	def only_numbers(self, action: str, current: str, char: str) -> bool:
		if int(action) == 0: return True # If delete character
		if '.' in current and len(current.split('.')[1]) == 2: return False # prevent more than 2 decimal
		return (char.isdigit() or char == ".") # only allow digits and decimal

	def _validateInput(func: callable) -> callable:
		def wrapper(self):
			self.invalidLabel.pack_forget()
			try:
				self.amountDue = float(self.entry.get())
			except ValueError:
				self.invalidLabel.grid(row=3, column=0)
				return
			func(self)

		return wrapper

	@_validateInput
	def calculate(self) -> None:
		print(self.amountDue)

	def sum(self, value: float) -> None:
		if self.total == 0 and not self.mode: return
		self.total += value * (1 if self.mode else -1)
		if self.total < 0: self.total = 0
		self.totalLabel.configure(text=f"Total: {self.total:.2f}")

if __name__ == '__main__':
	window = Window()
