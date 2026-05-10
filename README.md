# BookStoreAPI
/books/ (POST): Used to create a new book. The create_book function is responsible for processing this request. It expects a Book object as input, appends it to the books list, and returns the created book.
/books/ (GET): Retrieves a list of all books using the get_books function, returning a list of books.
/books/{ISBN} (GET): Retrieves a specific book by its ISBN. The get_book function searches for a book with the provided ISBN and returns it. If not found, it raises an HTTP 404 error.
/books/{ISBN} (PUT): Updates a book with a specific ISBN. The update_book function finds the book by ISBN, updates its details with the provided data, and returns the updated book. If not found, it raises an HTTP 404 error.
/books/{ISBN} (DELETE): Deletes a book by ISBN. The delete_book function removes the book from the books list and returns the deleted book. If not found, it raises an HTTP 404 error