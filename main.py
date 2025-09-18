from create_operations import Create
from read_operations import Read
from update_operations import Update
from delete_operations import Delete

def menu():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Member")
        print("2. Add Book")
        print("3. List All Books")
        print("4. Search Books")
        print("5. Member Details")
        print("6. Update Book Stock")
        print("7. Update Member Email")
        print("8. Delete Member")
        print("9. Delete Book")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Member name: ")
            email = input("Member email: ")
            print("Added:", Create.add_member(name, email))
        elif choice == "2":
            title = input("Book title: ")
            author = input("Book author: ")
            category = input("Book category: ")
            stock = int(input("Stock: "))
            print("Added:", Create.add_book(title, author, category, stock))
        elif choice == "3":
            books = Read.list_books()
            for b in books:
                print(b)
        elif choice == "4":
            field = input("Search by (title/author/category): ").strip()
            query = input("Search query: ").strip()
            books = Read.search_books(query, field)
            for b in books:
                print(b)
        elif choice == "5":
            member_id = int(input("Member ID: "))
            details = Read.member_details(member_id)
            print("Member Info:", details["member"])
            print("Borrowed Books:", details["borrowed_books"])
        elif choice == "6":
            book_id = int(input("Book ID: "))
            stock = int(input("New Stock: "))
            print("Updated:", Update.update_book_stock(book_id, stock))
        elif choice == "7":
            member_id = int(input("Member ID: "))
            email = input("New Email: ")
            print("Updated:", Update.update_member_email(member_id, email))
        elif choice == "8":
            member_id = int(input("Member ID: "))
            print(Delete.delete_member(member_id))
        elif choice == "9":
            book_id = int(input("Book ID: "))
            print(Delete.delete_book(book_id))
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
