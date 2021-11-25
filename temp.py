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
    


# BOOTSTRAP (JavaScript Framework to make the web pretty)
from flask_bootstrap import Bootstrap
Bootstrap(app)

# FLASK - WTForms!
from flask_wtf import FlaskForm
from wtforms import StringField#, PasswordField, BooleanField, SelectField
from wtforms.validators import  DataRequired#, InputRequired, Length, Email, EqualTo,

class SearchForm(FlaskForm):
  name = StringField('Type the name of the company you want to see data: ', validators=[DataRequired()])


@app.route('/', methods=['GET','POST']) #añadido ,methods=['GET','POST']
def index():
    form=SearchForm()


    if request.method == 'POST':
        companies=BalanceSheet.query.filter(BalanceSheet.company_name.contains(form.name.data)).all()
        result = True

    else:
        companies= BalanceSheet.query.filter(BalanceSheet.id>=0).limit(40).all()
        result = False

    entries=[]
    for ticker in BalanceSheet.query.filter(BalanceSheet.id>=0).all():
        entries+=[(ticker.company_name)]
    return render_template('index.html',module='home', rows=companies, form=form, entries=entries, result = result)



import pandas as pd
pd.set_option('display.float_format', lambda x: '%.3f' % x)
df = pd.read_sql("""SELECT * FROM balance_sheet;""", conn)
