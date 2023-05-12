# library-management

The goal of the library management system is to provide a program that allows both the manager and customers to interact with the library.
The manager is responsible for managing the login and signup page, adding books, removing books, updating book details, and generating invoices.
On the other hand, customers have limited access and can only view books, check book availability, rent books, and pay bills.

The program is implemented using Python and consists of several classes and functions. Here's an overview of the components:

1. The "Book" class represents a book in the library. It has attributes such as ID, title, author, publisher, quantity, and price.

2. The "Library" class is responsible for managing the books. It has methods to load books from a CSV file, display all books, check the availability of a book,
   rent a book and generate invoices.

3. The "load_books()" method reads the book data from a CSV file (e.g., "books.csv") and creates Book objects to store in the 'Library' instance.

4. The "display_books()" method shows a formatted list of all available books, including their ID, title, author, publisher, quantity, and price.
5.The "book_exists()" method checks if a book with a given ID exists in the library.

6. The "rent_book()" method allows a customer to rent a book by providing its ID. 
   If the book is available, its quantity is decreased by 1, and the Book object is returned. If the book is not available, 'None' is returned.

7. The "generate_invoice()" method calculates the total cost of rented books and displays an invoice with detailed information about the rented books,
   including their ID, title, author, publisher, quantity (always 1 for rented books), and individual prices.
   It also provides the total price for all the rented books.

8. The "main()" function serves as the entry point of the program. 
   It handles user login and signup, displays the available options based on the user's role (manager or customer)
   and calls the respective methods based on the user's choice.
   
The program runs in a loop until the user chooses to exit.
It provides a console-based interface for users to interact with the library management system, view books, check availability, rent books, and pay bills.
