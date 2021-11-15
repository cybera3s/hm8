from models import Passenger, SingleTrip, CreditCard, TimeCredit
from metro.exceptions import RegisterError, BankAccountError, AuthenticationError


def main_menu():
    """main menu function"""
    while True:
        print("1. register new Passenger")
        print("2. manage bank account")
        print("3. register new trip")
        print("4. admin panel")
        print("5. exit")

        option = input(">>> ")

        if option == "1":

            register_menu()

        elif option == "2":

            unique_id = int(input("enter your unique id: "))
            try:
                passenger = Passenger.authenticate(unique_id)
                manage_bank_account_menu(passenger)

            except (AuthenticationError, BankAccountError) as e:
                print(e)

        elif option == "3":

            unique_id = int(input("enter your unique id: "))
            try:
                passenger = Passenger.authenticate(unique_id)
                card_menu(passenger)
            except (AuthenticationError, BankAccountError) as e:
                print(e)

        elif option == "4":

            # todo: admin panel section
            pass

        elif option == "5":

            # todo: exit
            exit()

        else:
            print("wrong option, try again")


def register_menu():
    """register new Passenger"""
    fullname = input("enter your fullname : ")
    phone_number = input("enter your phone number : ")
    email = input("enter your email(optional): ")

    try:
        passenger = Passenger(fullname, phone_number, email)
        print(passenger.register())
    except RegisterError as e:
        print(e)


def authenticate(unique_id):
    """authenticate a passenger by unique_id"""

    try:
        return Passenger.authenticate(unique_id)

    except AuthenticationError as e:
        print(e)


def manage_bank_account_menu(passenger):
    """management panel for bank account"""
    while True:
        print("1. deposit")
        print("2. withdraw")
        print("3. show account balance")
        print("4. Back to main menu")

        option = input("enter your option: ")

        if option == "1":

            amount = input("enter your amount to deposit: ")
            try:

                passenger.bank_account.deposit(amount)

            except BankAccountError as e:
                print(e)

        elif option == "2":

            amount = input("enter your amount to withdraw: ")
            try:

                passenger.bank_account.withdraw(amount)

            except BankAccountError as e:
                print(e)

        elif option == "3":

            print(passenger.bank_account.get_balance())

        elif option == "4":

            main_menu()

        else:

            print("wrong option, try again")


def card_menu(passenger):

    while True:
        print("1. list cards")
        print("2. buy new card")
        print("3. back to main menu")

        option = input(">>> ")

        if option == "1":

            if not passenger.list_cards():
                print("there is no card for select, buy first")
            else:
                for i, c in enumerate(passenger.list_cards(), 1):
                    print(f"{i} : {c}")

        elif option == "2":

            buy_cards_menu(passenger)

        elif option == "3":

            main_menu()

        else:
            print("wrong option, try again")

def buy_cards_menu(passenger):
    """buy cards menu"""
    while True:
        print("1. buy Single Trip metro card for 1000")
        print("2. buy credit metro card")
        print("3. buy time-credit metro card")
        print("4. back to main menu")

        option = input("your option>>> ")

        if option == "1":

            card = SingleTrip(passenger)
            passenger.bank_account.withdraw(str(card.price))
            card.save_card()

        elif option == "2":

            pass

        elif option == "3":

            pass

        elif option == "4":

            main_menu()

        else:

            print("wrong option, try again")