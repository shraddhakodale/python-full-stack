"""
Kiran Academy - Task 04
Flight Booking Console Application using Object-Oriented Programming (OOP)
Language: Python 3

Run:
    python flight_booking.py
"""

from abc import ABC, abstractmethod


class Flight:
    """Stores flight information and manages seat availability."""

    def __init__(self, code, airline, source, destination, available_seats, base_fare):
        self.__code = code
        self.__airline = airline
        self.__source = source
        self.__destination = destination
        self.__available_seats = available_seats
        self.__base_fare = base_fare

    @property
    def code(self):
        return self.__code

    @property
    def airline(self):
        return self.__airline

    @property
    def source(self):
        return self.__source

    @property
    def destination(self):
        return self.__destination

    @property
    def available_seats(self):
        return self.__available_seats

    @property
    def base_fare(self):
        return self.__base_fare

    def has_seats(self, count):
        return 0 < count <= self.__available_seats

    def reserve_seats(self, count):
        """Update seats only when enough seats are available."""
        if not self.has_seats(count):
            return False
        self.__available_seats -= count
        return True

    def display(self):
        print(
            f"{self.code:<8} | {self.airline:<18} | "
            f"{self.source:<12} to {self.destination:<12} | "
            f"Seats: {self.available_seats:<3} | Fare: Rs. {self.base_fare:,.2f}"
        )


class Passenger(ABC):
    """Abstract base class for passengers."""

    def __init__(self, name, age):
        self.name = name.strip()
        self.age = age

    @abstractmethod
    def get_discount_rate(self):
        """Return the passenger's discount as a decimal."""
        raise NotImplementedError

    @property
    def passenger_type(self):
        return self.__class__.__name__.replace("Passenger", "")


class RegularPassenger(Passenger):
    def get_discount_rate(self):
        return 0.0


class StudentPassenger(Passenger):
    def get_discount_rate(self):
        return 0.10


class Booking:
    """Represents one confirmed booking."""

    def __init__(self, booking_id, flight, passenger, ticket_count, subtotal, discount, total):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.ticket_count = ticket_count
        self.subtotal = subtotal
        self.discount = discount
        self.total = total

    def display_summary(self):
        rate = self.passenger.get_discount_rate() * 100
        print("\n========== BOOKING SUMMARY ==========")
        print("Booking ID          :", self.booking_id)
        print("Flight              :", self.flight.code)
        print("Airline             :", self.flight.airline)
        print("Route               :", f"{self.flight.source} to {self.flight.destination}")
        print("Passenger           :", self.passenger.name)
        print("Age                 :", self.passenger.age)
        print("Passenger type      :", self.passenger.passenger_type)
        print("Number of tickets   :", self.ticket_count)
        print(f"Base fare per ticket: Rs. {self.flight.base_fare:,.2f}")
        print(f"Subtotal            : Rs. {self.subtotal:,.2f}")
        print(f"Discount ({rate:.0f}%)       : Rs. {self.discount:,.2f}")
        print(f"Final amount        : Rs. {self.total:,.2f}")
        print("=====================================")


class FlightBookingSystem:
    """Controls flights, bookings, validation, and the menu."""

    def __init__(self):
        self.flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Sky Connect", "Mumbai", "Bengaluru", 25, 3500),
            Flight("PN303", "Deccan Wings", "Pune", "Hyderabad", 18, 3000),
        ]
        self.bookings = []
        self.next_booking_number = 1001

    def display_flights(self):
        print("\n================ AVAILABLE FLIGHTS ================")
        print(f"{'Code':<8} | {'Airline':<18} | {'Route':<27} | Seats | Base Fare")
        print("-" * 83)
        for flight in self.flights:
            flight.display()
        print("=" * 83)

    def find_flight_by_code(self, code):
        code = code.strip().upper()
        for flight in self.flights:
            if flight.code == code:
                return flight
        return None

    @staticmethod
    def calculate_fare(flight, passenger, ticket_count):
        subtotal = flight.base_fare * ticket_count
        discount = subtotal * passenger.get_discount_rate()
        total = subtotal - discount
        return subtotal, discount, total

    @staticmethod
    def validate_booking_details(name, age, ticket_count):
        if not name.strip():
            return "Passenger name cannot be blank."
        if age <= 0:
            return "Age must be greater than 0."
        if ticket_count <= 0:
            return "Number of tickets must be greater than 0."
        return None

    def book_flight(self):
        print("\n--------------- BOOK A FLIGHT ---------------")
        code = input("Enter flight code: ").strip().upper()
        flight = self.find_flight_by_code(code)
        if flight is None:
            print("Booking failed: Flight code does not exist.")
            return

        name = input("Enter passenger name: ").strip()

        try:
            age = int(input("Enter age: ").strip())
        except ValueError:
            print("Booking failed: Age must be a whole number.")
            return

        category = input("Passenger type (Regular/Student): ").strip().lower()
        if category not in ("regular", "student"):
            print("Booking failed: Passenger type must be Regular or Student.")
            return

        try:
            ticket_count = int(input("Enter number of tickets: ").strip())
        except ValueError:
            print("Booking failed: Ticket count must be a whole number.")
            return

        error = self.validate_booking_details(name, age, ticket_count)
        if error:
            print("Booking failed:", error)
            return

        if not flight.has_seats(ticket_count):
            print("Booking failed: Not enough seats available.")
            print("No booking was created. Available seats remain unchanged.")
            return

        if category == "student":
            passenger = StudentPassenger(name, age)
        else:
            passenger = RegularPassenger(name, age)

        subtotal, discount, total = self.calculate_fare(flight, passenger, ticket_count)

        # Change seat count and save booking only after all validation succeeds.
        if not flight.reserve_seats(ticket_count):
            print("Booking failed: Not enough seats available.")
            print("No booking was created. Available seats remain unchanged.")
            return

        booking_id = f"BK{self.next_booking_number}"
        booking = Booking(
            booking_id, flight, passenger, ticket_count, subtotal, discount, total
        )
        self.bookings.append(booking)
        self.next_booking_number += 1

        print("\nBooking confirmed!")
        booking.display_summary()

    def view_booking(self):
        if not self.bookings:
            print("\nNo confirmed booking exists yet. Please book a flight first.")
            return
        self.bookings[-1].display_summary()

    def run(self):
        print("\nWelcome to Kiran Air Booking")
        while True:
            print("\n1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")
            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.display_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    system = FlightBookingSystem()
    system.run()
