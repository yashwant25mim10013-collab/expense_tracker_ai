
import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    def __init__(self,master,navigate):
        super().__init__(master,width=220,corner_radius=0); self.grid_propagate(False)
        ctk.CTkLabel(self,text="💰",font=ctk.CTkFont(size=40)).pack(pady=(18,0))
        ctk.CTkLabel(self,text="Expense &\nTask Manager",font=ctk.CTkFont(size=16,weight="bold")).pack(pady=(0,12))
        items=[
            ("🏠 Dashboard","Dashboard"),("💰 Expenses","Expenses"),("📋 Tasks","Tasks"),
            ("📊 Analytics","Analytics"),("🤖 Smart Insights","Smart Insights"),("💳 Budget","Budget"),
            ("🔁 Recurring","Recurring"),("⏰ Reminders","Reminders"),("📤 Reports","Reports"),
            ("👤 Profiles","Profiles"),("⚙️ Settings","Settings")]
        for text,page in items:
            ctk.CTkButton(self,text=text,anchor="w",height=34,fg_color="transparent",
                          hover_color=("gray80","gray25"),command=lambda p=page:navigate(p)).pack(fill="x",padx=10,pady=2)
        ctk.CTkLabel(self,text="v2.0 • Smart Student Edition",text_color="gray").pack(side="bottom",pady=12)
