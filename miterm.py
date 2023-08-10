# Global list to store all the tickets
tickets_list = []

# Function to import tickets from the text file into the Special List
def import_tickets_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            ticket_id, event_id, username, timestamp, priority = line.strip().split(',')
            tickets_list.append([ticket_id, event_id, username, timestamp, int(priority)])

# Function to display the admin menu
def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. Display Statistics")
        print("2. Book a Ticket")
        print("3. Display all Tickets")
        print("4. Change Ticket’s Priority")
        print("5. Disable Ticket")
        print("6. Run Events")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_statistics()
        elif choice == '2':
            book_ticket()
        elif choice == '3':
            display_all_tickets()
        elif choice == '4':
            change_ticket_priority()
        elif choice == '5':
            disable_ticket()
        elif choice == '6':
            run_events()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

# Function to display the normal user menu
def user_menu():
    while True:
        print("\nUser Menu")
        print("1. Book a Ticket")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            book_ticket()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

# Function to display event statistics
def display_statistics():
    # Implement functionality to display event statistics (e.g., event with the highest number of tickets)
    pass

# Function to book a ticket
def book_ticket():
    username = input("Enter your username: ")
    event_id = input("Enter the event ID: ")
    timestamp = input("Enter the date of the event (YYYYMMDD): ")
    priority = int(input("Enter the priority of the ticket: "))
    
    ticket_id = str(len(tickets_list) + 1)  # Auto-incrementing ticket ID

    tickets_list.append([ticket_id, event_id, username, timestamp, priority])
    print(f"Ticket booked successfully! Ticket ID: {ticket_id}")

# Function to display all tickets
def display_all_tickets():
    today = datetime.date.today().strftime("%Y%m%d")
    for ticket in sorted(tickets_list, key=lambda x: (x[3], x[1])):
        if ticket[3] >= today:  # Display only upcoming events
            print(f"Ticket ID: {ticket[0]}, Event ID: {ticket[1]}, Username: {ticket[2]}, Date: {ticket[3]}, Priority: {ticket[4]}")

# Function to change ticket priority
def change_ticket_priority():
    ticket_id = input("Enter the ticket ID you want to change the priority for: ")
    for ticket in tickets_list:
        if ticket[0] == ticket_id:
            new_priority = int(input("Enter the new priority: "))
            ticket[4] = new_priority
            print(f"Priority for ticket ID {ticket_id} changed to {new_priority}")
            return
    print(f"Ticket ID {ticket_id} not found.")

# Function to disable a ticket
def disable_ticket():
    ticket_id = input("Enter the ticket ID you want to disable: ")
    for ticket in tickets_list:
        if ticket[0] == ticket_id:
            tickets_list.remove(ticket)
            print(f"Ticket ID {ticket_id} disabled.")
            return
    print(f"Ticket ID {ticket_id} not found.")

# Function to run events for today
def run_events():
    today = datetime.date.today().strftime("%Y%m%d")
    today_events = [ticket for ticket in tickets_list if ticket[3] == today]
    sorted_today_events = sorted(today_events, key=lambda x: x[4], reverse=True)  # Sort by priority

    for event in sorted_today_events:
        print(f"Running event - Ticket ID: {event[0]}, Event ID: {event[1]}, Username: {event[2]}, Priority: {event[4]}")

    # Remove the events that have been run from the tickets list
    for event in today_events:
        tickets_list.remove(event)

# Main function to start the program
def main():
    # A. Import tickets from the text file into the Special List without user intervention.
    file_path = "path/to/your/tickets_file.txt"  # Replace with the actual file path
    import_tickets_from_file(file_path)

    print("Welcome to the Corrupted Ticketing System!")

    # B. Greet the user and ask for their username and password
    username = input("Enter your username: ")
    password = input("Enter your password (leave empty for normal user): ")

    if username == "admin" and password == "admin123123":
        admin_menu()
    else:
        user_menu()

if __name__ == "__main__":
    import datetime
    main()
