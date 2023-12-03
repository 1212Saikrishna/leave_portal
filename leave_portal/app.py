from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_mail import Mail, Message
from flask_migrate import Migrate
from config import Config
import random
import string

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class LeaveRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(50))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    status = db.Column(db.String(20))
    reason = db.Column(db.String(100))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    otp = db.Column(db.String(6))
    otp_timestamp = db.Column(db.DateTime)
    password_reset_token = db.Column(db.String(32))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def send_otp_email(user):
    otp = ''.join(random.choices(string.digits, k=6))
    user.otp = otp
    user.otp_timestamp = datetime.utcnow()
    db.session.commit()

    msg = Message('OTP for SIENT Leave Portal', recipients=[user.email])
    msg.body = f'Your OTP is: {otp}'
    mail.send(msg)

@app.route('/')
@login_required
def home():
    leave_requests = LeaveRequest.query.all()
    return render_template('home.html', leave_requests=leave_requests)

@app.route('/submit_leave', methods=['GET', 'POST'])
@login_required
def submit_leave():
    if request.method == 'POST':
        employee_name = request.form['employee_name']
        start_date_str = request.form['start_date']
        end_date_str = request.form['end_date']
        reason = request.form['reason']
        status = 'Pending'  # Default status when submitting a leave request

        # Convert date strings to Python date objects
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

        new_leave_request = LeaveRequest(
            employee_name=employee_name,
            start_date=start_date,
            end_date=end_date,
            reason=reason,
            status=status
        )

        db.session.add(new_leave_request)
        db.session.commit()
        flash('Leave request submitted successfully', 'success')

        return redirect(url_for('home'))

    return render_template('submit_leave.html')

@app.route('/approve_leave/<int:id>', methods=['GET', 'POST'])
@login_required
def approve_leave(id):
    leave_request = LeaveRequest.query.get(id)
    if request.method == 'POST':
        if leave_request:
            leave_request.status = 'Approved'
            db.session.commit()
            flash('Leave request approved', 'success')
        return redirect(url_for('home'))
    return render_template('approve_leave.html', leave_request=leave_request)

@app.route('/reject_leave/<int:id>', methods=['GET', 'POST'])
@login_required
def reject_leave(id):
    leave_request = LeaveRequest.query.get(id)

    if request.method == 'POST':
        if leave_request:
            leave_request.status = 'Rejected'
            db.session.commit()
            flash('Leave request rejected', 'danger')
        return redirect(url_for('home'))

    return render_template('reject_leave.html', leave_request=leave_request)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            send_otp_email(user)
            flash('OTP has been sent to your email. Check your inbox.', 'info')
            return render_template('verify_otp.html', user=user)
        else:
            flash('Login failed. Please check your username and password.', 'danger')
    return render_template('login.html')

@app.route('/verify_otp/<int:user_id>', methods=['GET', 'POST'])
def verify_otp(user_id):
    user = db.session.query(User).get(user_id)
    if request.method == 'POST':
        entered_otp = request.form['otp']
        user = db.session.query(User).get(user_id)
        if not user:
            flash('Invalid user.', 'danger')
            return redirect(url_for('login'))

        if user.otp and user.otp == entered_otp:
            login_user(user)
            flash('Login successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid OTP. Please try again.', 'danger')

    return render_template('verify_otp.html', user=user)



@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        if User.query.filter_by(username=username).first():
            flash('Username is already taken. Please choose another one.', 'danger')
        elif User.query.filter_by(email=email).first():
            flash('Email is already registered. Please use another email.', 'danger')
        else:
            new_user = User(username=username, password=password, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful. Please check your email for OTP.', 'success')

            # Send OTP email to the newly registered user
            send_otp_email(new_user)

            return render_template('verify_otp.html', user=new_user)

    return render_template('register.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    if request.method == 'POST':
        logout_user()
        flash('You have been logged out', 'info')
        return redirect(url_for('login'))
    return render_template('logout.html')  # Add a template for logout confirmation if needed

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    messages = []  # Create an empty list to store flash messages

    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()

        if user:
            # Generate a reset token and send an email with the reset link
            send_password_reset_email(user)
            messages.append(('Password reset link sent to your email. Check your inbox.', 'info'))
            return redirect(url_for('login'))
        else:
            messages.append(('Email not found. Please check your email address.', 'danger'))

    return render_template('forgot_password.html', messages=messages)

def send_password_reset_email(user):
    reset_token = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    user.password_reset_token = reset_token
    db.session.commit()

    reset_link = url_for('reset_password', token=reset_token, _external=True)
    msg = Message('Password Reset Request', recipients=[user.email])
    msg.body = f'To reset your password for sientleaveportal click the here:  {reset_link}'
    mail.send(msg)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user = User.query.filter_by(password_reset_token=token).first()

    messages = []  # Create an empty list to store flash messages

    if not user:
        messages.append(('Invalid or expired reset token. Please try again.', 'danger'))
        return redirect(url_for('login'))

    if request.method == 'POST':
        new_password = request.form['new_password']
        user.password = new_password
        user.password_reset_token = None
        db.session.commit()

        messages.append(('Password reset successful. You can now log in with your new password.', 'success'))
        return redirect(url_for('login'))

    return render_template('reset_password.html', token=token, messages=messages)


if __name__ == '__main__':
    app.app_context().push()
    db.create_all()

    if not User.query.filter_by(username='admin').first():
        admin_user = User(username='admin', password='password', email='admin@example.com')
        db.session.add(admin_user)
        db.session.commit()

    app.run(debug=True, port=7000)
