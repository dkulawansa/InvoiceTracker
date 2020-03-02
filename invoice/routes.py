import os
import secrets

from flask import render_template, url_for, flash, redirect, request, abort
from invoice import app, db
from invoice.forms import InvoiceForm, InvoiceItemForm

from .models import Base, Invoice, InvoiceItem

@app.route("/")
@app.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    invoices = db.session.query(Invoice).order_by(Invoice.date_created.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', invoices=invoices)


@app.route("/about", methods=['post','get'])
def about():
    return render_template('about.html', title='About')
	
					
@app.route("/invoice/new", methods=['GET', 'POST'])
def new_invoice():
    form = InvoiceForm()
    if form.validate_on_submit():
        invoice = Invoice(cust_name=form.cust_name.data, date_created=form.date_created.data.strftime('%x'))
        db.session.add(invoice)
        db.session.commit()
        flash('Your invoice has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('invoice.html', title='New Invoice',
                           form=form, legend='New Invoice')

@app.route("/invoiceitem/<int:invoice_id>", methods=['GET', 'POST'])
def new_invoiceitem(invoice_id):
    form = InvoiceItemForm()
    invoice = db.session.query(Invoice).filter_by(id=invoice_id).first_or_404()
    if form.validate_on_submit():
        invoice_item = InvoiceItem(invoice_id=invoice.id, amount=form.amount.data, description=form.description.data)
        db.session.add(invoice_item)
        db.session.commit()
        flash('Your invoice item has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_invoice_item.html', title='New Invoice Item',
                           form=form, legend='New Invoice Item')
						   
						   