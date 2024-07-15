import os

def display_menu():
    print("\n--- Note-taking app ---")
    print("1. Add Note")
    print("2. View your Notes")
    print("3. Delete Note")
    print("4. Exit")

def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added!")

def view_notes():
    if not os.path.exists("notes.txt"):
        print("No notes found.")
        return

    with open("notes.txt", "r") as file:
        notes = file.readlines()

    if notes:
        print("\n--- Your Notes ---")
        for index, note in enumerate(notes, start=1):
            print(f"{index}. {note.strip()}")
    else:
        print("No notes found.")

def delete_note():
    if not os.path.exists("notes.txt"):
        print("No notes found.")
        return

    with open("notes.txt", "r") as file:
        notes = file.readlines()

    if not notes:
        print("No notes found.")
        return

    view_notes()
    try:
        note_number = int(input("Enter the number of the note to delete: "))
        if 1 <= note_number <= len(notes):
            del notes[note_number - 1]
            with open("notes.txt", "w") as file:
                file.writelines(notes)
            print("Note deleted successfully.")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, Please try again!")

if __name__ == "__main__":
    main()
