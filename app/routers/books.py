from fastapi import APIRouter


router = APIRouter(prefix="/books")

@router.get("/")
def get_books():
    return {"Books": "Yes"}


@router.get("/{book_id}")
def get_book_by_id(book_id: int):
    return {"Book": book_id}
