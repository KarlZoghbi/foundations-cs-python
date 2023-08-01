import datetime #https://www.w3schools.com/python/python_datetime.asp
import os        #https://www.digitalocean.com/community/tutorials/python-os-module (i used import os so i cn search if the tickets.txt file is in the system)


users = {"admin": "admin123123"} #this dictionary is to store the admin user and password

def load_data(): #Load ticket data from the "tickets.txt" file if it exists,otherwise initialize an empty list and set the ticket_id.
    

  global tickets
  global ticket_id

  tickets = []

  if os.path.exists("tickets.txt"):
    file = open("tickets.txt", "r")
    for line in file:
      if line.strip():
        tickets.append(line.strip().split(","))
    filelen = len(tickets)
    if filelen == 0:
      ticket_id = 100
    else:
      ticket_id = int(tickets[filelen-1][0][4:])
      file.close()
  if not os.path.exists("tickets.txt"):
    open("tickets.txt", "w").close()
    ticket_id = 100

    
def login(): #Get user input for login credentials and validate the user. Return "admin" for admin user, the username for normal users, and an empty string for invalid login.
   
               
  username = input("Enter username: ")
  if username == "admin":
    password = input("Enter password: ")
    if password == users["admin"]:
      print("Admin login successful!")
      return "admin"
    else:
      print("Invalid admin password!")
      return ""

  print("User login successful!")
  return username
  
def admin_menu():

  #https://www.tutorialspoint.com/triple-quotes-in-python
  print("""
  Admin Menu
  1. Display Statistics
  2. Book Ticket
  3. Display Tickets
  4. Change Priority
  5. Disable Ticket
  6. Run Events
  7. Logout
  """)

  choice = input("Enter choice: ")
  if choice == "1":
      display_stats()
  elif choice == "2":
      book_ticket_admin()
  elif choice == "3":
      display_tickets()
  elif choice == "4":
      change_priority()
  elif choice == "5":
      disable_ticket()
  elif choice == "6":
      run_events()
  elif choice == "7":
      return

  save_data()
  
  print("\nOperation completed! Menu reloaded below:")  
  admin_menu()
  
def user_menu():

  print("""  
  User Menu
  1. Book Ticket
  7. Exit
  """)

  choice = input("Enter choice: ")
  if choice == "1":
      book_ticket_user()
  elif choice == "7":
      print("Exiting program...")
      save_data()
      exit()
      
  print("\nOperation completed! Menu reloaded below:")
  user_menu()
  
def book_ticket_admin():
  name = input("Enter name: ")
  event = "ev" + input("Enter event ID: ")
  date = datetime.datetime.today().strftime("%Y%m%d") #https://www.programiz.com/python-programming/datetime/current-datetime
  priority = input("Enter priority: ")

  global ticket_id
  ticket_id += 1
  id = "tick" + str(ticket_id)

  ticket = [id, event, name, date, priority]
  tickets.append(ticket)

  print("Ticket booked successfully!")
  
def book_ticket_user():
  event = "ev" + input("Enter event ID: ")
  date = datetime.datetime.today().strftime("%Y%m%d") 

  global ticket_id
  ticket_id += 1
  id = "tick" + str(ticket_id) #https://www.w3schools.com/python/ref_func_str.asp

  ticket = [id, event, username, date, "0"]
  tickets.append(ticket)

  print("Ticket booked successfully!")
  save_data()

def display_stats():

  counts = {}
  for t in tickets:
    id = t[1]
    if id in counts:
      counts[id] += 1
    else:
      counts[id] = 1

  max_count = 0
  popular = None
  
  for id, count in counts.items():
    if count > max_count:
      max_count = count
      popular = id

  print(f"Most popular event is {popular} with {max_count} tickets")
  
def display_tickets():

  today = datetime.datetime.today().strftime("%Y%m%d")

  print("Upcoming tickets:")

  filtered_tickets = [t for t in tickets if int(t[3]) >= int(today)]

  def sort_key(ticket):
    return ticket[3] 
  
  sorted_tickets = sorted(filtered_tickets, key=sort_key) #https://www.w3schools.com/python/ref_func_sorted.asp

  for t in sorted_tickets:
    print(t[0], t[1], t[2], t[3], t[4])

def change_priority():
  id = input("Enter ticket ID to modify: ")
  priority = input("Enter new priority: ")
  
  for t in tickets:
    if t[0] == id:
      t[4] = priority
      print("Priority updated successfully!")
      return
  
  print("Ticket not found with given ID")
  
def disable_ticket():
  id = input("Enter ticket ID to disable: ")
  
  for i, t in enumerate(tickets): #https://www.geeksforgeeks.org/enumerate-in-python/
    if t[0] == id:
      del tickets[i] 
      print("Ticket disabled successfully!")
      return
  
  print("Ticket not found with given ID")

def run_events():

  global tickets
  
  today = datetime.datetime.today().strftime("%Y%m%d")

  todays_events = [t for t in tickets if t[3]==today]

  print("Today's events:")
  for t in todays_events:
    print(t[1])  
    
  todays_events = [t for t in todays_events if t[3] != today]
  
  save_data()

def save_data():

  file = open("tickets.txt", "w")

  for t in tickets:
    row = ",".join(t)
    file.write(row + "\n")
  file.close()


# Main program
load_data()

while True:

  username = login()

  if username == "admin":
    admin_menu()

  elif username:
    user_menu()

  else:
    print("Invalid login")
    break
  print("Thank you for using the program")
  break

save_data()