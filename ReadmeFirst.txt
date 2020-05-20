Invoice Tracker
================
It is recommended that you use python 3.6  to run this application.
Clone the git repository name InvoiceTracker.  Activate the virtualenv and use the following command to install the requirements 

pip install -r requirements.txt

In addition to that you will need to download the latest version of the postgres database.
Once database is installed and running, open the psql CLI or PGAdmin web client to create a database called invoice. 
I have used the database with userid = postgres and password =tiger in this application, so the connection string for the database instance is:
 'postgresql+psycopg2://postgres:tiger@localhost/testdb'
If you have used different credentials, you may set the connection string in the __init__.py file in the invoice folder.

The next step is to create database objects, namely two tables, invoices and invoice_items.
For that you will need to open the Python shell from project folder
In the python REPL run the following commands to create the two tables

>>>from invoice.models import Base
>>> Base.metadata.create_all(bind=db.engine)
>>
Once done, type quit() to exit the shell. You can make sure whether table are created by going PGAdmin or psql CLI.

If you are running the app on windows system run the following command to start the application 
 
set FALSK_APP=invoice
flask run




In Linux environment run
export FALSK_APP=invoice 
flask run

If everything goes well you will get some warnings and a link like the following to run the application on the browser
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

You can go to invoice page with this link http://127.0.0.1:5000/invoice/new

Bellow are 3 screenshots that I create while testing the application.

Thanks.
