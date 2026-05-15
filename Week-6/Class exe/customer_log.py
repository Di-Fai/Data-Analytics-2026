# 1. Create the log file using write mode
def create_log():
    try:
        with open(FILENAME, "w") as file:
            file.write("=== Customer Interaction Log ===\n")
            file.write("Date | Customer | Issue | Rep\n")
            file.write("-" * 60 + "\n")

        print(f"Log created: {FILENAME}")

    except FileNotFoundError:
        print("File could not be created.")


# 2. Append new records using append mode
def append_records(entries):
    try:
        if not os.path.exists(FILENAME):
            print("Log file does not exist. Please create the log first.")
            return

        records = [
            f"{date} | {customer:<15} | {issue:<15} | {rep}\n"
            for date, customer, issue, rep in entries
        ]

        with open(FILENAME, "a") as file:
            file.writelines(records)

        print(f"{len(records)} record(s) appended.")

    except FileNotFoundError:
        print("Log not found. Run option 1 to create it.")


# 3. Read and display the entire log using read mode
def display_log():
    try:
        with open(FILENAME, "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("Log not found. Run option 1 to create it.")


# 4. Search for a customer name using readlines
def search_customer(name):
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()

        matches = [line for line in lines if name.lower() in line.lower()]

        if matches:
            print(f'Found {len(matches)} record(s) for "{name}":')
            print("".join(matches))
        else:
            print(f'No records found for "{name}".')

    except FileNotFoundError:
        print("Log not found. Run option 1 to create it.")


# 5. Count entries and update the header using r+ mode
def update_entry_count():
    try:
        with open(FILENAME, "r+") as file:
            lines = file.readlines()

            count = sum(
                1 for line in lines[1:]
                if line.strip() and not line.startswith("-")
            )

            lines[0] = f"=== Customer Interaction Log | Entries: {count} ===\n"

            file.seek(0)
            file.writelines(lines)
            file.truncate()

        print(f"Header updated. Total entries: {count}")

    except FileNotFoundError:
        print("Log not found. Run option 1 to create it.")


# 6. Show only the header line using readline
def show_header():
    try:
        with open(FILENAME, "r") as file:
            header = file.readline()
            print("Header:", header.strip())

    except FileNotFoundError:
        print("Log not found. Run option 1 to create it.")


# Sample customer interaction records
SAMPLE = [
    ("2025-05-01", "Alice Nguyen", "Billing query", "J. Park"),
    ("2025-05-01", "Bob Carter", "Login issue", "S. Diaz"),
    ("2025-05-02", "Carol Singh", "Refund request", "J. Park"),
    ("2025-05-02", "Alice Nguyen", "Follow-up", "M. Lee"),
]


# Main menu
def main():
    while True:
        print("\n=== Customer Log Manager ===")
        print("1 Create / reset log")
        print("2 Append sample records")
        print("3 Display full log")
        print("4 Search by customer name")
        print("5 Update entry count in header")
        print("6 Show header line only")
        print("0 Quit")

        choice = input("Choose: ").strip()

        if choice == "1":
            create_log()

        elif choice == "2":
            append_records(SAMPLE)

        elif choice == "3":
            display_log()

        elif choice == "4":
            name = input("Customer name to search: ")
            search_customer(name)

        elif choice == "5":
            update_entry_count()

        elif choice == "6":
            show_header()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()