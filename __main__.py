#!/usr/bin/env python3.11
from customtkinter import set_appearance_mode, set_default_color_theme
from customtkinter import CTk, CTkEntry, CTkButton, CTkLabel, CTkFrame
from customtkinter import DISABLED

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

		self.left_frame: CTkFrame = CTkFrame(master=self, width=((self.width / 2) - 20), height=(self.height - 40))
		self.left_frame.grid_propagate(False)
		self.left_frame.grid(row=0, column=0, pady=20, padx=10)

		# Static label
		_mainLabel: CTkLabel = CTkLabel(master=self.left_frame, text="Change Due Calculator")
		_mainLabel.grid(row=0, column=0, pady=12, padx=10)

		charValidation = self.register(self.only_numbers)
		self.entry: CTkEntry = CTkEntry(
			master=self.left_frame,
			placeholder_text="Amount Charged...",
			width=200,
			height=40,
			validate="key",
			validatecommand=(charValidation, '%d', '%s', '%S')
		)
		self.entry.grid(row=1, column=0, pady=12, padx=10)

		# Warning Label
		self.invalidLabel: CTkLabel = CTkLabel(master=self.left_frame, text="Not a Number!", text_color="red", font=("Arial", 24, 'bold'))
		
		calculateButton: CTkButton = CTkButton(master=self.left_frame, text="Calculate", command=self.calculate, width=200, height=50)
		calculateButton.grid(row=2, column=0, pady=12, padx=10)

		self.right_frame: CTkFrame = CTkFrame(master=self, width=((self.width / 2) - 20), height=(self.height - 40))
		self.right_frame.grid_propagate(False)
		self.right_frame.grid(row=0, column=1, pady=20, padx=10)

		self.total: float = 0.0
		self.totalLabel: CTkLabel = CTkLabel(master=self.right_frame, text=f"Total: {self.total}", font=("Arial", 24, 'bold'))
		self.totalLabel.grid(row=0, column=0, pady=12, padx=10)

		self.mainloop()

	def quitApplication(self, event=None) -> None: self.destroy()

	def only_numbers(self, action: int, current: str, char: str) -> bool:
		if action == 0: return True # If delete character
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

if __name__ == '__main__':
	window = Window()
