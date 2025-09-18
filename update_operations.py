from db import sb

class Update:
    @staticmethod
    def update_book_stock(book_id, stock):
        resp = sb.table("books").update({"stock": stock}).eq("book_id", book_id).execute()
        return resp.data

    @staticmethod
    def update_member_email(member_id, email):
        resp = sb.table("members").update({"email": email}).eq("member_id", member_id).execute()
        return resp.data
