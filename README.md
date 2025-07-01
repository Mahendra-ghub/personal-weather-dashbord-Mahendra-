
# 🌾 Weather Dashboard – Weather Dashboard Web App

**Weather Dashboard** is a Flask-powered web application that allows users to register, log in, and view current weather information based on their chosen location. The app features a clean, modern user interface with background images, blur effects, and smooth user interaction.

Passwords are securely hashed before storing in a local SQLite database. Users can also update their location after registration, which reflects immediately in their weather dashboard.

---

## 📌 Key Features

- 🔒 **User Authentication**
  - Register and login with email & password
  - Passwords are stored securely using hashing (`werkzeug.security`)
  
- 🌍 **Location-Based Weather**
  - User's city & country location stored in DB
  - Displays temperature, humidity, condition, and wind speed
  
- 🎨 **Stylish UI**
  - Full background images (dashboard, login, register, location update)
  - Glassmorphism form containers (blurred, semi-transparent)
  - Responsive layout with modern design
  
- 🗃️ **SQLite Integration**
  - `users.db` stores all user records securely

---

## 🗂️ Project Structure

```
climatepro/
│
├── app.py              # Main Flask app and route initialization
├── auth.py             # User authentication logic (register, login, logout)
├── models.py           # DB schema and operations (init, insert, fetch users)
├── weather.py          # Dummy or API-based weather fetch function
├── requirements.txt    # Python package dependencies
├── users.db            # SQLite database (auto-created if not exists)
│
├── templates/          # HTML templates using Jinja2
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   └── update_location.html
│
├── static/             # Background images and static assets
│   ├── Agri11.png
│   ├── Das-bg.png
│   └── location.png
│
└── README.md           # You're here!
```

---

## 💻 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/personal-weather-dashboard/weather_dashboard.git
cd weather_dashboard
```

### 2. Set up a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate 
```

### 3. Install required packages
```bash
pip install -r requirements.txt
```

### 4. Run the Flask app
```bash
python app.py
```

Then open your browser and visit:
```
http://localhost:5000
```

---

## 🧪 Usage Guide

| Page | URL | Description |
|------|-----|-------------|
| 📝 Register | `/register` | Create a new account |
| 🔐 Login | `/login` | Log in with email & password |
| 🌤️ Dashboard | `/dashboard` | View weather info and user details |
| 🌍 Update Location | `/update-location` | Change saved location |
| 🚪 Logout | `/logout` | End session |

---

## 🔐 Password Security

Weather Dashboard uses `werkzeug.security` to hash and verify passwords securely:

- `generate_password_hash()` hashes passwords during registration
- `check_password_hash()` verifies input at login
- Stored passwords are **never in plaintext**

Example:
```
Weather_dashboard/Web_pages/Users database.png

```

---

## 🗃️ SQLite Database

The app stores data in a local SQLite file: `users.db`

### Tables:

#### `users`
| Column   | Type   | Description           |
|----------|--------|-----------------------|
| email    | TEXT   | Primary Key           |
| password | TEXT   | Hashed password       |
| location | TEXT   | User's city, country  |
![alt text](<../Desktop/2_Lang_Projects/Python_Projects/Weather_dashboard/Web_pages/Users database.png>)

---

## 📸 Screenshots (Optional)

Add screenshots for:
- 🔐 Login page with blurred glass form 
- 📝 Registration form with styled background
- 🌤️ Weather dashboard
- 🌍 Update location screen  

Example:
```
Weather_dashboard/Web_pages/Login page.png
Weather_dashboard/Web_pages/Regstration.png
Weather_dashboard/Web_pages/Dashboard.png
Weather_dashboard/Web_pages/update.png
---

## 📦 Requirements

All dependencies are listed in `requirements.txt`:
```
Flask
werkzeug
```

You can install them via:
```bash
pip install -r requirements.txt
```

---

## 🧠 Roadmap & Future Enhancements

- 🌐 Integrate OpenWeatherMap API for real-time data
- 🌱 Add crop and agricultural log features
- 📱 Improve mobile responsiveness
- 📤 User profile images
- 📧 Email verification
- 🔐 Password reset workflow

---

## 🛡️ License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) — you are free to use, modify, and distribute with attribution.

---

## 🙌 Acknowledgments

- Flask framework
- Werkzeug for secure password hashing
- DB Browser for SQLite
- Unsplash for background images

---

## 🤝 Contributing

Contributions are welcome!  
To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Added feature"`
4. Push to branch: `git push origin feature-name`
5. Open a pull request

---

**Made with ❤️ using Flask**
