from pydantic import BaseModel, Field
from typing import Annotated

class Book(BaseModel):
    id: int
    title: str
    author: str
    # review: int | None = None
    review: Annotated[int | None, Field(ge=1, le=5)] = None  # Assicurarsi che il valore sia compreso tra 1 e 5 e il valore di default è None
    
book1 = Book(id=1, title="1984", author="George Orwell", review=5)
print(book1)
book2 = Book(id=2, title="Brave New World", author="Aldous Huxley")
print(book2)
try:
    book3 = Book(id=3, title="Fahrenheit 451", author="Ray Bradbury", review=6)  # Questo causerà un errore di validazione
except ValueError as e:
    print(f"Errore di validazione: {e}")

print("Esempio di Book completato con successo.")