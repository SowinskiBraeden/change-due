#!/usr/bin/env python3.11
from customtkinter import set_appearance_mode, set_default_color_theme
from customtkinter import CTk, CTkEntry, CTkButton, CTkLabel, CTkFrame

class Window:
	def __init__(self):
		self.amountDue: float = 0.0
		
		set_appearance_mode("dark")
		set_default_color_theme("dark-blue")

		self.root = CTk()
		self.root.geometry("720x480")

		self.frame = CTkFrame(master=self.root)
		self.frame.pack(pady=20, padx=60, fill="both", expand=True)

		# Static label
		_mainLabel: CTkLabel = CTkLabel(master=self.frame, text="Change Due Calculator")
		_mainLabel.pack(pady=12, padx=10)

		self.entry: CTkEntry = CTkEntry(master=self.frame, placeholder_text="Amount Charged...")
		self.entry.pack(pady=12, padx=10)

		self.invalidLabel = CTkLabel(master=self.frame, text="Not a number", text_color="red")

		calculateButton: CTkButton = CTkButton(master=self.frame, text="Calculate", command=self.calculate)
		calculateButton.pack(pady=12, padx=10)

		self.root.mainloop()

	def _validateInput(func: callable) -> callable:
		def wrapper(self):
			self.invalidLabel.pack_forget()
			try:
				self.amountDue = float(self.entry.get())
			except ValueError:
				self.invalidLabel.pack()
				return
			func(self)

		return wrapper

	@_validateInput
	def calculate(self) -> None:
		print(self.amountDue)

if __name__ == '__main__':
	window = Window()
