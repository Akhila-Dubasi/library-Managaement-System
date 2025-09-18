from db import sb

class BorrowReturn:

    @staticmethod
    def borrow_book(member_id, book_id):
        book = sb.table("books").select("*").eq("book_id", book_id).execute().data
        if not book:
            return "Book not found."
        if book[0]['stock'] <= 0:
            return "Book out of stock."

        sb.table("borrow_records").insert({"member_id": member_id, "book_id": book_id}).execute()
        sb.table("books").update({"stock": book[0]['stock'] - 1}).eq("book_id", book_id).execute()
        return "Book borrowed successfully."

    @staticmethod
    def return_book(member_id, book_id):
        record = sb.table("borrow_records").select("*").eq("member_id", member_id).eq("book_id", book_id).is_("return_date", None).execute().data
        if not record:
            return "No active borrow record found."

        sb.table("borrow_records").update({"return_date": "NOW()"}).eq("record_id", record[0]['record_id']).execute()
        book = sb.table("books").select("*").eq("book_id", book_id).execute().data
        sb.table("books").update({"stock": book[0]['stock'] + 1}).eq("book_id", book_id).execute()
        return "Book returned successfully."
