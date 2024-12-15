#list of foods
foods = [
    "Hotdog",
    "Itlog",
    "Chicken",
    "Sisig",
    "Tapa"
]

#price of foods
price = [
    35,
    25,
    75,
    75,
    75
]

#Function to display menu
def display_menu():
    print("Menu:")
    for i in range(5):
        print(f"{i+1}. ${price[i]} {foods[i]}")

#Function that prompts user to choose item
def choose_item():
    global choose 
    choose = int(input("Choose an item: "))

#Function that displays the total of the selected item
def calculate_total():
    print(f"Total cost: ${price[choose-1]}")

#Function for payment processing
def payment_process():
    balance = float(input("Enter the amount of cash: "))
    #loop that repeatedly ask for payment if the balance is less than the price of the selected item
    while balance < price[choose-1]:
        print("Insufficient amount. Please provide more cash.")
        balance = float(input("Enter the amount of cash: "))
    #Display the change
    else:
        print("Valid amount")
        change = balance - price[choose-1]
        print("Change:", change)

display_menu()
choose_item()
#Checks if the selected item is valid before calculating the total and processing the payment
if choose != 0 or choose > len(foods):
    calculate_total()
    payment_process()