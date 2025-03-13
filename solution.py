employees = {}

def add_employee():
    emp_id = input("Enter Employee ID (must start with 'E'): ")
    if not emp_id.startswith("E"):
        print("Error: Employee ID must start with 'E'.")
        print("---------------------------------------------------")
        return
    if emp_id in employees:
        print("Error: Employee ID must be unique.")
        print("---------------------------------------------------")
        return
    
    name = input("Enter Employee Name: ")
    if not name.replace(" ", "").isalpha():
        print("Error: Name must contain only alphabets.")
        print("---------------------------------------------------")
        return
    
    age = input("Enter Employee Age: ")
    if not age.isdigit() or int(age) <= 0:
        print("Error: Age must be a positive integer.")
        print("---------------------------------------------------")
        return
    
    department = input("Enter Employee Department: ")
    employees[emp_id] = {"name": name, "age": int(age), "department": department}
    print("Employee added successfully.")
    print("---------------------------------------------------")

def remove_employee():
    emp_id = input("Enter Employee ID to remove: ")
    if emp_id not in employees:
        print("Error: Employee ID not found.")
        print("---------------------------------------------------")
        return
    
    del employees[emp_id]
    print("Employee removed successfully.")
    print("---------------------------------------------------")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    if emp_id not in employees:
        print("Error: Employee ID not found.")
        print("---------------------------------------------------")
        return
    
    name = input("Enter new name (leave blank to keep unchanged): ")
    age = input("Enter new age (leave blank to keep unchanged): ")
    department = input("Enter new department (leave blank to keep unchanged): ")
    
    if name and not name.replace(" ", "").isalpha():
        print("Error: Name must contain only alphabets.")
        return
    if age and (not age.isdigit() or int(age) <= 0):
        print("Error: Age must be a positive integer.")
        return
    
    if name:
        employees[emp_id]["name"] = name
    if age:
        employees[emp_id]["age"] = int(age)
    if department:
        employees[emp_id]["department"] = department
    
    print("Employee details updated successfully.")
    print("---------------------------------------------------")

def search_employee():
    key = input("Enter Employee ID or Name to search: ")
    results = {emp_id: details for emp_id, details in employees.items() 
               if key.lower() in emp_id.lower() or key.lower() in details["name"].lower()}
    
    if results:
        for emp_id, details in results.items():
            print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['department']}")
    else:
        print("No matching employee found.")
        print("---------------------------------------------------")

def sort_employees():
    criteria = input("Enter sorting criteria (name, age, department): ")
    if criteria not in ["name", "age", "department"]:
        print("Error: Invalid sorting criteria. Choose from 'name', 'age', or 'department'.")
        print("---------------------------------------------------")
        return
    
    sorted_employees = sorted(employees.items(), key=lambda x: x[1][criteria])
    for emp_id, details in sorted_employees:
        print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['department']}")

def display_employees():
    if not employees:
        print("No employees to display.")
        print("---------------------------------------------------")
        return
    print("****Employee List****")
    for emp_id, details in employees.items():
        print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['department']}")

while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Update Employee")
    print("4. Search Employee")
    print("5. Sort Employees")
    print("6. Display Employees")
    print("7. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_employee()
    elif choice == "2":
        remove_employee()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        search_employee()
    elif choice == "5":
        sort_employees()
    elif choice == "6":
        display_employees()
    elif choice == "7":
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Please try again.")
