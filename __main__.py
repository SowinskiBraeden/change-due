#!/usr/bin/env python3.11
from customtkinter import set_appearance_mode, set_default_color_theme
from customtkinter import CTk, CTkEntry, CTkButton, CTkLabel, CTkFrame, CTkSwitch, StringVar
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
		mainLabel.grid(row=0, column=0, pady=12)

		calculateFrame: CTkFrame = CTkFrame(master=self.left_frame, width=((self.width / 2 - 20) / 2), height=(self.height / 2 - 110), fg_color="gray15")
		calculateFrame.grid_propagate(False)
		calculateFrame.grid(pady=(0, 12), padx=15)

		self.amount = StringVar()
		self.amountBox: CTkEntry = CTkEntry(
			master=calculateFrame,
			width=(((self.width / 2 - 20) / 2) - 24),
			height=50,
			textvariable=self.amount
		)
		self.amountBox.grid(row=0, column=0, pady=12, padx=10)
		
		calculateButtonFrame: CTkFrame = CTkFrame(master=calculateFrame, width=(((self.width / 2 - 20) / 2) - 24), height=(self.height / 2 - 196), fg_color="gray15")
		calculateButtonFrame.grid_propagate(False)
		calculateButtonFrame.grid(row=1, column=0, pady=(0, 12), padx=10)

		buttons: list[CTkButton] = [CTkButton(
			master=calculateButtonFrame,
			text=f'{i}',
			command=lambda: self.amountSum(f'{i}'),
			width=(((self.width / 2 - 20) / 2) - 48) / 3,
			height=(self.height / 2 - 196) / 4 - 12,
		) for i in range(0, 10)]

		buttons[0].grid(row=3, column=1, padx=(0, 12), pady=(12, 0))
		i = 1
		for r in range(3):
			for c in range(3):
				buttons[i].grid(row=r, column=c, padx=(0, 12), pady=(12, 0))
				i += 1

		# Warning Label
		self.invalidLabel: CTkLabel = CTkLabel(master=self.left_frame, text="Not a Number!", text_color="red", font=("Arial", 20, 'bold'))
		
		calculateButton: CTkButton = CTkButton(master=self.left_frame, text="Calculate", command=self.calculate, width=200, height=50)
		calculateButton.grid(row=1, column=2, pady=12, padx=10)

		clearButton: CTkButton = CTkButton(master=self.left_frame, text="Clear", command=self.clear, width=200, height=50)
		clearButton.grid(row=1, column=3, pady=12, padx=10)
		
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

	def calculate(self) -> None:
		print(self.amountDue)

	def sum(self, value: float) -> None:
		if self.total == 0 and not self.mode: return
		self.total += value * (1 if self.mode else -1)
		if self.total < 0: self.total = 0
		self.totalLabel.configure(text=f"Total: {self.total:.2f}")

	def amountSum(self, value: str) -> None:
		pass

	def clear(self) -> None:
		pass

if __name__ == '__main__':
	window = Window()
