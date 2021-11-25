# CONNECTING OUR DATABASE using SQLite and SQLAlchemy!
import sqlite3
conn = sqlite3.connect("./database/company_balancesheet_database.db")
app.config['SECRET_KEY'] = "ThisIsASecretKey_SoThatCommunicationBetween_AppAndForms_AreEncrypted"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./database/company_balancesheet_database.db'
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class BalanceSheet(db.Model):
    __tablename__ = 'balance_sheet'
    id = db.Column(db.Integer, primary_key=True)
    nif_fical_number_id = db.Column(db.String(9))
    company_name = db.Column(db.String(80))
    CNAE = db.Column(db.Integer)
    p10000_TotalAssets_h0 = db.Column(db.Float)
    p10000_TotalAssets_h1 = db.Column(db.Float)
    p10000_TotalAssets_h2 = db.Column(db.Float)
    p20000_OwnCapital_h0 = db.Column(db.Float)
    p20000_OwnCapital_h1 = db.Column(db.Float)
    p20000_OwnCapital_h2 = db.Column(db.Float)
    p31200_ShortTermDebt_h0 = db.Column(db.Float)
    p31200_ShortTermDebt_h1 = db.Column(db.Float)
    p31200_ShortTermDebt_h2 = db.Column(db.Float)
    p32300_LongTermDebt_h0 = db.Column(db.Float)
    p32300_LongTermDebt_h1 = db.Column(db.Float)
    p32300_LongTermDebt_h2 = db.Column(db.Float)
    p40100_40500_SalesTurnover_h0 = db.Column(db.Float)
    p40100_40500_SalesTurnover_h1 = db.Column(db.Float)
    p40100_40500_SalesTurnover_h2 = db.Column(db.Float)
    p40800_Amortization_h0 = db.Column(db.Float)
    p40800_Amortization_h1 = db.Column(db.Float)
    p40800_Amortization_h2 = db.Column(db.Float)
    p49100_Profit_h0 = db.Column(db.Float)
    p49100_Profit_h1 = db.Column(db.Float)
    p49100_Profit_h2 = db.Column(db.Float)
    detailed_status = db.Column(db.String(150))
