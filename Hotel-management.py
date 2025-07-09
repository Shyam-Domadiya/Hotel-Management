class HotelManagement:

    def __init__(self):
        print("\nWelcome to the Hotel Management System!\n")
        
        # It shows available rooms in the hotel
        self.available_room = ["A-908", "A-620", "A-320"]
        self.room_prize = 5000
        # Used to store booked rooms
        self.booked_room = {} 

        # Staff with roles
        self.staff = {"Receptionist": ["John"]}

        # menu
        self.menu = {"Burger": 50, "Pasta": 80,"Salad": 40}
        self.orders = []
        self.total_fc = 0
    # Room Management System
    def room_management(self): 
        while True:
            print("\n===== Room Management System =====")
            print("1. Add Room")
            print("2. Remove Room")
            print("3. Room Check-in")
            print("4. Room Check-Out")
            print("5. View Room Status")
            print("6. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.add_room()
            elif choice == "2":
                self.remove_room()
            elif choice == "3":
                self.room_check_in()
            elif choice == "4":
                self.room_check_out()
                self.final_bill()
            elif choice == "5":
                self.room_status()
            elif choice == "6":
                print("Exiting Room Management System...")
                break
            else:
                print("Invalid choice! Please enter a valid option.")

    # Add New Rooms in the Hotel
    def add_room(self): 
        room = input("\nEnter Room Number: ").upper()
        if room[0].isalpha():
            if room not in self.available_room:
                self.available_room.append(room)
                print(f"Room No. {room} added successfully!")
            else:
                print("Room already exists!")
        else:
            print("Invalid room number format. Please enter a valid room number.")

    # Remove Specific Room in Hotel
    def remove_room(self): 
        room = input("\nEnter Room Number to Remove: ").upper()
        if room in self.available_room:
            self.available_room.remove(room)
            print(f"Room No. {room} removed successfully!")
        else:
            print("Room does not exist or is already booked!")

    # Room Booking (Check-in)
    def room_check_in(self): 
        if not self.available_room:
            print("\nNo rooms available for booking!\n")
        else:
            name = input("Enter Guest Name: ").upper()
            self.available_room.sort()  
            room = self.available_room.pop(0)
            self.booked_room[name] = room
            print(f"Room No. {room} successfully booked for {name}!")

    # Room Check-Out
    def room_check_out(self): 
        name = input("\nEnter Guest Name for Check-Out: ").upper()
        if name in self.booked_room:
            room = self.booked_room[name]
            self.booked_room.pop(name)
            self.available_room.append(room)
            print(f"{name} has checked out. Room No. {room} is now available.")    
        else:
            print("No booking found under this name.")

    # Show Room Status
    def room_status(self): 
        print("\n===== Room Status =====")
        print(f"Available Rooms: {self.available_room}")
        print(f"Booked Rooms: {self.booked_room}")

    # Staff Management System
    def staff_management(self): 
        while True:
            print("\n===== Staff Management System =====")
            print("1. Add Staff")
            print("2. Remove Staff")
            print("3. View Staff")
            print("4. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.add_staff()
            elif choice == "2":
                self.remove_staff()
            elif choice == "3":
                self.view_staff()
            elif choice == "4":
                print("Exiting Staff Management System...")
                break
            else:
                print("Invalid choice! Please enter a valid option.")

    # Add Staff Member
    def add_staff(self): 
        name = input("\nEnter Staff Member Name: ").capitalize()
        print("1. Receptionist\n2. Housekeeper\n3. Chef\n4. Waiter\n5. Security Guard")
        
        role_choice = input("Enter Staff Member Role Number: ")
        roles = { "1": "Receptionist", "2": "Housekeeper", "3": "Chef", "4": "Waiter", "5": "Security Guard" }
        
        if role_choice in roles:
            role = roles[role_choice]
            self.staff.setdefault(role, []).append(name)
            print(f"{name} has been added as {role}!")
        else:
            print("Invalid choice! Please select a valid role.")

    # Remove Staff Member
    def remove_staff(self):
        role_choice = input("\nEnter Staff Role Number to Remove a Member: ")
        roles = { "1": "Receptionist", "2": "Housekeeper", "3": "Chef", "4": "Waiter", "5": "Security Guard" }

        if role_choice in roles:
            role = roles[role_choice]
            if role in self.staff and self.staff[role]:
                name = input(f"Enter {role}'s Name to Remove: ").capitalize()
                if name in self.staff[role]:
                    self.staff[role].remove(name)
                    print(f"{name} has been removed from {role}!")
                else:
                    print(f"{name} not found in {role}!")
            else:
                print(f"No staff members found in {role}!")
        else:
            print("Invalid choice! Please select a valid role.")

    # View All Staff Members
    def view_staff(self): 
        print("\n===== Current Staff Members =====")
        for role, names in self.staff.items():
            print(f"{role}: {', '.join(names) if names else 'None'}")

    # Restaurant Management System
    def restaurant_management(self): 
        
        def menu():
            print("========menu=========")
            for i,j in self.menu.items():
                print(f"{i}:Rs.{j}")

        def place_order():
            menu()
            item = input("Enter Item To Order:").capitalize()
            if item in self.menu:
                quantity = int(input(f"Enter quantity of {item}: "))
                for order in self.orders:
                    if order["item"] == item:
                        order["quantity"] += quantity
                        print(f"Updated {item} quantity to {order['quantity']}")
                        return
                self.orders.append({"item": item, "quantity": quantity})
                print(f"{quantity}x {item} added to order!")

                self.total_fc += self.menu[item]*quantity
            else:
                print(f"Sorry, {item} is not Available")
            print(self.orders)

        def view_order():
            print(f"You can Order :{self.orders}")

        while True:
            print("\n===== Restaurant Management =====")
            print("1. Show Menu")
            print("2. Place Food Order")
            print("3. View Order")
            print("4. Exit")
                
            choice = int(input("\nEnter your choice: "))
            
            if choice == 1:
                menu()
            
            elif choice == 2:
                place_order()
                
            elif choice == 3:
                view_order()

            elif choice == 4:
                break
                
            else:
                print("Invalid choice! Please enter a valid option.")
    
    def final_bill(self):
        print("========Your Final Bill========")
        print(f"Bill Of Your Room:{self.room_prize}")
        print(f"Bill of Your ordered food:{self.total_fc}")
        print(f"Total:{self.room_prize+self.total_fc}")
        print("Thanks For visiting")

# Main Menu
hm = HotelManagement()

while True:
    print("\n===== Main Menu =====")
    print("1. Room Management")
    print("2. Staff Management")
    print("3. Restaurant Management")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        hm.room_management()
    elif choice == "2":
        hm.staff_management()
    elif choice == "3":
        hm.restaurant_management()
    elif choice == "4":
        print("Thank you for using Hotel Management System. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a valid option.")