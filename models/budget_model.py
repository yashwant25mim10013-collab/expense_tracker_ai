
from database.database import get_connection
from datetime import date

class BudgetModel:
    @staticmethod
    def get():
        c=get_connection(); r=c.execute("SELECT * FROM budget WHERE id=1").fetchone(); c.close(); return r
    @staticmethod
    def set_amount(amount):
        c=get_connection()
        c.execute("""INSERT INTO budget(id,amount,month) VALUES(1,?,?)
                     ON CONFLICT(id) DO UPDATE SET amount=excluded.amount,month=excluded.month""",
                  (amount,date.today().strftime("%Y-%m")))
        c.commit(); c.close()
