from db import sb

class Read:
    @staticmethod
    def list_books():
        resp = sb.table("books").select("*").execute()
        return resp.data

    @staticmethod
    def search_books(query, field="title"):
        resp = sb.table("books").select("*").ilike(field, f"%{query}%").execute()
        return resp.data

    @staticmethod
    def member_details(member_id):
        member = sb.table("members").select("*").eq("member_id", member_id).execute().data
        borrowed = sb.table("borrow_records").select("*, books(*)").eq("member_id", member_id).execute().data
        return {"member": member, "borrowed_books": borrowed}
