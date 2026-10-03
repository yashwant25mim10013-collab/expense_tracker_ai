
from datetime import datetime
from database.database import get_connection, hash_password

class UserModel:
    @staticmethod
    def authenticate(username,password):
        c=get_connection()
        r=c.execute("SELECT * FROM users WHERE username=? AND password_hash=?",
                    (username,hash_password(password))).fetchone()
        c.close(); return r
    @staticmethod
    def create(username,password,display_name):
        c=get_connection()
        try:
            c.execute("INSERT INTO users(username,password_hash,display_name,created_at) VALUES(?,?,?,?)",
                      (username,hash_password(password),display_name,datetime.now().isoformat(timespec="seconds")))
            c.commit(); return True
        except Exception: return False
        finally: c.close()
    @staticmethod
    def all_users():
        c=get_connection(); r=c.execute("SELECT id,username,display_name,created_at FROM users ORDER BY id").fetchall(); c.close(); return r
