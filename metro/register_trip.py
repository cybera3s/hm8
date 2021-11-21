from utils import any_key, clear_screen
from models import *
from metro.menus import trip_management_menu
from metro.exceptions import TripError


def register_trip(passenger):
    """register trip section"""

    # list cards section

    # if passenger has no cards
    if not passenger.list_cards():

        print("There is no card to show, Buy first")
        any_key()

    else:

        my_cards = passenger.list_cards()

        print("__________________ CARDS LIST __________________\n")
        for i, c in enumerate(my_cards, 1):
            print(f"\t{i}: {c}")

        try:

            card = int(input("\nselect your desired card: "))

            if card <= 0 or my_cards[card - 1] not in my_cards:
                raise IndexError()

            selected_card = my_cards[card - 1]
            clear_screen()
            print(selected_card, "selected")
            clear_screen(1)
            # use different cards
            if isinstance(selected_card, SingleTrip):
                selected_card.use_card()  # just delete it from card list

            else:
                selected_card.use_card(Trip.PRICE)
                print(selected_card)

            print("Pay successfully...")
            clear_screen(1.5)

        except (IndexError, ValueError):

            clear_screen()
            print("invalid option, try again")
            any_key()
            trip_management_menu(passenger)

        except MetroCardError as e:

            clear_screen()
            print(e)
            any_key()
            trip_management_menu(passenger)

        while True:

            clear_screen(1)
            print("Available stations")
            print(Trip.get_stations())

            origin = input("\torigin station: ")
            destination = input("\tdestination station: ")

            try:

                trip = Trip(origin, destination)
                print(trip)
                trip.progress()
                print("trip successfully done")
                trip_management_menu(passenger)

            except TripError as e:

                clear_screen()
                print(e)
                any_key()
