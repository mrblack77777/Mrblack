import os

def create_file():
    # Prompt user for file name
    file_name = input("Enter file name: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    
    # Create new file
    with open(file_name, 'w') as file:
        print(f"{file_name} created.")

def open_file():
    # Prompt user for file name
    file_name = input("Enter file name: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    # Check if file exists
    if os.path.isfile(file_name):
        with open(file_name, 'r') as file:
            # Print contents of file
            print(file.read())
    else:
        print(f"{file_name} does not exist.")

def edit_file():
    # Prompt user for file name
    file_name = input("Enter file name: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    # Check if file exists
    if os.path.isfile(file_name):
        # Open file in append mode
        with open(file_name, 'a') as file:
            # Prompt user for new text to add to file
            new_text = input("Enter new text: ")
            file.write("\n" + new_text)
            print(f"Text added to {file_name}.")
    else:
        print(f"{file_name} does not exist.")

def save_file():
    # Prompt user for file name
    file_name = input("Enter file name: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    # Check if file exists
    if os.path.isfile(file_name):
        # Open file in write mode
        with open(file_name, 'w') as file:
            # Prompt user for new text to write to file
            new_text = input("Enter new text: ")
            file.write(new_text)
            print(f"{file_name} saved.")
    else:
        print(f"{file_name} does not exist.")

# Main program loop
while True:
    print("""
Notepad Options:
1. Create new file
2. Open existing file
3. Edit existing file
4. Save changes to file
5. Exit
    """)
    user_choice = input("Enter your choice (1-5): ")

    if user_choice == "1":
        create_file()
    elif user_choice == "2":
        open_file()
    elif user_choice == "3":
        edit_file()
    elif user_choice == "4":
        save_file()
    elif user_choice == "5":
        break
    else:
        print("Invalid choice. Try again.")
