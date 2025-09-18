from db import sb

class Create:
    @staticmethod
    def add_member(name, email):
        payload = {"name": name, "email": email}
        resp = sb.table("members").insert(payload).execute()
        return resp.data

    @staticmethod
    def add_book(title, author, category, stock):
        payload = {"title": title, "author": author, "category": category, "stock": stock}
        resp = sb.table("books").insert(payload).execute()
        return resp.data
