# Import required libraries
import csv

# Define the Book class
class Book:
    def __init__(self, id, title, author, publisher, quantity, price):
        self.id = id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.quantity = quantity
        self.price = price

# Define the Library class
class Library:
    def __init__(self):
        self.books = []

    # Load books from CSV file
    def load_books(self):
        with open('books.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader) # Skip header row
            for row in reader:
                book = Book(int(row[0]), row[1], row[2], row[3], int(row[4]), float(row[5]))
                self.books.append(book)

    # Display all books
    def display_books(self):
        print('Available Books:')
        print('----------------')
        print('ID   Title                Author          Publisher          Quantity  Price')
        print('----------------------------------------------------------------------------')
        for book in self.books:
            print(f'{book.id:<4} {book.title:<20} {book.author:<15} {book.publisher:<18} {book.quantity:<9} ${book.price:.2f}')

    # Check if book exists by ID
    def book_exists(self, id):
        for book in self.books:
            if book.id == id:
                return True
        return False
    
    # Rent a book by ID
    def rent_book(self, id):
        for book in self.books:
            if book.id == id:
                if book.quantity > 0:
                    book.quantity -= 1
                    return book
                else:
                    return None
        return None

    # Add a new book
    def add_book(self, id, title, author, publisher, quantity, price):
        if self.book_exists(id):
            print('Book already exists')
        else:
            book = Book(id, title, author, publisher, quantity, price)
            self.books.append(book)
            print('Book added successfully')

    # Remove a book by ID
    def remove_book(self, id):
        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                print('Book removed successfully')
                return
        print('Book not found')

    # Update book details by ID
    def update_book(self, id, title=None, author=None, publisher=None, quantity=None, price=None):
        for book in self.books:
            if book.id == id:
                if title is not None:
                    book.title = title
                if author is not None:
                    book.author = author
                if publisher is not None:
                    book.publisher = publisher
                if quantity is not None:
                    book.quantity = quantity
                if price is not None:
                    book.price = price
                print('Book details updated successfully')
                return
        print('Book not found')

    # Generate invoice for rented books
    def generate_invoice(self, rented_books):
        total_price = 0
        print('Invoice:')
        print('--------')
        print('ID   Title                Author          Publisher          Quantity  Price')
        print('----------------------------------------------------------------------------')
        for book in rented_books:
            print(f'{book.id:<4} {book.title:<20} {book.author:<15} {book.publisher:<18} 1 ${book.price:.2f}')
            total_price += book.price
        print('----------------------------------------------------------------------------')
        print(f'Total Price: ${total_price:.2f}')

# Define the main function
def main():
    library = Library()
    library.load_books()
    rented_books = []  # List to store rented books

    # Ask user to sign up or login
    while True:
        print('1. Sign up')
        print('2. Login')
        choice = input('Enter choice: ')
        #sigin up
        if choice == '1':
            username = input('Enter username: ')
            password = input('Enter password: ')
            # Save the username and password in a file or database for future reference
            print('Sign up successful!')
            break
        #login
        elif choice == '2':
            username = input('Enter username: ')
            password = input('Enter password: ')
            # Check if the username and password match the stored credentials
            # If the login is successful, proceed to the next step
            # Otherwise, display an error message and ask the user to try again
            print('Login successful!')
            break
        else:
            print('Invalid choice. Please try again.')

    # User is logged in
    while True:
        print('1. View books')
        print('2. Check book availability')
        print('3. Rent book')
        print('4. Pay bill')
        print('5. Exit')
        choice = input('Enter choice: ')

        if choice == '1':
            library.display_books()

        elif choice == '2':
            book_id = int(input('Enter book ID: '))
            if library.book_exists(book_id):
                print('Book is available')
            else:
                print('Book is not available')

        
        elif choice == '3':
            
            book_id = int(input('Enter book ID: '))
            if library.book_exists(book_id):
                rented_book = library.rent_book(book_id)
                if rented_book is not None:
                    rented_books.append(rented_book)
                    print('Book rented successfully')
                    # Add the rented book to a list to calculate the bill later
                    
                else:
                    print('Book is not available for rent')
            else:
                print('Book not found')

        elif choice == '4':
            # Pass the rented_books list to the generate_invoice() method
            library.generate_invoice(rented_books)

        elif choice == '5':
            print('Thank you for using the library management system!')
            break
        
        else:
            print('Invalid choice. Please try again.')

# Call the main function
if __name__ == '__main__':
    main()
