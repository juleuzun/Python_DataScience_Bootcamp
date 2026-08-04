# ==========================================
# Library Application
# ==========================================
# A simple library management system that allows
# the user to add, remove, and list books.
# ==========================================


# Create a list containing book names and authors
books = [
    ["İnce Memed", "Yaşar Kemal"],
    ["Ağrı Dağı Efsanesi", "Yaşar Kemal"],
    ["Onuncu Köy", "Fakir Baykurt"],
    ["Baba Evi", "Orhan Kemal"],
]


# Keep the application running until the user chooses to exit
while True:

    # Display the main menu
    print("\n==== LIBRARY APPLICATION ====")
    print("1 - Add Book")
    print("2 - Remove Book")
    print("3 - List Books")
    print("4 - Exit")

    selection = input("Please select an option: ")

    # ==========================================
    # Add Book
    # ==========================================

    if selection == "1":

        # Get the book name and author name from the user
        book_name = input("Book name: ").strip()
        author_name = input("Author name: ").strip()

        # Check whether the book already exists
        is_found = False

        for book in books:
            if (
                book[0].lower() == book_name.lower()
                and book[1].lower() == author_name.lower()
            ):
                is_found = True
                break

        # Display a message if the book already exists
        if is_found:
            print("This book is already registered.")

        # Otherwise, add the new book to the list
        else:
            books.append([book_name, author_name])
            print(f'"{book_name}" successfully added to the library.')

    # ==========================================
    # Remove Book
    # ==========================================

    elif selection == "2":

        # Ask the user for the author's name
        author = input("Author name: ").strip()

        # Create lists to store matching books and their indexes
        found_books = []
        indices = []

        # Search for books written by the selected author
        for i in range(len(books)):
            if books[i][1].lower() == author.lower():
                found_books.append(books[i])
                indices.append(i)

        # Display a message if no books are found
        if len(found_books) == 0:
            print("No books found by this author.")

        else:
            print("\nBooks by this author:")

            # Display the books written by the selected author
            for i in range(len(found_books)):
                print(f"{i + 1} - {found_books[i][0]}")

            # Ask the user which book they want to remove
            choice = int(input("Enter the number of the book you want to remove: "))

            # Check whether the selected number is valid
            if choice < 1 or choice > len(found_books):
                print("Invalid choice.")

            else:
                # Find the actual index in the original books list
                actual_index = indices[choice - 1]

                # Remove the selected book
                removed_book = books.pop(actual_index)

                print(
                    f'"{removed_book[0]}" has been successfully '
                    f"removed from the library."
                )

    # ==========================================
    # List Books
    # ==========================================

    elif selection == "3":

        # Check whether there are any books in the library
        if len(books) == 0:
            print("There are no books registered in the library.")

        else:
            print("\nBooks in the library:\n")

            # Display all books with their authors
            for i in range(len(books)):
                print(f"{i + 1} - {books[i][0]} - {books[i][1]}")

    # ==========================================
    # Exit
    # ==========================================

    elif selection == "4":
        print("Program finished.")
        break

    # ==========================================
    # Invalid Selection
    # ==========================================

    else:
        print("Invalid selection, please try again.")
