from customtkinter import CTkButton

def initializeCurrencyButtons(root, cmd) -> list[CTkButton]:
  return [
    CTkButton(
      master=root, 
      text="$100 Bill", 
      width=152, 
      height=70, 
      font=("Arial", 24, 'bold'), 
      fg_color="Burlywood3", 
      hover_color="Burlywood4",
      command=lambda: cmd(100)
    ),
    
    CTkButton(
      master=root, 
      text="$50 Bill", 
      width=152, 
      height=70, 
      font=("Arial", 24, 'bold'), 
      fg_color="IndianRed3", 
      hover_color="IndianRed4",
      command=lambda: cmd(50)
    ),
    
    CTkButton(
      master=root, 
      text="$20 Bill", 
      width=152, 
      height=70, 
      font=("Arial", 24, 'bold'), 
      fg_color="medium sea green", 
      hover_color="sea green",
      command=lambda: cmd(20)
    ),
    
    CTkButton(
      master=root, 
      text="$10 Bill", 
      width=152, 
      height=70, 
      font=("Arial", 24, 'bold'), 
      fg_color="MediumPurple3", 
      hover_color="MediumPurple4",
      command=lambda: cmd(10)
    ),
    
    CTkButton(
      master=root, 
      text="$5 Bill", 
      width=152, 
      height=70, 
      font=("Arial", 24, 'bold'), 
      fg_color="royal blue", 
      hover_color="dark slate blue",
      command=lambda: cmd(5)
    ),

    CTkButton(
      master=root, 
      text="$2 Coin", 
      width=152, 
      height=70, 
      font=("Arial", 24, 'bold'), 
      fg_color="honeydew4", 
      hover_color="gray37",
      command=lambda: cmd(2)
    ),
    
    CTkButton(
      master=root, 
      text="$1 Coin",
      width=152, 
      height=70, 
      font=("Arial", 24, 'bold'), 
      fg_color="lightgoldenrod4", 
      hover_color="tan4",
      command=lambda: cmd(1)
    ),

    CTkButton(
      master=root, 
      text="Quarter ($0.25)", 
      width=152, 
      height=70, 
      font=("Arial", 19, 'bold'), 
      fg_color="honeydew4", 
      hover_color="gray37",
      command=lambda: cmd(0.25)
    ),
    
    CTkButton(
      master=root, 
      text="Dime ($0.10)", 
      width=152, 
      height=70, 
      font=("Arial", 19, 'bold'), 
      fg_color="honeydew4", 
      hover_color="gray37",
      command=lambda: cmd(0.1)
    ),
    
    CTkButton(
      master=root, 
      text="Nickel ($0.05)", 
      width=152, 
      height=70, 
      font=("Arial", 19, 'bold'), 
      fg_color="honeydew4", 
      hover_color="gray37",
      command=lambda: cmd(0.05)
    ),
    
    CTkButton(
      master=root, 
      text="Penny ($0.01)", 
      width=152, 
      height=70, 
      font=("Arial", 19, 'bold'), 
      fg_color="saddle brown", 
      hover_color="OrangeRed4",
      command=lambda: cmd(0.01)
    ),
  ]
