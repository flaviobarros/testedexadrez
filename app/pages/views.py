# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from flask import render_template
from flask_user import login_required, roles_required

from app.app_and_db import app


# The Home page is accessible to anyone
@app.route('/')
def home_page():
    fen = 'r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R'
    return render_template('pages/home_page.html', fen=fen)

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
