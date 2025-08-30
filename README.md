

# Flask App with Blueprints

This project is a simple Flask web application structured using **Blueprints** to organize routes and views.  
It demonstrates how to separate authentication routes and general application views into different files for maintainability and scalability.

## Project Structure

- **main.py** → The entry point of the application. It creates and runs the Flask app.
- **views.py** → Contains the main routes (e.g., home page).
- **auth.py** → Contains authentication-related routes (e.g., login, logout, sign-up).
- **README.md** → Project documentation (this file).

## Features

- Uses Flask Blueprints for modular route handling.
- Basic routes for:
  - Home (`/`)
  - Login (`/login`)
  - Logout (`/logout`)
  - Sign Up (`/sign-up`)
- Placeholder HTML responses (can be replaced with templates).

## Running the App

1. Install dependencies:
   ```bash
   pip install flask
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Access in your browser:
   - Home: http://127.0.0.1:5000/
   - Login: http://127.0.0.1:5000/login
   - Logout: http://127.0.0.1:5000/logout
   - Sign Up: http://127.0.0.1:5000/sign-up

## Next Steps

- Add HTML templates and render them using `render_template`.
- Implement proper authentication (Flask-Login, sessions, etc.).
- Add database integration for users.