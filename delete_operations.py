from db import sb

class Delete:
    @staticmethod
    def delete_member(member_id):
        borrowed = sb.table("borrow_records").select("*").eq("member_id", member_id).execute().data
        if borrowed:
            return "Cannot delete: member has borrowed books"
        resp = sb.table("members").delete().eq("member_id", member_id).execute()
        return resp.data

    @staticmethod
    def delete_book(book_id):
        borrowed = sb.table("borrow_records").select("*").eq("book_id", book_id).execute().data
        if borrowed:
            return "Cannot delete: book is borrowed"
        resp = sb.table("books").delete().eq("book_id", book_id).execute()
        return resp.data
