
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from auth import register_user, login_user, token_required
from weather import get_weather
from models import init_db, get_user_by_email, update_location, insert_agri_log, get_agri_logs

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

init_db()

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        result = register_user(request.form)
        return result
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        result = login_user(request.form)
        if isinstance(result, dict):
            session['token'] = result['token']
            return redirect('/dashboard')
        return result
    return render_template('login.html')

@app.route('/dashboard')
@token_required
def dashboard(current_user):
    weather_data = get_weather(current_user['location'])
    agri_logs = get_agri_logs(current_user['email'])
    return render_template('dashboard.html', user=current_user, weather=weather_data, logs=agri_logs)

@app.route('/update-location', methods=['GET', 'POST'])
@token_required
def update_location_route(current_user):
    if request.method == 'POST':
        new_location = request.form.get('location')
        update_location(current_user['email'], new_location)
        return redirect('/dashboard')
    return render_template('update_location.html', user=current_user)

@app.route('/add-log', methods=['POST'])
@token_required
def add_log(current_user):
    crop = request.form.get('crop')
    observation = request.form.get('observation')
    date = request.form.get('date')
    insert_agri_log(current_user['email'], crop, observation, date)
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.pop('token', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
