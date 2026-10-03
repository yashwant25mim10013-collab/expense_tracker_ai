import customtkinter as ctk
from components.header import Header
from components.dialogs import info, error
from models.budget_model import BudgetModel
from models.expense_model import ExpenseModel
from utils.date_utils import month_range
from utils.validators import valid_amount
from utils.helpers import money

class BudgetPage(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master,fg_color="transparent"); self.app=app
        Header(self,"Monthly Budget").pack(anchor="w",pady=(0,15))
        box=ctk.CTkFrame(self); box.pack(fill="x",padx=20,pady=20)
        ctk.CTkLabel(box,text="Set Monthly Budget",font=ctk.CTkFont(size=18,weight="bold")).pack(pady=15)
        self.amount=ctk.CTkEntry(box,placeholder_text="Budget amount"); self.amount.pack(padx=30,pady=8)
        ctk.CTkButton(box,text="Save Budget",command=self.save).pack(pady=8)
        self.info=ctk.CTkLabel(box,text=""); self.info.pack(pady=20)
        self.refresh()

    def refresh(self):
        b=BudgetModel.get(); start,end=month_range()
        spent=ExpenseModel.total_between(start,end)
        amount=float(b["amount"]) if b else 0
        remaining=amount-spent
        self.info.configure(text=f"Budget: {money(amount,self.app.currency)}\nSpent: {money(spent,self.app.currency)}\nRemaining: {money(remaining,self.app.currency)}")

    def save(self):
        if not valid_amount(self.amount.get()): return error("Invalid","Enter a positive budget.")
        BudgetModel.set_amount(float(self.amount.get())); self.amount.delete(0,"end"); self.refresh(); self.app.refresh_all(); info("Saved","Budget updated.")
