# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from flask import Flask, render_template, request 
from flask_user import login_required, roles_required
from app.pages.forms import ContactForm
from app.app_and_db import app


# The Home page is accessible to anyone
@app.route('/')
def home_page():
    form = ContactForm()
    return render_template('pages/home_page.html', form=form)

# The Member page is accessible to authenticated users (users that have logged in)
@app.route('/member')
@login_required             # Limits access to authenticated users
def member_page():
    return render_template('pages/member_page.html')

# The Admin page is accessible to users with the 'admin' role
@app.route('/admin')
@roles_required('admin')    # Limits access to users with the 'admin' role
def admin_page():
    return render_template('pages/admin_page.html')

# A contact page to test form 
@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        return 'Form posted.'

    elif request.method == 'GET':
        return render_template('pages/contact.html', form=form)
