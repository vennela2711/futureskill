# Ticket Booking System (Foundation for Algorand Integration)

import uuid

# In-memory storage
events = {
    "Concert": {"total_seats": 5, "booked_seats": 0},
    "Movie": {"total_seats": 5, "booked_seats": 0},
    "Bus": {"total_seats": 5, "booked_seats": 0}
}

bookings = {}


class Ticket:
    def __init__(self, name, event):
        self.ticket_id = str(uuid.uuid4())[:8]
        self.name = name
        self.event = event
        self.status = "Booked"

    def cancel(self):
        self.status = "Cancelled"

    def __str__(self):
        return f"""
Ticket ID: {self.ticket_id}
Name: {self.name}
Event: {self.event}
Status: {self.status}
"""


def show_events():
    print("\nAvailable Events:")
    for event, data in events.items():
        available = data["total_seats"] - data["booked_seats"]
        print(f"{event} → Available Seats: {available}")


def book_ticket():
    show_events()
    event = input("\nEnter event name: ")

    if event not in events:
        print("❌ Invalid event!")
        return

    if events[event]["booked_seats"] >= events[event]["total_seats"]:
        print("❌ No seats available!")
        return

    name = input("Enter your name: ")
    ticket = Ticket(name, event)

    bookings[ticket.ticket_id] = ticket
    events[event]["booked_seats"] += 1

    print("\n✅ Ticket Booked Successfully!")
    print(ticket)


def view_ticket():
    ticket_id = input("Enter Ticket ID: ")

    if ticket_id in bookings:
        print(bookings[ticket_id])
    else:
        print("❌ Ticket not found!")


def cancel_ticket():
    ticket_id = input("Enter Ticket ID: ")

    if ticket_id in bookings:
        ticket = bookings[ticket_id]

        if ticket.status == "Cancelled":
            print("⚠️ Already cancelled!")
            return

        ticket.cancel()
        events[ticket.event]["booked_seats"] -= 1

        print("⚠️ Ticket Cancelled!")
    else:
        print("❌ Ticket not found!")


def menu():
    while True:
        print("\n=== Ticket Booking System ===")
        print("1. Show Events")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_events()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            view_ticket()
        elif choice == "4":
            cancel_ticket()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    menu()