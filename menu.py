import data
import validation
import reports
FIELD_NAMES=["Admission No.", "Name", "Blood Type", "Age"]
def get_number(question):
    while True:
        try:
            return int(input(question))
        except ValueError:
            print("Please enter a number.")
def ask_admission():
    while True:
        text = input("Enter Admission No.: ").strip()
        if validation.is_valid_admission(text):
            return text
        print("Invalid admission number. Use letters or digits only.")
def ask_name():
    while True:
        text = input("Enter Name: ").strip()
        if validation.is_valid_name(text):
            return text.title()
        print("Invalid name. Use letters only.")
def ask_blood():
    while True:
        text = input("Enter Blood Type: ").strip()
        if validation.is_valid_blood_type(text):
            return text.upper()
        print("Invalid blood type. Choose from:", validation.BLOOD_TYPES)
def ask_age():
    while True:
        text = input("Enter Age: ").strip()
        if validation.is_valid_age(text):
            return int(text)
        print("Invalid age. It must be between 18 and 65.")
def ask_value(position):
    if position == data.ADMISSION:
        return ask_admission()
    elif position == data.NAME:
        return ask_name()
    elif position == data.BLOOD:
        return ask_blood()
    else:
        return ask_age()
def choose_field(action):
    for i in range(4):
        print(str(i + 1) + ". " + action + " " + FIELD_NAMES[i])
    choice = get_number("Enter your choice: ")
    if choice >= 1 and choice <= 4:
        return choice - 1
    print("Invalid choice.")
    return -1
def show_donor(d):
    print("  Admission No:", d[0], "| Name:", d[1], "| Blood:", d[2], "| Age:", d[3])
# ---------- Menu options ----------
def create():
    while True:
        admission = ask_admission()
        name = ask_name()
        blood = ask_blood()
        age = ask_age()

        if data.add_donor(admission, name, blood, age):
            print("Donor saved successfully!")
        else:
            print("This admission number already exists.")

        again = input("Add another? (y/n): ")
        if again.lower() == "n":
            break
def read():
    if len(data.donors) == 0:
        print("No records available.")
        return
    for d in data.donors:
        show_donor(d)
def search():
    position = choose_field("Search by")
    if position == -1:
        return
    value = input("Enter the value to search for: ")
    results = data.search_donors(position, value)
    if len(results) == 0:
        print("Record not found.")
    for d in results:
        show_donor(d)
def update():
    position = choose_field("Update")
    if position == -1:
        return
    old_value = input("Enter the existing value: ")
    if len(data.search_donors(position, old_value)) == 0:
        print("Record not found.")
        return

    new_value = ask_value(position)
    if position == data.ADMISSION:
        if len(data.search_donors(position, new_value)) > 0:
            print("That admission number already exists.")
            return

    count = data.update_donors(position, old_value, new_value)
    print(count, "record(s) updated.")
def delete():
    position = choose_field("Delete by")
    if position == -1:
        return
    value = input("Enter the value to delete: ")
    removed = data.delete_donors(position, value)
    if len(removed) == 0:
        print("Record not found.")
    for d in removed:
        print("Deleted:")
        show_donor(d)
def report():
    if len(data.donors) == 0:
        print("No data to report.")
        return
    print("Donors per blood type:")
    counts = reports.count_by_blood_type(data.donors)
    for blood in sorted(counts):
        print("  " + blood + ":", counts[blood])
    summary = reports.age_summary(data.donors)
    print("Youngest:", summary[0], "| Oldest:", summary[1], "| Average age:", summary[2])
def run():
    while True:
        print("\n--- Blood Donation Data Menu ---")
        print("1. Create Blood Donation Data")
        print("2. Read Blood Donation Data")
        print("3. Search Blood Donation Data")
        print("4. Update Blood Donation Data")
        print("5. Delete Blood Donation Data")
        print("6. Report / Statistics")
        print("7. Exit")
        choice = get_number("Enter your choice: ")

        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            search()
        elif choice == 4:
            update()
        elif choice == 5:
            delete()
        elif choice == 6:
            report()
        elif choice == 7:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
