import json
import os

FILE_NAME = "tickets.json"


def load_tickets():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tickets(tickets):
    with open(FILE_NAME, "w") as file:
        json.dump(tickets, file, indent=4)


def create_ticket(tickets):
    user = input("User name: ")
    issue = input("Describe the problem: ")

    ticket_id = len(tickets) + 1

    ticket = {
        "id": ticket_id,
        "user": user,
        "issue": issue,
        "status": "Open"
    }

    tickets.append(ticket)
    save_tickets(tickets)

    print("\nTicket created successfully!\n")


def list_tickets(tickets):

    if not tickets:
        print("\nNo tickets found.\n")
        return

    print("\n--- TICKETS ---")

    for ticket in tickets:
        print(
            f"""
ID: {ticket['id']}
User: {ticket['user']}
Issue: {ticket['issue']}
Status: {ticket['status']}
---------------------------
"""
        )


def resolve_ticket(tickets):

    try:
        ticket_id = int(input("Enter ticket ID to resolve: "))

        for ticket in tickets:
            if ticket["id"] == ticket_id:
                ticket["status"] = "Resolved"
                save_tickets(tickets)
                print("\nTicket resolved!\n")
                return

        print("Ticket not found.")

    except ValueError:
        print("Please enter a valid number.")


def menu():

    tickets = load_tickets()

    while True:

        print("""
===== HELP DESK SYSTEM =====

1 - Open Ticket
2 - List Tickets
3 - Resolve Ticket
4 - Exit

""")

        option = input("Choose an option: ").strip()

        if option == "1":
            create_ticket(tickets)

        elif option == "2":
            tickets = load_tickets()
            list_tickets(tickets)

        elif option == "3":
            resolve_ticket(tickets)

        elif option == "4":
            print("Exiting system...")
            break

        else:
            print("Invalid option.")


menu()