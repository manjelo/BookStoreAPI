from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    publication_year: int
    ISBN: str

books = []

@app.post("/books",response_model= Book)
async def create_book(B: Book):
    books.append(B)
    return B

@app.get("/books")
async def get_books():
    return books

@app.get("/books/{book_ISBN}", response_model=Book)
async def get_book(book_ISBN: str):
    book = next((book for book in books if book.ISBN == book_ISBN), None)
    if book == None:
        raise HTTPException(status_code=404, detail="ISBN does not match any book")
    return book

@app.put("/books/{book_ISBN}", response_model=Book)
async def update_book(book_ISBN:str, new_book: Book):
    old_book = next((book for book in books if book.ISBN == book_ISBN), None)
    if old_book == None:
        books.append(new_book)
        return new_book
    for field in new_book.model_dump(exclude_unset=True):
        setattr(old_book, field, getattr(new_book,field))
    return old_book

@app.delete("books/{book_ISBN}", response_model=Book)
async def delete_book(bookISBN: str):
    book = next((book for book in books if book.ISBN == bookISBN), None)
    if book == None:
        raise HTTPException(status_code=404, detail="book does not exist")
    books.remove(book)
    return book

